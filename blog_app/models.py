from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	content=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	commentor=models.ForeignKey(User, on_delete=models.CASCADE)
	comment=models.CharField(500)
	created_at=models.DateTimeField(auto_now_add=True)
	post=models.ForeignKey(Post, on_delete=models.PROTECT)# AS WE DON'T WANT TO DELETE THE POST ON DELTEITON OF COMMENT
