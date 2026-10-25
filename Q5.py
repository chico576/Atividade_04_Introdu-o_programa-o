dvd = float(input())
jr_men = float(input())
vlr_men = float(input())
mes = dvd_f = total_pg = j_pg = 0


if dvd > 0:
    while (mes * vlr_men < dvd):
        total_pg += (vlr_men + ((jr_men*0.01) * vlr_men))
        j_pg += (jr_men*0.01 * vlr_men)
        mes += 1


print(f"Dívida ínicial de R${dvd:.2f} paga em {mes} mêses, \n totalizando R${total_pg:.2f} devido ao juros total de R${j_pg:.2f}.")

