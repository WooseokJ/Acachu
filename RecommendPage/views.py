from django.shortcuts import render

# Create your views here.
def recommendList(request):
    return render(request,'RecommendPage/recommendList.html')

def details(request):
    return render(request,'RecommendPage/details.html')