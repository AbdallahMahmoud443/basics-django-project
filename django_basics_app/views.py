import datetime
from django.http import HttpResponse
from django.shortcuts import render
import requests

from django_basics_app.models import Authors



# Create your views here.


#* Function Based View
def Home(request):
    pagePath ="django_basics_app/home.html"
    return render(request,pagePath)

def Index(request):
    pagePath ="django_basics_app/index.html"
    return render(request,pagePath)

def About(request):
    return HttpResponse("<h1> About Page </h1> <p>Welcome To Our Website Our Team Happy To Login In Website</p>") #* Response

def Service(request):
    content="<h1> Services Page</h1><p> Service 1 </p> <p> Service 2 </p><p> Service 3 </p><p> Service 4 </p>"
    return HttpResponse(content) #* Response

def GetPost(request): #* function with get request
    #*  get,post,delete,patch
    message=''
    if(request.method == "GET"):
        if(request.GET.get("postNumber") and request.GET.get("post")):
             message = f"<h1>Post Number : {request.GET.get("postNumber")}</h1><h2>Content : {request.GET.get ("post")}</h2>"
        else:
            message = "<h2>Invalid Post :(</h2>"
            
        return HttpResponse(message);


def ShowDateTime(request):
    Today = datetime.datetime.now()
    PagePath = "django_basics_app/showdateTime.html" #* Path of html page
    dict = {'today':Today}
    return render(request,PagePath,dict) #* dict is context send to HTML template


import logging
def ShowLoggingsMessages(request):
    logging.debug(f"Debug Message #1 dateTime: {datetime.datetime.now()}")
    logging.info("Info messages #2")
    logging.warn("Warning Message #3")
    logging.error("Error Message #4")
    logging.critical("critical Message #5")
    
    custom_logger = logging.getLogger("myCunstom_Logger");
    custom_logger.debug(f"Debug Message #1 dateTime: {datetime.datetime.now()}")
    custom_logger.info("Info messages #2")
    custom_logger.warn("Warning Message #3")
    custom_logger.error("Error Message #4")
    custom_logger.critical("critical Message #5")
    return HttpResponse("LoggingMessages in console")

def ShowIfTagDemo(request):
    PagePath='django_basics_app/IfTagDemo.html'
    user ={"UserName":"Abdallah Mahmoud",
          "Age":26,
          "IslogedIn":True,
          "Role":"Admin",
          "Country":"Egypt",
          "JobTitle":"Django Developer",
          "WorkExperience":5,
          "Skills":["Reactjs","php",".net","ux","ui"],
          "StatusCode":None,
          }
    dict = {"user":user}
    return render(request,PagePath,dict)

def ShowProducts(request):
    Products =[];
    Products.append( {'productID':1,'productName':"AMD Ryzen 3990",'quantity':100,'unitsInStock':50,'disContinued':False,'cost':3000})
    Products.append( {'productID':2,'productName':"AMD Ryzen 3980",'quantity':100,'unitsInStock':50,'disContinued':False,'cost':4000})
    Products.append( {'productID':3,'productName':"AMD Ryzen 3970",'quantity':100,'unitsInStock':50,'disContinued':False,'cost':5000})
    Products.append( {'productID':4,'productName':"AMD Ryzen 3960",'quantity':100,'unitsInStock':50,'disContinued':False,'cost':6000})
    Products.append( {'productID':5,'productName':"AMD Ryzen 3950",'quantity':100,'unitsInStock':50,'disContinued':False,'cost':7000})
    Products.append( {'productID':6,'productName':"AMD Ryzen 3940",'quantity':100,'unitsInStock':50,'disContinued':True,'cost':8000})
    Products.append( {'productID':7,'productName':"AMD Ryzen 3930",'quantity':100,'unitsInStock':50,'disContinued':True,'cost':9000})
    Products.append( {'productID':8,'productName':"AMD Ryzen 3920",'quantity':100,'unitsInStock':50,'disContinued':True,'cost':10000})
    Processors = [
    {'Category': 'AMD', 'processors': ['Ryzen 3990', 'Ryzen 3970','Ryzen 3960','Ryzen 3950']},
    {'Category': 'Intel', 'processors':['Xeon 8362', 'Xeon 8358','Xeon 8380']}
  ];
    PagePath='django_basics_app/forTagDemo.html'
    dict ={"products":Products,"ProductsCount":len(Products),"Processors":Processors}
    return render(request,PagePath,dict);


