# Generated by Django 3.2.4 on 2021-07-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0003_todos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]