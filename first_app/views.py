from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Users
from django.core import serializers

import logging
logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'first_app/index.html'

class UserData(APIView):
    def get(self, request, format=None):
        users = Users.objects.all()
        data = serializers.serialize("json", users)
        logger.debug(f'{data}')
        
        # data = {
        #     'Name': 'Max'
        # }
        return Response(data)


