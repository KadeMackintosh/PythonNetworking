#!/usr/bin/env python

class Pozdrav:
    def __init__(self, paMeno):
        self.aMeno = paMeno
        self.aPozdravEN = "Hello"
        self.aPozdravSK = "Nazdar"

    def pozdravMna(self, paJazyk):
        if paJazyk == "EN":
            return self.aPozdravEN + " " + self.aMeno
        if paJazyk == "SK":
            return self.aPozdravSK + " " + self.aMeno


jazyk = input("Enter language/Vyberte jazyk (SK/EN): ")
meno = input("Enter name/Zadajte meno: ")

hello = Pozdrav(meno)
pozdrav = hello.pozdravMna(jazyk)

print(pozdrav)




