from django.db import models

class country(models.Model):
	name = models.CharField(max_length=50)
	body_1 = models.TextField()
	body_2 = models.TextField()
	title_img = models.ImageField(upload_to="images/")
	img_1 = models.ImageField(upload_to="images/")
	img_2 = models.ImageField(upload_to="images/")
	img_3 = models.ImageField(upload_to="images/",blank=True)
	img_4 = models.ImageField(upload_to="images/",blank=True)
	Date_of_Publishing = models.DateTimeField()
	Author = models.CharField(max_length=50)
	def __str__(self):
		return self.name
	class Meta:
		abstract = True


class india(country):
	class Meta:
		verbose_name_plural = "Indians"
		ordering = ['-Date_of_Publishing']

class Australia(country):
	class Meta:
		verbose_name_plural = "Australians"
		ordering = ['-Date_of_Publishing']

class South_Africa(country):
	class Meta:
		verbose_name_plural = "South_Africans"
		ordering = ['-Date_of_Publishing']

class England(country):
	class Meta:
		verbose_name_plural = "England's"
		ordering = ['-Date_of_Publishing']

