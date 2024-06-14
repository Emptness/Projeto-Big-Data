phones_combined = pd.concat([list_phones_appear_fev, list_phones_appear_abr, list_phones_appear_mar])
list_phones_appear_total = list_phones_appear_abr.groupby('Celular mais trabalhado', as_index=False).sum()


solutions_combined = pd.concat([list_solutions_fev, list_solutions_abr, list_solutions_mar])
list_solutions_total = list_solutions_abr.groupby('Serviço mais trabalhado', as_index=False).sum()

junção_resultados = pd.concat([list_phones_appear_total, list_solutions_total], axis=1)
display(junção_resultados)