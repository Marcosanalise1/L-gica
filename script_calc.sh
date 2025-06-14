!#/bin/bash

echo "Atualizando os repositórios e instalando o python"

#Atualização dos repositórios
sudo apt update

#Instalação do python
sudo apt install python3

echo "Bem vindo ao programa Calculadora"

python3 /home/aula/modulo1/python/calc.py