def GetAllUserFromAPI():
    BASE_PATH = "https://fakestoreapi.com"
    response = requests.get(f"{BASE_PATH}/users")
    usersData = response.json();
    return usersData

def GetAllUsers(request):
    users = GetAllUserFromAPI();
    PagePath = "django_basics_app/showAllUsers.html";
    dict = {"users":users}
    return render(request,PagePath,dict)



def GetAllUsersWithCard(request):
    users = GetAllUserFromAPI();
    image ="https://i.pravatar.cc"
    PagePath = "django_basics_app/showAllUsers2.html";
    dict = {"users":users,"image":image}
    return render(request,PagePath,dict)

def GetUserFromAPI(User_id):
    BASE_PATH = "https://fakestoreapi.com"
    
    response = requests.get(f"{BASE_PATH}/users/{User_id}")
    userData = response.json();
    return userData

def GetUserById(request):

    if request.method == "POST":
        User_id = int(request.POST.get("userID"))
        if request.POST.get("btnNext"):
            User_id +=1
            if User_id >=11:
                User_id=1
        if request.POST.get("btnPrevious"):
            User_id -=1
            if User_id == 0:
                User_id =10
    else:
        User_id = 1

    pagePath = "django_basics_app/showUser.html"
    userData=GetUserFromAPI(User_id)
    image ="https://i.pravatar.cc"
    dict={"user":userData,"image":image}
    return render(request,pagePath,dict)

def PassDataFromModelToTemplate(request):
    author1=  Authors("Ahmed Ali","Egypt","White Days")
    pagePath = "django_basics_app/modelwithtemp.html"
    AuthorsList=[]
    AuthorsList.append(Authors('Lesnor', "USA","UFC"))
    AuthorsList.append(Authors('Nate Diaz', "USA","UFC"))
    AuthorsList.append(Authors('Nick Diaz', "USA","UFC"))
    AuthorsList.append(Authors('Johnson', "USA","UFC"))
    AuthorsList.append(Authors('Connors McGregor', "USA","UFC"))
    AuthorsList.append(Authors('Michael Chandler', "USA","UFC"))
    dict={"author":author1,"authors":AuthorsList}
    return render(request,pagePath,dict)

def BuiltInFiltter(request):
    pagePath = "django_basics_app/builtinfilters.html"
    Processors=[
    {"name": "Ryzen 3970", "cores": 32},
    {"name": "Ryzen 3950", "cores": 16},
    {"name": "Ryzen 3990", "cores": 64},
                ]
    dict={
        "ProbationPeriod":4,
        "FirstName":"Connors",
        "LastName":"McGregor",
        "PayForFight":123456,
        "FirstQuarter":["Jan","Feb","Mar"],
        "SecondQuarter":["Apr","May","Jun"],
        "FQuarter":[1,2,3],
        "SQuarter":[4,5,6],
        "AboutMe":"i'am Notorious and I'am Ruthless too!",
        "now":datetime.datetime.now(),
        "PreviousFight":"",
        "NextFight":None,   
        "Processors":Processors,
        "Message":"<h1>I am using escape</h1>",
        "WebSite":"https://www.uiacademy.co.in"
    }
    return render(request,pagePath,dict)

def CustomFilter(request):
    pagePath = "django_basics_app/customfilters.html"
    webframeworks={        
        'Description':'Django is a Python framework that makes it easier to create dynamic web sites using Python',
        'InDemand':'4.8',
        'PollNumber':57650}
    return render(request,pagePath,webframeworks)

def staticFiles(request):
    pagePath = "django_basics_app/staticfiles.html"
 
    return render(request,pagePath)