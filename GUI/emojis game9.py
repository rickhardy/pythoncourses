
from os import listdir
from random import randint, shuffle
from guizero import App, Text, Box, PushButton, TextBox




def check_answer (chosen, correct):
    global score
    #print (chosen,correct)
    if chosen == correct:
        #print ("correct")
        score +=  1
    else:
        #print ("incorrect") 
        None
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

def counter():
    timer1.value = int(timer1.value) - 1
    
    if int(timer1.value) == 0:
        # reset the timer
        #print ('last round:', last_round)
        timer1.cancel(counter)
        app.warn("Out Of Time", "Next?")
        
        app.destroy()     
     

    

#general variables
score = 0
images = listdir('./images')
grid_size=4
num_grids=3
num_rounds = 3


#main program 

#this runs the app a number of times
for i in range(0,num_rounds):
    
    grid=[]

    for game_grid in range (0,num_grids):
        grid.append  (get_emoji_set (grid_size))
        grid[game_grid][0][0]=grid[0][0][0]
        grid [game_grid] = shuffle_2d_list (grid [game_grid])
        
    #at the end record the correct image then shuffle the first list again  
    correct_image = grid[0][0][0] 
    grid[0] = shuffle_2d_list(grid [0])    
    
    app = App(title="My app", height=500, width=1200, layout="grid")
    
    head_banner = Box (app, grid = [0,0], layout="grid")
    
    text= Text (head_banner, text='score',grid=[0,0])
    text2= Text (head_banner, text=score,grid=[1,0])
    timer1 = Text (head_banner, text="Get Ready",grid=[2,0])
    timer1.value = 20
    


    timer1.repeat(1000, counter)
    
    app.display()
    
    buttons=[]
    grid_box=[]
    
    for grid_num in range (0, num_grids):
        grid_box.append ( Box(app, layout="grid", grid=[grid_num*2 ,1]))
        space = Text(app, text="     ", grid=[grid_num*2+1,1])
            
        for button_x in range(0,grid_size):
            for button_y in range (0,grid_size):
                buttons.append( PushButton(grid_box[grid_num], command=check_answer, args=[grid[grid_num][button_x][button_y],correct_image], grid=[button_x,button_y], image='./images/'+grid[grid_num][button_x][button_y] ))
             
    app.display()
    
    if i == num_rounds -1 :
        
        last_round = True
        print ("last round" , i, last_round)

print ('Final score: ', score)






