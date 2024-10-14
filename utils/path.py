import sys
import os

def path_for_modules():
    # Adiciona o diretório 'modules' de forma dinâmica ao sys.path
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do script
    modules_path = os.path.join(current_dir, 'modules')  # Caminho dinâmico para a pasta 'modules'

    # Adiciona 'modules' ao sys.path
    if modules_path not in sys.path:
        return modules_path