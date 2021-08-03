from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string



def index(request):
    if request.method == 'GET':
        palabra = get_random_string(length=14)
        context = {"palabra": palabra}
    if 'contador' in request.session:
       request.session['contador'] = request.session['contador'] + 1
    else:
        request.session['contador'] = 1 
    return render(request,'random_word/index.html',context)

def resetear(request):
    request.session['contador'] = 0 
    return redirect("/palabra")