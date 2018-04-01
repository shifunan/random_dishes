# -*- coding: utf-8 -*-

import os
os.chdir('/Users/shifunan/Desktop')

from dishes_lib import Ingredient

chinese_name_input = '芹菜'
celery = Ingredient(english_name='celery', chinese_name=chinese_name_input)
print celery.chinese_name
print celery.english_name

print celery.CheckIs(chinese_name_input)
print celery.CheckIs('韭菜')


print(
    str("a = {input}\n"
        "b = {another_input}")
        .format(input=1,
                another_input=2))