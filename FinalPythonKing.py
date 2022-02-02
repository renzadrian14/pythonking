import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from random import randrange
from distutils import command
from tkinter.ttk import Button
from builtins import *
from _ast import If
from pygame.scrap import lost
from audioop import reverse
import sys
import os

x = 100
y = 45
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
win = pygame.display.set_mode((100,100))

currentPlayersIndex=0    
score=0
index=0
genNum_list=[] 

question_list=["Generics is a data types that is not supported in python ?",
               "Python was created by Guido van Rossum.",
               "Python supports both procedure-oriented and object-oriented programming",
               "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI)",
            "s3 = s1 + s2 is an applicable statement to concatenate two strings to a third",
            "ord() is a function use to convert a single character to its integer value",
            "not in is a operator in python that evaluates to true if it does not finds a variable in the specified sequence and false otherwise",
            "islower() is a function that checks in a string that all characters are in lowercase",
            "'hello'+1+2+3 is a valid statement?",
            "Say s='hello' the return value of type(s) will be str",
            "What is the output of print 0.1 + 0.2 == 0.3 ?",
            "k = 2 + 3l is not a complex number ?",
            "Float is the type of inf ?",
            "-5 evaluate to ~4",
            "~~~~~~5 evaluate to +5",
            "We cannot use a keyword as a variable name, function name or any other identifier",
            "To check whether string s1 contains s2, use s1.__contains__(s2)",
            "the output of L[1:] if L = [1,2,3] is 2,3",
            "cmp(dict1, dict2) is a use to function compares elements of both dictionaries dict1, dict2",
            "Class is not a core datatype",
            "the return type of function id is int",
            "Keywords are the reserved words in Python",
            "isdecimal() is the function that checks in a string that all characters are decimal",
            "PYTHONHOME environment variable for Python is an alternative module search path",
            "str(x) is a function use to convert an object to a string in python",
            "str(x) is a function use to convert an object to a string in python",
            "X**y is the correct operator for power(x^y)",
            "// is floor division",
            "Python is case sensitive when dealing with identifiers",
            "79 is the maximum possible length of an identifier",
            "Which of the following is invalid",
            "1st_string is an invalid variable",
            "underscore are used to indicate a private variables of a class",
            "eval is not a keyword",
            "All the keywords except True , False and None are in lowercase and they must be written as it is",
            "variable names in Python can be any length",
            "a b c = 1000 2000 3000 is an invalid statement",
            "The answer of this expression, 22 % 3 is 1",
            "the output of this expression, 3*1**3 is 3",
            "Parentheses have the highest precedence in the expression",
            "in cannot be a variable",
            "input('Enter a string') is a function you use to read a string",
            "Multiplication,Division,Addition and Subtraction have the same precedence",
            "Variable name in Python can consist of uppercase and lowercase letters, digits and the underscore character",
            "All variable names must begin with a letter of the alphabet or an underscore",
            "sum will add all the numbers in the list"
            #false
            "Python modules is a collection of functions and methods"

            "A Library is a collection of Python modules",
            
            "The Python Standard Library is a collection of function and methods",
            
            "The requests library is not the standard for making HTTP requests in Python",
            
            "The math module is a standard module in Python and is not always available",
            
            "In Python, 'Hello', is different as \"Hello\"",
            
            "Lists are formed by placing a semicolon-separated list of expressions in square brackets",
            
            "The argument to the return() call is a return value of a function call, which returns None",
            
            "An imaginary literal yields a unicode number with a real part of 0.0",
            
            "'lambda arguments: expression' yields a function method",
            
            "Division of an integer by another integer yields a double",
            
            "In a set the unique values are not retained",
            
            "OR is higher precedence than AND in python and is evaluated first",
            
            "NOT has second precedence, then AND, then OR",
            
            "Global variable can be define inside a function",
            
            "When prefixed with the letter 'r' or 'R' a string literal becomes a method",
            
            "\"\"x is not an escape sequence",
            
            "In Python strings, the backslash \"\"\ is a function",
            
            "The default beginning of a range is 1",
            
            "The range will include the beginning of the range and all numbers up to including the end of the range",
            
            "checkit will check if the value is not in the set",
            
            "The ** operator in the function multiply the parameter by 2.",
            
            "the floor method will return the smallest integer value less than or equal to the parameter as a float type",
            
            "A docstring is a package that occurs as the first statement in a module, function, class, or method definition",
            
            "match will only check if the pattern exists in the middle of the string",
            
            "The join() method takes all items in an iterable and joins them into two string",
            
            "Indentation is not important in python",
            
            "Parenthesis are the syntax for a dictionary declaration",
            
            "Curly braces are used to initialize a tuple",
            
            "The len function will not return the number of keys in a dictionary",
            
            "keys to a dictionary can be mixed between strings and integers and they represent the same keys",
            
            "Keys can only be immutable types, so a dictionary can be used as a key",
            
            "The tuples cannot have mixed length",
            
            "The proper way to actually remove all items from a dictionary is to call the 'clean' method of the dictionary object",
            
            "The del function is used to edit key value pairs from a dictionary",
            
            "-1 refers to the beginning of a list or the first character in a string",
            
            "the in keyword can be used to measure a value in a list, set, or dict",
            
            "When a list is passed to the append method of list, the entire list is added as an element of the list.  The lists are merged",
            
            "The + operator appends the elements in each list into a second list",
            
            "Tuples are mutable and don't have an append method",
            
            "You cannot assign arbitrary typed information to functions",
            
            "In order to create a library create a directory for the package name and then put an _init_.py file in the directory",
            
            "getattr() can be used to get the value of a member variable of a method",
              
            "setattr() is used to get the object attribute its value. ",
            
            "str is a built in function that converts an ascii code to a 1 letter string",
            
            "is instance will not return true if the first parameter is an instance of the class type of the second parameter"]

