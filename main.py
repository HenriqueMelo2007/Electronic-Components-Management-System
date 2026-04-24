"""
Ponto de Entrada

Este script atua como o inicializador da aplicação. Ele verifica se o módulo 
está sendo executado como o script principal e, em caso positivo, invoca a 
função main do pacote de interface de linha de comando (CLI) para iniciar 
o ciclo de vida do programa.
"""
from management_system.cli import main

if __name__ == "__main__":
    main()