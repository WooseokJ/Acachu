from django.shortcuts import render

# Create your views here.
def Img(request):
    return render(request,'ImageSearchPage/ImageSearchPage.html')