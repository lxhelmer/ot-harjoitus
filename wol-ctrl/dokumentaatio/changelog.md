# Changelog

## Viikko 3
- Lisätty DeviceRepository joka hallitsee listaa laitteista
- Lisätty testit DeviceRepositorylle
- Lisätty yksinkertainen teksti ui testailua ja demoamista varten
- Lisätty invoke toiminnallisuus
## Viikko 4
- Siirretty ohjelman toiminnallisuus graafiseen käyttöliittymään
- Lisätty käyttäjiä varten user respository ja sille testit
- Lisätty koodin laadun seuraamista varten pylint
- Kehitetty päivittyvä rakenne laitteiden esittämiseen graafisessa uissa
## Viikko 5
- Lisätty kirjatusumisnäkymä ja muokattu uin rakennetta helpommin laajennettavaksi
- Lisätty uihin multiView toiminnallisuus
- lisätty kirjatumisesta vastaava LoginService jota UI käyttää
- lisätty LoginServicelle testit
- Toteutettu LoginServiceen salasanan hashing
## Viikko 6
- Lisätty sql backend repsotiorioille (device ja user)
- Muokattu testit toimimaan repositorioiden kassa ja käyttämään omaa testi tietokantaa
- Lisätty poetry run invoke init joka alustaa tietokannat ja lisää tarvittavan data kansion
- Muokattu ui toimimaan uuden tieto skeeman kanssa jossa eri kentät kuin aiemmin
- Lisäty kattavat docstringit
