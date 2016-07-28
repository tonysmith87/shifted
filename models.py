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
    staff_id = models.IntegerField(primary_key=True)
    absent = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Absent'
        unique_together = (('staff_id', 'absent'),)


class Client(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    person_id = models.IntegerField(unique=True)
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Client'


class Comment(models.Model):
    client_id = models.IntegerField(primary_key=True)
    meal_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Comment'
        unique_together = (('client_id', 'meal_id'),)


class Meal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    menu = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    date = models.CharField(max_length=100, blank=True, null=True)
    client_id = models.IntegerField()

    class Meta:
        managed = False
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
        managed = False
        db_table = 'Person'


class Roster(models.Model):
    meal_id = models.IntegerField(primary_key=True)
    staff_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Roster'
        unique_together = (('meal_id', 'staff_id'),)


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    person_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Staff'
