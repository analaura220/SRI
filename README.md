# Sistema de Recuperação de Informação (SRI)

## Descrição

Interface gráfica em Python para busca de artigos científicos com suporte a busca booleana e vetorial.

## Funcionalidades

### 1. Busca Booleana

- Separa palavras e operadores booleanos (AND, OR)
- Processa operadores da esquerda para direita
- **AND**: Realiza interseção de resultados
- **OR**: Realiza união de resultados

**Exemplo de uso:**

```
palavra1 and palavra2 or palavra3
```

### 2. Busca Vetorial

- Remove vírgulas da consulta
- Realiza união de todos os termos buscados
- Retorna artigos que contêm qualquer um dos termos

**Exemplo de uso:**

```
palavra1, palavra2, palavra3
```

ou

```
palavra1 palavra2 palavra3
```

## Características

- Normalização automática para minúsculas
- Mantém acentuação das palavras
- Exibe resultados com Ranking, Título, Autores, Resumo, Palavras Chaves, Link, Filiação e Relevância
- Botão "Ver Detalhes" mostra termos, TF e IDF de cada artigo

## Requisitos

### Bibliotecas Python

```bash
pip install mysql-connector-python
```

### Banco de Dados

- MySQL Server
- Banco de dados "SRI" criado e populado conforme o arquivo `Banco_SRI.sql`

## Configuração

1. Edite o arquivo `config.py` ou diretamente na classe `SistemaBuscaSRI` com as credenciais do seu banco de dados:

```python
self.db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sua_senha',  # Altere aqui
    'database': 'SRI'
}
```

## Como Executar

```bash
python interface_busca.py
```

## Estrutura do Banco de Dados

### Tabelas Utilizadas:

- **Artigos**: Informações dos artigos (título, filiação, resumo, etc.)
- **Autores**: Autores dos artigos (com ordem)
- **Dicionario**: Termos indexados
- **Documentos**: Relaciona artigos com termos (TF, IDF)

## Fluxo de Uso

1. Digite a consulta no campo de entrada
2. Selecione o tipo de busca (Booleana ou Vetorial)
3. Clique em "Pesquisar"
4. Visualize os resultados na tabela
5. Selecione um artigo e clique em "Ver Detalhes" para ver os termos, TF e IDF
6. Clique duas vezes no artigo e será direcionado para o arquivo

## Detalhes Técnicos

### Busca Booleana

- Vetores separados: `palavras[]` e `operadores[]`
- Processamento sequencial da esquerda para direita
- Utiliza operações de conjunto (intersection/union)

### Busca Vetorial

- Vetor único: `palavras[]`
- Remove vírgulas e separa por espaços
- Utiliza apenas união (union)

### Janela de Detalhes

- GROUP BY por artigo
- Exibe: termo, tf_logaritimo, idf_logaritimo
- Dados da tabela Documentos com JOIN em Dicionario
