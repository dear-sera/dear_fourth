#alt+enter를 누르면 import를 선택가능
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

#시범삼아 헬로우월드만 나오게 함수 설정
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


"""has_ownership =
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
이 4가지 decorator를 배열에 넣어서 지정 가능하다
"""
has_ownership = [account_ownership_required, login_required]


@login_required  #로그인이 된 상태인지, 안 된 상태라면 로그인창으로 보내주는 코드를 가짐, @이를 붙이면 decorator로 함수의 앞뒤에 붙게된다
def hello_world(request):

    if request.method == "POST":  #post 메서드 일 경우

        temp = request.POST.get('hello_world_input')  #request에서 post방식 중 hello_world_input이라는 데이터를 가져오기

        new_hello_world = HelloWorld()  #모델을 불러와서 이 모델 안에서 나오는 새로운 객체가 변수로 들어가게
        new_hello_world.text = temp  #모델 안에 text속성에 temp를 넣어주기
        new_hello_world.save()   #저장을 하면 실제 DB에 저장이 된다


        # render를 통해 연결을 원한다면 처음인자는 request로 요청, 두번째는 해당 html의 이름, context= 데이터꾸러미, 객체를 내보내 주는 것
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  #기본 주소로 다시 재접속

    else:  #post가 있다면 그냥 주소창을 검색하는 방식인 get방식도 있어야 에러가 없기에 작성해준다
        hello_world_list = HelloWorld.objects.all()   #helloworld의 모든 데이터를 가져올 수 있다
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


#계정을 만드는 함수
class AccountCreateView(CreateView):  #계정을 만드는 클래스 생성, 아래 파라미터가 들어간다
    model = User  #User = 장고에서 기본 제공해주는 모델, ctrl+b를 누르면 소스코드로 넘어가진다
    form_class = UserCreationForm   #user모델을 만드는 데 필요한 폼, 장고에서 기본 폼을 제공해준다
    success_url = reverse_lazy('accountapp:hello_world')  #가입에 성공했을 때, 어디 경로로 다시 재연결을 할 것인지, reverse와 비슷하지만 class에서 사용이 가능
    template_name = 'accountapp/create.html'  #회원가입 시 html경로 설정


#계정의 정보를 보는 함수
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'  #다른 사람이 페이지에 접속할 땐 mypage가 보이지 않게
    template_name = 'accountapp/detail.html'


#계정 업데이트 함수
#method_decorator= 일반 함수에 사용하는 decorator를 메서드에 사용할 수 있도록 해주는 decorator
@method_decorator(has_ownership, 'get')  #매개변수 첫번째는 사용할 decorator을 넣고, 두번째는 메소드 방식을 넣어준다
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):  #계정의 정보를 업데이트 해주는 클래스
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm   #업데이트 시 아이디를 고정(비활성화)해놓은 form으로 지정
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


#계정 삭제 함수
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')  #delete 후에 로그인 html으로 이동
    template_name = 'accountapp/delete.html'