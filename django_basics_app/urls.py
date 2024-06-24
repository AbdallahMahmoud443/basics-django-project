from django.urls import path
from . import views


urlpatterns =[
    path("",views.Index,name="indexPage"),
    path("index",views.Index,name="indexPage"),
    path("home",views.Home,name="homePage"),
    path("about",views.About,name="aboutPage"),
    path("service",views.Service,name="aboutService"),
    path("post",views.GetPost,name="getPostPage"),
    path("showDateTime",views.ShowDateTime,name="showDateTimePage"),
    path("showloggers",views.ShowLoggingsMessages,name="showloggersPage"),
    path("ifTageDemo",views.ShowIfTagDemo,name="ifTagePage"),
    path("forTageDemo",views.ShowProducts,name="forTagePage"),
    path("showUsers",views.GetAllUsers,name="allUsersPage"),
    path("showUsers2",views.GetAllUsersWithCard,name="allUsersPage2"),
    path("showuser",views.GetUserById,name="showuserPage"),
    path("modelwithtemp",views.PassDataFromModelToTemplate,name="modelwithtempPage"),
    path("builtinfilters",views.BuiltInFiltter,name="builtinfiltersPage"),
    path("customfilters",views.CustomFilter,name="customfiltersPage"),
    path("staticfiles",views.staticFiles,name="staticfilesPage"),

];