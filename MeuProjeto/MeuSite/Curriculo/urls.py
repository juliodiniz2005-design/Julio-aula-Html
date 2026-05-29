from django.urls import path
from Curriculo import views

app_name = 'Curriculo'

urlpatterns = [
    path("curriculo1/", views.Curriculo1, name="Curriculo1"),
    path("curriculo2/", views.Curriculo2, name="Curriculo2"),
]