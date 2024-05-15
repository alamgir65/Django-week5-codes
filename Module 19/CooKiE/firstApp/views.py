from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('nameee' , 'Alamgir Hossain', max_age=10) 
    response.set_cookie('bari' , 'Noakhali') 
    return response

def get_cookies(request):
    name = request.COOKIES.get('nameee')
    return render(request, 'get_cookie.html', {'name': name})

def delete_cookies(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('namee')
    return response

def set_session(request):
    # data = {
    #     'name' : 'Rahim',
    #     'age' : 20,
    #     'language' : 'Bangla'
    # }
    # request.session.update(data)
    request.session['name'] = "Rohim"
    return render(request, 'home.html')

def get_session(request):
    # name = request.session.get('name', 'Guest')
    # age = request.session.get('age')
    # language = request.session.get('language')
    if 'name' in request.session:
        name = request.session.get('name')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse('Your session has been expired')
def delete_session(request):
    # del request.session['name'] This is for only name delete 
    request.session.flush()
    return render(request, 'delete_session.html')