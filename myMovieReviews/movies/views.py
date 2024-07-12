from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def movie_list(request):
   # default 정렬 기준: title
   order_condition = request.GET.get("sort_by", 'title')
   print(f"Sorting by: {order_condition}")  # 디버깅용

   movies = Movie.objects.order_by(order_condition)
   print(f"Number of movies: {movies.count()}")  # 디버깅용
   context = {
      "movies": movies,
      "current_sort": order_condition,
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
   if movie.runningtime >= 60:
      hour = movie.runningtime // 60
      minute = movie.runningtime % 60
   
   context = {
      "movie": movie,
      'runningtime_hour': hour,
      'runningtime_minute': minute
   }
   return render(request, 'movie_detail.html', context)

def movie_update(request, pk):
   movie = Movie.objects.get(id = pk)
   if request.method == 'POST':
      movie.title = request.POST["title"]
      movie.release = request.POST["release"]
      movie.director = request.POST["director"]
      movie.leadrole = request.POST["leadrole"]
      movie.genre = request.POST["genre"]
      movie.evaluation = request.POST["evaluation"]
      movie.runningtime = request.POST["runningtime"]
      movie.review = request.POST["review"]

      movie.save()
      return redirect(f"/movies/{pk}")
   
   context = {
      "movie": movie
   }
   return render(request, 'movie_update.html', context)

def movie_delete(request, pk):
   if request.method == 'POST':
      movie = Movie.objects.get(id = pk)
      movie.delete()
   return redirect("/movies")