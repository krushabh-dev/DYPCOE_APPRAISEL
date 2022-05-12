# Generated by Django 4.0.3 on 2022-03-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_formone_formtwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('currentclass', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('academicyear', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=200)),
                ('subjectname', models.CharField(max_length=200)),
                ('numberoftaught', models.IntegerField()),
                ('lastyresult', models.IntegerField()),
                ('currentyresult', models.IntegerField()),
                ('fclaimedmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('currentclass', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('studentbatch', models.IntegerField()),
                ('numberofstudent', models.IntegerField()),
                ('avgresult', models.IntegerField()),
                ('adoncourse', models.IntegerField()),
                ('othercourse', models.IntegerField()),
                ('allclear', models.IntegerField()),
                ('fclaimedmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('academicyear', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=200)),
                ('currentclass', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('subjectname', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('studentactivityname', models.CharField(max_length=200)),
                ('currentclass', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('subjectname', models.CharField(max_length=200)),
                ('numberofstudent', models.IntegerField()),
                ('dateofactivity', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
            ],
        ),
    ]
