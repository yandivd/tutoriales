# Generated by Django 3.2.8 on 2022-08-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Productos'),
        ),
    ]
