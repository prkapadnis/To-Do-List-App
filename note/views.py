from django.contrib.auth.models import User
from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from note.models import Task
from .forms import TaskForm

login_required(login_url='/login')


def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    incomeplete = Task.objects.filter(
        user=request.user, complete=False).count()
    context = {'tasks': tasks, 'incomeplete': incomeplete}
    return render(request, "note/home.html", context)


login_required(login_url='/login')


def createNote_view(request):
    if request.method == 'POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.instance.user = request.user
            taskform.save()
            return redirect('/Note/home')
    else:
        taskform = TaskForm()
    context = {'form': taskform}
    return render(request, "note/createNote_view.html", context)


login_required(login_url='/login')


def updateNote_view(request, id):
    taskModel = Task.objects.get(id=id)
    taskform = TaskForm(instance=taskModel)
    if request.method == 'POST':
        taskform = TaskForm(request.POST, instance=taskModel)
        if taskform.is_valid():
            taskform.save()
            return redirect('/Note/home')
    else:
        taskform = TaskForm(instance=taskModel)
    context = {'form': taskform}
    return render(request, 'note/updateNote_view.html', context)


login_required(login_url='/login')


def deleteNote_view(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/Note/home')
