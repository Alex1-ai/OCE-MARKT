# Generated by Django 4.1.7 on 2023-03-05 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_old_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Tagged',
            new_name='tagged',
        ),
    ]
