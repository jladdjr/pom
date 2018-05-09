# Generated by Django 2.0.4 on 2018-05-09 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poms', models.IntegerField(default=0)),
                ('goal', models.IntegerField(default=0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pom.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='progress',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pom.Project'),
        ),
    ]
