# Detecção de ocupação de ambientes com sensores IoT

Projeto avaliativo do curso SCTEC Aperfeiçoar - Integração de IA com Dados.

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

- `data/`: arquivos da base de dados
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

## Resultados

Será preenchido ao final do projeto.

## Melhorias possíveis

Será preenchido ao final do projeto.