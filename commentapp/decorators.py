"""
article 페이지에서 요청한 유저와 현재 유저가 맞는가에 대한 함수를 지정해준다
"""

from django.http import HttpResponseForbidden
from articleapp.models import Article

#article의 소유권을 가진 함수 만들기
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:  #현재 작성자와 요청받은 유저가 동일하지 않다면
            return HttpResponseForbidden()  #에러 http로 보낸다(금지된 요청)
        return func(request, *args, **kwargs)
    return decorated