#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def description(self):
        print("%s :\n taille = %s") %(self.name, self.weight)


class Spell(Item):
    def __init__(self,  name, weight, cost, damage):
        Item.__init__(self, name, weight)
        self.cost = cost
        self.damage = damage

    def use(self, character):
        if character.mana > self.cost:
            character.mana -= self.cost

    def description(self):
        print("%s :\n taille = %s \n coût en Mana = %s \n dommage = %s") %(self.name, self.weight, self.cost, self.damage)


class Apple(Item):
    def __init__(self, weight, gain):
        Item.__init__(self, "Apple", weight)
        self.gain = gain
    
    def use(self, character):
        character.health += self.gain
