# Generated by Django 5.1.6 on 2025-02-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
