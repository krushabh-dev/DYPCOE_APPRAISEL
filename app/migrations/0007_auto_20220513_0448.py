# Generated by Django 2.2.12 on 2022-05-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_formfive_formfour_formsix_formthree'),
    ]

    operations = [
        migrations.CreateModel(
            name='BformFive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('EOrganised', models.CharField(max_length=200)),
                ('EAttended', models.CharField(max_length=200)),
                ('UploadReport', models.CharField(max_length=200)),
                ('UploadCertificate', models.CharField(max_length=200)),
                ('NameEvent', models.CharField(max_length=200)),
                ('UploadEventCertificate', models.CharField(max_length=200)),
                ('NPTELName', models.CharField(max_length=200)),
                ('NPTELCert', models.CharField(max_length=200)),
                ('IEnchanchedQualification', models.CharField(max_length=200)),
                ('IEnchanchedQualificationProof', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BformFour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('NoOfPHDGuided', models.CharField(max_length=200)),
                ('NoOfPGguided', models.CharField(max_length=200)),
                ('NoOfBEPrjGuided', models.CharField(max_length=200)),
                ('ResearchProjectCompleted', models.CharField(max_length=200)),
                ('InProdDevelopment', models.CharField(max_length=200)),
                ('Consultancy', models.CharField(max_length=200)),
                ('EditorialBoard', models.CharField(max_length=200)),
                ('PaperPublishedwithIndustry', models.CharField(max_length=200)),
                ('EvidanceOne', models.CharField(max_length=200)),
                ('EvidanceTwo', models.CharField(max_length=200)),
                ('EvidanceThree', models.CharField(max_length=200)),
                ('EvidanceFour', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BFormProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('FormOne', models.CharField(max_length=20)),
                ('FormTwo', models.CharField(max_length=20)),
                ('FormThree', models.CharField(max_length=20)),
                ('FormFour', models.CharField(max_length=20)),
                ('FormFive', models.CharField(max_length=20)),
                ('FormSix', models.CharField(max_length=20)),
                ('NetCoutFormFilled', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BformThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('NoOFBookPatent', models.CharField(max_length=200)),
                ('EcopyofBookPatent', models.CharField(max_length=200)),
                ('journallink', models.CharField(max_length=200)),
                ('publisherName', models.CharField(max_length=200)),
                ('publisherCategory', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BformThreeB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Econtent', models.CharField(max_length=200)),
                ('UploadEvidance', models.CharField(max_length=200)),
                ('UploadCopy', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BformTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nameofpaper', models.CharField(max_length=200)),
                ('nameofjournal', models.CharField(max_length=200)),
                ('paperlink', models.CharField(max_length=200)),
                ('journallink', models.CharField(max_length=200)),
                ('fclaimedmarks', models.IntegerField()),
                ('totalmarks', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='facultymembers',
            name='FacultyID',
            field=models.CharField(default='FACULTYID', max_length=20),
        ),
        migrations.AddField(
            model_name='facultymembers',
            name='email',
            field=models.EmailField(default='example@example.in', max_length=200),
        ),
        migrations.AddField(
            model_name='facultymembers',
            name='nameofDepartment',
            field=models.CharField(default='Information Technology', max_length=200),
        ),
        migrations.AddField(
            model_name='facultymembers',
            name='nameofInstitute',
            field=models.CharField(default='DYP', max_length=200),
        ),
        migrations.AlterField(
            model_name='facultyinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='facultymembers',
            name='lastupdated',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='formfive',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formfour',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formfour',
            name='studentbatch',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='formone',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formprogress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formsix',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formthree',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='formtwo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
