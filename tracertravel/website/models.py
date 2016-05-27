#encoding:utf-8
from django.db import models

class Customer(models.Model):

	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	direccion = models.CharField(max_length = 50)
	descripcion = models.TextField()
	dni = models.IntegerField(verbose_name = "DNI")

	def __unicode__ (self):

		return "{0} {1}".format(self.dni, self.apellido)

