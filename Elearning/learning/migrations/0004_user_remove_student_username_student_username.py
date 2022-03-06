# Generated by Django 4.0.3 on 2022-03-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_rename_name_student_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.ManyToManyField(blank=True, max_length=70, to='learning.user'),
        ),
    ]
