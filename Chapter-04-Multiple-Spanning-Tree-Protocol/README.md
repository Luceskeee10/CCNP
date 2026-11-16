# Chapter 04 — Multiple Spanning Tree Protocol

**Official Cert Guide 2nd Edition · Layer 2 · Lab profile `campus`**

**Focus:** MST region, revision, VLAN-instance mapping.

**Leerdoelen:** Create MSTI 1 VLANs 10,20 and MSTI 2 VLANs 30,40.

## Files
- `topology.json`: kopie van de volledige topologiespecificatie voor GNS3-deployment.
- `01-configuration.md`: guided configuration met taken en verificatie.
- `02-troubleshooting.md`: storingsscenario en bewijschecklist.
- `03-expert-challenge.md`: no-hints incident.
- `configs/starting/`: per-node veilige, minimale startconfiguraties (aanpassen aan image).
- `configs/solutions/`: doelconfiguratie-aanwijzingen, géén vendor-onafhankelijk werkende volledige running config.

**Eerst:** deployment met `python tools/gns3_deploy.py --chapter 4 --router-template "IOSv" --switch-template "IOSvL2"`; daarna interface-toewijzing dubbelchecken.
