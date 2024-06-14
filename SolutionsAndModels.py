def replace_solution_names(array):
  solution_names = []

  for x in array:
    solution_name = str(x).split(' e ')[0]
    solution_name = solution_name.split(' / ')[0].lstrip()
    solution_names.append(solution_name)
  return solution_names

def get_all_phone_models(all_models):
  return set(all_models)

def get_most_appear_data(data):
  return data.value_counts()

month_movement['Modelo Do aparelho'] = replace_phone_model_name(month_movement['Modelo Do aparelho'])
month_movement['Solução'] = replace_solution_names(month_movement['Solução'])

phone_model_most_appear = get_most_appear_data(month_movement['Modelo Do aparelho'])
solution_most_worked = get_most_appear_data(month_movement['Solução'])