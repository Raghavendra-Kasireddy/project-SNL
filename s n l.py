import pygame,random,sys,pygame.mixer_music
pygame.init()
pygame.mixer_music.load("D:\\Python\\snlbgm.mp3")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0)
laddersound = pygame.mixer.Sound("D:\\Python\\laddereffect.mpeg")
snakesound = pygame.mixer.Sound("D:\\Python\\snakeeffect.MP3.mpeg")
rollsound = pygame.mixer.Sound("D:\\Python\\rolleffect.MP3.mpeg")



#loads
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("S & L ")
logo=pygame.image.load("D:\\Python\\S&L logo.png").convert_alpha()
pygame.display.set_icon(logo)
scaledp1 = pygame.transform.scale(pygame.image.load("D:\\Python\\p1.png").convert_alpha(), (60, 60))
scaledp2 = pygame.transform.scale(pygame.image.load("D:\\Python\\p2.png").convert_alpha(), (60, 60))
congrats=pygame.transform.scale(pygame.image.load("D:\\Python\\congrats.png").convert_alpha(),(400,200))
board = pygame.transform.scale(pygame.image.load("D:\\Python\\snlboard.png").convert_alpha(), (500, 567)) 
woodbg = pygame.transform.scale(pygame.image.load("D:\\Python\\woodbg.png").convert_alpha(), (600, 800))
bg=pygame.image.load("D:\\Python\\snlbackground.png").convert_alpha()  
wood_img=pygame.transform.scale(pygame.image.load("D:\\Python\\button.png").convert_alpha(),(200,50))
restart_img=pygame.transform.scale(pygame.image.load("D:\\Python\\restart_img.png").convert_alpha(),(100,100))
options_menu=pygame.transform.scale(pygame.image.load("D:\\Python\\options_menu.png").convert_alpha(),(400,350))
SNL_text =pygame.transform.scale(pygame.image.load("D:\\Python\\SNLtext.png").convert_alpha(),(600,400)) 
mute_img = pygame.transform.scale(pygame.image.load("D:\\Python\\0m.png").convert_alpha(), (100,100))  
unmute_img = pygame.transform.scale(pygame.image.load("D:\\Python\\1m.png").convert_alpha(),(100,100))
leave_img = pygame.transform.scale(pygame.image.load("D:\\Python\\leave.png").convert_alpha(),(75,75))  

coordinates = {0:(275,734),1:(55,564),2:(105,564),3:(155,564),4:(202,564),5:(255,564),6:(305,564),7:(355,564),8:(405,564),9:(455,564),10:(505,564),
               11:(505,508),12:(455,508),13:(405,508),14:(355,508),15:(305,508),16:(255,508),17:(202,508),18:(155,508),19:(105,508),20:(55,508),
                21:(55,450),22:(105,450),23:(155,450),24:(202,450),25:(255,450),26:(305,450),27:(355,450),28:(405,450),29:(455,450),30:(505,450),
                31:(505,396),32:(455,396),33:(405,396),34:(355,396),35:(305,396),36:(255,396),37:(202,396),38:(155,396),39:(105,396),40:(55,396),
                41:(55,336),42:(105,336),43:(155,336),44:(202,336),45:(255,336),46:(305,336),47:(355,336),48:(405,336),49:(455,336),50:(505,336),
                51:(505,280),52:(455,280),53:(405,280),54:(355,280),55:(305,280),56:(255,280),57:(202,280),58:(155,280),59:(105,280),60:(55,280),
                61:(55,220),62:(105,220),63:(155,220),64:(202,220),65:(255,220),66:(305,220),67:(355,220),68:(405,220),69:(455,220),70:(505,220),
                71:(505,161),72:(455,161),73:(405,161),74:(355,161),75:(305,161),76:(255,161),77:(202,161),78:(155,161),79:(105,161),80:(55,161),
                81:(55,106),82:(105,106),83:(155,106),84:(202,106),85:(255,106),86:(305,106),87:(355,106),88:(405,106),89:(455,106),90:(505,106),
                91:(505,52),92:(455,52),93:(405,52),94:(355,52),95:(305,52),96:(255,52),97:(202,52),98:(155,52),99:(105,52),100:(55,52)}

dice_images = [None] 
for i in range(1, 7):                                                   #load dice imgs
    img = pygame.image.load(f"D:\\Python\\{i}.png").convert_alpha()
    scaled_img = pygame.transform.scale(img, (100,100))
    dice_images.append(scaled_img)

