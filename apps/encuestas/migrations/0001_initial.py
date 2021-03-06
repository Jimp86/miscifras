# Generated by Django 3.0.9 on 2020-12-23 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpPublica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=35, null=True)),
                ('contador', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='PadronElectoral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(blank=True, max_length=120, null=True)),
                ('provincia', models.CharField(blank=True, max_length=60, null=True)),
                ('canton', models.CharField(blank=True, max_length=120, null=True)),
                ('circunscripcion', models.CharField(blank=True, max_length=120, null=True)),
                ('parroquia', models.CharField(blank=True, max_length=120, null=True)),
                ('estadoParroquia', models.CharField(blank=True, max_length=120, null=True)),
                ('zona', models.CharField(blank=True, max_length=120, null=True)),
                ('junta', models.CharField(blank=True, max_length=120, null=True)),
                ('homonimo', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VotosPresidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('numero_votos', models.IntegerField(default=0)),
                ('ipPublica', models.CharField(default='', max_length=35)),
                ('aceptado', models.BooleanField(default=False)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participantes.Candidatos')),
            ],
        ),
        migrations.CreateModel(
            name='VotosConcejal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('numero_votos', models.IntegerField(default=0)),
                ('ipPublica', models.CharField(default='', max_length=35)),
                ('aceptado', models.BooleanField(default=False)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participantes.Candidatos')),
            ],
        ),
        migrations.CreateModel(
            name='VotosAlcalde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('numero_votos', models.IntegerField(default=0)),
                ('ipPublica', models.CharField(default='', max_length=35)),
                ('aceptado', models.BooleanField(default=False)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participantes.Candidatos')),
            ],
        ),
    ]
