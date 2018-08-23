#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class Character(object):
class Character:
    def __init__(self, name, health, mana, power, xp):
        self.name = name
        self.health = health
        self.mana = mana
        self.xp = xp
        self.power = power
        self.inventory = []

    # def description(self):
    #     print("%s: \nvie:%s\nmana:%s\nexpérience:%s\nforce:%s\ninventaire:%s") %(self.name, self.health, self.mana, self.xp, self.power, self.inventory)

    # def move(self, x, y):
    #     print("%s se déplace") %(self.name)

    def attack(self, enemy):
        print("%s attaque %s") %(self.name, enemy.name)
        self.xp += 1
        # armor à prevoir
        enemy.health = enemy.health - self.power

    def pick(self, item):
        print("%s ramasse %s") %(self.name, item.name)
        self.inventory.append(item)

    def drop(self, item):
        print("%s jette %s") %(self.name, item.name)
        self.inventory.remove(item)

    def use(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print("%s utilise %s") %(self.name, item.name)
            item.use(self)
        else:
            print("le %s n'est pas disponible") %(item.name)
            raise

# class Wizard(object):
class Wizard(Character):
    def __init__(self, name):
        Character.__init__(self, name, 100, 100, 50, 0)
        self.spells = []

    # def description(self):
    #     print("%s: \nvie:%s\nmana:%s\nexpérience:%s\nforce:%s\ninventaire:%s\nsort:%s") %(self.name, self.health, self.mana, self.xp, self.power, self.inventory, self.spells)

    def invoke(self, spell, enemy):
        if spell in self.inventory:
            print("%s envoie un sort %s à %s") %(self.name, spell.name, enemy.name)
            self.use(spell)
            enemy.health -= spell.damage
        else:
            print("le %s n'est pas disponible") %(spell.name)
            raise

# class Warrior(object):
class Warrior(Character):
    def __init__(self, name, armor):
        Character.__init__(self, name, 200, 0, 300, 0)
        self.armor = armor

    # def description(self):
    #     print("%s: \nvie:%s\nmana:%s\nexpérience:%s\nforce:%s\ninventaire:%s\nsort:%s") %(self.name, self.health, self.mana, self.xp, self.power, self.inventory, self.armor)



# hermelen = Warrior("Hermelen", 100, 50, 1, 25, [], 10)
# hermelen.description()
# dorian = Wizard("Dorian", 100, 50, 1, 25, [], [])
# dorian.description()
