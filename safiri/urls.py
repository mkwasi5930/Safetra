from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='Home'),
    path('Udrive',views.SelfDrive,name='Udrive'),
    path('Sublet',views.LetCar,name='Sublet'),
    path('Taxcab',views.TaxCab,name="Taxcab"),
    path('About',views.About,name= 'About'),
    path('thanks',views.thanksPage,name='thanks'),
]