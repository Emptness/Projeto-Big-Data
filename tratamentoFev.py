df_marca = ['Samsung', 'Moto', 'Philco', 'Iphone', 'Xiaomi', 'LG']

def substitui_marca(marca,df_marca):
  for i in df_marca:
    if i.lower() in str(marca).lower():
      return i
    elif 'sansung' in str(marca).lower():
      return 'Samsung'
