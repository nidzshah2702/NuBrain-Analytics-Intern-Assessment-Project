from django.db import models

    
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

