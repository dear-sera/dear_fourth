"""
메인 앱인 dear_fourth 의 urls안에 있는 urlpatterns와 같은 리스트를 만들어야한다
"""
from django.urls import path

from accountapp.views import hello_world

#이름을 설정하는 이유는 현재 account/hello_world 경로에 접근 할 땐 "127.0.0.1:8000/account/hello_world"라서 이걸 간편식으로 지정
#추후 "accountapp:hello_world"로 사용가능
app_name = "accountapp"

urlpatterns = [
    #path다음 첫번째는 경로위치, 두번째는 views에서 만들어준 헬로우월드함수 가져오기, name은 경로에 대한 이름
    path('hello_world/', hello_world, name='hello_world')
]