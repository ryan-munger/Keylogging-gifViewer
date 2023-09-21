import os
import PySimpleGUI as sg
import requests
import random

from PIL import Image, ImageTk, ImageSequence
from URL import cat_url, dog_url, otter_url, capybara_url

sg.theme('DarkBlue1')    
sg.set_options(font=("Times New Roman", 16))   

# uses http request to download the selected gif
def getImage(img_url):
    path = 'display.gif'
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)

# obtains the gifs and displays them in new window
def cat():
    getImage(cat_url[random.randrange(10)])
    gifViewer('Cat Gif!', 'Yippee!')

def dog():
    getImage(dog_url[random.randrange(10)])
    gifViewer('Dog Gif!', 'Hooray!')

def otter():
    getImage(otter_url[random.randrange(10)])
    gifViewer('Otter Gif!', 'Wahoo!')

def capybara():
    getImage(capybara_url[random.randrange(10)])
    gifViewer('Capybara Gif!', 'Yay!')
 
# displays the downloaded gif in a new window
def gifViewer(title, display_text):
    
    gif_filename = r'display.gif'

    layout = [[sg.Text(display_text, background_color='#A37A3B', text_color='#FFF000',  justification='c', key='-T-', font=("Bodoni MT", 30))],
            [sg.Image(key='-IMAGE-')], [sg.Button('Close')]]

    gifWindow = sg.Window(title, layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)

    gifWindow['-T-'].expand(True, True, True)      # Make the Text element expand to take up all available space

    interframe_duration = Image.open(gif_filename).info['duration']     # get how long to delay between frames

    while True:
        for frame in ImageSequence.Iterator(Image.open(gif_filename)):
            event, values = gifWindow.read(timeout=interframe_duration)
            if event == sg.WIN_CLOSED or event == 'Close':
                break    
            gifWindow['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) )
        if event == sg.WIN_CLOSED or event == 'Close':
            break
    
    gifWindow.close()
    

# main window that opens 
def main():
    
    layout = [[sg.Text('What kind of gif do you want?')], 
              [sg.Text('Note: Each key press will result in a new gif, please close window before requesting another.', background_color='#A37A3B', text_color='#FFF000',  justification='l', key='-T-', font=("Bodoni MT", 10))], 
              [sg.Button('Cat Gif'), sg.Button('Dog Gif'), sg.Button('Otter Gif'), sg.Button('Capybara Gif'), sg.Exit()]]   
    windowMain = sg.Window('Gif Generator', layout, finalize=True)

    # Window Event Loop, handles which windows launch and button presses
    while True:                             
            event, values = windowMain.read() 
            if event == sg.WIN_CLOSED or event == 'Exit':
                break      
            elif event == 'Cat Gif':
                cat()
            elif event == 'Dog Gif':
                dog()
            elif event == 'Otter Gif':
                otter()
            elif event == 'Capybara Gif':
                capybara()
            
    windowMain.close()

main()
