# Chapter 09 — Advanced OSPF

**Official Cert Guide 2nd Edition · Routing · Lab profile `routing`**

**Focus:** Multi-area routing, LSAs, ABRs, area summary.

**Leerdoelen:** Use area 0 backbone and area 10/20 loopbacks with summaries.

## Files
- `topology.json`: kopie van de volledige topologiespecificatie voor GNS3-deployment.
- `01-configuration.md`: guided configuration met taken en verificatie.
- `02-troubleshooting.md`: storingsscenario en bewijschecklist.
- `03-expert-challenge.md`: no-hints incident.
- `configs/starting/`: per-node veilige, minimale startconfiguraties (aanpassen aan image).
- `configs/solutions/`: doelconfiguratie-aanwijzingen, géén vendor-onafhankelijk werkende volledige running config.

**Eerst:** deployment met `python tools/gns3_deploy.py --chapter 9 --router-template "IOSv" --switch-template "IOSvL2"`; daarna interface-toewijzing dubbelchecken.
