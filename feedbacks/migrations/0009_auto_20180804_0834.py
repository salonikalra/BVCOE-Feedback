# Generated by Django 2.0.6 on 2018-08-04 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0008_auto_20180804_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.ManyToManyField(to='feedbacks.Department'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.ManyToManyField(to='feedbacks.Semester'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(to='feedbacks.Teacher'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='department',
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.ManyToManyField(to='feedbacks.Department'),
        ),
    ]
