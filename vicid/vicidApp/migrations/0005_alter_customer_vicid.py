# Generated by Django 4.2.5 on 2023-10-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicidApp', '0004_remove_customer_customer_id_alter_customer_vicid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='VICID',
            field=models.BigAutoField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
