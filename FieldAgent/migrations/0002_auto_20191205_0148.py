# Generated by Django 3.0 on 2019-12-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FieldAgent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seasonalservey',
            name='id',
        ),
        migrations.AlterField(
            model_name='seasonalservey',
            name='surveyId',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
