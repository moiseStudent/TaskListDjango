from django.shortcuts import render, redirect
from .models import Task

def index(request):
    
    task = Task.objects.all()

    return render(request, 'index.html', {'tasks': task})

### Create a task
def new(request):
    
    if request.method == 'POST':

        title_post = request.POST['title']
        description_post = request.POST['description']

        task = Task(title=title_post, description=description_post)
        task.save()
        
        return redirect('index')

    return render(request, 'create.html')

### Edit task
def edit(request, id):
    
    task = Task.objects.get(id=id)

    task.title = request.POST['title']
    task.description = request.POST['description']
    task.status = request.POST['status']

    task.save()
    return redirect('index')

### Delete task
def delete(request, id):

    Task.objects.get(id=id).delete()
    return redirect('index')
    