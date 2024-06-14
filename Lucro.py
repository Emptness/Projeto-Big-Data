lucro_fev = df_fev ['Lucro'].sum()
lucro_fev_f="R$ {:.2f}".format(lucro_fev)

lucro_abr = df_abr ['Lucro'].sum()
lucro_abr_f = "R$ {:.2f}".format(lucro_abr)

lucro_mar = df_mar ['Lucro'].sum()
lucro_mar_f = "R$ {:.2f}".format(lucro_mar)

lucro_total = lucro_fev +  lucro_mar + lucro_abr
lucro_total_f = "R$ {:.2f}".format(lucro_total)

lucro_medio = lucro_total / 3
lucro_medio_f = "R$ {:.2f}".format(lucro_medio)

lucro_fev_df = pd.DataFrame({'Lucro': [lucro_fev_f]})
lucro_abr_df = pd.DataFrame({'Lucro': [lucro_abr_f]})
lucro_mar_df = pd.DataFrame({'Lucro': [lucro_mar_f]})
lucro_total_df = pd.DataFrame({'Lucro': [lucro_total_f]})
lucro_medio_df = pd.DataFrame({'Lucro': [lucro_medio_f]})