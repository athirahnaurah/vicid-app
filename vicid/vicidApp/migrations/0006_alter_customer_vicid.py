# Generated by Django 4.2.5 on 2023-10-02 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicidApp', '0005_alter_customer_vicid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='VICID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]