# Generated by Django 2.0.6 on 2018-07-31 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(max_length=15, unique=True)),
                ('department_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['department_name'],
            },
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('param1', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The objectives of this course were made clear to me by this teacher.')),
                ('param2', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The teacher speaks, articulates and explains concepts clearly.')),
                ('param3', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The teacher adheres to the timings schedule and enforces discipline in the class.')),
                ('param4', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='Interest generated by the teacher.')),
                ('param5', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The lectures were well structured and focused on the topics.')),
                ('param6', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='Accessibility of the teacher in and out of the class.')),
                ('param7', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The teacher has fair knowledge on the subject matter.')),
                ('param8', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='Effective use of teaching aids.')),
                ('param9', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='Time spend on lecturing by teacher for course coverage was sufficient and lesson plan was followed.')),
                ('param10', models.PositiveSmallIntegerField(choices=[(1, 'Unsatisfactory'), (2, 'Satisfactory'), (3, 'Good'), (4, 'Very Good'), (5, 'Outstanding')], default=None, verbose_name='The teacher encourage students to raise pertinent questions and answer them.')),
                ('total', models.PositiveIntegerField(blank=True, null=True)),
                ('average', models.FloatField()),
                ('message', models.CharField(blank=True, max_length=100, null=True, verbose_name='Anything else you want to say.')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='accounts.Student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_number', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['semester_number'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=15, unique=True)),
                ('subject_name', models.CharField(max_length=100, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='feedbacks.Department')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='feedbacks.Semester')),
            ],
            options={
                'ordering': ['subject_name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=15, unique=True)),
                ('teacher_name', models.CharField(max_length=100, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='feedbacks.Department')),
            ],
            options={
                'ordering': ['teacher_name'],
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='feedbacks.Subject'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='feedbacks.Teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('student', 'teacher', 'subject')},
        ),
    ]