answerNques_list=[1,1,1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,1,1,1,1,
                  1,1,1,1,1,1,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,0,
                  0,0,0,0,0,0,0,0,0,]

players=[]
playersScore=[]

# playersF=open('players.txt','x')
# playersScoreF=open('playersScore.txt','x')



green=(50,205,50)
light_green=(56,93,56)

yellowgreen=(165,198,3)    
width = 500 #width of the screen
height= 500 #height of the screen
rows = 20
win = pygame.display.set_mode((width, height))
 
class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=((40,64,0))):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
 
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, yellowgreen, circleMiddle, radius)
            pygame.draw.circle(surface, yellowgreen, circleMiddle2, radius)
       

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
 
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
            keys = pygame.key.get_pressed()
 
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)
       
 
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
 
 
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
       
 
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)
 
 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
 
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, yellowgreen, (x,0),(x,w))
        pygame.draw.line(surface, yellowgreen, (0,y),(w,y))
       
 
def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill(yellowgreen)
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    pygame.display.update()
    
def checknum():
    
    global genNum,index
    genNum=randrange(len(question_list))
    
    if genNum not in genNum_list:
        index=genNum
        genNum_list.append(genNum)
        print(genNum_list)
    
    else:
        checknum()

    
def askquestion(subject,content):
    
    global genNum,genNum_list,question_list,answerNques_list,index
        
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    x=messagebox.askyesno(subject, content)
    
    return x       
           
def randomSnack(rows, item):
 
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            
            continue
            
        else:
            break
       
    return (x,y)
  
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
    
def text_objects(text,font):
    
    black=(0,0,0)
    textSurface=font.render(text,True,(40,64,0))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))
    
    smallText = pygame.font.SysFont("connection",20)

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)
    
def message_display(text,x,y,size):    
    largeText = pygame.font.SysFont("connection",size,)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x),(y))
    win.blit(TextSurf, TextRect)  
          
            
def highScoreFrame():
    global players,playersScore
    running=True
    
    #sorting the score by descending order
    temp = sorted(zip(playersScore, players), key=lambda x: x[0], reverse=True)
    playersScore, players = map(list, zip(*temp))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
        win.fill(yellowgreen)
        
        message_display("High Score", (width/2),((height/2)-(height*.40)),30)
        
        width_loc_player=110
        height_loc_player=120
        
        width_loc_playerScore=350
        height_loc_playerScore=120
        
        for a in range(len(players)):
            score_Font=pygame.font.SysFont("connection",20)
            score_Surf=score_Font.render(str(players[a]),1,(40,64,0))
            score_Pos=[(width_loc_player),(height_loc_player)]
            win.blit(score_Surf,score_Pos)
            
            height_loc_player+=25
            
            score_Font=pygame.font.SysFont("connection",20)
            score_Surf=score_Font.render(str(playersScore[a]),1,(40,64,0))
            score_Pos=[(width_loc_playerScore),(height_loc_playerScore)]
            win.blit(score_Surf,score_Pos)
            
            height_loc_playerScore+=25
            
             
        buttonBack=button("Back",120, ((height/2)+(height*.30)),250,25,  (171, 233, 0), light_green, intro)
        pygame.display.update()
        
            
def loginFrame():    
    running=True
    global score,currentUser
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(150, ((height/2)-(height*.15)), 140, 32)
    color_inactive = pygame.Color(40,64,0)
    color_active = pygame.Color('grey')
    color = color_inactive
    active = False
    username = ''
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(username)
#                         text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                            
        win.fill(yellowgreen)

        # Render the current value of username.
        txt_surface = font.render(username, True, (40,64,0))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)
        
        currentUser=username
        
        print(username)

        message_display("PYTHON KING",250,((height/2)-(height*.40)),30)
        
#         message_display("Log In",250,((height/2)-(height*.30)),30)
        
        message_display("Enter Your Username: ", 250,((height/2)-(height*.20)),20)
 
        buttonStartt=button("START",120, (height/2),250,25,   (171, 233, 0), light_green, startGame)
        buttonBackk=button("BACK",120, 290,250,25,  (171, 233, 0), light_green, intro)        
        pygame.display.flip()
        pygame.display.update()
                
