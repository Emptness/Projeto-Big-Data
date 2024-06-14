import numpy as np

products = [
    "Reforma Geral", "Reparo do áudio", "Substituição",
    "troca da bateria", "troca de bateria", "Troca de Frontal e botão Biometria",
    "Troca de tela", "troca de tela e doc", "Troca de tela e pelicula",
    "Troca de tela+pelicula", "venda da bateria"
]
max_values = [490, 250, 200, 180, 300, 300, 400, 490, 500, 1590, 100]
min_values = [170, 250, 200, 80, 120, 280, 120, 200, 250, 295, 100]
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
quantities_df = pd.DataFrame(index=products, columns=months)
values_df = pd.DataFrame(index=products, columns=months)
expense_reduction = 5193

for month in months:
    quantities = {
        product: np.random.randint(2, 15)
        for product in products
    }
    quantities_df[month] = quantities.values()

    values = {
        product: np.random.randint(min_value, max_value + 1)
        for product, min_value, max_value in zip(products, min_values, max_values)
    }
    values_df[month] = values.values()

monthly_values = values_df * quantities_df
monthly_totals = monthly_values.sum() - expense_reduction
item_means = values_df.mean(axis=1).round(2)

print("Quantidade de itens de cada mês:")
print(quantities_df)

print("Valor total dos 12 meses:")
print(monthly_totals)

print("Média dos valores de cada item:")
print(item_means)

monthly_totals_df = pd.DataFrame(monthly_totals.values, index=months, columns=["Valor Total"])
item_means_df = pd.DataFrame(item_means.values, index=products, columns=["Média de Valores"])

quantities_df.to_excel('Quantidade Simulada.xlsx')
monthly_totals_df.to_excel('Meses Simulados.xlsx')
item_means_df.to_excel('Média Simulada.xlsx')