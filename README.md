# Verkstedpåminner

Notater og påminnelser for kundemottaket på bilverkstedet.

**Live:** https://hardwaregnome2.github.io/verkstedpaaminner/

## Innhold

| Fil | Hva den er |
|---|---|
| `index.html` | Appen slik den kjører på GitHub Pages. Bygges fra `kilde/` – ikke rediger den direkte. |
| `firebase-config.js` | Kobling til Firebase-prosjektet `verkstedpaaminner`. Verdiene er ikke hemmelige. |
| `kilde/verkstedpaaminner.html` | Hovedappen (all funksjonalitet, utseende og logikk). |
| `kilde/innlogging.html` | Innloggingsskjermen. |
| `kilde/firebase-modul.html` | Kobling til Firebase: innlogging, godkjenning av brukere og database. |
| `kilde/firestore.rules` | Sikkerhetsreglene. Legges inn manuelt i Firebase-konsollen (Firestore → Rules). |
| `kilde/bygg.py` | Setter sammen `index.html` fra filene over. |

## Endre appen

1. Gjør endringen i filene under `kilde/` (som regel `kilde/verkstedpaaminner.html`).
2. Kjør `python3 kilde/bygg.py` fra rotmappen for å lage ny `index.html`.
3. Commit og push. GitHub Pages er oppdatert etter 1–2 minutter.

Kundedata ligger i Firebase (europe-north1) og påvirkes ikke av endringer i koden.
