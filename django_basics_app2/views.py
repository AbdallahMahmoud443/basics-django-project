from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"django_basics_app2/home.html")