from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm
from .forms import FindForm
from django.db.models import Q
from django.core.paginator import Paginator


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data,3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)


def index2(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hellooooooooooooooo',
        'message': 'all friendsssssssss',
        'data': data,
    }
    return render(request, 'hello/index2.html', params)


def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)
