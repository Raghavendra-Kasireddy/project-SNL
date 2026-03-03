import pygame
import random
import time;
pygame.init()

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("S & L ")
logo=pygame.image.load("D:\\Python\\S&L logo.png").convert_alpha()
pygame.display.set_icon(logo)
p1=pygame.image.load("D:\\Python\\p1.png").convert_alpha()                 #player 1 img
p2=pygame.image.load("D:\\Python\\p2.png").convert_alpha()
scaledp1 = pygame.transform.scale(p1, (60, 60))
scaledp2 = pygame.transform.scale(p2, (60, 60))
B=pygame.image.load("D:\\Python\\snlboard.png").convert_alpha() 
board = pygame.transform.scale(B, (500, 567)) 
bg=pygame.image.load("D:\\Python\\snlbackground.png").convert_alpha()                                      #board img  

coordinates = {1:(55,564),2:(105,564),3:(155,564),4:(202,564),5:(255,564),6:(305,564),7:(355,564),8:(405,564),9:(455,564),10:(505,564),
               11:(505,508),12:(455,508),13:(405,508),14:(355,508),15:(305,508),16:(255,508),17:(202,508),18:(155,508),19:(105,508),20:(55,508),
                21:(55,450),22:(105,450),23:(155,450),24:(202,450),25:(255,450),26:(305,450),27:(355,450),28:(405,450),29:(455,450),30:(505,450),
                31:(505,396),32:(455,396),33:(405,396),34:(355,396),35:(305,396),36:(255,396),37:(202,396),38:(155,396),39:(105,396),40:(55,396),
                41:(55,336),42:(105,336),43:(155,336),44:(202,336),45:(255,336),46:(305,336),47:(355,336),48:(405,336),49:(455,336),50:(505,336),
                51:(505,280),52:(455,280),53:(405,280),54:(355,280),55:(305,280),56:(255,280),57:(202,280),58:(155,280),59:(105,280),60:(55,280),
                61:(55,220),62:(105,220),63:(155,220),64:(202,220),65:(255,220),66:(305,220),67:(355,220),68:(405,220),69:(455,220),70:(505,220),
                71:(505,161),72:(455,161),73:(405,161),74:(355,161),75:(305,161),76:(255,161),77:(202,161),78:(155,161),79:(105,161),80:(55,161),
                81:(55,106),82:(105,106),83:(155,106),84:(202,106),85:(255,106),86:(305,106),87:(355,106),88:(405,106),89:(455,106),90:(505,106),
                91:(505,52),92:(455,52),93:(405,52),94:(355,52),95:(305,52),96:(255,52),97:(202,52),98:(155,52),99:(105,52),100:(55,52)
    }

dice_images = [None] 
for i in range(1, 7):                                                   #load dice imgs
    path = f"D:\\Python\\{i}.png"
    img = pygame.image.load(path).convert_alpha()
    scaled_img = pygame.transform.scale(img, (100, 100))
    dice_images.append(scaled_img)

Arial = pygame.font.SysFont("Arial", 30)
text_surface = Arial.render("Press 'R' to roll", True, (185, 80, 255))   #text permanent
position_1 = Arial.render("Player Position 1: ", True, (255, 93, 93)) 
position_2 = Arial.render("Player Position 2: ", True, (255, 93, 93)) 

dice_1 = 0
dice_2 = 0

#roll function
def roll():
    global text_surface,current_dice
    dice= random.choices([1,2,3,4,5,6],[11,22,14,23,18,12])[0]                           #probability of dice
    result_str = f"You rolled : {dice}"
    current_dice = dice
    text_surface = Arial.render(result_str, True, (185, 80, 255))        

#ladder function
def ladders(position):
    ladder={5:27, 9:51, 22:60, 28:54,44:79,53:69, 66:88, 71:92, 85:97}
    if position in ladder:
        return ladder[position]
    return position

#snake function
def snakes(position):
    snake={99:4, 91:49, 86:46, 80:43, 37:19, 13:7}
    if position in snake:
        return snake[position]
    return position
    
