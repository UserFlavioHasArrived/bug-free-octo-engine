#from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
def estudantes(request):
    if request.method == 'GET':
            estudante = {
                'id':'25',
                'nome':'flavio'
            }
    return JsonResponse(estudante)