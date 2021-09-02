# Generated by Django 3.1.5 on 2021-04-08 17:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import util.upload
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comum', '0001_initial'),
        ('social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('foto_temp', models.ImageField(upload_to='fotos')),
                ('foto', models.BinaryField(blank=True, default=None, null=True)),
                ('thumbnail', models.BinaryField(blank=True, default=None, null=True)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_foto_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_foto_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=100)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_genero_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_genero_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='ModeloTipoPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrgaoExpedidor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=20)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacao.estado')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_orgaoexpedidor_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_orgaoexpedidor_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Órgão Expedidor',
                'verbose_name_plural': 'Órgãos Expedidores',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=150)),
                ('nome_social', models.CharField(blank=True, max_length=150, null=True)),
                ('data_nascimento', models.DateField(blank=True, default=None, null=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='CPF inválido', regex='[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}\\-?[0-9]{2}')])),
                ('rg', models.CharField(blank=True, max_length=15, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=150, null=True)),
                ('nome_pai', models.CharField(blank=True, max_length=150, null=True)),
                ('mae_falecido', models.BooleanField(default=False)),
                ('mae_nao_declarado', models.BooleanField(default=False)),
                ('pai_falecido', models.BooleanField(default=False)),
                ('pai_nao_declarado', models.BooleanField(default=False)),
                ('enderecos', models.ManyToManyField(blank=True, to='comum.Endereco')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='localizacao.estado')),
                ('estado_civil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.estadocivil')),
                ('foto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='foto_pessoa', to='cadastros.foto')),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.genero')),
                ('grau_instrucao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.graudeinstrucao')),
                ('nacionalidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='localizacao.pais')),
                ('naturalidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='localizacao.cidade')),
                ('necessidade_especial', models.ManyToManyField(blank=True, to='social.NecessidadeEspecial')),
                ('orgao_expedidor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orgao_expedidor_pessoa', to='cadastros.orgaoexpedidor')),
                ('orientacao_sexual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.orientacaosexual')),
                ('profissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.profissao')),
                ('raca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.raca')),
                ('religiao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.religiao')),
                ('telefones', models.ManyToManyField(blank=True, to='comum.Telefone')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_pessoa_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_pessoa_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vulgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulgo', models.CharField(max_length=150)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pessoa')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=150)),
                ('sigla', models.CharField(blank=True, max_length=30, null=True)),
                ('enderecos', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='setor_endereco', to='comum.endereco')),
                ('setor_pai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='setorpai', to='cadastros.setor')),
                ('telefones', models.ManyToManyField(blank=True, to='comum.Telefone')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_setor_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_setor_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='RegimePrisional',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_regimeprisional_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_regimeprisional_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Regime Prisional',
                'verbose_name_plural': 'Regimes Prisionais',
            },
        ),
        migrations.CreateModel(
            name='Periculosidade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=20)),
                ('observacao', models.CharField(blank=True, max_length=500, null=True)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_periculosidade_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_periculosidade_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Periculosidade',
                'verbose_name_plural': 'Periculosidades',
            },
        ),
        migrations.CreateModel(
            name='OutroNome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outro', models.CharField(max_length=150)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pessoa')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grau_de_instrucao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.graudeinstrucao')),
                ('orientacao_sexual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.orientacaosexual')),
                ('profissao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.profissao')),
                ('raca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.raca')),
                ('religiao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='social.religiao')),
            ],
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=150)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_funcao_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_funcao_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Função',
                'verbose_name_plural': 'Funções',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('num_cod', models.CharField(max_length=30)),
                ('observacao', models.CharField(blank=True, max_length=100, null=True)),
                ('arquivo_temp', models.FileField(upload_to='documentos')),
                ('arquivo', models.BinaryField(blank=True, default=None, null=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipo_documentos', to='cadastros.tipodocumento')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_documentos_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_documentos_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='ComportamentoInterno',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_comportamentointerno_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_comportamentointerno_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comportamento de Interno',
            },
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('delete_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('excluido', models.BooleanField(default=False)),
                ('cargo', models.CharField(max_length=150)),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('usuario_edicao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updatedcadastros_cargos_related', to=settings.AUTH_USER_MODEL)),
                ('usuario_exclusao', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletecadastros_cargos_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cargos',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='CaracteristicaFisica',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('arquivo', models.ImageField(null=True, upload_to=util.upload.diretorio_upload)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.pessoa')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=False)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modelotipopessoa')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tipos_pessoa', to='cadastros.pessoa')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('pessoa', 'modelo')},
            },
        ),
        migrations.CreateModel(
            name='DocumentoPessoa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=80)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='')),
                ('validade', models.DateField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='localizacao.estado')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacao.pais')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos', to='cadastros.pessoa')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documentos', to='cadastros.tipodocumento')),
                ('usuario_cadastro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('tipo', 'numero', 'estado', 'pais')},
            },
        ),
    ]