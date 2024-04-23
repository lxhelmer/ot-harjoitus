# WOL-hallintaohjelmisto
**wol** (wake-on-lan) hallintaohjelman. Ohjelmaan voi lisätä hallittavia tietokoneita ja lähettäää *wol* komentoja lähiverkon yli.

## Dokumentaatio

[Changelog](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/changelog.md)

[Vaatimusmäärittely](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/arkkitehtuuri.md)

[Viikon 5 release](https://github.com/lxhelmer/ot-harjoitus/releases/tag/viikko5)



## Asennus
### Siirry kansioon wol-ctrl

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Sovellus käynnistetään komennolla:

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

### OHJELMAA VOI TÄLLÄ HETKELLÄ KÄYTTÄÄ TUNNUKSIN "admin" "admin"
