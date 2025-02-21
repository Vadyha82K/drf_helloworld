from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hello_world_drf(request):
    return Response({'message': 'hello world'})

def hello_world(request):
    return JsonResponse({'message': 'hello world'})