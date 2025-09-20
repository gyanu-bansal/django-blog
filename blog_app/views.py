from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
	post_objs=Post.objects.all()
	return render(request,'index.html',{'post_objs':post_objs})

def post_detail(request,post_id):
	post=Post.objects.get(id=post_id)
	comments=post.comment_set.all()
	form=CommentForm()
	return render(request,'post_detail.html',{'post':post,'comments':comments,'form':form})

@login_required
def create_post(request):
	if request.method=='POST':
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect('index')
		
	else:
		form=PostForm()
		return render(request,'create_post.html',{'form':form})
@login_required
def create_comment(request,post_id):
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.commentor=request.user
			comment.post=Post.objects.get(id=post_id)
			comment.save()
			return redirect('post_detail',post_id)

		