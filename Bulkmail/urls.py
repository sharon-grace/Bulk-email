"""
URL configuration for Bulkmail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mailapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('create/',views.create),
    path('adduser/',views.adduser),
    path('login1/',views.login1),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    path('viewuser/',views.viewuser),
    path('deleteuser/<int:id>',views.deleteuser),
    path('updateprofile/<int:id>',views.updateprofile),
    path('profile/<int:id>',views.profile),
    path('sendmail/',views.sendmail),
    path('sendmail1/',views.sendmail1),
    path('sales/',views.sales),
    path('updatesales/<int:id>',views.updatesales),
    path('viewsales/',views.viewsales),
    path('sendsales/',views.sendsales),
    path('sendsales1/',views.sendsales1),
    path('tutor1/',views.tutor1),
    path('updatetutor/<int:id>',views.updatetutor),
    path('updatetutor1/<int:id>',views.updatetutor1),
    path('accountant1/',views.accountant1),
    path('updateaccountant/<int:id>',views.updateaccountant),
    path('updateaccountant1/<int:id>',views.updateaccountant1),

    path('sendtutor/',views.sendtutor),
    path('sendaccountant/',views.sendaccountant),
    path('sendstudent/',views.sendstudent),
    path('sendtutor1/',views.sendtutor1),
    path('sendstudent1/',views.sendstudent1),
    path('sendaccountant1/',views.sendaccountant1),
    path('didntconnect/',views.didntconnect),
    path('adddidnt/',views.adddidnt),
    path('viewdidnt/',views.viewdidnt),
    path('deletedidnt/<int:id>',views.deletedidnt),
    path('sendmaildidnt/',views.sendmaildidnt),
    path('senddidint1/',views.senddidint1),
    path('about/',views.about),
    path('team/',views.team),





    

]
