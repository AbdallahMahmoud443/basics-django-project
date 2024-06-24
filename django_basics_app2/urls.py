from django.urls import path
from . import views


urlpatterns = [
    path("",views.Home,name="App2Home"),
    path("home",views.Home,name="App2HomePage")
]
