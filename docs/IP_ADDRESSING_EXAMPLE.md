# Voorbeeld IP addressing (zelf aanpassen aan de specifieke interface)

Voor router-routerlinks gebruik unieke /30 IPv4-subnets, bijvoorbeeld:

| Link | A | B |
|---|---|---|
| R1–R2 | 10.0.12.1/30 | 10.0.12.2/30 |
| R2–R3 | 10.0.23.1/30 | 10.0.23.2/30 |
| R1–R4 | 10.0.14.1/30 | 10.0.14.2/30 |
| R2–R4 | 10.0.24.1/30 | 10.0.24.2/30 |
| R3–R5 | 10.0.35.1/30 | 10.0.35.2/30 |
| R4–R5 | 10.0.45.1/30 | 10.0.45.2/30 |

Loopbacks: R1–R5 `10.255.<n>.<n>/32`. For L2 campus: VLAN 10 = 192.168.10.0/24, VLAN 20 = 192.168.20.0/24, VLAN 30 = 192.168.30.0/24, VLAN 40 = 192.168.40.0/24. Actual CLI interfaces depend on GNS3 template. `192.0.2.0/24` addresses in examples are TEST-NET examples, not Internet-reachable.
