# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Absent(models.Model):
    staff = models.ForeignKey('Staff')
    absent = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'Absent'


class Client(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    person = models.ForeignKey('Person')
    rate = models.IntegerField()

    class Meta:
        db_table = 'Client'


class Comment(models.Model):
    client = models.ForeignKey('Client')
    meal = models.ForeignKey('Meal')
    comment = models.CharField(max_length=255)
    date = models.CharField(max_length=100)

    class Meta:
        db_table = 'Comment'


class Meal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    menu = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    date = models.CharField(max_length=100, blank=True, null=True)
    client = models.ForeignKey('Client')
    meal_comment = models.TextField(blank=True, null=True, default="")

    class Meta:
        db_table = 'Meal'


class Person(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=1000)
    register_date = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.IntegerField()
    last_login = models.CharField(max_length=100)

    class Meta:
        db_table = 'Person'


class Roster(models.Model):
    meal = models.ForeignKey('Meal')
    staff = models.ForeignKey('Staff')

    class Meta:
        db_table = 'Roster'


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    person = models.ForeignKey('Person')
    rate = models.IntegerField(default=0, null=True)
    client = models.ForeignKey('Client')


    class Meta:
        db_table = 'Staff'
