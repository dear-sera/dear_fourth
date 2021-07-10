from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):  #create와 updateform은 크게 다르지 않은데, 맨 아랫줄을 추가해주면 의미가 달라진다
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True  #폼을 초기화 후에 username을 비활성화 시켜준다

