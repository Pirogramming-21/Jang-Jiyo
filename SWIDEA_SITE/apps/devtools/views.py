from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm
from apps.ideas.models import Idea

# Create your views here.
def list(request):
   devtools = DevTool.objects.all()
   ctx = {'devtools': devtools}
   return render(request, 'devtools/list.html', ctx)

def register(request):
   if request.method == "GET":
      form = DevToolForm()
      ctx = {'form': form}
      return render(request, 'devtools/register.html', ctx)

   form = DevToolForm(request.POST)
   if form.is_valid():
      devtool = form.save()
   return redirect('devtools:detail', pk=devtool.pk)

def detail(request, pk):
   devtool = DevTool.objects.get(id=pk)
   ideas = Idea.objects.filter(devtool=devtool)

   ctx = {'devtool': devtool, 'ideas': ideas}
   return render(request, 'devtools/detail.html', ctx)

def delete(request, pk):
   DevTool.objects.get(id=pk).delete()
   return redirect("devtools:list")

def update(request, pk):
   devtool = DevTool.objects.get(id=pk)
   if request.method == "GET":
      form = DevToolForm(instance=devtool)
      ctx = {'form': form, 'pk':pk}
      return render(request, 'devtools/update.html', ctx)

   form = DevToolForm(request.POST, instance=devtool)
   if form.is_valid():
      form.save()

   return redirect("devtools:list")