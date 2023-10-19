# Generated by Django 4.2.6 on 2023-10-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech', '0003_category_tag_blogpost_categories_blogpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(blank=True, to='Tech.category'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Tech.tag'),
        ),
    ]
