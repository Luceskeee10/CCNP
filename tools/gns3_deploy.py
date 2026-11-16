#!/usr/bin/env python3
"""Deploy CCNP ENCOR lab topologies to GNS3 2.2 using installed node templates.
Only creates projects, nodes and links; does not download IOS images or push configs.
"""
import argparse, json, os, sys, urllib.request, urllib.error, base64, pathlib
BASE=pathlib.Path(__file__).resolve().parents[1]

def call(url,method='GET',payload=None,auth=None):
    data=None if payload is None else json.dumps(payload).encode('utf8')
    headers={'Content-Type':'application/json'}
    if auth:
        user,password=auth
        headers['Authorization']='Basic '+base64.b64encode(f'{user}:{password}'.encode()).decode()
    req=urllib.request.Request(url,method=method,data=data,headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=40) as res:
            body=res.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f'{method} {url}: HTTP {e.code}: {e.read().decode("utf8","replace")[:500]}') from e

def pick_template(templates,name):
    hits=[t for t in templates if t.get('name','').casefold()==name.casefold()]
    if len(hits)!=1:
        hits=[t for t in templates if name.casefold() in t.get('name','').casefold()]
    if len(hits)!=1: raise RuntimeError(f'Template {name!r} match count {len(hits)}; use --list-templates and specify exact name')
    return hits[0]['template_id']

def endpoint_for(node, ordinal):
    """Choose an actual unused GNS3 port; template interface numbering can vary.
    Keeps ports lexically in API ordering so links map to port labels.
    """
    ports=node.get('ports') or []
    if len(ports)<=ordinal:
        raise RuntimeError(f"{node['name']}: needs port #{ordinal+1} but template only exposes {len(ports)} ports. Increase NICs in the GNS3 template.")
    port=ports[ordinal]
    return {'node_id':node['node_id'],'adapter_number':port['adapter_number'],'port_number':port['port_number']}, port.get('name','?')

def deploy(args,chapter,templates,auth):
    specfile=next((BASE/'topologies').glob(f'Chapter-{chapter:02d}-*.json'))
    topology=json.loads(specfile.read_text(encoding='utf8'))
    pfx=args.url.rstrip('/')
    project_name=f'ENCOR {chapter:02d} - {topology["name"]}'
    if args.dry_run:
        print(json.dumps(topology,indent=2));return
    existing=call(pfx+'/v2/projects',auth=auth)
    if any(p['name']==project_name for p in existing):
        raise RuntimeError(f'Project {project_name!r} already exists. Rename or delete manually; deployment is intentionally non-destructive.')
    project=call(pfx+'/v2/projects','POST',{'name':project_name,'auto_start':False,'show_interface_labels':True},auth)
    pid=project['project_id'];nodes={}
    try:
        for n in topology['nodes']:
            if n['role']=='pc':
                node=call(f'{pfx}/v2/projects/{pid}/nodes','POST',{'name':n['name'],'node_type':'vpcs','compute_id':'local','x':n['x'],'y':n['y']},auth)
            else:
                template=pick_template(templates,args.switch_template if n['role']=='switch' else args.router_template)
                node=call(f'{pfx}/v2/projects/{pid}/templates/{template}','POST',{'name':n['name'],'x':n['x'],'y':n['y']},auth)
            nodes[n['name']]=node
        report=[]
        for l in topology['links']:
            ep1,if1=endpoint_for(nodes[l['a']],l['port_a'])
            ep2,if2=endpoint_for(nodes[l['b']],l['port_b'])
            call(f'{pfx}/v2/projects/{pid}/links','POST',{'nodes':[ep1,ep2]},auth)
            report.append({'link':f'{l["a"]} {if1} <--> {l["b"]} {if2}', 'a':ep1,'b':ep2})
        report_file=BASE/'deployment-reports'/f'chapter-{chapter:02d}-interfaces.json'
        report_file.parent.mkdir(parents=True,exist_ok=True)
        report_file.write_text(json.dumps({'project':project_name,'project_id':pid,'links':report},indent=2))
        print(f'Created {project_name} ({pid}), {len(nodes)} nodes, {len(report)} links')
        print('Interface map:',report_file)
    except Exception:
        print(f'Partial project {project_name} may exist on GNS3; inspect before retrying.',file=sys.stderr)
        raise

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--url',default='http://127.0.0.1:3080',help='GNS3 controller URL')
    ap.add_argument('--username',default=None)
    ap.add_argument('--password-env',default='GNS3_PASSWORD',help='Environment variable for controller password')
    ap.add_argument('--router-template',default='IOSv')
    ap.add_argument('--switch-template',default='IOSvL2')
    ap.add_argument('--chapter',type=int,choices=range(1,30))
    ap.add_argument('--all',action='store_true',help='Deploy all 29 projects (resource intensive)')
    ap.add_argument('--list-templates',action='store_true')
    ap.add_argument('--dry-run',action='store_true',help='Print topology data without deployment; no server required')
    args=ap.parse_args()
    if not (args.chapter or args.all or args.list_templates):ap.error('choose --chapter N, --all or --list-templates')
    if args.username and not os.getenv(args.password_env):ap.error('missing password environment variable')
    auth=(args.username,os.getenv(args.password_env)) if args.username else None
    try:
        templates=[] if args.dry_run else call(args.url.rstrip('/')+'/v2/templates',auth=auth)
        if args.list_templates:
            for t in templates:print(f"{t.get('name','?')}\t{t.get('template_id','')}\t{t.get('template_type','')}")
        else:
            for n in range(1,30) if args.all else [args.chapter]:deploy(args,n,templates,auth)
    except (RuntimeError,urllib.error.URLError) as ex:
        print(f'ERROR: {ex}',file=sys.stderr);sys.exit(2)
