# Veiledning for Claude

Appen brukes i kundemottaket på et bilverksted. Eieren skriver norsk (bokmål) – svar på norsk.

## Arbeidsflyt
- Rediger aldri `index.html` direkte. Den bygges med `python3 kilde/bygg.py` fra filene i `kilde/`.
- `kilde/verkstedpaaminner.html` er én selvstendig HTML-fil med all app-logikk. Den kjører også som Claude-artefakt
  (uten Firebase); sky-spesifikk oppførsel styres av `window.VERKSTED_SKY` / konstanten `SKY`.
- Sky-utgaven bruker `kilde/firebase-modul.html`, som gir appen samme `window.claude.use("db" | "user")`-grensesnitt
  som artefakt-runtime, men mot Firestore og Firebase Auth.
- Etter endringer: sjekk JS-syntaks (`node --check` på skriptet), test i nettleser hvis mulig, bygg, og be eieren om
  bekreftelse før push – siden er offentlig.

## Data og sikkerhet
- Firestore-stier: `notater`, `mapper`, `oppslag`, `system/{maler,wipe,oppsett}`, `brukere/{uid}`,
  private notater i `data/users/{uid}/{id}`.
- Roller i `brukere/{uid}.rolle`: admin, bruker, venter, sperret. Første konto blir admin.
- Nye felter i eksisterende dokumenter krever ingen regelendring. Nye samlinger krever oppdatering av
  `kilde/firestore.rules`, og reglene må limes inn manuelt i Firebase-konsollen.
- Kundedata skal aldri lagres i localStorage i sky-utgaven.
