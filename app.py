# Created by: Allen
# For personal use because wordle became too easy

from random import randint
import PySimpleGUI as sg

def get_random_word() -> str:
    f = open('valid-wordle-words.txt')
    random_idx = randint(0, sum(1 for _ in f))
    f.seek(0)
    for _ in range(random_idx - 1):
        f.readline()
    word = f.readline()
    print(f"random_idx: {random_idx}, word: {word}")
    f.close()
    return word

def main():
    
    sg.theme('DarkAmber')

    layout = [[sg.Text('Your starting word: '), sg.Text(size=(15,1), key='-OUTPUT-')],
            [sg.Button('Generate random word'), sg.Button('Exit')]]

    window = sg.Window('random_wordle_start', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Generate random word':
            window['-OUTPUT-'].update(get_random_word())
            
    window.close()
        
if __name__ == "__main__":
    main()