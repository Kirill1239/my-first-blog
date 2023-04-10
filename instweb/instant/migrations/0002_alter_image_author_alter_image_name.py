# Generated by Django 4.1.7 on 2023-04-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instant.user'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(help_text='выберите файл', upload_to='images1/'),
        ),
    ]
