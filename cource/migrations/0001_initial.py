# Generated by Django 3.0 on 2019-12-14 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('short_name', models.CharField(max_length=50)),
                ('credit', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='3')),
                ('require_credit', models.IntegerField(default=0)),
                ('for_all', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('capacity', models.IntegerField(default=40)),
                ('taken', models.IntegerField(default=0)),
                ('fill', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('cource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cource.Cource')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Teacher')),
            ],
        ),
    ]