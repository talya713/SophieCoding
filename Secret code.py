from tkinter import *



new = ''

a = input("Would you like to encode something or decode: ")



if a == "encode":
    print("hi")
    root_1 = Tk()
    root_1.title("Encoder")
    answer_text = Label(root_1, text="Type in the message you want to encode! ", font = ('Times',13))
    answer_text.pack()
    root_1.geometry("600x400+600+300")
    entry_1 = Entry(root_1,justify = 'center', cursor = "dot" )
    entry_1.pack()
    button = Button(root_1, text='Ask', command=lambda: coded()) #Lambda makes sure that the code soes not go to the code does not instantly go to the clicked function.
    button.pack()
    
def coded():
    
    
    new = ''
    for i in entry_1.get():
        if i == 'a':
            i = ' '
        elif i == 'e':
            i = '#'
        elif i == 'i':
            i = '~'
        elif i == "o":
            i = "%"
        elif i == "u":
            i = "("
        elif i == "y":
            i = "/"
        elif i == ' ':
            i = "*"
        elif i == "i":
            i = "="
        elif i == "r":
            i = "@"
        
        
        print("kebab")
        new = new+i
        
    
    '''
    first_letters = new[:3] 
    new = new[3:]+ first_letters 
    ''' 
    print (new)
    
    
if a == "decode":  
    print("bloop")
    root_2 = Tk()
    root_2.title("Encoder")
    answer_text = Label(root_2, text="Type in the message you want to encode! ", font = ('Times',13))
    answer_text.pack()
    root_2.geometry("600x400+600+300")
    entry_2 = Entry(root_2,justify = 'center', cursor = "dot" )
    entry_2.pack()
    button_2 = Button(root_2, text='Ask', command=lambda: decoded()) #Lambda makes sure that the code soes not go to the code does not instantly go to the clicked function.
    button_2.pack() 
    
    
def decoded():
    
    
    new_2 = ''
    for i in entry_2.get():
        if i == ' ':
            i = 'a'
        elif i == '#':
            i = 'e'
        elif i == '~':
            i = 'i'
        elif i == "%":
            i = "o"
        elif i == "(":
            i = "u"
        elif i == "/":
            i = "y"
        elif i == '*':
            i = " "
        elif i == "=":
            i = "i"
        elif i == "@":
            i = "r"
        
        
        new_2 = new_2+i
        print (new_2)
        print ("kebab")
    
    '''
    first_letters = new_2[:3] 
    new_ = new[3:]+ first_letters
    '''  

   

    
'''
new_2 = ''
    
for y in b:
    if y == '1':
        y = 'a'
    elif y == '2':
        y = 'b'
    elif y == '3':
        y = 'c'
    new_2 = new_2+y
'''
