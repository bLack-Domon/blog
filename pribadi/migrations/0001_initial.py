# Generated by Django 4.2 on 2023-04-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=250, null=True)),
                ('tentang_diri', models.CharField(blank=True, max_length=250, null=True)),
                ('hp', models.CharField(blank=True, max_length=250, null=True)),
                ('fb', models.CharField(blank=True, max_length=250, null=True)),
                ('ig', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Profil Diri',
            },
        ),
    ]
