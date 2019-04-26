from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from datetime import datetime
from django.contrib.auth.decorators import login_required
from questions.models import Questions
import random
def homepage(request):
    return render(request,'homepage.html',{})
    
def Login(request):
    if request.method=="POST":
        user = authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            if user.is_FirstLogin==True:
                user.FirstLogin=datetime.now()
                user.is_FirstLogin=False
                user.save()
            return redirect("/start")

def start(request):
    return render(request,"start.html",{})
    
def random_questions(questions_attempted):
    while(True):
        x=random.randint(1,)
        t=list(map(int,questions_attempted.split()))
        print(t)
        if x not in t:
            q=Questions.objects.filter(question_id=x).values_list('question','question_id','question_is_active')[0]
            if q[2]:
                return q 
@login_required
def question(request):
    # return HttpResponse("Working")
    l=request.user.questions_attempted
    q=random_questions(l)
    request.user.questions_attempted=request.user.questions_attempted +" "+str(q[1])
    request.user.save()
    return HttpResponse(q[0])
    