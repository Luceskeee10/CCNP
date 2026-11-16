# Fault 01 solution

Use `show spanning-tree vlan 10` and compare bridge IDs; expected SW1 is root for VLAN 10. Remove wrong root election and restore priority; root changes can briefly disrupt flows.
