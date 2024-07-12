from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def movie_list(request):
   movies = Movie.objects.all()
   context = {
      "movies": movies
   }
   return render(request, 'movie_list.html', context)

def movie_create(request):
   if request.method == "POST":
      Movie.objects.create(
         title = request.POST["title"],
         release = request.POST["release"],
         director = request.POST["director"],
         leadrole = request.POST["leadrole"],
         genre = request.POST["genre"],
         evaluation = request.POST["evaluation"],
         runningtime = request.POST["runningtime"],
         review = request.POST["review"]
      )
      return redirect("/movies")
   return render(request, 'movie_create.html')

def movie_detail(request, pk):
   movie = Movie.objects.get(id = pk)
   context = {
      "movie": movie
   }
   return render(request, 'movie_detail.html', context)