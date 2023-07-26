from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    form = TodoItemForm()
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})

