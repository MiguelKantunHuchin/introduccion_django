# Generated by Django 4.1 on 2024-06-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_habilidades_empleado_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre Completo'),
        ),
    ]