def delay_and_ignore_input(ms):
    start = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start < ms:
        pygame.event.get()  # Clear all events (ignore input)
        pygame.time.delay(10)

#game variables
current_player=1   
player_position_1=0
player_position_2=0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                roll()
                if current_player == 1:
                    dice_1 = current_dice
                    for i in range(current_dice):
                        player_position_1 += 1
                        screen.blit(bg,(0,0))
                        screen.blit(board,(50,50))
                        if player_position_1 > 0 and player_position_1 <= 100:
                            x1,y1 = coordinates[player_position_1]
                            screen.blit(scaledp1, (x1-15,y1))
                        if player_position_2 > 0 and player_position_2 <= 100:
                            x2, y2 = coordinates[player_position_2]
                            screen.blit(scaledp2, (x2-7, y2))

                        screen.blit(text_surface,(200,725)) 
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
                    position_1 = Arial.render(f"Player Position 1: {player_position_1}", True, (255, 93, 93))
                    
                    if player_position_1 >= 100:
                        if player_position_1 > 100:
                            player_position_1 -= current_dice
                            position_1 = Arial.render(f"Player Position 1: {player_position_1}", True, (255, 93, 93))
                        if player_position_1 == 100:
                            position_1 = Arial.render("Congratulations! You win!", True, (255, 93, 93))
                            player_position_1 = 0
                            player_position_2 = 0
                            delay_and_ignore_input(1000)
                    if current_dice == 6:
                        current_player = 1
                    else:
                        current_player = 2

                else:
                    dice_2 = current_dice                 
                    for i in range(current_dice):
                        player_position_2 += 1
                        screen.blit(bg,(0,0))
                        screen.blit(board,(50,50))
                        if player_position_1 > 0 and player_position_1 <= 100:
                            x1, y1 = coordinates[player_position_1]
                            screen.blit(scaledp1, (x1-15,y1))
                        if player_position_2 > 0 and player_position_2 <= 100:
                            x2, y2 = coordinates[player_position_2]
                            screen.blit(scaledp2, (x2-7, y2)) 

                        screen.blit(text_surface,(200,725)) 
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
                    position_2 = Arial.render(f"Player Position 2: {player_position_2}", True, (255, 93, 93))
                   
                    if player_position_2 >= 100:
                        if player_position_2 > 100:
                            player_position_2 -= current_dice
                            position_2 = Arial.render(f"Player Position 2: {player_position_2}", True, (255, 93, 93))
                        if player_position_2 == 100:
                            position_2 = Arial.render("Congratulations! You win!", True, (255, 93, 93))
                            player_position_1 = 0
                            player_position_2 = 0
                            delay_and_ignore_input(1000)
                    if current_dice == 6:
                        current_player = 2
                    else:
                        current_player = 1
    screen.blit(bg, (0, 0))                                       #background color
    screen.blit(board,(50,50))                                        #draw board

    if current_player == 1 and dice_1 > 0:
        pygame.draw.rect(screen, (240,236,89), (40, 665, 120, 120), border_bottom_right_radius=25, border_top_left_radius=25)
    if dice_1 > 0:
        screen.blit(dice_images[dice_1], (50, 675))
    if current_player == 2 and dice_2 > 0:
        pygame.draw.rect(screen, (240,236,89), (440, 665, 120, 120), border_bottom_right_radius=25, border_top_left_radius=25)
    if dice_2 > 0:
        screen.blit(dice_images[dice_2], (450, 675))

    # Draw player 1 at their current position
    if player_position_1 > 0 and player_position_1 <= 100:
        x1, y1 = coordinates[player_position_1]
        screen.blit(scaledp1, (x1-15,y1))

    # Draw player 2 at their current position
    if player_position_2 > 0 and player_position_2 <= 100:
        x2, y2 = coordinates[player_position_2]
        screen.blit(scaledp2, (x2-7, y2))                              # Adjust position to center the player image

    screen.blit(text_surface,(200,725))                                #refresh roll text
    screen.blit(position_1,(5,5))                                   #refresh position
    screen.blit(position_2,(350,5))

    pygame.display.flip()
    pygame.time.Clock().tick(60)   
pygame.quit()
