from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('home2/',views.home2,name='home2'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('pages/formone',views.formone,name='formone'),
    path('pages/formtwo',views.formtwo,name='formtwo'),
    path('pages/formthree',views.formthree,name='formthree'),
    path('pages/formfour',views.formfour,name='formfour'),
    path('pages/formfive',views.formfive,name='formfive'),
    path('pages/formsix',views.formsix,name='formsix'),
    path('forms/formone',views.moreformone,name='IIformone'),
    path('forms/formtwo',views.moreformtwo,name='IIformtwo'),
    path('forms/formthree',views.moreformthree,name='IIformthree'),
    path('forms/formfour',views.moreformfour,name='IIformfour'),
    path('forms/formfive',views.moreformfive,name='IIformfive'),
    path('forms/formsix',views.moreformsix,name='IIformsix'),
    path('pages/hod',views.hod,name='hod'),
    path('pages/fetchprofile/<str:emailid>',views.fetchprofile,name='fetchprofile'),
    path('pages/fetchformone/<str:emailid>',views.fetchformone,name='fetchformone'),
    path('pages/fetchformtwo/<str:emailid>',views.fetchformtwo,name='fetchformtwo'),
    path('pages/fetchformthree/<str:emailid>',views.fetchformthree,name='fetchformthree'),
    path('pages/fetchformfour/<str:emailid>',views.fetchformfour,name='fetchformfour'),
    path('pages/fetchformfive/<str:emailid>',views.fetchformfive,name='fetchformfive'),
    path('pages/fetchformsix/<str:emailid>',views.fetchformsix,name='fetchformsix'),
    path('logout',views.logout_view,name='logout'),
    path('profileupdate',views.profileupdate,name='profileupdate'),
]