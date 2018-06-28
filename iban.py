
# ---------------------------------------------------------------------------------------
# FORMATEE EL NUMERO DE CUENTA
# ---------------------------------------------------------------------------------------
def formatee_el_numero_de_cuenta(la_cuenta_cliente: str, los_dos_digitos):
    iniciales_del_pais = "CR"
    return "{}{}{}".format(iniciales_del_pais, los_dos_digitos, la_cuenta_cliente)

# ---------------------------------------------------------------------------------------
# FORMATEE EL NUMERO COMO TEXTO
# ---------------------------------------------------------------------------------------
def formatee_el_numero_como_texto(el_numero_verificador: int):
    return str(el_numero_verificador)


# ---------------------------------------------------------------------------------------
# FORMATEE EL NUMERO PRCEDIDO CON UN CERO
# ---------------------------------------------------------------------------------------
def formatee_el_numero_precedido_con_un_cero(el_numero_verificador: int):
    return "0{}".format(el_numero_verificador)


# ---------------------------------------------------------------------------------------
# TIENE UN SOLO DIGITO
# ---------------------------------------------------------------------------------------
def tiene_un_solo_digito(el_numero_verificador: int):
    return el_numero_verificador < 10


# ---------------------------------------------------------------------------------------
# FORMATEE COMO DOS DIGITOS
# ---------------------------------------------------------------------------------------
def formatee_como_dos_digitos(el_numero_verificador: int):

    if tiene_un_solo_digito(el_numero_verificador):
        return formatee_el_numero_precedido_con_un_cero(el_numero_verificador)
    else:
        return formatee_el_numero_como_texto(el_numero_verificador)


# ---------------------------------------------------------------------------------------
# CALCULE EL NUMERO VERIFICADOR
# ---------------------------------------------------------------------------------------
def calcule_el_numero_verificador(el_requerimiento: int):
    return int(98 - el_requerimiento % 97)


# ---------------------------------------------------------------------------------------
# COMBIERTA A NUMERO
# ---------------------------------------------------------------------------------------
def combierta_a_numero(el_requerimiento: str):
    return int(el_requerimiento)


# ---------------------------------------------------------------------------------------
# FORMATEE EL REQUERIMIENTO
# ---------------------------------------------------------------------------------------
def formatee_el_requerimiento(la_cuenta_cliente: str):
    el_codigo_del_pais = "00"
    el_numero_iso_del_pais = "1227"
    return "{}{}{}".format(la_cuenta_cliente, el_numero_iso_del_pais, el_codigo_del_pais)


# ---------------------------------------------------------------------------------------
# GENERE EL REQUERIMIENTO COMO NUMERO
# ---------------------------------------------------------------------------------------
def genere_el_requerimiento_como_numero(la_cuenta_cliente: str):
    el_requerimiento = formatee_el_requerimiento(la_cuenta_cliente)
    return combierta_a_numero(el_requerimiento)


# ---------------------------------------------------------------------------------------
# GENERE EL NUMERO VERIFICADOR
# ---------------------------------------------------------------------------------------
def genere_el_numero_verificador(la_cuenta_cliente: str):
    el_requerimiento_como_numero = genere_el_requerimiento_como_numero(la_cuenta_cliente)
    return calcule_el_numero_verificador(el_requerimiento_como_numero)


# ---------------------------------------------------------------------------------------
# GENERE LOS DOS DIGITOS VERIFICADORES
# ---------------------------------------------------------------------------------------
def genere_los_dos_digitos_verificadores(la_cuenta_cliente: str):
    el_numero_verificador = genere_el_numero_verificador(la_cuenta_cliente)
    return formatee_como_dos_digitos(el_numero_verificador)


# ---------------------------------------------------------------------------------------
# GENERE EL NUMERO DE LA CUENTA IBAN
# ---------------------------------------------------------------------------------------
def genere_el_numero_de_cuenta_iban(la_cuenta_cliente: str):
    los_digitos = genere_los_dos_digitos_verificadores(la_cuenta_cliente)
    return formatee_el_numero_de_cuenta(la_cuenta_cliente, los_digitos)


# =======================================================================================

el_resultado_esperado = "CR1010200009007408120"
el_resultado_obtenido = genere_el_numero_de_cuenta_iban("10200009007408120")

print("Resultado esperado: {}".format(el_resultado_esperado))
print("Resultado obtenido: {}".format(el_resultado_obtenido))










