from ClassLightBot import *

r = LightBot('subor1.txt', (3, 4, 2))
print(r)
r.rob('kkpkkkzlk')
print(r.robot())
print(r)
print(r.kolko())





# a= LightBot("subor1.txt",(1,2,3))
#
# print(a)
# print(a.kolko())
# ['4 5\n', '2 3 1\n', '0 2 0 s\n', '1 3 2']
#riadok stlpec vyska

#[[g/w/l,bool: visited,int: height, bool: on/ off]]


# l, p = otočí sa vľavo, resp. vpravo o 90 stupňov
#
# k = urobí krok dopredu, ale len vtedy,
#     ak je toto políčko v rovnakej výške ako to, na ktorom stojí
#
# s = skočí na políčko pred sebou, ale len vtedy,
#     ak je buď o jedna vyššie alebo ľubovoľne (aspoň o 1) nižšie
#
# z = zasvieti, resp. zhasne políčko pod sebou
#     (len ak má toto políčko svoju lampu)