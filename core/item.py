#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def useObject(self):
        print("l'objet a été utilisé")

    def description(self):
        print("%s :\n taille = %s") %(self.name, self.weight)


class Spell(Item):
    def __init__(self,  name, weight, cost, damage):
        Item.__init__(self, name, weight)
        self.cost = cost
        self.damage = damage

    def description(self):
        print("%s :\n taille = %s \n coût en Mana = %s \n dommage = %s") %(self.name, self.weight, self.cost, self.damage)


class Apple(Item):
    def __init__(self, weight, gain):
        Item.__init__(self, "Apple", weight)
        self.gain = gain
