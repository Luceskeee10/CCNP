# Lab 02.1 — Configuration

**Situation:** je implementeert Spanning Tree Protocol in een nieuw enterprise-lab.

**Requirements:** Set SW1 root for VLAN 10 and SW2 for VLAN 20.

## Deliverables
1. Teken de forwarding/control-plane-paden in de topologie en beschrijf de rol van ieder apparaat.
2. Configureer basis-hostnames, IP-connectiviteit en het hoofdstukspecifieke protocol/feature: **PVST+, RSTP, root election and port roles**.
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
