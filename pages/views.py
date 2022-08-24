from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# request is the object which is passed and response is returned
# response is an object
# This is an FBV object 
# class based views have better dry(dont repeat yourself)
def homePageView(request):return HttpResponse("Hello World")

