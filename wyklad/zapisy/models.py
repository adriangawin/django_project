from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Wykladowca(models.Model):
  imie = models.CharField(max_length=40)
  nazwisko = models.CharField(max_length=40)
  website = models.URLField()

  def __unicode__(self):
  	return u'%s %s' % (self.imie, self.nazwisko)

class Student(models.Model):
  imie = models.CharField(max_length=40)
  nazwisko = models.CharField(max_length=40)

  def __unicode__(self):
  	return u'%s %s' % (self.imie, self.nazwisko)

class Wyklad(models.Model):
  nazwa = models.CharField(max_length=140)
  wykladowca = models.ForeignKey(Wykladowca)
  studenci = models.ManyToManyField(Student, blank=True)

  def __unicode__(self):
  	return self.nazwa
  
