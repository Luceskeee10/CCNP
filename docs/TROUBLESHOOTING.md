# Troubleshooting workflow

1. Verzamel symptoom + scope: wie, wat, sinds wanneer, welke VLAN, welke subnet.
2. Verifieer L1/L2: `show interfaces status`, `show interfaces trunk`, `show spanning-tree`, `show etherchannel summary`, `show mac address-table`.
3. Verifieer L3: `show ip interface brief`, `show arp`, `show ip route`, `show ip cef`, `show ip protocols`.
4. Verifieer control plane: `show ip ospf neighbor`, `show ip ospf database`, `show ip eigrp neighbors`, `show bgp ipv4 unicast summary`.
5. Wijzig zo weinig mogelijk, maak config diff, test niet alleen ping maar de vereiste route/policy.
6. Documenteer root cause, impact, fix, rollback, preventie en relevante commandoutput.

**Scoring:** analyse 30, verantwoorde verificatie 20, herstel 30, root-cause-uitleg 20. Minimaal 80/100.
