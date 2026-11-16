# CCNP ENCOR 350-401 – GNS3 Learning Academy

Een **uitvoerbaar leerproject als bronpakket** met 29 hoofdstukken, 87 opdrachten (29 configuratie-, 29 troubleshooting-, 29 challenge-labs), 29 GNS3-projectscaffolds, topologiespecificaties en een script dat echte GNS3-nodes/links kan aanmaken via de GNS3 Controller API.

> **Belangrijk:** Cisco IOSv/IOSvL2/IOL/IOS XE-images zitten **niet** in dit pakket (licenties). De `.gns3`-bestanden zijn lege, geldige **projectscaffolds** en tonen nog geen werkende router/switch-topologie totdat `tools/gns3_deploy.py` de nodes en links aanmaakt in jouw eigen GNS3-server, met jouw reeds geïnstalleerde router/switch-templates. De deployment is niet op een live GNS3-server getest. Bekijk `docs/INSTALLATIE.md`.

## Starten (GNS3 2.2 aanbevolen)

1. Importeer legitiem verkregen IOSv / IOSvL2 of andere geschikte templates in GNS3. Zet je GNS3-controller/API aan, typisch `http://127.0.0.1:3080`.
2. `python tools/gns3_deploy.py --list-templates`
3. `python tools/gns3_deploy.py --chapter 2 --router-template "IOSv" --switch-template "IOSvL2"`
4. Open het nieuwe project in GNS3; controleer de interface-toewijzing in `Chapter-02-*/topology.json` en in het deployrapport. Configureer de nodes met `configs/starting/` of door de labinstructies te volgen.
5. Voor een volgende opdracht laad je een eigen GNS3 snapshot of de configuratie uit `configs/solutions/` (niet automatisch gepusht).

## Het pakket

- `chapters/`: 29 hoofdstukken × drie gedetailleerde opdrachten + verificatie en solutions.
- `gns3-projects/`: `.gns3` projectscaffolds per hoofdstuk (GNS3 2.2).
- `topologies/`: volledig gespecificeerde netwerkdiagrammen en links als JSON.
- `tools/gns3_deploy.py`: maakt **daadwerkelijk** projecten, nodes en links op jouw GNS3-controller met bestaande templates.
- `tools/validate_project.py`: controleert structuur en JSON.
- `automation/`: werkend Python mock-API voorbeeld, Ansible-playbook en inventory-template.
- `tracking/`: studievoortgang als CSV.
- `docs/`: installatie, beperkingen, scores, troubleshooting-methodiek.

## Capaciteit & scope

GNS3 met eigen appliance-images voor Layer 2/3; sommige features zijn image/licentieafhankelijk. Wireless RF, echte Cisco SD-Access/SD-WAN fabric en sommige securityfuncties zijn **conceptuele / begeleide labs**, geen volledige RF- of fabric-emulatie. Voor deze thema's zijn gespecialiseerde appliances, echte hardware of Cisco sandboxes nodig.

## Copyright

Originele zelfgeschreven opdrachten. Geen Cisco OS-images, boekhoofdstukken of examenmateriaal inbegrepen.
