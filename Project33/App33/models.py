from django.db import models

# Create your models here.
# Моделі - це класи, призначені для відображення на базу даних
# є "представниками" таблиць у БД
class User(models.Model) :                         # в моделях ID створюється автоматично 
    first_name = models.CharField(max_length=64)   # і не вимагає явного оголошення.
    last_name  = models.CharField(max_length=64)   # SQL-аналог: name VARCHAR(64) 
    email      = models.CharField(max_length=128)
    phone      = models.CharField(max_length=16)    
    birthdate  = models.DateField(null=True)  



class Role(models.Model) :
    name = models.CharField(max_length=32)    # опис ролі, очікується, що відповідає посаді співробітника
    create_level = models.IntegerField        # Рівень доступу
    read_level   = models.IntegerField        # до секретних даних
    update_level = models.IntegerField        # з відповідними 
    delete_level = models.IntegerField        # операціями



class Access(models.Model) :
    user  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role  = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    login = models.CharField(max_length=32)    
    salt  = models.CharField(max_length=32)    
    dk    = models.CharField(max_length=32)    


'''
Д.З. Створити модель - журнал доступу до сайту
дата-час
Access з яким відбувся вхід
статус відповіді сервер - число (200/401/...)

Створити міграцію, виконати міграцію, додати скріншот адмін-панелі сайту (з новою моделлю)
'''