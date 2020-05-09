from django.shortcuts import render
from poll.models import *
from django.http import Http404

# Create your views here.
def index(request):
    context={}
    questions =Question.objects.all()
    context['title'] ='poll' #if you want to show dynami content
    context['questions'] =questions
    return render(request,'poll/index.html',context) #poll/index is becoz indez is inside poll folder in template

def details(request,id=None): #if you pass any thing in the rl you pass the data as argument
    context={}
    try:
        questions =Question.objects.get(id=id)
    except:
        raise Http404

    context['questions'] =questions
    return render(request,'poll/details.html',context)