"""

"""
#alt+enter를 누르면 import를 선택가능
from django.http import HttpResponse
from django.shortcuts import render

#시범삼아 헬로우월드만 나오게 함수 설정
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":  #post 메서드 일 경우

        temp = request.POST.get('hello_world_input')  #request에서 post방식 중 hello_world_input이라는 데이터를 가져오기

        new_hello_world = HelloWorld()  #모델을 불러와서 이 모델 안에서 나오는 새로운 객체가 변수로 들어가게
        new_hello_world.text = temp  #모델 안에 text속성에 temp를 넣어주기
        new_hello_world.save()   #저장을 하면 실제 DB에 저장이 된다

        # render를 통해 연결을 원한다면 처음인자는 request로 요청, 두번째는 해당 html의 이름, context= 데이터꾸러미, 객체를 내보내 주는 것
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:  #post가 있다면 그냥 주소창을 검색하는 방식인 get방식도 있어야 에러가 없기에 작성해준다
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
