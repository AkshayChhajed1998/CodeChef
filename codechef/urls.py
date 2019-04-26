"""codechef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import r3finishf,r3finish,Qrender,ret_list,nextpage,skip,homepage,Login,start,question,logintime,finish,Logout,buzz_question,r3homepage,r3start,r3Login,ret_currentQ
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',homepage),
    url(r'^login$',Login),
    url(r'^start$',start),
    url(r'^get/question$',question),
    url(r'^get/firstlogintime$',logintime),
    url(r'^finish$',finish),
    url(r'^logout$',Logout),
    url(r'^r3home$',r3homepage),
    url(r'^r3login$',r3Login),
    url(r'^r3start$',r3start),
    url(r'^r3get/question$',buzz_question),
    #url(r'^get/firstlogintime$',logintime),
    url(r'^r3get/currQ$',ret_currentQ),
    url(r'^r3skip$',skip),
    url(r'^nextpage$',nextpage),
    url(r'^user_list$',ret_list),
    url(r'^Qrender$',Qrender),
    url(r'^r3finish$',r3finish),
    url(r'^r3finishf$',r3finishf)

]
