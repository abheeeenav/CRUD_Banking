# Generated by Django 3.2 on 2021-04-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=20)),
                ('userFirstName', models.CharField(max_length=100)),
                ('userLastName', models.CharField(max_length=100)),
                ('userAge', models.CharField(max_length=20)),
                ('userGender', models.CharField(max_length=20)),
                ('userDistrict', models.CharField(max_length=100)),
                ('userState', models.CharField(max_length=100)),
                ('userNationality', models.CharField(max_length=100)),
                ('userAadhaar', models.CharField(max_length=100)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userContact', models.CharField(max_length=15)),
                ('userImage', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'userDetails',
            },
        ),
    ]
