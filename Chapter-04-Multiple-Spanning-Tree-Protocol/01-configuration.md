# Lab 04.1 — Configuration

**Situation:** je implementeert Multiple Spanning Tree Protocol in een nieuw enterprise-lab.

**Requirements:** Create MSTI 1 VLANs 10,20 and MSTI 2 VLANs 30,40.

## Deliverables
1. Teken de forwarding/control-plane-paden in de topologie en beschrijf de rol van ieder apparaat.
2. Configureer basis-hostnames, IP-connectiviteit en het hoofdstukspecifieke protocol/feature: **MST region, revision, VLAN-instance mapping**.
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
