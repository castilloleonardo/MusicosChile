# Generated by Django 3.1.3 on 2020-11-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=100)),
                ('fecha', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('usuario', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]
