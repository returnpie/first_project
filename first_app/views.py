from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': "Hello i want to prettier..!!!"}
    return render(request, 'first_app/index.html', context=my_dict)


def help_view(request):
    return render(request, 'first_app/help.html')