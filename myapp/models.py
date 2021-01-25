from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=60, unique=True)
	author = models.CharField(max_length=60)
	dop = models.DateField(verbose_name="Date of Publication")
	content = models.TextField(blank=True)
	def __str__(self):  # string repr. of object
		return self.title


# Django ORM
# python manage.py makemigrations
# python manage.py migrate