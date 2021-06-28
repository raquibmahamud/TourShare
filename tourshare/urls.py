

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="tourshare"),
    path("aboutus/",views.about, name="AboutUs"),
    path("createteam/",views.createteam, name="CreateTeam"),
    path("checkout/",views.checkout, name="CheckOut"),
    
    path("jointeam/",views.jointeam, name="JoinTeam"),
    path("signin/",views.signin, name="SignIn"),
    path("signout/",views.signout, name="SignOut"),
    
    path("signup/",views.signup, name="Signup"),
    path("contactus/",views.contactus, name="ContactUs"),

]
