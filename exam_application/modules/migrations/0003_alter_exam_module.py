# Generated by Django 4.0.4 on 2022-05-21 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_module_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='modules.module'),
        ),
    ]
