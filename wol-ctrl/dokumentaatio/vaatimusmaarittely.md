# Sovellusmäärittely

## Sovelluksen tarkotus
Sovellus tarjoaa yksinkertaisen käyttöliittymän järjestelmien etä käynnistämiseen wol-kutsuja (wake-on-lan) kutsuja käyttäen. 
Sovellus tarjoaa mahdollisuuden hallita laitteiden tietoja. Lisätä uusia laitteita, poistaa vanhoja laitteita.
Säilytettäviä tietoja ovat wol kutsun vaatimat tiedot (ip- ja mac-osoite) sekä laitteen uniikki nimi. Laitteet ovat myös sidottu laitteen
lisänneeseen käyttäjään.

## Käyttäjät
Sovelluksessa on yhdentasoisia käyttäjiä. Käyttäjällä on pääsy hänen omiin laitteisiinsa. Laitteet eivät näy ristiin käyttäjien välillä.
Järjestelmässä on testailua ja demoamista varten valmiiksi populoitu oletuskäyttäjä 'admin' jota voi käyttää salasanalla 'admin'

## Toiminnallisuu
Järjestelmässä voi luoda uusia käyttäjiä kirjautua käyttäjällä sisään sekä lisätä ja poistaa laitteita. Tämän lisäksi sovelluksella voi
lähettää WOL kutsun. Ohjelma generoi laitekohtaisen 'magic' paketin ja esittää sen myö käyttäjälle tekstimuodossa.

### Näkymät
Ohjelma koostuu kolmesta näkymästä. Ensimmäisenä käyttäjä aloittaa kirjatumisnäkymästä. Kirjautumisnäkymässä käyttäjä voi kirjautua sisään
jo luodun käyttäjän tilille. Näkymästä voi siirtyä myös luomaan uuden käyttäjän. Käyttäjän luomis näkymässä käyttäjä siirretään automaattisesti
luonnin jälkeen sovelluksen päänäkymään. Päänäkymässä käyttäjän laitteet on listattuna. Kun käyttäjä lisää uuden laitteen lisätään se näkymään.
Laitteita voi myös poistaa ja niihin voi lähettää wol kutsuja. Jos laitteen lisäys tai wol-kutsun lähetys epäonnistuu esitetään asia käyttäjälle
status alueiden kautta.

## WOL-VIESTI
Tässä liitteen esimerkkikuva sovelluksen lähettämästä WOL-viestistä verkkoliikenteestä kaapattuna.
![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/testing.png)

## Jatkokehitysideita
Sovelluksissa voisi olla käyttäjä joukkoja joilla olisi käytössä yhteisiä laitteita. Sovelluksessa voisi olla myös eritasoisia käyttäjiä siten että
joillakin käyttäjillä on laajemmat oikeudet. Tämä mahdollistaisi esimerkiksi käyttäjien hallinnan.
