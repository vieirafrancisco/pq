# PQ

Este projeto tem como objetivo fazer uma versão simples do [RQ](https://python-rq.org/) em python. O RQ consiste em um agendador de tarefas (jobs) utilizando filas.  
Neste trabalho iremos implementar workers que irão ter suas próprias threads para tratar os jobs de uma queue específica. Race condition é evitada quando os wokers tentam tirar um mesmo job de uma fila específica.  
Esse mecânismo é muito utilizado em sistemas que fazem muitas requisições à API's.

## Exemplo:
O exemplo que iremos utilizar para executar nossa ferramenta é:
- Extrair o html de uma página utilizando sua URL
- Pegar somente o que tiver de textos desse html (tags p, h1, h2,...,etc)
- Salvar em um diretório chamado de artigos e cada arquivo tem o nome com sua respectiva URL

## Requirements:
- python 3.6+
- virtualenv

## Setup:
**Criar virtualenv:**
```bash
virtualenv venv
```

**Entrar na virtualenv:**
```bash
source venv/bin/activate  # linux
venv\Scripts\activate  # windows
```

**Instalar Dependências:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Uso:

```bash
python main.py
```

Agora é só olhar no diretório `artigos` e os arquivos resultantes vão estar lá :)

## Dupla:
Francisco Vieira  
Jadson Lucio

## Informações:
Trabalho referênte a matéria de Computação Paralela na PLE da UFAL

## Licença:
[MIT License](https://github.com/vieirafrancisco/pq/blob/main/LICENSE)
