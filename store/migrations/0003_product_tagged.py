# Generated by Django 4.1.7 on 2023-03-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Tagged',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
