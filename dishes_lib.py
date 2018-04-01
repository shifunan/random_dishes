#!/usr/bin/python
# -*- coding: utf-8 -*-
class Ingredient(object):
    '''Contains ingredient info
    
    Attributes:
        english_name: English name of the ingredient
        chinese_name: Chinese name of the ingredient
    '''
    def __init__(self, english_name, chinese_name, other_names=None):
        self.english_name = english_name
        self.chinese_name = chinese_name.decode('utf-8')
        self.names = [self.english_name, self.chinese_name, other_names]
    
    def CheckIs(self, ingredient_name):
        found = False
        for name in self.names:
            if name == ingredient_name.decode('utf-8'):
                found = True
        return found
    
    def Print(self):
        print("Ingredient's name is:\n"
              "\tEnglish name: {english_name}\n",
              "\tChinese name: {chinese_name}\n")

'''
class IngredientList(object):
    def __init__(self, ingredients, quantity):
        return None
        
class Dish(object):
    def __init__(self, english_name, chinese_name, ingredient_list):
'''