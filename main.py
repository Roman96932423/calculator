import flet as ft
from time import sleep


def main(page):
    page.title = 'Calculator'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_btn(u_text, u_click=None):
        return ft.OutlinedButton(
            u_text,
            on_click=u_click
        )

    def get_number_1(event):
        result.value += '1'
        page.update()

    def get_number_2(event):
        result.value += '2'
        page.update()

    def get_number_3(event):
        result.value += '3'
        page.update()

    def get_number_4(event):
        result.value += '4'
        page.update()

    def get_number_5(event):
        result.value += '5'
        page.update()

    def get_number_6(event):
        result.value += '6'
        page.update()

    def get_number_7(event):
        result.value += '7'
        page.update()

    def get_number_8(event):
        result.value += '8'
        page.update()

    def get_number_9(event):
        result.value += '9'
        page.update()

    def get_number_0(event):
        result.value += '0'
        page.update()

    def get_division(event):
        result.value += '/'
        page.update()

    def get_multiplication(event):
        result.value += '*'
        page.update()

    def get_subtraction(event):
        result.value += '-'
        page.update()

    def get_addition(event):
        result.value += '+'
        page.update()

    def get_dot(event):
        result.value += '.'
        page.update()

    def delete_last_element(event):
        result.value = result.value[:len(result.value)-1]
        page.update()

    def delete_all(event):
        result.value = ' '
        page.update()

    def get_result(event):
        try:
            result.value = str(eval(result.value))
        except SyntaxError:
            result.value = "Unknown operation"
            page.update()
            sleep(1.5)
            result.value = ''
        except ZeroDivisionError:
            result.value = "Can't division by zero"
            page.update()
            sleep(1.5)
            result.value = ''
        page.update()

    result = ft.Text(f'{''}')

    button_1 = create_btn('1', get_number_1)
    button_2 = create_btn('2', get_number_2)
    button_3 = create_btn('3', get_number_3)
    button_4 = create_btn('4', get_number_4)
    button_5 = create_btn('5', get_number_5)
    button_6 = create_btn('6', get_number_6)
    button_7 = create_btn('7', get_number_7)
    button_8 = create_btn('8', get_number_8)
    button_9 = create_btn('9', get_number_9)
    button_0 = create_btn('0', get_number_0)

    page.add(
        ft.Row(
            [
                result
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                create_btn('d', delete_all),
                create_btn('b', delete_last_element),
                create_btn('/', get_division)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                button_1,
                button_2,
                button_3,
                create_btn('x', get_multiplication)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                button_4,
                button_5,
                button_6,
                create_btn('-', get_subtraction)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                button_7,
                button_8,
                button_9,
                create_btn('+', get_addition)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                button_0,
                create_btn('.', get_dot),
                create_btn('=', get_result)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
