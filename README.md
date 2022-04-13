# Boas vindas ao repositório do projeto TING(Trybe is not Google)!

O projeto consiste em uma aplicação que simule o algoritmo de indexação de documentos similar ao do Google. Ou seja, a ideia do projeto é anexar arquivos de texto e posteriormente manipular funções de busca sobre estes arquivos de texto.

## Tecnologia Usada

- Python

## Habilidades

- Manipular Deque

- Manipular Pilhas

- Manipular Nó & Listas ligadas

- Manipular Listas duplamentes ligadas

## Rodando o Projeto Localmente

1° - `git clone https://github.com/lucasam1992/project-ting.git` - Clone o repositório para a sua máquina <br />
2° - `cd project-ting` - Entre na pasta do repositório clonado <br />
3° - `python3 -m venv .venv && source .venv/bin/activate` - Crie e ative o ambiente virtual para o projeto <br />
4° - `python3 -m pip install -r dev-requirements.txt` - Instale as dependências <br />

### Requisitos

- 1 - Implemente uma fila para armazenar os arquivos que serão lidos. Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- 2 - Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Todas as mensagens de erro devem ir para a `stderr`.

- 3 - Implemente uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o preprocessamento do conteúdo.

- 4 - Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- 5 - Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.

- 6 - Implemente uma função `exists_word` dentro do módulo `word_search`, que valide a existência da palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha conforme apresentação abaixo.

- 7 - Implemente uma função `search_by_word` dentro do módulo `word_search`, que busque a palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha, o conteúdo e o arquivo da ocorrência.

## Autor

- Lucas Machado
