"""dear_fourth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  #장고 기본앱이라 기본적으로 설정되어 있다
    #앱을 추가하기 위해서 새로운 app의 urls를 만들어준다
    path('accounts/', include('accountapp.urls')),  #path= 이 앱으로 이동시켜준다, include=accountapp앱 내부에 있는 urls.py를 포함해서 그 하위 디렉토리로 분기하라는 것
]