#game variables
current_player=1   
player_position_1=90
player_position_2=90
dice_1 = 0
dice_2 = 0
position_1 = pygame.font.SysFont("Arial", 30).render(f"Player Position 1: {player_position_1}", True, (255, 255, 255))
position_2 = pygame.font.SysFont("Arial", 30).render(f"Player Position 2: {player_position_2}", True, (255, 255, 255))

#roll function
def roll():
    rollsound.play() 
    global current_dice
    dice= random.choices([1,2,3,4,5,6],[11,22,14,23,18,12])[0]                           #probability of dice
    
    current_dice = dice
    
           
#ladder function
def ladders(position):
    ladder={5:27, 9:51, 22:60, 28:54,44:79,53:69, 66:88, 71:92, 85:97}
    if position in ladder:
        laddersound.play()
        return ladder[position]
    return position

#snake function
def snakes(position):
    
    snake={99:4, 91:49, 86:46, 80:43, 37:19, 13:7}
    if position in snake:
        snakesound.play()
        return snake[position]
    return position
    
def delay_and_ignore_input(ms):
    start = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start < ms:
        pygame.event.get()  # Clear all events (ignore input)
        pygame.time.delay(10)

# Button properties
roll_button = pygame.Rect(240,670,120,50)
roll_text = pygame.font.SysFont("Arial", 30).render("Roll (R)", True, (255, 255, 255))
quit_roll_button = pygame.Rect(0,50,50,50)
quit_button=pygame.Rect(230,243,80,80)
mute_button = pygame.Rect(150,250,60,60)
rst_quit=pygame.Rect(380,470,80,80)
play_again=pygame.Rect(150,460,80,80)


def main_menu():
    menu_running = True
    play_rect = pygame.Rect(200, 400, 200, 50)
    options_rect = pygame.Rect(200, 500, 200, 50)
    screen.blit(pygame.transform.scale(woodbg,(600,800)),(0,0))
    screen.blit(SNL_text,(0,0))
    screen.blit(wood_img,(200,400))
    screen.blit(wood_img,(200,500))
    play_text = pygame.font.SysFont("Arial", 30).render("Play (P)", True, (255, 255, 255))
    options_text = pygame.font.SysFont("Arial", 30).render("Options (O)", True, (255, 255, 255))
    screen.blit(play_text, (play_rect.x+60, play_rect.y+5))
    screen.blit(options_text, (options_rect.x+40, options_rect.y+5))
    pygame.display.flip()
    while menu_running:    
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_p)):
                play_game()
            if (event.type == pygame.MOUSEBUTTONDOWN and options_rect.collidepoint(event.pos) or (event.type == pygame.KEYDOWN and event.key == pygame.K_o)):
                options()
            if event.type == pygame.QUIT:
                sys.exit()
              
