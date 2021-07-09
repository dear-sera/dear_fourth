"""
메인 앱인 dear_fourth 의 urls안에 있는 urlpatterns와 같은 리스트를 만들어야한다
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

#이름을 설정하는 이유는 현재 account/hello_world 경로에 접근 할 땐 "127.0.0.1:8000/account/hello_world"라서 이걸 간편식으로 지정
#추후 "accountapp:hello_world"로 사용가능
app_name = "accountapp"

urlpatterns = [
    #path다음 첫번째는 경로위치, 두번째는 views에서 만들어준 헬로우월드함수 가져오기, name은 경로에 대한 이름
    path('hello_world/', hello_world, name='hello_world'),

    #로그인, 로그아웃 기능은 따로 설정없이 여기에 path만 적어주면 된다
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('create/', AccountCreateView.as_view(), name='create'),  #as_view를 넣는 이유는 클래스view를 함수view로 만들어주기 위해서
]