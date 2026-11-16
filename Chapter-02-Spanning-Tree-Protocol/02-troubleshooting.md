# Lab 02.2 — Troubleshooting

## Incident
Een netwerk met werkende basisconnectiviteit faalt na een configuratiewijziging. Symptomen: **Unexpected root bridge; blocked access uplink**.

## Preparatie (door jezelf of labpartner)
1. Bouw eerst lab 02.1 werkend.
2. Bewaar een GNS3 snapshot.
3. Injecteer één fout die de genoemde symptomen veroorzaakt. Injecteer daarna een **tweede onafhankelijke fout** in hetzelfde thema.
4. Laat je partner de storingen oplossen, of wacht tot je zelf niet meer weet welke configuratie afwijkt.

## Troubleshooting, zonder hints
- Verzamel symptomen en uitsluitingen voordat je CLI wijzigt.
- Vergelijk de control-plane informatie met effectieve forwarding.
- Test hypothesen op één wijziging tegelijk.
- Stel een rollback op.
- Leg de root cause vast in `incident-report.md`.

## Evidence
Minimaal: `show running-config`, interface-status, protocolstatus, `ping`/`traceroute` en één verifieerbare post-fix test. Geef jezelf 0–100 punten volgens `docs/TROUBLESHOOTING.md`.
