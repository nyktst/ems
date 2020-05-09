from django.shortcuts import render
from poll.models import *
from django.http import Http404,HttpResponse

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

def poll(request,id=None): #if you pass any thing in the rl you pass the data as argument
    if request.method == "GET":
        context={}
        try:
            questions =Question.objects.get(id=id)
        except:
            raise Http404

        context['questions'] =questions
        return render(request,'poll/poll.html',context)

    if request.method == "POST" :
        user_id = 1
        print(request.POST)
        data =request.POST
        ret = Answer.objects.create(user_id = user_id, choice_id = data['choice'])
        if ret:
            return HttpResponse("successfull")
        else:
            return HttpResponse("error")