# Generated by Django 3.1.5 on 2021-05-07 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("juridico", "0003_auto_20210507_1030"),
    ]

    operations = [
        migrations.AddField(
            model_name="normasjuridicas",
            name="usuario_ativacao",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Ativacao_normas_juridicas_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="normasjuridicas",
            name="usuario_inativacao",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Inativação_normas_juridicas_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="titulolei",
            name="usuario_ativacao",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Ativacao_titulo_lei_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="titulolei",
            name="usuario_inativacao",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="Inativação_titulo_lei_related",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
