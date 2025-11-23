# Інструментарій Django для роботи з формами
from django import forms
from django.core.exceptions import ValidationError
import re   # regular expressions

# класи-форми описують склад форм у вигляді спеціальних елементів
class RegForm(forms.Form) :
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Ім'я"}),
        min_length=2, 
        max_length=64, 
        label="Ім'я",
        error_messages={
            'required': "Необхідно ввести ім'я",
            'min_length': "Ім'я повинно мати щонайменше 2 символи",
            'max_length': "Ім'я не повинно перевищувати 64 символи"
        })
    
    last_name  = forms.CharField(
        min_length=2, 
        max_length=64, 
        label="Прізвище",
        error_messages={
            'required': "Необхідно ввести прізвище",
            'min_length': "Прізвище повинно мати щонайменше 2 символи",
            'max_length': "Прізвище не повинно перевищувати 64 символи"
        })
    
    login  = forms.CharField(
        min_length=2, 
        max_length=64, 
        label="Логін",
        error_messages={
            'required': "Необхідно ввести логін",
            'min_length': "Логін повинен мати щонайменше 2 символи",
            'max_length': "Логін не повинен перевищувати 64 символи"
        })
    
    email  = forms.CharField(
        min_length=2, 
        max_length=128, 
        label="E-mail",
        error_messages={
            'required': "Необхідно ввести E-mail",
            'min_length': "E-mail повинен мати щонайменше 2 символи",
            'max_length': "E-mail не повинен перевищувати 128 символів"
        })
    
    phone  = forms.CharField(
        min_length=10, 
        max_length=16, 
        label="Телефон",
        error_messages={
            'required': "Необхідно ввести телефон",
            'min_length': "Телефон повинно мати щонайменше 10 символів",
            'max_length': "Телефон не повинно перевищувати 16 символів"
        })
    
    birthdate  = forms.DateField(
        label="Дата народження",
        required=False)    

    password = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': "Необхідно ввести пароль"
        }
    )

    repeat = forms.CharField(                         # повтор паролю
        widget=forms.PasswordInput(), 
        required=False )
    
    is_agree = forms.BooleanField(
        help_text="Я приймаю політику конфіденційності сайту",
        error_messages={
            'required': "Ви маєте погодитись з політикою конфіденційності сайту"
        }
    )


    def clean(self):                                  # Custom validation
        cleaned_data = super().clean()                # базова валідація
        if 'password' in cleaned_data :               # Умова на те, що пароль пройшов базову валідацію
            password = cleaned_data['password']       # Беремо за основу значення, що пройшло перевірку
            if len(password) < 4 :                    # та додаємо наступну групу перевірок
                self.add_error(                       # Реєструємо нову помилку валідації
                    "password",                       #  для поля "password"
                    ValidationError("Пароль має містити принаймні 4 символи"))
            if not re.search(r"\d", password) :       # умова від зворотнього - не знайдено цифру
                   self.add_error(                    # без elif - обидві помилки можуть
                    "password",                       # бути одночасно
                    ValidationError("Пароль має містити принаймні одну цифру"))
                   
        if 'repeat' in cleaned_data :        
            repeat = cleaned_data['repeat']
            if repeat != cleaned_data.get('password', '') :
                self.add_error(
                    'repeat',
                    ValidationError("Повтор не збігається з паролем")
                )

        if 'first_name' in cleaned_data :        
            first_name = cleaned_data['first_name']   # використання регулярного виразу-шаблону 
            if re.search(r"\d", first_name):          # для пошуку в імені довільної цифри
                self.add_error('first_name',
                    ValidationError("В імені не допускаються цифри"))
                
        return cleaned_data
            

'''
Спадкування (ООП)
super: [data method()]
child(super):
    method():... ?? переозначення "стирає" старий метод або додає новий?
                 !! додає новий: існують обидва методи: child.method, super.method 

Регулярні вирази - шаблони (мова шаблонів) для задач оброблення рядків                                
Ідея - використання спец.символів:
Набори:
\d - будь-яка цифра    "\d" - одна цифра, "\d\d" - дві цифри поспіль 
\D - не-цифра          "\d\D\d" - дві цифри, розділені будь-яким символом, що не є цифрою
\w - word-символ (припустимий в іменах змінних: малі, великі літери, цифри та "_") 
\W - non-word
\s - space-symbol (пробіл, табуляція тощо)
\S - non-space
[asd] - один символ з набору допустимих символів (символи перелічуються без роздількиків,
            [a,s,d] - asd та ",")
[a-f], [a-fA-F] - один символ з діапазону
[^asd], [^a-f] - окрім зазначених символів            
'''