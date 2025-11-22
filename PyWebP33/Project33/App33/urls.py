from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('clonning/', views.clonning, name='clonning'),
    path('layouting/', views.layouting, name='layouting'),
    path('lottery/', views.lottery, name='lottery'),
    path('params/', views.params, name='params'),
    path('forms/', views.forms, name='forms'),
    path('statics/', views.statics, name='statics'),
    path('taxi/', views.taxi_car, name='taxi_car'),
    # path('form-delivery/', views.form_delivery, name='form_delivery'),
    path('models/', views.models, name='models'),
    path('form-styled/', views.form_styled, name='forms_styled'),
]

'''
Д.З. Реалізувати у файлі-шаблоні додатковий блок "footer"
який розміщуватиметься у footer-і.
Перенести до нього відомості про "Сторінка завантажена о"
Заповнювати ці дані з контексту при завантаженні.
'''