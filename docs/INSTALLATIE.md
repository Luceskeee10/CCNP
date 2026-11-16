# Installatie en eerste lab

## Vereisten
- Python 3.9+ (enkel standaardbibliotheek); geen pip-pakketten nodig voor deployment.
- GNS3 controller/server 2.2.x bereikbaar, met templates voor IOSv (routers), IOSvL2 (switches) of functioneel gelijkwaardige legitieme appliances. Zet voldoende QEMU-NICs op de templates: **minimaal 8 interfaces voor switching en 6 voor routing**.
- VPCS komt doorgaans standaard met GNS3.
- GNS3 VM aanbevolen wanneer je lokaal resources beperkt zijn.

## Voorbeeld PowerShell (Windows)
```powershell
cd CCNP-ENCOR-Lab-Academy
python .\tools\gns3_deploy.py --list-templates
python .\tools\gns3_deploy.py --chapter 2 --router-template "IOSv" --switch-template "IOSvL2"
python .\tools\validate_project.py
```
Gebruik `--url http://<GNS3-controller>:3080` als de controller elders staat. Met controller-authenticatie gebruik `--username` en `--password-env GNS3_PASSWORD`; zet je wachtwoord in een environment variable, **niet** in een command history. Default is localhost. GNS3-API is niet bedoeld om onbeveiligd op internet te publiceren.

## Waarom het .gns3-bestand nog leeg is
De projecten zijn geldig als GNS3-projectscaffold maar lokale QEMU templates verwijzen naar imagebestanden met **jouw** bestandsnaam, compute-server en template UUID. Die kunnen niet vooraf ingevuld worden zonder jouw lokale GNS3-installatie. Het deployscript maakt de nodes met GNS3's officiële `POST /v2/projects/{id}/templates/{id}` en links met `POST /v2/projects/{id}/links`.

## Inhoudelijk werken
- **Configuration:** maak de eisen zelf werkend; de startconfiguratie bevat slechts hostnames en interface-basics.
- **Troubleshooting:** leg met de instructies uit `troubleshooting.md` de fout(en) handmatig aan, maak eerst een GNS3 snapshot, en herstel daarna zonder in de solution te kijken. Voor vier hoofdstukken zijn concrete fout-injectie CLI-bestanden aanwezig.
- **Challenge:** mix van meerdere symptomen en een incidentrapport. Niet alle scenarios zijn volledig geïmplementeerde virtuele snapshots.

## Caveats
- De gegenereerde topologieën bevatten apparaatlinks, maar geen door het script toegepaste CLI-configuraties; dit voorkomt vendor- en imageafhankelijke command failures.
- Interfaces worden volgens nodepoort-volgorde verbonden; de precieze Cisco interface-namen (`Gi0/0` versus `Gi0/1`) verschillen per image. Gebruik het generated deploy JSON of je GNS3-linklabels om de mappen naar CLI-interfaces te vertalen.
- GNS3 3.x API compatibility is niet bevestigd. 
- IP-adressen en loopbacks zijn leernetten, geen productie-netwerk. 
