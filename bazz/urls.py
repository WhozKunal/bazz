"""
URL configuration for bazz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from bazz import views
# url deails
#path(url,function.page)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.homepage),
    path('header/',views.header),
    path('footer/',views.footer),
    path('',views.homepage),
    #path('about/',views.about),
    path('services/',views.services),
    path('contact/',views.contact),
    path('homepage/<slug:about>',views.about),
    path('thanku/',views.thanku),
    



    

    
]
