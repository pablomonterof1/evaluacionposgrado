# Generated by Django 5.2 on 2025-05-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programasposgrado', '0011_delete_maestriacohortemodalidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programaposgrado',
            name='cohorte',
            field=models.IntegerField(choices=[(1, 'Primera'), (2, 'Segunda'), (3, 'Tercera'), (4, 'Cuarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Septima'), (8, 'Octava'), (9, 'Novena'), (10, 'Decima')], default=1),
            preserve_default=False,
        ),
    ]
