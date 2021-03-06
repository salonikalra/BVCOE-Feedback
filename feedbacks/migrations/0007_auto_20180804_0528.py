# Generated by Django 2.0.6 on 2018-08-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0006_auto_20180803_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(null=True, related_name='subjects', to='feedbacks.Teacher'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ManyToManyField(related_name='subjects', to='feedbacks.Department'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.ManyToManyField(related_name='subjects', to='feedbacks.Semester'),
        ),
    ]
