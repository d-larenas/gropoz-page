# Generated by Django 3.2 on 2023-01-13 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteregister',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logs_page.sitealert'),
        ),
    ]
