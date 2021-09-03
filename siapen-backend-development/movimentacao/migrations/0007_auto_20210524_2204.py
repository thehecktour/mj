# Generated by Django 3.1.5 on 2021-05-25 01:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movimentacao", "0006_analisepedido"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedidoinclusao",
            name="data_movimentacao",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2021, 5, 25, 1, 4, 54, 628871, tzinfo=utc),
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="PedidoInclusaoMovimentacao",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("motivo", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "fase_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="movimentacao.fasespedido",
                    ),
                ),
                (
                    "pedido_inclusao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="movimentacao.pedidoinclusao",
                    ),
                ),
                (
                    "usuario_cadastro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="usuario_movimentacao_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
