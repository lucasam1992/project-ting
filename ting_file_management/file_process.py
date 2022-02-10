from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    info_file = txt_importer(path_file)

    info_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(info_file),
        "linhas_do_arquivo": info_file
    }

    instance.enqueue(info_return)
    print(info_return, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
