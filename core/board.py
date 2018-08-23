#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class Board(object):
class Board:
    def __init__(self, width, height) :
        self.grid = []
        self.width = width
        self.height = height
        for lig in range(height):
            lig = []
            self.grid.append(lig)
            for col in range(width):
                lig.append(col)
        # print(self.grid)
    def display(self) :
        for lig in range(self.height):
            line = ""
            for col in range(self.width):
                line += "-"
            line += "\n"
        print(line)    
