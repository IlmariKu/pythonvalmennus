# Python-kurssin materiaalit

Lataa tämä koodi ylläolevasta Code ja Download Zip-nappulasta.

Seuraa ohjeita ennakkoasennus-sähköpostista

Tilauslomake:
https://ilmariku.github.io/robottikurssi/tilauslomake.html

# Harjoitteet (kurssin jälkeen!)

> Tässä on muutama tehtävä, jolla voit harjoitella robottien kirjoittamista omaa iloa tai hyötyä varten.

> Tehtäviä ei ole erikseen suunniteltu tiettyä tarkoitusta tai päämäärää varten. Voit ihan yhtä hyvin keksiä myös omat tehtäväsi jos koet sen parempana.

> Yleisesti ottaen, oman projektin tekeminen on paras tapa oppia asioita. Jos tiedät jo mitä haluaisit luoda, pääset parhaiten vauhtiin vain aloittamalla projektisi kanssa.

> Jos et tiedä vastausta johonkin kysymykseen tai ongelmaan, googlaile rohkeasti! Aloita kysymyksesi "python" -sanalla ja muotoile englanniksi asia mitä haluaisit tehdä tai minkä kanssa koet ongelmia.

> Harjoituksiin ei ole esimerkkiratkaisuja. Harjoituksissa on kuvattuna miltä oikeanlainen vastaus näyttää

## Harjoite 1. Hae Ylen sivuilta päivän sää ja vertaa sitä asettamaasi helle- tai pakkasrajaan

> Vaikeustaso: Keskitaso

- Mene sivulle www.yle.fi
- Etsi sivun valikoista säästä kertova sivu
- Aseta oma helle- tai pakkasraja koodiin
- Ota sivulta kellonaika, sekä tämänhetkinen lämpötila

![](kuvat/weather1.png 'Päivän sää Ylen sivulla.')

#### Tulosta (print-komento) komentoriville seuraavat asiat:

`Sää Helsingissä on tänään (kellonaika) (päivän lämpötila).`

Jos asettamasi raja ei ylittynyt:

`Hellerajasi (oma arvosi) ei tänään ylittynyt! Hellerajasta jäätiin vaille X astetta.`

Jos raja ylittyi:

`Helleraja ylitetty X asteella! Helsingissä on tänään (päivän sää) lämmintä.`

## Harjoite 2. CSV-tiedoston kirjoittaminen päivän lämpötiloista

> Vaikeustaso: Keskitaso

- Lue samalta sääsivulta päivän kellonajat (kuva alla)

![alt text](kuvat/weather2.png 'Päivän sää Ylen sivulla.')

#### Kirjoita CSV-tiedosto päivän lämpötiloista esimerkin mukaisesti:

- Lue tunnettain olevat tiedot sivulta käyttäen `for`-silmukkaa. Ei siis määrittämällä jokaista sääkohtaa erikseen.

- Lue tiedot sivulta ja kirjoita allaolevan mukainen CSV-taulukko tietokoneellesi sivulta saaduista tiedoista ja tallenna tiedosto nimellä `saatiedot.csv`

| Kellonaika | Sää | Tuntuu kuin | Sademäärä |
| ---------- | --- | ----------- | --------- |
| 13:00      | +19 | +20         | 0 mm      |
| 14:00      | +19 | +21         | 0 mm      |
| 15:00      | +19 | +21         | 0 mm      |
| 16:00      | +19 | +20         | 0 mm      |
| 17:00      | +18 | +19         | 0 mm      |
| 18:00      | +18 | +17         | 0 mm      |
| 19:00      | +17 | +17         | 0 mm      |
| 20:00      | +17 | +16         | 0 mm      |
| 21:00      | +17 | +16         | 0 mm      |

## Harjoite 3.

> Vaikeustaso: Vaikea

- Avaa ylläoleva säätiedosto `saatiedot.csv` koodissasi ja päätä paras aika mennä ulos.

- Paras aika mennä on sateeton ja lämpimin hetki päivästä.

- Lisähaasteena: Laita koodisi tulostamaan komentoriville kuinka monta minuuttia sinun tulee odottaa, jolloin paras aika on. Tähän tarvitset `datetime`-moduulia

- Tulosta tiedot komentoriville tälläisessä muodossa:

> Kello 14:00 on lämpimin sää, +19 astetta ja 0 mm tunnissa sadetta!
