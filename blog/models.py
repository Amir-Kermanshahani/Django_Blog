from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Post(models.Model):
	Adult = 'adult'
	Teen = 'teenager'

	AGE_FIELDS = (
		(Adult, 'adult'),
		(Teen, 'teenager')
		)

	title = models.CharField(max_length=255)
	content = models.TextField()
	Active = models.BooleanField(default=False)
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now=True)
	Age = models.CharField(max_length=255, default=Adult, choices=AGE_FIELDS)
	author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
	image = models.ImageField(upload_to='blog/', default='blog/image.jpg')
	category = models.ManyToManyField(Category)
	#tags = TaggableManager()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-updated_time']



class Subject(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)
	subject = models.CharField(max_length=255, null=True)
	description = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.subject


class Comment(models.Model):
		
	post = models.ForeignKey(Post, on_delete = models.CASCADE, null=True)
	name = models.CharField(max_length = 255)
	email = models.EmailField()
	subject = models.CharField(max_length = 255)
	message = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=False)


	def __str__(self) -> str:
		return self.name