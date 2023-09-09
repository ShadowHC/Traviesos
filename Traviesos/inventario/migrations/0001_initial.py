# Generated by Django 4.2.4 on 2023-09-08 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_categoria', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_marca', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'db_table': 'marcas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_producto', models.CharField(max_length=30)),
                ('Precio_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Imagen_producto', models.CharField(max_length=100)),
                ('Descripcion_producto', models.CharField(max_length=50)),
                ('Id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria')),
                ('Id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_proveedor', models.CharField(max_length=30)),
                ('Apellido_proveedor', models.CharField(max_length=30)),
                ('Telefono_Proveedor', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_Cantidad', models.IntegerField()),
                ('Id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'db_table': 'stocks',
                'ordering': ['id'],
            },
        ),
    ]
