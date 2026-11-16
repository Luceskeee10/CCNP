# Lab 05.1 — Configuration

**Situation:** je implementeert VLAN Trunks and EtherChannel Bundles in een nieuw enterprise-lab.

**Requirements:** Build Po1 LACP across two links; permit VLANs 10/20/30.

## Deliverables
1. Teken de forwarding/control-plane-paden in de topologie en beschrijf de rol van ieder apparaat.
2. Configureer basis-hostnames, IP-connectiviteit en het hoofdstukspecifieke protocol/feature: **802.1Q trunks, LACP, port channels, VTP/DTP interpretation**.
3. Zorg dat de gewenste reachability en het gekozen voorkeurs-/failoverpad aantoonbaar werken. Voeg minimaal één expliciete test met verwachte output toe.
4. Sla volledige `show running-config` (zonder secrets) en protocolstatus op.
5. Simuleer een link failure; leg uit welke tabellen en timers reageren.

## Verification checklist
- [ ] Onderliggende interfaces zijn `up/up` waar nodig.
- [ ] Interfaces en protocolstatus kloppen met de ontwerpen.
- [ ] Vereiste datapaden slagen; ongewenste paden zijn gefilterd.
- [ ] Een linkuitval geeft de bedoelde, verklaarde response.
- [ ] Outputs bewaard en geanalyseerd.

**Let op:** niet elke feature wordt door iedere IOSv/IOSvL2-build ondersteund. Voor conceptuele wireless/fabric hoofdstukken vervang CLI door meetplan / sandboxresultaten.
