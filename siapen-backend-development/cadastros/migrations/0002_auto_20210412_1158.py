# Generated by Django 3.1.5 on 2021-04-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("cadastros", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="documentos",
            name="observacao",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        )
    ]
