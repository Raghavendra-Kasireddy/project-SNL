import pygame
import random
import time;
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()                                             #FPS control
pygame.display.set_caption("S & L ")
p1=pygame.image.load("D:\\Python\\p1.png").convert_alpha()                 
p2=pygame.image.load("D:\\Python\\p2.png").convert_alpha()
scaledp1 = pygame.transform.scale(p1, (60, 60))
scaledp2 = pygame.transform.scale(p2, (60, 60))
SAM=pygame.image.load("D:\\Python\\S&L logo.png").convert_alpha()                 #sam img
scaledSAM = pygame.transform.scale(SAM, (40,40))

board = pygame.image.load("D:\\Python\\board.png").convert_alpha()   
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
    snake={99:4, 91:49, 86:46, 89:43, 37:19, 13:7}
    if position in snake:
        return snake[position]
    return position
    


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
                    player_position_1 += current_dice
                    player_position_1 = ladders(player_position_1)               #ladder occurence
                    player_position_1 = snakes(player_position_1)                #snake occurence
                    position_1 = Arial.render(f"Player Position 1: {player_position_1}", True, (255, 93, 93))
                    if player_position_1 >= 100:
                        if player_position_1 > 100:
                            player_position_1 -= current_dice
                            position_1 = Arial.render(f"Player Position 1: {player_position_1}", True, (255, 93, 93))
                        if player_position_1 == 100:
                            position_1 = Arial.render("Congratulations! You win!", True, (255, 93, 93))
                            time.sleep(2)
                            player_position_1 = 0
                            player_position_2 = 0
                    if current_dice == 6:
                        current_player = 1
                    else:
                        current_player = 2
                else:
                    dice_2 = current_dice                 
                    player_position_2 += current_dice
                    player_position_2 = ladders(player_position_2)              #ladder occurence
                    player_position_2 = snakes(player_position_2)               #sanke occurence
                    position_2 = Arial.render(f"Player Position 2: {player_position_2}", True, (255, 93, 93))
                    if player_position_2 >= 100:
                        if player_position_2 > 100:
                            player_position_2 -= current_dice
                            position_2 = Arial.render(f"Player Position 2: {player_position_2}", True, (255, 93, 93))
                        if player_position_2 == 100:
                            position_2 = Arial.render("Congratulations! You win!", True, (255, 93, 93))
                            time
                            player_position_1 = 0
                            player_position_2 = 0
                    if current_dice == 6:
                        current_player = 2
                    else:
                        current_player = 1
                print(player_position_1, player_position_2)             #debugging
    screen.fill((194, 252, 255))                                        #background color

    if dice_1 > 0:
        screen.blit(dice_images[dice_1], (50, 675))                     #display dice image
    if dice_2 > 0:
        screen.blit(dice_images[dice_2], (575, 675))
    screen.blit(board, (150,75)) 
    screen.blit(scaledSAM, (155
    ,615))                                         #display sam img
    screen.blit(scaledp1, (150 + player_position_1 * 30, 75 + 300 - player_position_1 * 30))   #display player 1
    screen.blit(scaledp2, (150 + player_position_2 * 30, 75 + 300 - player_position_2 * 30))   #display player 2
    screen.blit(text_surface, (275,725))                                #refresh roll text
    screen.blit(position_1, (25, 25))                                   #refresh position
    screen.blit(position_2, (400, 25))
    screen.blit(Arial.render(f"current player :{current_player}", True,(255, 86, 160)), (250, 750)) #current player turn

    pygame.display.flip()
    clock.tick(30)   

pygame.quit()
