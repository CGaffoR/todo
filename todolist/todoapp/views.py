from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

# Create your views here.

def indexTodo(request):
    return render(request, 'index.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'home.html',
    {'all_items':all_todo_items})

def add_todo_view(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/home/')

def delete_todo_view(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/home/')