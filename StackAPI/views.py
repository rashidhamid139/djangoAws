from time import time
from django.shortcuts import render, redirect
import requests, json
from django.core.paginator import Paginator
from django.http import HttpResponse

from math import ceil



def home(request ):

    url = "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
    resp = requests.get(url)
    resp  = json.loads(resp.text)['items']
    paginator = Paginator(resp, 3)
    page = request.GET.get('page')
    print("reqiest",request.session)
    contacts = paginator.get_page(page)
    try:
        if request.session['count']:
            print("Inside Loop", request.session)
            if ceil(request.session['time'] - time()) <= 60:
                if request.session['count'] <= 5:
                    return render(request, 'StackAPI/home.html', {'contacts': contacts})
                else:
                    return render(request, 'StackAPI/warn.html')
            else:
                return render(request, 'StackAPI/warn.html')

    except:
        request.session['count']=1
        request.session['time']=time()
    return render(request, 'StackAPI/home.html', {'contacts':contacts} )


def access_session1(request):
    url = "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
    resp = requests.get(url)
    resp = json.loads(resp.text)['items']
    paginator = Paginator(resp, 3)
    page = request.GET.get('page')
    print("reqiest", request.session)
    contacts = paginator.get_page(page)


    if request.session.get('name') and request.session.get('password'):

        return render(request, 'StackAPI/home.html', {'contacts': contacts})
        # return  HttpResponse(response)
    else:
        return redirect('createsession')





def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Testing Cookie</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Test <br> Cookie Created")
    else:
        response = HttpResponse("Testing: <br> Your Browser doesnt accept cookies")
    return response








def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Testing:<br> Session is set</h1>")



# def access_session(request):
#     response = "<h1>Welcome to Testing Session</h1><br>"
#     if request.session.get('name'):
#         response += "Name: {0}<br>".format(request.session.get('name'))
#     if request.session.get('password'):
#         response += "Password : {0}<br>".format(request.session.get('password'))
#         return  HttpResponse(response)
#     else:
#         return redirect('createsession')
#






