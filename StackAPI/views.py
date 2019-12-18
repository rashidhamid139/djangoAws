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

    try:
        if request.session['count']:
            print("Inside Loop", request.session)
            if ceil(request.session['time'] - time()) <= 60:
                if request.session['count'] < 5:
                    return render(request, 'StackAPI/home.html', {'contacts': contacts})
                else:
                    return render(request, 'StackAPI/warn.html')
            else:
                return render(request, 'StackAPI/warn.html')

    except:
        request.session['count']= 0
        request.session['time']=time()
    print(request.session['count'])
    if request.session.get('name') and request.session.get('password'):
        request.session['count'] += 1


        return render(request, 'StackAPI/home.html', {'contacts': contacts})
        # return  HttpResponse(response)
    else:
        return redirect('createsession')



def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Testing:<br> Session is set</h1>")


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<center><h1><Strong>Session is Deleted</strong></h1></center>")



def check_session(request):
    if request.session.get('name'):
        print(request.session['name'])
        return redirect('createsession')
    else:
        return redirect('createsession')