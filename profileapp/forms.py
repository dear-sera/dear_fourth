"""
account에서는 기본 장고 제공폼이 있지만 그 외는 스스로 만들어야 해서 프로필폼을 생성해준다
"""

from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']