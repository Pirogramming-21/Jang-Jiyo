from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def main(request):
   posts = Post.objects.all()
   context = {'posts': posts}
   return render(request, 'post/list.html', context)

def create(request):
   if request.method == 'GET':
      form = PostForm()
      context = {'form': form}
      return render(request, 'post/create.html', context)
   form = PostForm(request.POST, request.FILES)
   if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
   return redirect('post:main')

def comment(request, pk):
   post = Post.objects.get(id=pk)
   form = CommentForm()
   comments = post.comments.all()
   context = {
      'post': post, 
      'form': form,
      'comments': comments,
   }
   return render(request, 'post/comment.html', context)

@csrf_exempt
def comment_create(request, post_id):
   if request.method == 'POST':
      try:
         data = json.loads(request.body.decode('utf-8'))
         text = data.get('text')
         if text:
               post = Post.objects.get(id=post_id)
               comment = Comment.objects.create(
                  post=post,
                  user=request.user,
                  text=text
               )
               response = {
                  'id': comment.id,
                  'text': comment.text,
                  'user': comment.user.username,
               }
               return JsonResponse(response, status=200)
         else:
               return JsonResponse({'error': 'Text is required'}, status=400)
      except json.JSONDecodeError:
         return JsonResponse({'error': 'Invalid JSON'}, status=400)
   return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def comment_delete(request, post_id, comment_id):
   request = json.loads(request.body)
   comment = Comment.objects.get(id=comment_id, post_id = post_id)
   comment.delete()
   print("delete!!")
   return JsonResponse({'success': True})

@csrf_exempt
def post_like(request, post_id):
   post = Post.objects.get(id=post_id)
   user = request.user
   if post.like.filter(id = user.id).exists():
      post.like.remove(user)
      liked = False
   else:
      post.like.add(user)
      liked = True
   context = {'like_count': post.like.count(), 'liked': liked}
   return JsonResponse(context)