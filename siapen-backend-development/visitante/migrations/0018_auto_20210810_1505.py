# Generated by Django 3.1.5 on 2021-08-10 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("visitante", "0017_auto_20210809_1452")]

    operations = [
        migrations.RemoveField(model_name="anuencia", name="arquivo"),
        migrations.RemoveField(model_name="anuencia", name="arquivo_temp"),
        migrations.AddField(
            model_name="anuencia",
            name="documento",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="documento_visitante_related",
                to="visitante.documentosvisitante",
            ),
            preserve_default=False,
        ),
    ]
