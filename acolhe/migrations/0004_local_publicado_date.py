# Generated by Django 2.2.2 on 2019-06-20 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acolhe', '0003_local_acolhido'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='publicado_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]