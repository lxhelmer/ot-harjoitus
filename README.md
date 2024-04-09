# Ohjelmistotekniikka, harjoitustyö
**wol** (wake-on-lan) hallintaohjelman. Ohjelmaan voi lisätä hallittavia tietokoneita ja lähettäää *wol* komentoja lähiverkon yli.

## Dokumentaatio

[Changelog](https://github.com/lxhelmer/ot-harjoitus/blob/main/changelog.md)

[vaatimusmäärittely](https://github.com/lxhelmer/ot-harjoitus/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/lxhelmer/ot-harjoitus/blob/main/dokumentaatio/tuntikirjanpito.md)



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
