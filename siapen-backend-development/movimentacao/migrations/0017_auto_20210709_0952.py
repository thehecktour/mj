# Generated by Django 3.1.5 on 2021-07-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0016_merge_20210709_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoinclusao',
            name='tipo_escolta',
            field=models.CharField(blank=True, choices=[('INCLUSAO', 'INCLUSÃO')], default=None, max_length=20, null=True),
        ),
    ]