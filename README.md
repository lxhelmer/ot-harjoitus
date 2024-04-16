# WOL-hallintaohjelmisto
**wol** (wake-on-lan) hallintaohjelman. Ohjelmaan voi lisätä hallittavia tietokoneita ja lähettäää *wol* komentoja lähiverkon yli.

## Dokumentaatio

[Changelog](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/changelog.md)

[Vaatimusmäärittely](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/lxhelmer/ot-harjoitus/blob/main/wol-ctrl/dokumentaatio/tuntikirjanpito.md)


### Siirry kansioon wol-ctrl

## Asennus

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
