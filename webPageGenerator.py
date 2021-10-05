# Python Version: 3.7.8
#
# Author: Ryan Spears
#


from tkinter import *
import webbrowser


# This function creates a new html file, gets the input from the
# user, and then displays it in a new tab in their browser.
def generate():
    newFile = open('generatedFile.html', 'a')

    INPUT = bodyText.get('1.0', 'end-1c')

    txtBody = '<html>\n\t<body>\n\t\t<h1>\n\t\t\t{}\n\r\t\t</h1>\n\r\t</body>\n\r</html>'.format(INPUT)
    
    newFile.write(txtBody)
    newFile.close()

    webbrowser.open('generatedFile.html', new = 2, autoraise = True)

# All of this below is pretty self explanatory...
win = Tk()
win.title('Webpage Generator')
win.minsize(300, 300)

lbl2 = Label(win, text = 'Type your body text below.')
lbl2.grid(row = 1, padx = 75, pady = 25)

bodyText = Text(win, height = 2, width = 25)
bodyText.grid(row = 3, padx = 75, pady = 25)

lbl = Label(win, text = 'Click the button to generate \nyour webpage.')
lbl.grid(row = 5, padx = 75, pady = 25)

btn = Button(win, text = 'Generate', command = generate)
btn.grid(row = 7, padx = 75, pady = 25)

win.mainloop()
