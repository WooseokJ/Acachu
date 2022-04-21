from django.shortcuts import render

# Create your views here.
def Cho(request):
    return render(request,'ChoicePage\ChoicePage.html')

def Cat(request):
    return render(request,'ChoicePage\CategoryPage.html')

def Img(request):
    return render(request,'ChoicePage\ImageSearchPage.html')