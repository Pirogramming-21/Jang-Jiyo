from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm
from django.http import HttpResponse,JsonResponse
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

def comment_create(request, pk):
   post = Post.objects.get(id=pk)
   form = CommentForm(request.POST)
   if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.user = request.user
      comment.save()
   return redirect('post:comment', post.pk)

def comment_delete(request, post_pk, comment_pk):
   comment = Comment.objects.get(id=comment_pk)
   if request.user == comment.user:
      comment.delete()
   return redirect('post:comment', post_pk)

def post_like(request, pk):
   if request.is_ajax():
      post = Post.objects.get(id=pk)
      user = request.user
      if post.like.filter(id = user.id).exists():
         post.like.remove(user)
      else:
         post.like.add(user)
      context = {'like_count': post.like.count()}
      return HttpResponse(json.dumps(context), context_type='application/json')