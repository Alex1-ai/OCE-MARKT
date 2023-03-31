# Generated by Django 4.1.7 on 2023-03-29 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_variation'),
        ('orders', '0008_alter_orderproduct_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='variation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
        ),
    ]