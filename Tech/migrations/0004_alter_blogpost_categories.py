# Generated by Django 4.2.6 on 2023-10-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tech', '0003_remove_blogpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='categories',
            field=models.CharField(choices=[('IoT', 'Internet of Things'), ('Cybersecurity', 'Cybersecurity'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Biotechnology', 'Biotechnology'), ('Automotive', 'Automotive'), ('Aerospace', 'Aerospace'), ('Gaming', 'Gaming'), ('Fintech', 'Fintech'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]
