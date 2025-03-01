# Generated by Django 5.0.1 on 2024-02-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_alter_pet_slug'),
        ('photos', '0007_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='pets',
            field=models.ManyToManyField(related_name='pet_photos', to='pets.pet'),
        ),
    ]
