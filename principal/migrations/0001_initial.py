# Generated by Django 5.0.1 on 2024-01-05 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheptel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='CedricJ', max_length=40)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Cheptel',
                'verbose_name_plural': 'Cheptels',
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type_action', models.CharField(choices=[('Suppression_cellules_royales', 'Suppression_cellules_royales'), ('date_verification_santé', 'Date vérification santé'), ('Date_récole', 'Date de récolte'), ('Quantité_recolte', 'Quantité récolte'), ('Pose_hausses', 'Pose hausses'), ('Destruction', 'Destruction'), ('Traitement', 'Traitement')], max_length=100)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interventions', to='principal.intervention')),
            ],
            options={
                'verbose_name': 'Intervention',
                'verbose_name_plural': 'Interventions',
            },
        ),
        migrations.CreateModel(
            name='Ruche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='CedricJ', max_length=40)),
                ('status_hive', models.CharField(choices=[('En activité', 'En activité'), ('En attente', 'En attente'), ('Détruite', 'Détruite')])),
                ('queen_birthday', models.DateTimeField()),
                ('type_bee', models.CharField(choices=[('A.Scutellata', 'A.Scutellata'), ('A.Adansonii', 'A.Adansonii'), ('A.Mellifera', 'A.Mellifera'), ('A.Ligustica', 'A.Ligustica'), ('A.Syriaca', 'A.Syriaca'), ('A.Carnica', 'A.Carnica'), ('A.Intermissa', 'A.Intermissa'), ('Autre', 'Autre')])),
                ('contamination', models.CharField(choices=[('acarapisose', 'acarapisose'), ('loque_américaine', 'loque américaine'), ('infestation_par_le petit_coléoptère_des_ruches', 'infestation par_le_petit_coléoptère_des_ruches'), ('infestation_par_l’acarien_Tropilaelaps', 'infestation par l’acarien Tropilaelaps'), ('varroose', 'varroose')])),
                ('cheptel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ruches', to='principal.cheptel')),
            ],
            options={
                'verbose_name': "Caractéristique d'une ruche",
                'verbose_name_plural': "Caractéristiques d'une ruche",
            },
        ),
    ]