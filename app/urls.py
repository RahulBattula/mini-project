from django.urls import path,include

from .  import views

urlpatterns = [

   path('',views.home,name='home'),
   path('templates/register/',views.register,name='register'),
   path('templates/contact1/',views.register,name='contact1'),
  
    path('index.html',views.index,name='index'),
    path('home.html',views.home,name='home'),
    path('security.html',views.security,name='security'),
    path('about.html',views.about_us,name='about_us'),

    path('intermediate.html',views.intermediate,name='intermediate'),
    path('diploma.html',views.diploma,name='diploma'),
    path('index.html/details/',views.get_details,name='get_details'),
    path('mens.html',views.menstruation,name='menstruation'),
     path('thy.html', views.thy, name='thy'),
     path('fertility.html',views.fertility,name='fertility'),
   path('cancer.html', views.cancer, name='cancer'),
   path('dep.html',views.depression,name='depression'),
    path('iti.html',views.iti,name='iti'),
    path('para.html',views.paramedical,name='paramedical'),
    path('vocational.html',views.vocational,name='vocational'),
     
    #path('contact1.html',views.contact,name='contact1'), 
    path('feedback.html',views.feedback,name='feedback'), 
    
   
]
