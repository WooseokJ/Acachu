from django.shortcuts import render

# Create your views here.
def Aut(request):
    return render(request,'AuthManagedPage\AuthManagedPage.html')

def post(request):
    return render(request,'AuthManagedPage\post.html')

def contents(request):
    return render(request, 'AuthManagedPage\contents.html')