lucro_fev = df_fev['Lucro'].sum()
lucro_mar = df_mar['Lucro'].sum()
lucro_abr = df_abr['Lucro'].sum()

meta_mensal = 20000
lucro_total = lucro_fev + lucro_mar + lucro_abr
lucro_medio_mensal = lucro_total / 3
deficit = meta_mensal - lucro_medio_mensal

lucro_total_abr = month_movement['Lucro'].sum()
total_servicos_abr = len(month_movement)
lucro_medio_por_cliente = lucro_total_abr / total_servicos_abr

clientes_adicionais = deficit / lucro_medio_por_cliente

dias_uteis = 22
total_servicos_atuais = total_servicos_abr
clientes_totais = total_servicos_atuais + clientes_adicionais
media_diaria = clientes_totais / dias_uteis

print(f"Lucro atual médio mensal: R$ {lucro_medio_mensal:.2f}")

print(f"Deficit para alcançar a meta: R$ {deficit:.2f}")

print(f"Lucro médio por cliente: R$ {lucro_medio_por_cliente:.2f}")

print(f"Clientes adicionais necessários: {clientes_adicionais:.2f}")

print(f"Média diária de atendimentos necessários: {media_diaria:.2f}")

junção_resultados = pd.concat([list_phones_appear_total, list_solutions_total], axis=1)
display(junção_resultados)