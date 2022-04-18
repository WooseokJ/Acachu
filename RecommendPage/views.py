from django.shortcuts import render

# Create your views here.
def recommendList(request):
    return render(request,'RecommendPage/RecommendList.html')