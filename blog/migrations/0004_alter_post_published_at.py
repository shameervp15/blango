# Generated by Django 3.2.22 on 2023-11-01 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231026_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
