from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

# Create your views here.

def main(request):
    return render(request, 'main/index.html', {
    })
