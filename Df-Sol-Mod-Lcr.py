def dataframe_most_appear(series, column_names):
  new_dataframe = {
    column_names[0]: series.keys(),
    column_names[1]: series.values
  }

  return pd.DataFrame(new_dataframe)

list_phones_appear_fev = dataframe_most_appear(phone_model_most_appear, ['Celular mais trabalhado', 'Quantidade'])
list_solutions_fev = dataframe_most_appear(solution_most_worked, ['Serviço mais trabalhado', 'Quantidade'])
lucro_fev_df

junção_fev = pd.concat([list_phones_appear_fev, list_solutions_fev, lucro_fev_df], axis=1)
display(junção_fev)

def dataframe_most_appear(series, column_names):
  new_dataframe = {
    column_names[0]: series.keys(),
    column_names[1]: series.values
  }

  return pd.DataFrame(new_dataframe)

list_phones_appear_mar = dataframe_most_appear(phone_model_most_appear, ['Celular mais trabalhado', 'Quantidade'])
list_solutions_mar = dataframe_most_appear(solution_most_worked, ['Serviço mais trabalhado', 'Quantidade'])
lucro_mar_df

junção_mar = pd.concat([list_phones_appear_mar, list_solutions_mar, lucro_mar_df], axis=1)
display(junção_mar)

def dataframe_most_appear(series, column_names):
  new_dataframe = {
    column_names[0]: series.keys(),
    column_names[1]: series.values
  }

  return pd.DataFrame(new_dataframe)

list_phones_appear_abr = dataframe_most_appear(phone_model_most_appear, ['Celular mais trabalhado', 'Quantidade'])
list_solutions_abr = dataframe_most_appear(solution_most_worked, ['Serviço mais trabalhado', 'Quantidade'])
lucro_abr_df

junção_abr = pd.concat([list_phones_appear_abr, list_solutions_abr, lucro_abr_df], axis=1)
display(junção_abr)