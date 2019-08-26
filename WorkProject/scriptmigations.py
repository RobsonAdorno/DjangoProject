#!/usr/bin/python3
"""
Script para adicionar os migrations para dentro da base de dados.
"""
import os

makemigration = os.system('python3 manage.py makemigrations')
migration = os.system('python3 manage.py migrate')

if migration == 0 and makemigration == 0:
    print('Migrations gerado com sucesso')
else:
    print('Erro ao gerar os migrations')
