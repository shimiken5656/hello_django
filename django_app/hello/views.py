from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
#from .forms import HelloForm
from .forms import FindForm
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Friend, Message
from .forms import FriendForm, MessageForm



def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data,10)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)


# create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Create',
        'form':FriendForm(),
    }
    return render(request,'hello/create.html',params)

# edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Edit',
        'id': num,
        'form':FriendForm(instance=obj),
    }
    return render(request,'hello/edit.html',params)

# delete
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Delete',
        'id': num,
        'obj':friend,
    }
    return render(request,'hello/delete.html',params)

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
        'title': 'Find',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)

def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)