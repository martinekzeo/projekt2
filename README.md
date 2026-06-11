# Projekt 2 - Bulls and Cows

Jednoducha konzolova hra v Pythonu. Program vygeneruje nahodne ctyrciferne cislo a hrac se ho snazi uhodnout.

## Jak hra funguje

- cislo ma 4 cislice
- cislo nezacina nulou
- zadna cislice se neopakuje
- hrac zadava vlastni tipy
- program po kazdem tipu vypise pocet `bulls` a `cows`

## Vysvetleni

`Bull` znamena, ze cislice je spravna a je i na spravnem miste.

`Cow` znamena, ze cislice je spravna, ale je na spatnem miste.

Priklad:

```text
tajne cislo: 1234
tip hrace:   1325
vysledek:    1 bull, 2 cows
```

## Spusteni projektu

V terminalu spust:

```bash
python3 main.py
```

## Ukazka

```text
Hi there!
----------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
----------------------------------------
Enter a number: 1234
----------------------------------------
1 bulls, 2 cows
----------------------------------------
```
