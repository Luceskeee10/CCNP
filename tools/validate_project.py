#!/usr/bin/env python3
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
errors=[]
for n in range(1,30):
    t=list((root/'topologies').glob(f'Chapter-{n:02d}-*.json'))
    p=list((root/'gns3-projects').glob(f'Chapter-{n:02d}-*.gns3'))
    c=list((root/'chapters').glob(f'Chapter-{n:02d}-*'))
    if len(t)!=1 or len(p)!=1 or len(c)!=1:errors.append(f'{n}: missing/duplicate files');continue
    topo=json.loads(t[0].read_text()); scaffold=json.loads(p[0].read_text())
    ns={v['name'] for v in topo['nodes']}
    assert len(ns)==len(topo['nodes'])
    for l in topo['links']:
        if l['a'] not in ns or l['b'] not in ns:errors.append(f'{n}: invalid link {l}')
    if not {'nodes','links','drawings','computes'}<=scaffold['topology'].keys():errors.append(f'{n}: invalid .gns3 structure')
    for file in ['README.md','01-configuration.md','02-troubleshooting.md','03-expert-challenge.md','verification-commands.txt']:
        if not (c[0]/file).exists():errors.append(f'{n}: missing {file}')
print(f'Checked 29 chapters, 29 GNS3 project scaffolds and 29 topology JSON specs; issues={len(errors)}')
for err in errors:print(err)
sys.exit(bool(errors))
