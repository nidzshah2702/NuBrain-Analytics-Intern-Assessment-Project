# Generated by Django 2.2 on 2020-03-25 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author_post', '0003_auto_20200325_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('is_staff', models.IntegerField()),
                ('is_superuser', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author_post.User'),
        ),
    ]