def play_game():
    running = True
    while running:
        global current_player, player_position_1, player_position_2, dice_1, dice_2, position_1, position_2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_q)or(event.type == pygame.MOUSEBUTTONDOWN and quit_roll_button.collidepoint(event.pos)):
                restart()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r)or(event.type == pygame.MOUSEBUTTONDOWN and roll_button.collidepoint(event.pos)):
                roll()
                if current_player == 1:
                    dice_1 = current_dice
                    for i in range(current_dice):
                        player_position_1 += 1
                        screen.blit(woodbg,(0,0))
                        screen.blit(board,(50,50))
                        if player_position_1 >= 0 and player_position_1 <= 100:
                            x1,y1 = coordinates[player_position_1]
                            screen.blit(scaledp1, (x1-15,y1))
                        if player_position_2 >= 0 and player_position_2 <= 100:
                            x2, y2 = coordinates[player_position_2]
                            screen.blit(scaledp2, (x2-7, y2))

                        
                        screen.blit(position_1,(5,5)) 
                        screen.blit(position_2,(350,5))
                            
                        if dice_1 > 0:
                            pygame.draw.rect(screen, (240,236,89), (40, 665, 120, 120),border_bottom_right_radius=25,border_top_left_radius=25)
                            screen.blit(dice_images[dice_1], (50, 675))
                        if dice_2 > 0:
                            screen.blit(dice_images[dice_2], (450, 675))
                            
                        pygame.display.flip()
                        delay_and_ignore_input(200)
                    player_position_1 = ladders(player_position_1)               #ladder occurence
                    player_position_1 = snakes(player_position_1)                #snake occurence
                    position_1 = pygame.font.SysFont("Arial", 30).render(f"Player Position 1: {player_position_1}", True, (255,255,255))
                        
                    if player_position_1 >= 100:
                        if player_position_1 > 100:
                            player_position_1 -= current_dice
                            position_1 = pygame.font.SysFont("Arial", 30).render(f"Player Position 1: {player_position_1}", True, (255,255,255))
                        if player_position_1 == 100:
                            win_screen=True
                            
                            screen.blit(options_menu,(100,200))
                            screen.blit(congrats,(100,200))
                            screen.blit(leave_img,(380,470))
                            screen.blit(restart_img,(150,460))
                            screen.blit(pygame.font.SysFont("Arial",50).render("Player 1 won ", True, (255,255,255)),(190,400))
                            while win_screen :
                                for event in pygame.event.get():
                                    if event.type==pygame.QUIT:
                                        pygame.quit()
                                    if (event.type == pygame.MOUSEBUTTONDOWN and rst_quit.collidepoint(event.pos)):
                                        player_position_1=0
                                        player_position_2=0
                                        main_menu()
                                    if (event.type == pygame.MOUSEBUTTONDOWN and play_again.collidepoint(event.pos)):
                                        player_position_1 = 0
                                        player_position_2=0
                                        play_game()
                                pygame.display.flip()
                        delay_and_ignore_input(500)
                    if current_dice == 6:
                        current_player = 1
                    else:
                        current_player = 2

                else:
                    dice_2 = current_dice                 
                    for i in range(current_dice):
                        player_position_2 += 1
                        screen.blit(woodbg,(0,0))
                        screen.blit(board,(50,50))
                        if player_position_1 >= 0 and player_position_1 <= 100:
                            x1, y1 = coordinates[player_position_1]
                            screen.blit(scaledp1, (x1-15,y1))
                        if player_position_2 >= 0 and player_position_2 <= 100:
                            x2, y2 = coordinates[player_position_2]
                        screen.blit(scaledp2, (x2-7, y2)) 
                        
                        screen.blit(position_1,(5,5)) 
                        screen.blit(position_2,(350,5)) 
                            
                        if dice_1 > 0:
                                
                            screen.blit(dice_images[dice_1], (50, 675))
                                
                        if dice_2 > 0:
                            pygame.draw.rect(screen, (240,236,89), (440, 665, 120, 120),border_bottom_right_radius=25,border_top_left_radius=25)
                            screen.blit(dice_images[dice_2], (450, 675))

                        pygame.display.flip()
                        delay_and_ignore_input(200)

                    player_position_2 = ladders(player_position_2)              #ladder occurence
                    player_position_2 = snakes(player_position_2)               #sanke occurence
                    position_2 = pygame.font.SysFont("Arial", 30).render(f"Player Position 2: {player_position_2}", True, (255,255,255))
                    
                    if player_position_2 >= 100:
                        if player_position_2 > 100:
                                player_position_2 -= current_dice
                                position_2 = pygame.font.SysFont("Arial", 30).render(f"Player Position 2: {player_position_2}", True, (255,255,255))
                        if player_position_2 == 100:
                                
                                win_screen=True
                                screen.blit(options_menu,(100,200))
                                screen.blit(congrats,(100,200))
                                screen.blit(leave_img,(380,470))
                                screen.blit(restart_img,(150,460))
                                screen.blit(pygame.font.SysFont("Arial",50).render("Player 2 won ", True, (255,255,255)),(190,400))
                                while win_screen :
                                    for event in pygame.event.get():
                                        if event.type==pygame.QUIT:
                                            sys.exit()
                                        if (event.type == pygame.MOUSEBUTTONDOWN and rst_quit.collidepoint(event.pos)):
                                            player_position_1=0
                                            player_position_2=0
                                            main_menu()
                                        if (event.type == pygame.MOUSEBUTTONDOWN and play_again.collidepoint(event.pos)):
                                            player_position_1 = 0
                                            player_position_2 = 0
                                            play_game()
                                    pygame.display.flip()
                        delay_and_ignore_input(500)
                    if current_dice == 6:
                        current_player = 2
                    else:
                        current_player = 1
        screen.blit(woodbg, (0, 0))                                            #background color
        screen.blit(board,(50,50))
        screen.blit(position_1,(5,5))
        screen.blit(position_2,(350,5))                                         #draw board

        if current_player == 1 and dice_1 > 0:
            pygame.draw.rect(screen, (240,236,89), (40, 665, 120, 120), border_bottom_right_radius=25, border_top_left_radius=25)
        if dice_1 > 0:
            screen.blit(dice_images[dice_1], (50, 675))
        if current_player == 2 and dice_2 > 0:
            pygame.draw.rect(screen, (240,236,89), (440, 665, 120, 120), border_bottom_right_radius=25, border_top_left_radius=25)
        if dice_2 > 0:
            screen.blit(dice_images[dice_2], (450, 675))

        # Draw player 1 at their current position
        if player_position_1 >= 0 and player_position_1 <= 100:
            x1, y1 = coordinates[player_position_1]
            screen.blit(scaledp1, (x1-15,y1))

        # Draw player 2 at their current position
        if player_position_2 >= 0 and player_position_2 <= 100:
            x2, y2 = coordinates[player_position_2]
            screen.blit(scaledp2, (x2-7, y2))                              # Adjust position to center the player image

        screen.blit(leave_img,(-10,50))                                     #quit button
                       
        screen.blit(position_1,(5,5))                                      #refresh position
        screen.blit(position_2,(350,5))
        screen.blit(pygame.transform.scale(wood_img,(120,50)),(240,670))
        screen.blit(roll_text, (roll_button.x+20 , roll_button.y+3))

        pygame.display.flip()
        pygame.time.Clock().tick(60)   
    pygame.quit()

