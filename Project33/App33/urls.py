from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clonning/', views.clonning, name='clonning'),
    path('forms/', views.forms, name='forms'),
    path('form-styled/', views.form_styled, name='forms_styled'),
    path('hello/', views.hello, name='hello'),
    path('layouting/', views.layouting, name='layouting'),
    path('params/', views.params, name='params'),
    path('statics/', views.statics, name='statics'),
]

'''
Д.З. Реалізувати у файлі-шаблоні додатковий блок "footer"
який розміщуватиметься у footer-і.
Перенести до нього відомості про "Сторінка завантажена о"
Заповнювати ці дані з контексту при завантаженні.
'''