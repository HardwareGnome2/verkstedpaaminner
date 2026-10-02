# Bygger index.html (Firebase-utgaven) fra filene i denne mappen.
# Kjør fra repoets rot:  python3 kilde/bygg.py
import os

HER = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.dirname(HER)

def les(navn):
    with open(os.path.join(HER, navn), encoding='utf-8') as f:
        return f.read()

s = les('verkstedpaaminner.html')          # hovedappen (samme fil som Claude-artefakten)
innlogging = les('innlogging.html')        # innloggingsskjerm og stil
modul = les('firebase-modul.html')         # Firebase-kobling (innlogging, godkjenning, database)

assert s.count('<body>') == 1 and s.count('<script>\n"use strict";') == 1 and s.count('</body>') == 1
s = s.replace('<body>', '<body>\n' + innlogging, 1)
s = s.replace('<script>\n"use strict";', '<script>window.VERKSTED_SKY = true;</script>\n<script>\n"use strict";', 1)
s = s.replace('</body>', modul + '\n</body>', 1)

with open(os.path.join(ROT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(s)
print('index.html bygget,', len(s), 'tegn')
