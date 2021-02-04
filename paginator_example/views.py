import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
from django.views import View

from paginator_example.paginator import CustomPaginator


class UserEndPoint(View):
    def get(self, request):
        queryset = User.objects.all()

        page = request.GET.get('page', 1)
        page_size = request.GET.get('pageSize', 10)

        paginator = Paginator(queryset, per_page=page_size)
        # total = paginator.count
        data = paginator.get_page(page)

        return JsonResponse({
            'status': 201,
            'data': json.loads(serializers.serialize('json', data)),
            # 'total': total
        })

    def post(self, request):
        import json
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        User.objects.create_user(username=username, password=password)
        return JsonResponse({
            'status': 201,
            'msg': f'创建用户{username}成功',
        })


class UserV2EndPoint(View):
    def get(self, request):
        queryset = User.objects.all()
        paginator = CustomPaginator(request, queryset)
        data = paginator.get_page()

        return JsonResponse({
            'status': 201,
            'data': json.loads(serializers.serialize('json', data)),
        })
