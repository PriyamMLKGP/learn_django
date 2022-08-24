from django.urls import path
from .views import homePageView
# python regex for empty string
# reference to homepageview
# optional - named url pattern "home"
# if user request empty string "" django called homepageview
urlpatterns=[path("",homePageView,name="home"),]