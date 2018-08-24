#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class Board(object):
class Board:
    def __init__(self, width, height) :
        self.grid = []
        self.width = width
        self.height = height
        for lig in range(height):
            self.grid.append([])
            for col in range(width):
                self.grid[lig].append([])

    def move(self, character, x, y):
        if character.x is not None and character.y is not None:
            self.grid[character.x][character.y].remove(character)
        character.x = x
        character.y = y
        self.grid[character.x][character.y].append(character)
        character.move(x, y)
        # print(self.grid)

    def display(self) :
        map = ""
        for line in self.grid:
            row = ""
            for cell in line:
                if not cell:
                    row += "- "
                else:
                    row += "X "
            row +="\n"
            map += row
        print(map)
        return map
