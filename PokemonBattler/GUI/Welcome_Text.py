import PySimpleGUI as gui

layout = [
    [gui.Text("Are you ready to battle some Pokemon?")],
    [gui.Button("Yes!")]
]

window = gui.Window("Pokemon Battler", layout)

while True:
    event, values = window.read()
    if event == "Yes!" or event == gui.WIN_CLOSED:
        break
    
window.close()
