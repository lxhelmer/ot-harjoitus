# Ohjelman rakenne
Ohjelma koostii kolmesta kerroksesta. Käyttöliitymästä, Service/palvelu tasosta ja repositoryistä
Käyttöliittymä toteuttaa käyttäjälle näkyvän toiminnallisuuden. Käyttöliittymä esittää ja hallitsee repositoryjen tietoja joko suoraan tai palvelun kautta.
Yksinkertaisimmat interaktiot käyttöliittymän ja repositoryjen välillä on toteutettu suoraan käyttöliittymäkoodissa, mutta monimutkaisemmat esimerkiksi
käyttäjän sisäänkirjautumisen varmistaminen on oma palvelutasoinen luokka jonka kautta käyttöliittymällä on yhteys repositorioon.
Vastaavasti repositorioiden kannalta yksinkertainen toiminnallisuus on totetettu repositorio luokissa. Esimerkiksi yksinkertaiset lisäys ja poisto ominaisuudet.
Ohjelman äärimmäisenä ulottuvuutena on repositorioiden kommunikaatio tietokannan kanssa. Kommunikaatio tietokantojen kanssa on toteutettu repositorio luokkien osana.

![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/Screenshot%202024-04-16%20at%2023-06-14%20Document%20--%20SmartDraw.png)

# Ohjelman toiminta
Ohjelman käyttöliittymä käynnistetään siten että sille annetaan riippuvuudeksi laiterepositorio. Käyttöliittymä voi laiterepositorio luokkaa
käyttäen hakea, lisätä ja poistaa laitteita.
Järjestelmään kirjautuminen tapahtuu käyttöliittymässä kirjautumispalvelun kautta. Käyttöliittymä antaa syötetyt tunukset kirjautumispalvelulle.
Kirjautumispalvelu saa käyttäjä repositorion jonka avulla se voi tarkistaa käyttöliittymän sille antamien tunnusten oikeellisuuden. 


## Sekvenssikaavio käyttäjän kirjautumisesta ja uuden laitteen lisäämisestä
Esimerkki ohjelmaluokkien välisestä toiminnallisuudesta.

```mermaid
sequenceDiagram
  actor USER
  participant UI
  participant LoginService
  participant UserRepository
  participant DeviceView
  User ->> UI: click "login" button
  UI ->>+ LoginService: login("admin", "admin")
  LoginService ->>+ UserRepository: find_all()
  UserRepository -->>- LoginService: users
  LoginService -->>- UI: True
  UI -> DeviceView: generate()
  USER  ->> DeviceView: fill device info with "id", "dev", "usr"
  USER ->> DeviceView: click "add" button
  DeviceView ->> DeviceRepository: create("id","dev","usr")
  DeviceRepository -->> DeviceView: {"id", "dev", "usr"} 
```

