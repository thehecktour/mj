# Generated by Django 3.1.5 on 2021-07-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0001_initial'),
        ('pessoas', '0015_emailvisitante_rgvisitante_visitante'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='enderecos',
            field=models.ManyToManyField(blank=True, related_name='endereco_visitante_related', to='comum.Endereco'),
        ),
        migrations.AddField(
            model_name='visitante',
            name='telefones',
            field=models.ManyToManyField(blank=True, related_name='telefone_visitante_related', to='comum.Telefone'),
        ),
    ]