from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page'
}

# Create your views here.
def sports_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    result = num1 + num2
    return HttpResponse(str(result))