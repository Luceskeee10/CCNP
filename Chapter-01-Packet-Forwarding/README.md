# Chapter 01 — Packet Forwarding

**Official Cert Guide 2nd Edition · Forwarding · Lab profile `campus`**

**Focus:** ARP, MAC learning, CEF and L2/L3 forwarding.

**Leerdoelen:** VLAN 10/20 reachability and FIB verification.

## Files
- `topology.json`: kopie van de volledige topologiespecificatie voor GNS3-deployment.
- `01-configuration.md`: guided configuration met taken en verificatie.
- `02-troubleshooting.md`: storingsscenario en bewijschecklist.
- `03-expert-challenge.md`: no-hints incident.
- `configs/starting/`: per-node veilige, minimale startconfiguraties (aanpassen aan image).
- `configs/solutions/`: doelconfiguratie-aanwijzingen, géén vendor-onafhankelijk werkende volledige running config.

**Eerst:** deployment met `python tools/gns3_deploy.py --chapter 1 --router-template "IOSv" --switch-template "IOSvL2"`; daarna interface-toewijzing dubbelchecken.
