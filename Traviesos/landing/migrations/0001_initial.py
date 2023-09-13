# Generated by Django 4.2.4 on 2023-09-12 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacionAdicionalUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_completo', models.CharField(max_length=255)),
                ('Fecha_nacimiento', models.DateField()),
                ('Correo', models.EmailField(max_length=254)),
                ('Numero_telefonico', models.CharField(max_length=15)),
                ('Dirreccion_recidencia', models.CharField(max_length=30)),
                ('Numero_tarjeta', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Información Adicional de Usuario',
                'verbose_name_plural': 'Información Adicional de Usuarios',
            },
        ),
    ]
