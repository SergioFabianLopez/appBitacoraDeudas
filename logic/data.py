
from database.connection import execute_query


def get_login(param):
    data = execute_query('get_login', param)
    return data


def list_pays(param):
    data = execute_query('getAllPayments', param)
    return data


def add_pays(ppayments_date, pamount, imagen, paccounts_id):
    params = [ppayments_date, pamount, imagen, paccounts_id]
    result = execute_query("add_payment", params)

    if result:
        print("Pago agregado con éxito:", result)
    else:
        print("Error al agregar el pago.")
    return result


def list_accounts_user(params):
    result = execute_query("get_accounts_user", params)
    return result


def list_accounts_id(params):
    result = execute_query("get_accounts_id", params)
    return result
