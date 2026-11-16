# Lab 01.3 — Expert challenge

**Ticket:** 'Na een geplande change is de dienst gedeeltelijk onbereikbaar. Beperk impact zonder alle apparatuur te rebooten.'

**Service:** Packet Forwarding. **Problem family:** Wrong default gateway; missing VLAN on trunk.

**Constraints:** maximaal 45 minuten, geen config erase, behoud kritieke connectiviteit, noteer ieder commando dat de toestand verandert.

## Opdracht
1. Bouw een evidence-based hypotheselijst (minstens 3 mogelijke oorzaken).
2. Maak een laag-voor-laag fault tree voor de complete topology.
3. Diagnoseer één bewust ingebrachte primaire fout en één bijkomende fout.
4. Voer de minimaal noodzakelijke fix door en test een positieve én negatieve testcase.
5. Schrijf postmortem met root cause, detection gap en permanente mitigatie.

**Score:** 30 analyse / 20 bewijs / 30 herstel / 20 uitleg. De foutinjectie gebeurt handmatig; dit bestand bevat geen kant-en-klare kapotte appliance-snapshot.
