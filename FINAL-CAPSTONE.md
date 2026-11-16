# Final ENCOR Capstone — multi-domain troubleshooting

**Build:** campus (SW1–SW4) + R1–R5 routed core, area 0 OSPF, per-VLAN L3 gateways, LACP access redundancy, primary/backup upstream routing, AAA baseline, syslog. This is a design brief rather than an already-wired single GNS3 project.

**Incident pack:** (1) silent VLAN allowed-list mismatch; (2) STP unexpected root; (3) OSPF timer mismatch; (4) broken BGP next hop; (5) missing syslog; (6) access ACL blocking DNS. Introduce 3–6 of these on your own saved working topology. Timebox 120 minutes.

**Pass:** restore intended forwarding, preserve isolation, justify all fixes, supply tests and rollbacks and document incident report. Score 80+.
