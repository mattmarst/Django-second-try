# Generated by Django 4.2.6 on 2023-10-13 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_num',
        ),
        migrations.AddField(
            model_name='question',
            name='question_cat',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
