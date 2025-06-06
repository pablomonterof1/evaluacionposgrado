# Generated by Django 5.2 on 2025-05-12 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programasposgrado', '0005_alter_cohortes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComposicionCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('tipodedato', models.IntegerField(choices=[(1, 'Composición 1'), (2, 'Composición 2'), (3, 'Composición 3')])),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('programadeposgrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composicionca_titulacion', to='programasposgrado.maestriacohortemodalidad')),
            ],
        ),
    ]
