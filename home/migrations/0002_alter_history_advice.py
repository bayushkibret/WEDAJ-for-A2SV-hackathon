# Generated by Django 4.1.10 on 2023-09-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='advice',
            field=models.TextField(),
        ),
    ]