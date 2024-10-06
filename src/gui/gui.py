from nicegui import ui

def submit_form():

    name = name_input.value
    email = email_input.value
    age = age_input.value

    ui.notify(f'Name: {name}, Email: {email}, Age: {age}', position='center', color='green')


def create_form():
    with ui.card().style('width: 400px; margin: auto; padding: 20px;'):
        ui.label('Data Capture Form').style('font-size: 24px; text-align: center;')

        # Form fields
        name_input = ui.input(label='Name').style('margin-bottom: 10px;')
        email_input = ui.input(label='Email').style('margin-bottom: 10px;')
        age_input = ui.input(label='Age').style('margin-bottom: 20px;')

        # Submit button
        ui.button('Submit', on_click=submit_form).style('width: 100%;')