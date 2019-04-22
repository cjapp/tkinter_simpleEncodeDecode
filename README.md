
# Simple Ecryptor using Python and Tkinter #

This project is a simple program that lets the user enter 
text or load a file to ecode using the provided methods, 
or some they can add if they are interested. They can also
save the results to a file they specify so they can decode
it later.

The program uses python3, so that needs to be installed on the
user's computer before using the program. There are no outside
dependencies required from what I understand, tkinter and os are
included with python3.

It should also be noted that I developed this application using a
linux machine, so it is untested with other os's.

##Using the program##

Launch the program as you would normally for a python program:

**Linux Command Line:**

`<  python3 main.py >`

You will notice 2 textboxes on the right side of the newly opened window,
the one on the top is the input box, the one below is the result box that 
translates the input text depending on the options selected on the left 
side of the window. As input is entered, the result box will update 
accordingly and display the result.

The left side of the window has two radiobuttons labeled as encode and 
decode. Depending on what the input is (encoded text or readable), simply 
clicking the mode the user wants to use will set the application to that mode. 
The lower listbox lists the current method options to choose from; selecting 
one will allow the program to use that method when decoding or encoding the 
input text provided.

The menu at the top left of the window holds the open save and exit options.
Selecting open will allow the user to select a file to use as input text. 
Selecting save will allow the user to select a file to save the results to. 
Exit simply has the user close the program.

Try it out, see what you can encode and decode, try creating your own 
encode and decode methods aside from the default methods I have made.
