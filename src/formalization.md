# Formalizácia

# Matematická formulácia problému

TODO

# Formát psa

Formát `.psa` bol vytvorený pre interné potreby diplomovej práce. Je 
aktuálne iba dočasným riešením. Slúži pre 
testovacie účeli `psa-core`. Formát `.psa` bol inšpirovaný stránkou
[lopez-ibanez.eu](http://lopez-ibanez.eu/tsptw-instances) a je jeho rozšírením.

## Povinné sekcie

Formát je členený na viacero sekcií. Jadro tvoria prvé dve povinné sekcie.
Definujú inštanciu problému *atsp* (z anj. asymmetric travelling salesman problem).

- prvý riadok je prvá sekcia obsahuje jedno číslo, ktoré udáva celkový počet vrcholov $n$ v grafe
- nasledujúcich $n$ riadkov tvorí maticu vzdialeností (distance matrix), 
kde každý riadok má $n$ prvkov oddelených medzerami
- riadok začínájúci znakom `#`, je komentár, ktorý sa ignoruje

Uvádzame ukážku:
```
# prvá sekcia uvádza počet vrcholov
3
# druhá sekcia n riadkov, tvorí maticu vzdialeností
0 13 90
12 0 35
45 35 0
```

## Nepovinné sekcie:

- ak existuje daľších $n$ riadkov, obsahujú dvojice oddelené medzerami, definujú inštanciu problému
*atsp-tw* (asymmetric travelling salesman problem with time windows), kde prvý prvok dvojice je 
najskorší možný čas navštívenia daného vrchola a druhý prvok je najneskorší možný čas navštívenia 
vrchola.

Uvádzame ukážku:
```
...
# tretia sekcia n riadkov, dvojica najskorší a najneskorší čas navštívenia
0 13
12 50
0 66
```

- ďalšia sekcia obsahuje počet vozidiel $i$, ak nie je definované tak $i=1$. Pridaním tejto sekcie,
definujeme inštanciu problému *vrp-tw* (z anj. vehicle routing problem with time windows).

Uvádzame ukážku:
```
...
# pocet vozidiel m, 1 ak nie je definované
1
```

- ďalšia sekcia $m$ riadkov, kde každý riadok udáva kapacitu $i$-teho vozidla. Riadok obsahuje
$j$ prvkov oddelených medzerami, kde každý udáva nejaké kapacitné obmedzenie vozidla. Kapacitné 
obmedzenie vozidla je nezáporné číslo. Je to napríklad hmotnosť zásielky. Pridaním tejto sekcie
definujeme inštanciu problému *cvrp-tw* (z anj. capacited vehicle routing problem with time
windows).

Uvádzame ukážku:
```
...
# m riadkov, kde každý udáva kapacitu vozidla
6
```

- posledných $j$ riadkov, kde každý obsahuje $n$ prvkov. Každý prvok udáva obmedzenie pre
vrchol. Obmedzenie môže byť aj záporné. Suma prvkov v jednom riadku je rovná 0.

Kompletnú ukážku si môžete pozrieť tu: [cvrptw/cvrptw001.psa](./cvrptw/cvrptw001.psa).
