# Lab 09.1 — Configuration

**Situation:** je implementeert Advanced OSPF in een nieuw enterprise-lab.

**Requirements:** Use area 0 backbone and area 10/20 loopbacks with summaries.

## Deliverables
1. Teken de forwarding/control-plane-paden in de topologie en beschrijf de rol van ieder apparaat.
2. Configureer basis-hostnames, IP-connectiviteit en het hoofdstukspecifieke protocol/feature: **Multi-area routing, LSAs, ABRs, area summary**.
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
