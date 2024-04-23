# Sovellusmäärittely

## Sovelluksen tarkotus
Sovellus tarjoaa yksinkertaisen käyttöliittymän järjestelmien etä käynnistämiseen wol-kutsuja (wake-on-lan) kutsuja käyttäen. 
Sovellus tarjoaa mahdollisuuden hallita laitteiden tietoja. Lisätä uusia laitteita, poistaa vanhoja laitteita ja muokata laitekohtaisia tietoja. Säilytettäviä tietoja ovat mm laitteelle annetu nimi ja sen IP.

## Käyttäjät
Lähtokohtaisesti järjestelmään voi luoda käyttäjiä ja jokaisella käyttäjällä on sen omat tiedot järjestelmässä joita se voi muokata. Järjestelmään luodaan myös admin tason käyttäjä jolla
on mahdollisuus muokata käyttäjiä ja niiden tietoja.

## Toiminnallisuus
- Järjestelmän etusivuna toimii kirjautumissivu jolla käyttäjä voi kirjautua sisään tai luoda uuden käyttäjän normaaliin tapaan. 
- Käyttäjää luodessa voi valita onko käyttäjä normaali- vai admin-käyttäjä
- Normaali käyttäjä näkee järjestelmään kirjauduttuaan hallitsemiensa laitteiden tilan listana
- Käyttäjällä on heti tässä listauksessa mahdollisuus käynnistää laitteita.
- Käyttäjällä on myös mahdollisuus siirtyä laitekohtaiselle sivulle hallitsemaan laitteen tietoja.
- Admin-käyttäjä kirjauduttuaan näkee admin-käyttäjään hallinnassa olevat käyttäjät.
- Hän voi tästä näkymästä normaalin käyttäjän laitenäkymän tavoin siirtyä muokkaamaan käyttäjäkohtaisia tietoja
- Käyttäjän sivulle siirtyessä admin näkee käyttäjän tavoin käyttäjäkohtaiset hallittavat laitteet.

 ### Yhteenvetona
 Kuusi erillistä näkymää:
 - Kirjautumissivu
 - Käyttäjän luonti sivu
 - Normaalin käyttäjän etusivu jossa laitelistaus
 - Laitekohtainen hallintasivu
 - Admin-käyttäjän normaalikäyttäjä listaus näkymä
 - Admin-käyttäjän normaalikäyttäjä kohtainen hallintasivu
(Admin-käyttäjä käyttää laitteille samoja näkymiä kuin normaalikäyttäjä)

## Jatkokehitys
- Mahdollisuus rajata normaalikäyttäjiä eri joukkouhin
- Admin-käyttäjät voisivat vastaavasti hallita eri joukkoja rajatusti
- Admin käyttäjän mahdollisuus lisätä tietylle joukolle yhteinen laite
- Admin käyttäjän mahdollisuus lisätä laitteita joita normaalikäyttäjä ei voi muokata
- Normaalikäyttäjän mahdollisuus lisätä yksityinen adminkäyttäjien tavoittamattomissa oleva käyttäjä

## Tehty
- Laitteet listataan käyttäjälle
- Käyttäjä voi poistaa tai lisätä laitteen
- Ohjelma toimii graafisessa käyttöliittymässä
- Käyttäjä voi kirjautua sisään (toimii tällä hetkellä vain "admin","admin" tunnuksilla
- Kirjautumisen jälkeen näkymä vaihtuu laitenäkymään
