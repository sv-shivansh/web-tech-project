# Generated by Django 3.1.5 on 2021-03-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notelog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Pwd', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Pwd2',
            new_name='C_Pwd',
        ),
    ]
