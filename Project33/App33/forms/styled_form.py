# Інструментарій Django для роботи з формами
from django import forms

# класи-форми описують склад форм у вигляді спеціальних елементів
class StyledForm(forms.Form) :
    first_name = forms.CharField(
        min_length=2, 
        max_length=6, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести ім'я",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 64 символи"
        })
    
    last_name  = forms.CharField(
        min_length=2, 
        max_length=6, 
        label="Прізвище",
        error_messages={
            'required': "Необхідно ввести прізвище",
            'min_length': "Прізвище повинно мати щонайменше 2 символи",
            'max_length': "Прізвище не повинно перевищувати 64 символи"
        })
'''
Д.З. Додати до стилізованої форми поле для введення телефона
Реалізувати валідацію на довжину 10 символів
Прикласти скріншоти роботи сторінки у різних режимах
'''