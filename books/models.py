from django.db import models

# Create your models here.
class Book(models.Model):
	name      	  = models.CharField(max_length=255, null=True,blank=False)
	content_pdf   = models.FileField()	
	content_text  = models.TextField(null=True,blank=True)
	# user		= models.ForeignKey(User, default=1)
	# content		= models.CharField(max_length=255, null=True,blank=False)
	# liked 		= models.ManyToManyField(User, blank=True, related_name='liked') 
	# reply		= models.BooleanField(verbose_name='reply', default=False)
	# timestamp	= models.DateTimeField(auto_now_add=True)
	# updated		= models.DateTimeField(auto_now=True)
	# views  		= models.ManyToManyField(User,blank=True,related_name='views')

