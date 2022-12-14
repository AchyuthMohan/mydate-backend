# Generated by Django 4.0.6 on 2022-07-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('auth_phno', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
