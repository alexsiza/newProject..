from django.shortcuts import render


# Create your views here.
def teste(request):
    #return HttpResponse("Meu primeiro response html django")
    return render(request, 'teste.html')

def login(request):
    return render(request, 'login.html')

def creat_doc(request):
    return render(request, 'creat_doc.html')

def home(request):
    return render(request, 'home.html')
