from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import *
# Create your models here.

class DocumentType(models.Model):
	name = models.CharField(max_length = 50, null=True)
	def __str__(self):
		return '{}'.format(self.name)

class Gender(models.Model):
	name = models.CharField(max_length = 50, null=True)
	def __str__(self):
		return '{}'.format(self.name)
		
class Extended_User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='extended_user',primary_key=True)
	document_number= models.CharField(max_length = 50, null=True)
	phone1 = models.CharField(max_length = 50, null=True)
	phone2 = models.CharField(max_length = 50, null=True)
	address = models.CharField(max_length = 500, null=True)
	photo = models.ImageField(verbose_name='photo',upload_to='users/',blank=True)
	document_type = models.ForeignKey(DocumentType,on_delete=models.CASCADE,null=True)
	date_birth = models.DateField(null=True)
	description_address = models.TextField(null=True)
	gender = models.ForeignKey(Gender, on_delete = models.CASCADE, null=True)
	def __str__(self):
		return '{}'.format(self.user)

@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
	if created:
		extend = Extended_User.objects.create(user=instance)