def finisher():
    running=True
    global score
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
        win.fill(yellowgreen)
        
        
        message_display("Congratulations!", (width/2),((height/2)-(height*.40)),30)
        
        message_display("100", (width/2),((height/2)-(height*.30)),50)
        
             
        buttonBacktoMenu=button("Back to Menu",120, ((height/2)+(height*.30)),250,25, (171, 233, 0), light_green, intro)
        
        pygame.display.update()

           
def youLost():     
    redrawWindow(win)
    running=True
    global playersScore,currentPlayersIndex,score
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                 
        win.fill(yellowgreen)

        message_display("GAME OVER!", (width/2),((height/2)-(height*.40)),30)       
        message_display("Your Score is", (width/2),((height/2)-(height*.30)),50)
         
        if score >= playersScore[currentPlayersIndex]: 
            currentPlayerScore=playersScore[currentPlayersIndex]
            
            
             
            score_Font=pygame.font.SysFont("connection",70)
            score_Surf=score_Font.render(str(currentPlayerScore),1,(40,64,0))
            score_Pos=[(width/2),200]
            win.blit(score_Surf,score_Pos)
        else:    
             
            score_Font=pygame.font.SysFont("connection",70)
            score_Surf=score_Font.render(str(score),1,(40,64,0))
            score_Pos=[(width/2),200]
            win.blit(score_Surf,score_Pos)
         
        buttonPlayAgain=button("PLAY AGAIN",120, 380,250,25, (171, 233, 0), light_green, startGame)      
        buttonBacktoMenuu=button("BACK TO MENU",120, 420,250,25, (171, 233, 0), light_green, intro)
         
        pygame.display.update()
        
        
def startGame():
    global index,genNum_list,score,players,playersScore,currentPlayersIndex,genNum,currentUser
    global width, rows, s, snack

    if currentUser not in players:
#         playersF.write(currentUser)
#         playersScoreF.write(0)
        players.append(currentUser)
        playersScore.append(0)
        currentPlayersIndex=players.index(currentUser)
    else:
        currentPlayersIndex=players.index(currentUser)

    width = 500
    height=500
    rows = 20
    win = pygame.display.set_mode((height, width))
    s = snake((40,64,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(40,64,0))
    flag = True
 
    clock = pygame.time.Clock()
    redrawWindow(win)
    
    score=0
    genNum=0
    genNum_list.clear()
    s.reset((10,10))
    checknum()
    print(playersScore)
    while flag:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        
        pygame.time.delay(60)
        clock.tick(10)
        s.move()
        print(playersScore)
        if s.body[0].pos == snack.pos:
            if(len(s.body)-1) == len(question_list):
                finisher()
            else:
                response=askquestion("Question", question_list[index])
                if response == answerNques_list[index]:
                    s.addCube()
                else:
                    score=(len(s.body)-1)
                    if score >= playersScore[currentPlayersIndex]:
                        playersScore[currentPlayersIndex]=score
                        
                        playersF=open('players.txt','r+')
                        playersF.truncate(0)
                        playersF.seek(0)
                        
                        playersScoreF=open('playersScore.txt','r+')
                        playersScoreF.truncate(0)
                        playersScoreF.seek(0)
                        
                        with open('players.txt','w') as f:
                            for listitemP in players:
                                f.write('%s\n'% listitemP)
                                 
                        with open('playersScore.txt','w') as f:
                            for listitemPS in playersScore:
                                f.write('%s\n'% listitemPS)
                        
                        
                        youLost()
                    else:
                        youLost()                
                checknum()               
                snack = cube(randomSnack(rows, s), color=(40,64,0))          
        redrawWindow(win)
        win = pygame.display.set_mode((width, width)) 
               
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', (len(s.body)-1))
                score=(len(s.body)-1)
                if score >= playersScore[currentPlayersIndex]:
                                    
                    playersScore[currentPlayersIndex]=score
                    
                    with open('players.txt','w') as f:
                        for listitemP in players:
                                f.write('%s\n'% listitemP)
                                 
                    with open('playersScore.txt','w') as f:
                        for listitemPS in playersScore:
                                f.write('%s\n'% listitemPS)
                    youLost()
                else:
                    youLost()
        
    redrawWindow(win)
    pygame.display.update()
    
def intro():
    global players,playersScore
    currentUser=0
    score=0
    
    players.clear()
    playersScore.clear()
    
    with open('players.txt','r') as pf:
        for line in pf:
            currentplace = line[:-1]
            
            players.append(currentplace)
    with open('playersScore.txt','r') as psf:
        for line in psf:
            currentplace = line[:-1]
            
            playersScore.append(currentplace)
        for i in range(0, len(playersScore)): 
            playersScore[i] = int(playersScore[i])
    
    start =True
     
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
                
        win.fill(yellowgreen)
        
        message_display("PYTHON KING",(width/2),((height/2)-(height*.10)),50)        
        message_display("Knowledge Tester about Python",(width/2),(height/2),16)
        
        
        buttonStart=button("START", 120, 380, 250, 25, (171, 233, 0), light_green, loginFrame)
        buttonHighScores=button("HIGHSCORES",120,420,250,25,(171, 233, 0), light_green, highScoreFrame)
        
        pygame.display.update()
         
intro()   
