from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

#프로필 생성 함수
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  #프로필 객체 설정, commit=False= 임시저장하는 것 (실제 db엔 저장 x)
        temp_profile.user = self.request.user  #form유저를 당사자의 유저로 정해준다
        temp_profile.save()   #최종적으로 저장
        return super().form_valid(form)  #원래 클래스의 결과를 반환

    #프로필이 만들어진 뒤 나올 페이지는 mypage로 돌아가기 위해서 새로 함수를 지정해준다
    def get_success_url(self):
        return  reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})  #여기서 object란 Profile에 user의 pk를 찾아서 넘겨주게 된다

#프로필 업데이트 함수
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return  reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})  #여기서 object란 Profile에 user의 pk를 찾아서 넘겨주게 된다