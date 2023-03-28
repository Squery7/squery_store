# Generated by Django 4.1.7 on 2023-03-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=10)),
                ('nivel', models.IntegerField()),
                ('imagen', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
    ]