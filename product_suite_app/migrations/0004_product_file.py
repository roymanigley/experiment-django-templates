# Generated by Django 4.2.7 on 2023-11-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_suite_app', '0003_alter_product_date_alter_product_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
