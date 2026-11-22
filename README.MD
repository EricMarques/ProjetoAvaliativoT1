# Detecção de ocupação de ambientes com sensores IoT

Projeto avaliativo do curso SCTEC Aperfeiçoar - Integração de IA com Dados.

## Turma: T1
## Aluno: Eric Felipe Barros Marques

## Problema

Em um complexo industrial com sensores ambientais, é preciso saber se uma sala está ocupada ou vazia para desligar o ar-condicionado e a iluminação quando não há ninguém, reduzindo o gasto de energia. Neste projeto monto um pipeline de ciência de dados que prevê essa ocupação (0 = vazia, 1 = ocupada) a partir de leituras de sensores.

## Dados

Uso o Occupancy Detection Dataset, do repositório UCI Machine Learning Repository. As variáveis são temperatura, umidade, luminosidade, CO2, razão de umidade e a ocupação, que é a variável alvo.

Os arquivos ficam na pasta `data/`. O notebook baixa os dados automaticamente caso ainda não existam.

## Técnicas e tecnologias

- Python, pandas e numpy para manipulação dos dados
- matplotlib e seaborn para os gráficos
- scikit-learn para os modelos (KNN e Árvore de Decisão)
- Jupyter Notebook
- Git e GitHub para versionamento e organização das tarefas

O notebook segue sete fases: análise exploratória, limpeza dos dados, criação de uma nova variável, divisão treino e teste, escalonamento, ajuste de hiperparâmetros e avaliação final.

## Estrutura do repositório

- `data/raw/`: arquivos originais da base, sem alteração
- `data/processed/`: dados tratados, gerados no notebook
- `notebooks/analise_exploratoria.ipynb`: notebook com todo o pipeline
- `requirements.txt`: dependências com as versões usadas
- `README.md`: esta documentação

## Como executar

1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

No Linux ou macOS, a ativação é `source venv/bin/activate`.

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Abra o notebook em `notebooks/analise_exploratoria.ipynb` e execute as células em ordem.

## Organização do trabalho

Organizei as tarefas em um quadro no GitHub Projects, uma por fase do notebook. Usei a branch `develop` para reunir o trabalho e criei uma branch de feature para cada tarefa, integrada por pull request.

## Análise exploratória

A base tem duas classes, com cerca de 64% de leituras de ambiente desocupado e 36% de ocupado. A luminosidade é a variável mais relacionada à ocupação (correlação de 0,93), seguida pelo CO2 (0,77). A razão de umidade é muito correlacionada com a umidade e o CO2, por ser derivada de temperatura e umidade.v

## Limpeza dos dados

Removi 82 linhas duplicadas (de 2665 para 2583) e não encontrei valores ausentes. Nos boxplots, só a luminosidade tem outliers (3 leituras), que mantive por parecerem leituras reais. A base tratada é salva em `data/processed/`.

## Resultados

Será preenchido ao final do projeto.

## Melhorias possíveis

Será preenchido ao final do projeto.