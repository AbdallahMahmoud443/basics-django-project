from django.urls import path
from . import views


urlpatterns = [
    path("",views.Home,name="App3Home"),
    path("home",views.Home,name="App3HomePage")
]
