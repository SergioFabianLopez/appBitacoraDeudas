import flet as ft
from flet import View
from views.addpay import add_pay
from views.login import login_screen
from views.main import main_screen
from views.counts import counts

def open_main_screen(e):
    e.page.go("/main")

def open_add_payment_screen(e):
    e.page.go("/add-payment")

def open_exit_screen(e):
    e.page.go("/exit")

def route_change(e):
    page = e.page  # Obtén el objeto 'page' desde el evento 'e'
    print("Route change:", page.route)
    page.views.clear()
    
    if page.route == "/":
        page.views.append(
            View(
                "/",
                [
                    login_screen(page)
                ],
            )
        )
    elif page.route == "/main":
        page.views.append(
            View(
                "/main",
                [
                    main_screen(page)
                ],
            )
        )
    elif page.route == "/add-payment":
        page.views.append(
            View(
                "/add-payment",
                [
                    add_pay(page)
                ],
            )
        )
    elif page.route == "/counts":
        page.views.append(
            View(
                "/exit",
                [
                    counts(page)
                ],
            )
        )
    elif page.route == "/exit":
        page.views.append(
            View(
                "/exit",
                [
                    page.go("/")
                ],
            )
        )
    page.update()
