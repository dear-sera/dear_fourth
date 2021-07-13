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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),  #장고 기본앱이라 기본적으로 설정되어 있다
    #앱을 추가하기 위해서 새로운 app의 urls를 만들어준다
    # path= 이 앱으로 이동시켜준다, include=accountapp앱 내부에 있는 urls.py를 포함해서 그 하위 디렉토리로 분기하라는 것
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),


#settings.py안에 있는 값들을 가져올 수 있다, 미디어 폴더 안 사진들의 경로를 불러준다 (이래야 이미지를 서버에서 볼 수 있다)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)