def options():  
    while True:
        quit_rect = pygame.Rect(160, 400, 200, 50)
        screen.blit(options_menu,(100,200))
        screen.blit(leave_img,(250,243))
        screen.blit(wood_img,(200,400))
        quit_text = pygame.font.SysFont("Arial", 30).render("Quit game (Q)", True, (255, 255, 255))
        options_text = pygame.font.SysFont("Arial", 50).render("Options", True, (255, 93, 93))
        screen.blit(options_text,(230,100))
        screen.blit(quit_text, (quit_rect.x+60, quit_rect.y+5))
        if pygame.mixer_music.get_volume() > 0:
            screen.blit(unmute_img, (135,230))
        else:
            screen.blit(mute_img, (139,230))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_q)or(event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint(event.pos)):
                main_menu()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_m)or(event.type == pygame.MOUSEBUTTONDOWN and mute_button.collidepoint(event.pos)):
                if pygame.mixer_music.get_volume() > 0:
                    pygame.mixer_music.set_volume(0)
                else:
                    pygame.mixer_music.set_volume(0.3)
            if (event.type == pygame.MOUSEBUTTONDOWN and quit_rect.collidepoint(event.pos)) or (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit() 

def restart():
    while True:
        global player_position_1, player_position_2,current_player,dice_1,dice_2,position_1,position_2
        text=pygame.font.SysFont("Arial",50).render("Do you want to exit ?", True, (0,0,0))
        restart_rect = pygame.Rect(250,400,100,100)
        yes_rect = pygame.Rect(150, 350, 100, 50)
        no_rect = pygame.Rect(350, 350, 100, 50)    
        yes_text = pygame.font.SysFont("Arial", 30).render("Yes (Y)", True, (255, 255, 255))
        no_text = pygame.font.SysFont("Arial", 30).render("No (N)", True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_y)or(event.type == pygame.MOUSEBUTTONDOWN and yes_rect.collidepoint(event.pos)):
                main_menu()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_n)or(event.type == pygame.MOUSEBUTTONDOWN and no_rect.collidepoint(event.pos)):
                play_game()
            if (event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos)):
                player_position_1=0
                player_position_2=0
                dice_1=0
                dice_2=0
                current_player=1
                screen.blit(position_1,(5,5))
                screen.blit(position_2,(300,5))
                return
        screen.blit(options_menu,(100,200))
        screen.blit(pygame.transform.scale(wood_img,(100,50)),(160,350))
        screen.blit(pygame.transform.scale(wood_img,(100,50)),(360,350))
        screen.blit(restart_img,(250,403))
        screen.blit(yes_text, (yes_rect.x+20, yes_rect.y+5))
        screen.blit(no_text, (no_rect.x+20, no_rect.y+5))
        screen.blit(text,(120,250))
        pygame.display.flip()

main_menu()
pygame.quit()
sys.exit()

