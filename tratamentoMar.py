month_movement = pd.read_excel('/content/marco.xlsx')

month_movement.drop(columns=['Unnamed: 0'], inplace=True)

replace_models = {
  'samsunga21s': 'samsung',
  'sansung': 'samsung',
  'samsunga51' : 'samsung',
  'moto': 'motorola',
}

month_movement = month_movement.drop(7)
month_movement = month_movement.dropna()

def replace_phone_model_name(array):
  phone_model_name = []

  for x in array:
    first_word = str(x).split(' ', 1)[0]
    phone_model = first_word.lower()

    if(phone_model in replace_models.keys()):
      phone_model = replace_models[phone_model]

    phone_model_name.append(phone_model)

  return phone_model_name