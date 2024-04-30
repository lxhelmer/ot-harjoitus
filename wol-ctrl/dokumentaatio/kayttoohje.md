# Käyttöohje

## Asennus
### Siirry kansioon wol-ctrl

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```


2. Alusta ohjelma komennolla

```bash
poetry run invoke init
```

3. Sovellus käynnistetään komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoidaan komennolla:

```bash
poetry run invoke coverage-report
```

### Koodin laatu

Ohjelmakoodille voi ajaa linttauksen komennolla:
```bash
poetry run invoke lint
```

### OHJELMAA VOI TÄLLÄ HETKELLÄ KÄYTTÄÄ TUNNUKSIN "admin", "admin"



## Ohjelman näkymät 
Käyttäjätunnusten syöttö

Syöttämällä käyttäjätunnukset admin, admin pääsee järjestelmään sisälle.

![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/login_view.png)

Jäjestelmässä on valmiiksi muutama laiteobjekti.

![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/populated_device_view.png)

Uuden laitteen voi lisätä täyttämällä tyhjät kentät ja painamalla Add

![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/new_dev.png)

Uusi laite näkyy heti lisättynä listalla muiden laitteiden kanssa. Laitteita voi halutessaan poistaa
laitteen viereisestä Delete napista.

![img](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/new_in_list.png)
