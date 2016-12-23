from django.db import models as m

# Create your models here.
class DreamReal(m.Model):
	website = m.CharField(max_length=100)
	mail = m.EmailField(max_length=50)
	name = m.CharField(max_length=25)
	phonenumber = m.IntegerField()
	online = m.ForeignKey('Online', default=1)

	class Meta:
		db_table = "dreamreal"
		ordering = ('name',)

	def __str__(self):
		return self.name

class Online(m.Model):
	domain = m.CharField(max_length=30)

	class Meta:
		db_table = 'online'

class Profile(m.Model):
	name = m.CharField(max_length=100)
	picture = m.ImageField(upload_to = 'pictures')

	class Meta:
		db_table = "profile"