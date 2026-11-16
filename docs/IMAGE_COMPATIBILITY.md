# Image-compatibiliteit

- **IOSvL2**: bruikbaar voor klassieke switching (STP, MST, trunks, EtherChannel). Functionaliteit verschilt per versie; check eerst `?`.
- **IOSv / CSR1000v / C8000v**: bruikbaar voor veel L3-labs; performance en featurelicenties verschillen.
- **IOL/IOU**: alleen als je rechtmatig toegang hebt; interface-indeling en ondersteunde commands kunnen afwijken.
- **Built-in Ethernet Switch**: **niet** bruikbaar als volwaardig IOSvL2-alternatief voor STP/MST/LACP troubleshooten.
- **Wireless**: met gewone IOSv-nodes kan je RF en echte AP roaming niet emuleren; gebruik het simulatie-/analysewerkblad met hardware of een geschikte WLC-labomgeving.
- **SD-Access/SD-WAN**: reguliere IOSv-router-topologie toont hoogstens het underlay; geen volwaardige fabric. Gebruik Cisco labs/sandboxes.
- **Ansible/REST**: lokaal Python-voorbeeld werkt zonder Cisco-image; SSH-netwerkautomatisering vraagt bereikbare network devices.
