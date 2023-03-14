from django.urls import path
from app2 import views as v2




urlpatterns = [
    path ('port/',v2.port)
]

