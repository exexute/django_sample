from django.http import JsonResponse
from django.views import View

import logging

logger = logging.getLogger('sample_log')


class SampleLogEndPoint(View):
    def get(self, request):
        logger.info('access to SampleLogEndPoint')
        return JsonResponse({'status': 201, 'msg': 'success'})
