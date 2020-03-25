from django.db import models

# Create your models here.

class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.IntegerField()
    is_superuser = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

class UserProfileInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)



class Posts(models.Model):
    author_id = models.IntegerField()
    title = models.CharField(max_length=255)      
    description = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    birthdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'

