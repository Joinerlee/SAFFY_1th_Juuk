# Generated by Django 4.2.16 on 2024-11-18 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_savings_savingsoptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingsoptions',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.savings'),
        ),
    ]
