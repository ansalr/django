from django.urls import path
from calc import views

urlpatterns = [
    path('',views.home),
    path('wish/',views.wish)
]
