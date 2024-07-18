from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm

# Create your views here.
def main(request):
   sort_by = request.GET.get('sort_by', '')
   if sort_by == 'interest':
      ideas = Idea.objects.all().order_by('-interest')
   elif sort_by == 'title':
      ideas = Idea.objects.all().order_by('title')
   elif sort_by == 'created':
      ideas = Idea.objects.all().order_by('id')
   elif sort_by == 'latest':
      ideas = Idea.objects.all().order_by('-id')
   else:
      ideas = Idea.objects.all()

   if request.method == 'POST':
      idea_id = request.POST.get('idea_id')
      idea = Idea.objects.get(id=idea_id)

      if 'interest_plus' in request.POST:
         idea.interest += 1
      elif 'interest_minus' in request.POST:
         idea.interest -= 1
      idea.save()
      return redirect('ideas:main')

   ctx = {'ideas': ideas, 'sort_by': sort_by}
   return render(request, 'ideas/list.html', ctx)

def toggle_star(request, pk):
   idea = Idea.objects.get(id=pk)
   ideastar, register = IdeaStar.objects.get(idea=idea)
   ideastar.is_starred = not ideastar.is_starred
   ideastar.save()
   return redirect('ideas:main')

def register(request):
   if request.method == "GET":
      form = IdeaForm()
      ctx = {'form': form}
      return render(request, 'ideas/register.html', ctx)
   form = IdeaForm(request.POST, request.FILES)
   if form.is_valid():
      idea = form.save()
   return redirect('ideas:detail', pk=idea.pk)

def detail(request, pk):
   idea = Idea.objects.get(id=pk)
   ctx = {'idea': idea}
   return render(request, 'ideas/detail.html', ctx)

def delete(request, pk):
   Idea.objects.get(id=pk).delete()
   return redirect('ideas:main')

def update(request, pk):
   idea = Idea.objects.get(id=pk)
   if request.method == "GET":
      form = IdeaForm(instance=idea)
      ctx = {'form': form, 'pk': pk}
      return render(request, 'ideas/update.html', ctx)
   form = IdeaForm(request.POST, request.FILES, instance=idea)
   if form.is_valid():
      form.save()
   return redirect('ideas:detail', pk)