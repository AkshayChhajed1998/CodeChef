from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from datetime import datetime
from django.contrib.auth.decorators import login_required
from questions.models import Questions
import random
from django.core import serializers

def homepage(request):
    return render(request,'homepage.html',{'user':request.user})
    
def Login(request):
    if request.method=="POST":
        user = authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            if request.POST.get("language")=='1':
                user.language_selected=True
            else:
                user.language_selected=False
            if user.is_FirstLogin==True:
                user.FirstLogin=datetime.now()
                user.is_FirstLogin=False
            user.save()
            return redirect("/start")
        else:
            return render(request,"login.html",{'e':'INCORRECT CREDENTIALS'})
    else:
        return render(request,"login.html",{'e':' '})

def start(request):
    return render(request,"start.html",{})
    
def random_questions(questions_attempted,b):
    while(True):
        n=Questions.objects.count()
        x=random.randint(1,n)
        t=list(map(int,questions_attempted.split()))
        print(t)
        active_questions = Questions.objects.filter(question_is_active=True,language_option=b).count()
        if not len(t)==active_questions: 
            if x not in t:
                q=Questions.objects.filter(question_id=x).values_list('question','question_id','question_is_active','language_option')[0]
                if q[2] and q[3] == b:
                    return q
        else:
            return None 
@login_required
def question(request):
    # return HttpResponse("Working")
    ID=request.GET['ID']
    if not ID==' ': 
        Q=Questions.objects.filter(question_id=ID)[0]
        setattr(Q,'question_is_active',True)
        Q.save()    
    l=request.user.questions_attempted
    b=request.user.language_selected
    q=random_questions(l,b)
    if not q==None:
        request.user.questions_attempted=request.user.questions_attempted +" "+str(q[1])
        request.user.save()
        Q=Questions.objects.filter(question_id=q[1])[0]
        setattr(Q,'question_is_active',False)
        Q.save()
        data = serializers.serialize("json",[Q,])
        print(data[1:-1])
        return HttpResponse(data[1:-1])
    else:
        msg="Questions are Finished!!"
        return HttpResponse('<h1>'+msg+'</h1><input type="button" id="logout" onclick="location.href=\'/logout\';" value="LOGOUT" />')
         

def logintime(request):
    return HttpResponse(request.user.FirstLogin)

def finish(request):
    ID=request.GET['ID']
    msg="Time Over"
    if not ID==' ': 
        Q=Questions.objects.filter(question_id=ID)[0]
        setattr(Q,'question_is_active',True)
        Q.save()
    return HttpResponse('<h1>'+msg+'</h1><input type="button" id="logout" onclick="location.href=\'/logout\';" value="LOGOUT" />')

def Logout(request):
    logout(request)
    return redirect('/')

##########################################################ROUND 3########################################################################################

questions=0
players = 5
skipc=0

def buzz_random_questions():
    while(True):
        n=Questions.objects.count()
        x=random.randint(137,137+n)
        #t=list(map(int,questions_attempted.split()))
        #print(t)
        active_questions = Questions.objects.filter(question_is_active=True).count()
        if not active_questions==0: 
        #    if x not in t:
            q=Questions.objects.filter(question_id=x).values_list('question_id','question_is_active')[0]
            if q[1]:
                return q[0]
        else:
            return 0


def buzz_question(request):

    global questions
    global players
    buzz = request.GET['buzz']
    questions = buzz_random_questions()
    #if count<players:
    #    count=count+1
    #else:
    #    count=0
    if questions is 0:
        msg="Questions are Finished!!"
        return HttpResponse("<h1>"+msg+"</h1><input type=\"button\" id=\"nextpage\" onclick=\"location.href=\'/nextpage\'\" value=\"Next Page\" />")
    else:
        print(questions)
        Q=Questions.objects.filter(question_id=questions)[0]
        setattr(Q,'question_is_active',False)
        Q.save()
        data = serializers.serialize("json",[Q,])
        if buzz=='1':
            request.user.questions_attempted=request.user.questions_attempted +" "+str(questions)
            request.user.save()
        print(data[1:-1])
        return HttpResponse(data[1:-1])

def ret_currentQ(request):
    global questions
    if not questions==0:
        Q=Questions.objects.filter(question_id=questions)[0]
        data = serializers.serialize("json",[Q,])
        return HttpResponse(data[1:-1])
    else:
        msg="Questions are Finished!!"
        return HttpResponse("<h1>"+msg+"</h1><input type=\"button\" id=\"nextpage\" onclick=\"location.href=\'/nextpage\'\" value=\"Next Page\" />")

def r3homepage(request):
    return render(request,'round3_home.html',{'user':request.user})
    
def r3Login(request):
    if request.method=="POST":
        user = authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user is not None:
            login(request,user)
            if request.POST.get("language")=='1':
                user.language_selected=True
            else:
                user.language_selected=False
            if user.is_FirstLogin==True:
                user.FirstLogin=datetime.now()
                user.is_FirstLogin=False
            user.save()
            return redirect("/r3start")
        else:
            return render(request,"round3_login.html",{'e':'INCORRECT CREDENTIALS'})
    else:
        return render(request,"round3_login.html",{'e':' '})

def r3start(request):
    return render(request,"round3.html",{})

def skip(request):
    global skipc
    global questions
    global players
    skipc=skipc+1
    if skipc==players:
        questions = buzz_random_questions()
        skipc=0
    return HttpResponse("Success")

def nextpage(request):
    return render(request,'sel_questions.html',{})

def ret_list(request):
    print(request.user.questions_attempted)
    return HttpResponse(request.user.questions_attempted)

def Qrender(request):
    ID = request.GET['ID']
    Q = Questions.objects.filter(question_id=ID)[0]
    data = serializers.serialize("json",[Q,])
    print(data[1:-1])
    return HttpResponse(data[1:-1])

def r3finish(request):
    msg="It's Time for solving Selection";
    return HttpResponse("<h1>"+msg+"</h1><input type=\"button\" id=\"nextpage\" onclick=\"location.href=\'/nextpage\'\" value=\"Next Page\" />")

def r3finishf(request):
    msg="Time Over";
    return HttpResponse('<h1>'+msg+'</h1><input type="button" id="logout" onclick="location.href=\"/logout\";" value="LOGOUT" />')
