
from os import listdir
from random import randint, shuffle
from guizero import App, Text, Box, PushButton, TextBox

def check_answer (chosen, correct, current_score, app):
    global score
    #print (chosen,correct)
    if chosen == correct:
        print ("correct")
        score +=  1
    else:
        print ("incorrect") 
    app.destroy()
    
def get_emoji_set (grid_size):
    matched = []  
    for x in range (0,grid_size):
        matched.append([])       
        for y in range (0,grid_size):
            choice = randint (0,len(images))
            matched[x].append (images.pop (choice)) 
    return (matched) 

def shuffle_2d_list(grid_to_shuffle):
    shuffle (grid_to_shuffle)
    for ii, sublist in enumerate(grid_to_shuffle): 
        shuffle(grid_to_shuffle [ii])
    return (grid_to_shuffle)
        
def play_round():

    grid=[]

    for game_grid in range (0,num_grids):
        grid.append  (get_emoji_set (grid_size))
        grid[game_grid][0][0]=grid[0][0][0]
        grid [game_grid] = shuffle_2d_list (grid [game_grid])
        
    #at the end record the correct image then shuffle the first list again  
    correct_image = grid[0][0][0] 
    grid[0] = shuffle_2d_list(grid [0])    
    
    app = App(title="My app", height=500, width=1200, layout="grid")
    
    
    #top_bar = Box(app, grid=[0,0])
    
    buttons=[]
    grid_box=[]
    
    for grid_num in range (1, num_grids):
        grid_box.append ( Box(app, layout="grid", grid=[grid_num*2 ,0]))
        space = Text(app, text="     ", grid=[grid_num*2+1,0])
        
        for button_x in range(0,grid_size):
            for button_y in range (0,grid_size):
                buttons.append( PushButton(grid_box[grid_num], command=check_answer, args=[grid[grid_num][button_x][button_y],correct_image, score, app], grid=[button_x,button_y], image='./images/'+grid[grid_num][button_x][button_y] ))
    app.display()
    
    

#general variables
score = 0
images = listdir('./images')
grid_size=4
num_grids=3
num_rounds = 3

#main program 

#this runs the app a number of times

#app = App(title="My app", height=500, width=1200, layout="grid")

for i in range(0,num_rounds):
    play_round()
    print (score)

print ('Final score: ', score)





