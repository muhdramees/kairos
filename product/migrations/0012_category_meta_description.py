# Generated by Django 4.1.5 on 2023-01-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_category_image_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]