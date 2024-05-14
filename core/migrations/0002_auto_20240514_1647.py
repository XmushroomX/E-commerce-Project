# Generated by Django 3.0.14 on 2024-05-14 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SB', 'Shirts And Blouses'), ('TS', 'T-Shirts'), ('SK', 'Skirts')], default='default_category', max_length=2),
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'sale'), ('N', 'new'), ('P', 'promotion')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
