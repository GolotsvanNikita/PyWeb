from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('clonning/', views.clonning, name='clonning'),
    path('layouting/', views.layouting, name='layouting'),
    path('lottery/', views.lottery, name='lottery'),
    path('params/', views.params, name='params'),
    path('statics/', views.statics, name='statics'),
]

'''
Д.З. Реалізувати у файлі-шаблоні додатковий блок "footer"
який розміщуватиметься у footer-і.
Перенести до нього відомості про "Сторінка завантажена о"
Заповнювати ці дані з контексту при завантаженні.
'''