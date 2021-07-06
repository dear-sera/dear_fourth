"""

"""
#alt+enter를 누르면 import를 선택가능
from django.http import HttpResponse
from django.shortcuts import render

#시범삼아 헬로우월드만 나오게 함수 설정
def hello_world(request):
    return render(request, 'base.html')  #render를 통해 연결을 원한다면 처음인자는 request로 요청, 두번째는 해당 html의 이름
