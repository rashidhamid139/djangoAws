from time import time
from django.shortcuts import render
import requests, json
from django.core.paginator import Paginator
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


