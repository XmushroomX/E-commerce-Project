
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240517_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption1', models.CharField(max_length=100)),
                ('caption2', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]