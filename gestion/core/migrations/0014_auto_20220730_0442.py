# Generated by Django 3.2.9 on 2022-07-30 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_category_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cat',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
