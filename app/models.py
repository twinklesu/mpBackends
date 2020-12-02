# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# test table
class Test(models.Model):
    test = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'

# user_info table
class UserInfo(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=128, blank=True, null=True)
    user_pw = models.CharField(max_length=128, blank=True, null=True)
    user_nicknm = models.CharField(max_length=45, blank=True, null=True)
    user_town = models.CharField(max_length=128, blank=True, null=True)
    user_tel = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'

class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=128, blank=True, null=True)
    image = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    variety = models.CharField(max_length=128, blank=True, null=True)
    reg_num = models.CharField(max_length=128, blank=True, null=True)
    character = models.CharField(max_length=1024, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'pet'

class PostLost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    lost_loc = models.CharField(max_length=256, blank=True, null=True)
    lost_date = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    reg_num = models.CharField(max_length=128, blank=True, null=True)
    phone_num = models.CharField(max_length=32, blank=True, null=True)
    character = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_lost'

