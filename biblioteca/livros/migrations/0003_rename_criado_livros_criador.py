# Generated by Django 4.1.7 on 2023-04-01 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_rename_pagginas_livros_paginas_alter_livros_id_livro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='criado',
            new_name='criador',
        ),
    ]
