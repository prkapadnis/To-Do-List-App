from django.db.models.query import InstanceCheckMeta
from django.shortcuts import redirect, render
from django.contrib import messages
from note.models import Task
from .forms import TaskForm
# Create your views here.


def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    incomeplete = Task.objects.filter(complete=False).count()
    context = {'tasks': tasks, 'incomeplete': incomeplete}
    return render(request, "note/home.html", context)


def createNote_view(request):
    if request.method == 'POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.instance.user = request.user
            taskform.save()
            messages.success(
                request, f"The task is created with id {taskform.instance.id}")
            return redirect('/home')
    else:
        taskform = TaskForm()
    context = {'form': taskform}
    return render(request, "note/createNote_view.html", context)


def updateNote_view(request, id):
    taskModel = Task.objects.get(id=id)
    taskform = TaskForm(instance=taskModel)
    if request.method == 'POST':
        taskform = TaskForm(request.POST, instance=taskModel)
        if taskform.is_valid():
            taskform.save()
            messages.success(
                request, f'{taskform.instance.id} Note updated!!')
            return redirect('/home')
    else:
        taskform = TaskForm(instance=taskModel)
    context = {'form': taskform}
    return render(request, 'note/updateNote_view.html', context)
