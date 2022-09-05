from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class MoviesListApi(View):
    http_method_names = ['get']

    def get(self, request, version):
        # Получение и обработка данных
        return JsonResponse({'hello': 'world'})