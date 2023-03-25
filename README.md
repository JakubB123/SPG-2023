# SPG-2023
HomeWork

# Zadanie skúšky z 21.1.2019 - Robot Light-Bot
Robot Light-Bot sa veľmi sa podobá na robota Karla:

robot sa pohybuje v štvorcovej sieti, v ktorej sa môžu nachádzať tehličky (môže ich byť aj viac na sebe)
niektoré políčka (aj s tehličkami) sa dajú zasvietiť, resp. zhasnúť (políčka majú svoju lampu, a predstavte si, že tehličky sú polopriesvitné)
robot sa pohybuje len v rámci svojej štvorcovej siete týmito príkazmi:

- l, p = otočí sa vľavo, resp. vpravo o 90 stupňov
- k = urobí krok dopredu, ale len vtedy, ak je toto políčko v rovnakej výške ako to, na ktorom stojí
- s = skočí na políčko pred sebou, ale len vtedy, ak je buď o jedna vyššie alebo ľubovoľne (aspoň o 1) nižšie
- z = zasvieti, resp. zhasne políčko pod sebou (len ak má toto políčko svoju lampu)

Trieda LightBot:

    class LightBot:
        def __init__(self, meno_suboru, pozicia_robota):
            ...

        def robot(self):
            return ()

        def __str__(self):
            return ''

        def rob(self, prikazy):
            ...

        def kolko(self):
            return ()
Metódy:

**__init__(meno_suboru, pozicia_robota):**


subor má tento formát:

v prvom riadku sú dve celé čísla = počet riadkov a stĺpcov štvorcovej siete

každý ďalší riadok popisuje jedno políčko siete, pričom obsahuje buď tri celé čísla,

alebo tri čísla a ľubovoľný nemedzerový reťazec v tvare:

  **riadok stĺpec počet_tehličiek
  
  riadok stĺpec počet_tehličiek lampa**
  
v druhom prípade má dané políčko svoju lampu (lampy sú na začiatku zhasnuté)

všetky ostatné políčka v ploche sú prázdne bez tehličiek a bez lampy

parameter pozicia_robota = trojica čísel (riadok, stĺpec, smer), 

kde smer je číslo od 0 do 3 (pre východ, juh, západ, sever

**robot():**


vráti momentálnu pozíciu robota ako trojicu čísel (riadok, stĺpec, smer)

**__str__():**


vráti popis plochy, pričom pre každé políčko:

tam, kde je lampa a svieti, znak 'O', kde nesvieti 'o'

inak, kde bol robot '+', kde ešte nebol '.'

**rob(prikazy):**

parameter prikazy = postupnosť písmen z 'lpksz' (iné znaky ignoruje)

postupne vykoná príkazy, ak sa niektorý vykonať nedá, 

tento jeden ignoruje a pokračuje ďalšími príkazmi v postupnosti

metóda nič nevracia

**kolko():**


vráti dvojicu: počet nerozsvietených políčok s lampou a počet rozsvietených

Napr. pre súbor 'subor1.txt':

    4 5
    2 3 1
    0 2 0 s
    1 3 2
takýto test:

    if __name__ == '__main__':
        r = LightBot('subor1.txt', (3, 4, 2))
        print(r)
        r.rob('kkpkkkzlk')
        print(r.robot())
        print(r)
        print(r.kolko())
vypíše:

    ..o..
    .....
    .....
    ....+
    (0, 1, 2)
    .+O..
    ..+..
    ..+..
    ..+++
    (0, 1)
