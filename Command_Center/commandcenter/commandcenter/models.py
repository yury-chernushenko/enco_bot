from django.db import models

class History(models.Model):
	date = models.DateField()

class Message(models.Model):
	text = models.CharField(max_length=100)
	history = models.ForeignKey(History)
