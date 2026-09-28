from pathlib import Path 
import pandas as pd
import matplotlib.pyplot as plt

# Caminhos das pastas do projeto
PASTA_PROJETO = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"

# Cria a pasta que receberá os gráficos
PASTA_GRAFICOS.mkdir(exist_ok=True)

# Carregamento dos arquivos CSV
salarios = pd.read_csv(PASTA_DADOS / "query_01.csv")
localizacao = pd.read_csv(PASTA_DADOS / "query_02.csv")

# Padronização dos nomes das colunas
salarios.columns = salarios.columns.str.lower()
localizacao.columns = localizacao.columns.str.lower()

print("Dados de salários:", salarios.shape)
print("Dados de localização:", localizacao.shape)

# Visualização inicial
print("\nPrimeiras linhas dos dados de salários:")
print(salarios.head())

print("\nValores ausentes nos dados de salários:")
print(salarios.isnull().sum())

print("\nEstatísticas descritivas dos salários:")
print(salarios["salary"].describe().round(2))

# Salários por departamento
salario_departamento = (
    salarios.groupby("department_name")["salary"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
    .sort_values("mean", ascending=False)
)

print("\nSalários por departamento:")
print(salario_departamento)

# Salários por cargo
salario_cargo = (
    salarios.groupby("job_title")["salary"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
    .sort_values("mean", ascending=False)
)

print("\nSalários por cargo:")
print(salario_cargo)

# Salários por região
salario_regiao = (
    localizacao.groupby("region_name")["salary"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(2)
    .sort_values("mean", ascending=False)
)

print("\nSalários por região:")
print(salario_regiao)

# Exportação dos resumos
salario_departamento.to_csv(PASTA_DADOS / "resumo_departamentos.csv")
salario_cargo.to_csv(PASTA_DADOS / "resumo_cargos.csv")
salario_regiao.to_csv(PASTA_DADOS / "resumo_regioes.csv")

# Histograma dos salários
plt.figure(figsize=(9, 5))
plt.hist(salarios["salary"], bins=10, color="#4472C4", edgecolor="black")
plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Número de funcionários")
plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "histograma_salarios.png", dpi=300)
plt.close()

# Boxplot dos salários
plt.figure(figsize=(9, 4))
plt.boxplot(salarios["salary"], vert=False)
plt.title("Boxplot dos salários")
plt.xlabel("Salário")
plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "boxplot_salarios.png", dpi=300)
plt.close()

# Gráfico de salário médio por departamento
salario_departamento["mean"].sort_values().plot(
    kind="barh",
    figsize=(10, 6),
    color="#70AD47"
)
plt.title("Salário médio por departamento")
plt.xlabel("Salário médio")
plt.ylabel("Departamento")
plt.tight_layout()
plt.savefig(PASTA_GRAFICOS / "salario_medio_departamento.png", dpi=300)
plt.close()

print("\nAnálise concluída. Os gráficos foram salvos na pasta 'graficos'.")