from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
from django.views import View


class ExampleEndPoint(View):
    def get(self, request):
        username = request.GET.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            user.email = ''
            user.save()
        else:
            User.objects.create_user(username=username, password='123456')
        return JsonResponse({'status': 201, 'msg': f'用户{username}数据保存成功'})
