import pygame
import random, sys
pygame.init()

############################################################################
# This is a simple Pokemon Battle Simulator v1.5x 
#
# Update 1.xx : - Item menu accessible from MAIN_MENU
#               - Item menu/ ATK MENU/ QUIT accessible from Original Menu 
#               - Slider Roaming map with box collisions 
#               - Add audio to Battle and roaming scene
#               - Random choice for enemy /x
#               - Fix level up system for gameplay
#               - Fix HP bar update 
#               - .blit sprite name in battle
############################################################################

game_font = pygame.font.SysFont('Pokemon Classic Regular', 20)
game_boldFont = pygame.font.SysFont('Pokemon Classic Regular', 18, bold = True)
ATK_FONT = pygame.font.SysFont('Pokemon Classic Regular', 15)
WIDTH = 400
HEIGHT = 400
SCREEN = pygame.display.set_mode(( WIDTH, HEIGHT ))

######   R   G    B
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (105, 105, 105)
BLACK = (0, 0, 0)

############### SPRITES IMPORT
backg_image1 = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\background1.png')
backg_image2 = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\background2.png')

terminal_post = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\terminal_post.png')


play_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\pikachu_A120x120.png')

## POKEMON SPRITE OBJECT
## ROUTE 02
onix1_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\onix1_A120x120.png')
onix2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\onix2_A120x120.png')
charizard_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon maps and sprites\charizard_sprite_A120x120.png')

enemy_dict = { 'ONIX' : onix1_sprite, 'ONIX' : onix2_sprite, 'CHARIZARD' : charizard_sprite }
rand_enemy_choice = random.choice(list(enemy_dict.items()))
print(rand_enemy_choice[0])

## VERIDIAN FOREST
articuno1_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\veridian_pok\articuno_1_120x120.png')
articuno2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\veridian_pok\articuno_2_120x120.png')
mewto1_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\veridian_pok\mewto_1_120x120.png')
mewto2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\veridian_pok\mewto_1_120x120.png')

enemy_dict_2 = { 'ARTICUNO' : articuno1_sprite, 'ARTICUNO' : articuno2_sprite, 'MEWTO' : mewto1_sprite, 'MEWTO' : mewto2_sprite }
rand_enemy_choice_2 = random.choice(list(enemy_dict_2.items()))
print(rand_enemy_choice_2[0])

## PLAYER ROAMING
backg_image3 = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\route02_600x600.png')
backg_image4 = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\control_room_400x400_3.png')
backg_image5 = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\viridianforest_600x600.png')
map_pos = [ -180, 0 ]
map2_pos = [ 0, 0 ]
map3_pos = [ 0, -480 ]
map_vel = 1

playL_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteL_A25x25.png')
playR_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteR_A25x25.png')
playUP_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteUP_A25x25.png')
playDOWN_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteDOWN_A25x25.png')

playL2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteL_A25x25_2.png')
playR2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteR_A25x25_2.png')
playUP2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteUP_A25x25_2.png')
playDOWN2_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteDOWN_A25x25_2.png')

playL3_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteL_A25x25_3.png')
playR3_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteR_A25x25_3.png')
playUP3_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteUP_A25x25_3.png')
playDOWN3_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteDOWN_A25x25_3.png')

playL4_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteL_A25x25_4.png')
playR4_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteR_A25x25_4.png')
playUP4_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteUP_A25x25_4.png')
playDOWN4_sprite = pygame.image.load(r'C:\Users\Of Corrupted Vision\Documents\Source Python\pokemon game\version 1.5x (w color)\roam player\roam_spriteDOWN_A25x25_4.png')

L_LIST = [playL_sprite, playL2_sprite, playL3_sprite, playL4_sprite]
R_LIST = [playR_sprite, playR2_sprite, playR3_sprite, playR4_sprite]

UP_LIST = [playUP_sprite, playUP2_sprite, playUP3_sprite, playUP4_sprite]
DOWN_LIST = [playDOWN_sprite, playDOWN2_sprite, playDOWN3_sprite, playDOWN4_sprite]

img_index = 0
img_timer = 0










#------ROAMING------#
roam_pos = [(WIDTH/2)+100,(HEIGHT/2)-50]
roam_vel = 1
rand_prob = random.random()
rand_prob2 = random.random()

AIM_L = False
AIM_R = False
AIM_UP = False
AIM_DOWN = True

frame_speed = 1

RESPAWN_veridian = False
RESPAWN_route02 = False



#----------TRANSITION ANIMATION-------#
block_vel = 100

## first square
FIRST_SQUARE = True  #### True to start the square animation bool 
block_y1 = pygame.Rect(0,0,50,50)
block_y2 = pygame.Rect(WIDTH-50,HEIGHT-50,50,50)

block_x1 = pygame.Rect(0,HEIGHT-50,50,50)
block_x2 = pygame.Rect(WIDTH-50,0,50,50)

## second square
SECOND_SQUARE = False
block_y3 = pygame.Rect(50,50,50,50)
block_y4 = pygame.Rect(WIDTH-100,HEIGHT-50,50,50)

block_x3 = pygame.Rect(50,HEIGHT-100,50,50)
block_x4 = pygame.Rect(WIDTH-50,50,50,50)

## third square
THIRD_SQUARE = False
block_y5 = pygame.Rect(100,100,50,50)
block_y6 = pygame.Rect(WIDTH-150,HEIGHT-100,50,50)

block_x5 = pygame.Rect(100,HEIGHT-150,50,50)
block_x6 = pygame.Rect(WIDTH-100,100,50,50)

FINAL_SQUARE = False
block_x7 = pygame.Rect(100,HEIGHT-200,50,50)
block_x8 = pygame.Rect(WIDTH-150,150,50,50)



#-----PLAYER-----#
player_hp = 117
player_pos = [0,150]
play_pok = 'PIKACHU'
play_lvl = 2

max_tackle = 2
max_shock = 2
max_electburst = 4
max_hp = 117

inv = {'TAILWHIP':2, 'GROWL':2, 'THUNDERSHOCK':0}
exp_point = {"exp" : 1}

play_attk = False
#move_vel = 8

#-----ENEMY------#
enemy_hp = 117
enemy_pos = [400,50]
enemy_lvl = 10

onixAtk_list = ["TACKLE", "ROCKTHROW"]
charizardAtk_list = ["DRANGONCLAW", "FIRESPIN"]
articunoAtk_list = ['ICEBEAM','BLIZZARD']
mewtoAtk_list =['AMNESIA','LASERFOCUS']


#randAtk_enemy = random.choice(onixAtk_list)
enemy_attk = False

move_vel = 8
move_vel2 = 8

#-----STR RENDER-----#
'''
##INTRO
text_01_str = 'Wild '+ str(enemy_pok_name)
text_01 = game_font.render(text_01_str, False, (0,0,0))
text_01b = game_font.render("appeared !", False, (0,0,0))
'''

text_02 = game_font.render('Choose your',False, (0,0,0))
text_02b = game_font.render('ATTACK !',False, (0,0,0))

##ATTACK MENU
text_03 = ATK_FONT.render('TAILWHIP', False, BLACK)
text_04 = ATK_FONT.render('GROWL', False, BLACK)
text_05 = ATK_FONT.render('THUNDERSHOCK', False, BLACK)

##TYPE 
type_poke = ['ELECTRIC', 'NORMAL']


#-------SCENES------#
scene = 4 #### 0: INTRO 1:ATTACK MENU 2:PLAY/ ENEMY ATTACK  3: Critical Hit /Replay 4: FREE ROAMING 5: CONTROL ROOM 6: VERIDIAN FOREST 

##MENU SCENE
TAILWHIP_button = pygame.Rect(122,300,15,5)
GROWL_button = pygame.Rect(122,323,15,5)
THUNDERSHOCK_button = pygame.Rect(122,342,15,5)
click = False
MAIN_MENU = False ###must be at FALSE if scene = 0 (i.e.: Start the game) True for test on scene = 1 only

##INTRO
seq_intro1 = True
seq_intro2 = False

##ATTACK SCENE
seq_1 = True
seq_2 = False

##CRITICAL/ RESTART SCENE
seq_3 = False          ### False  to start from scene = 0, True to test scene = 3  
seq_4 = False
seq_5 = False
RESTART_button = pygame.Rect(50,310,15,5)
EXIT_button = pygame.Rect(50,343,15,5)

#-----UNCOVER ANIMATION------#
uncover_vel = 20

##PLAYER ATTACK SCENE
cover1_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-115),260,70)
cover1b_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-60),200,35)

##ENEMY ATTACK SCENE
cover2_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-115),340,70)
cover2b_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-60),250,35)


##CRITICAL/ RESTART SCENE
cover3_rect= pygame.Rect((WIDTH/2)-170,(HEIGHT-115),270,70)
cover3b_rect= pygame.Rect((WIDTH/2)-170,(HEIGHT-60),300,35)

####TO CONTROL ROOM TERMINAL
cover4_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-115),300,70)
cover4b_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-60),340,35)
transition_controlRoom = pygame.Rect(0,400,400,600)
transition_controlRoom2 = pygame.Rect(0,400,400,400)

###### TO VERIDIAN FROEST
transition_veridian = pygame.Rect(0,400,400,600)
transition_veridian2 = pygame.Rect(0,0,400,600)
cover5_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-115),300,70)
cover5b_rect = pygame.Rect((WIDTH/2)-170,(HEIGHT-60),340,35)


##########################################################
# MAIN LOOP FUNCTION
##########################################################



game = True
while game:
    pygame.time.delay(40)

    #print(exp_point)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            print('CLICKED')
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if event.type == pygame.KEYDOWN :
            frame_speed = 1
        if event.type == pygame.KEYUP :
            frame_speed = 0
            img_index = 0

        


    mouse_pos = pygame.mouse.get_pos()
    if click == True:
        if TAILWHIP_button.collidepoint(mouse_pos) and inv.get('TAILWHIP') > 0 and MAIN_MENU == True:
            inv['TAILWHIP'] = inv.get('TAILWHIP') - 1
            exp_point['exp'] = exp_point.get('exp') + 1
            enemy_hp -= 20
            #print(inv)
            click = False
            attk_name = 'TAILWHIP'
            dealt_dmg = 20
            scene = 2
            MAIN_MENU = False
            seq_1 = True
            
        if GROWL_button.collidepoint(mouse_pos) and inv.get('GROWL') > 0 and MAIN_MENU == True:
            inv['GROWL'] = inv.get('GROWL') - 1
            exp_point['exp'] = exp_point.get('exp') + 1
            enemy_hp -= 40
            #print(inv)
            click = False
            attk_name = 'GROWL'
            dealt_dmg = 40
            scene = 2
            MAIN_MENU = False
            seq_1 = True
            
        if THUNDERSHOCK_button.collidepoint(mouse_pos) and inv.get('THUNDERSHOCK') > 0 and MAIN_MENU == True:
            inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') - 1
            exp_point['exp'] = exp_point.get('exp') + 1
            enemy_hp -= 50
            #print(inv)
            click = False
            attk_name = 'THUNDERSHOCK'
            dealt_dmg = 117
            scene = 2
            MAIN_MENU = False
            seq_1 = True
    #print(scene, MAIN_MENU)

    #-------LVL UP-------#
    if exp_point.get('exp') > 2 and exp_point.get('exp') < 4 and inv.get('THUNDERSHOCK') < 1  :
        inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 1
        play_lvl = 3 

    if exp_point.get('exp') > 5 and exp_point.get('exp') < 7 and inv.get('THUNDERSHOCK') < 2:
        inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 2
        play_lvl = 4

    if exp_point.get('exp') > 8 and exp_point.get('exp') < 10 and inv.get('THUNDERSHOCK') < 3  :
        inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 3
        play_lvl = 5

    if exp_point.get('exp') > 11 and exp_point.get('exp') < 13 and inv.get('THUNDERSHOCK') < 4  :
        inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 4
        play_lvl = 6

    #print(exp_point, play_lvl)

    #------WIN/LOSE CASE------#
    if player_hp >= 0 and enemy_hp <= 0 :
        print('WIN')
        MAIN_MENU = False
        seq_3 = True

        enemy_hp = 1

        scene = 3

    if player_hp <= 0 and enemy_hp >= 0:
        print('LOSE')
        MAIN_MENU = False
        seq_3 = True

        player_hp = 1

        scene = 3



    #-----ROAMING CONTROL-----#
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] != 0 :
        AIM_UP = False
        AIM_DOWN = False
        AIM_L = True
        AIM_R = False

        roam_pos[0] -= roam_vel
        if map_pos[0] <= -10 :
            map_pos[0] += map_vel

        if map3_pos[0] <= -10 :
            map3_pos[0] += map_vel
        
        print('TRUE LEFT')

    if pressed[pygame.K_RIGHT] != 0 :
        AIM_UP = False
        AIM_DOWN = False
        AIM_L = False
        AIM_R = True

        roam_pos[0] += roam_vel
        if map_pos[0] >= -180 :
            map_pos[0] -= map_vel

        if map3_pos[0] >= -100 :
            map3_pos[0] -= map_vel
        
        print('TRUE RIGHT')


    if pressed[pygame.K_UP] != 0 :
        AIM_UP = True
        AIM_DOWN = False
        AIM_L = False
        AIM_R = False

        roam_pos[1] -= roam_vel
        if map_pos[1] <= -10 :
            map_pos[1] += map_vel

        if map3_pos[1] <= -10 :
            map3_pos[1] += map_vel
            print('TRUE UP')


    if pressed[pygame.K_DOWN] != 0 :
        AIM_UP = False
        AIM_DOWN = True
        AIM_L = False
        AIM_R = False

        roam_pos[1] += roam_vel
        if map_pos[1] >= -180 :
            map_pos[1] -= map_vel

        if map3_pos[1] >= -200 :
            map3_pos[1] -= map_vel
            print('TRUE DOWN')




    # Enemy ONIX used earthquake !  PIKACHU used SHOCK !
    ###############################################################
    # DRAW FUNCTION
    ###############################################################
    

    
    if scene == 0 and MAIN_MENU == False :

        SCREEN.blit(backg_image1,(0,0))
        SCREEN.blit(play_sprite,(player_pos[0],player_pos[1]))

        if RESPAWN_veridian == True :
            SCREEN.blit(rand_enemy_choice_2[1],(enemy_pos[0],enemy_pos[1]))
        
        if RESPAWN_route02 == True :
            SCREEN.blit(rand_enemy_choice[1],(enemy_pos[0],enemy_pos[1]))

        ## LVL
        enemylvl_str = str(enemy_lvl)
        enemylvlStr_render = game_boldFont.render(enemylvl_str, False, BLACK)
        SCREEN.blit(enemylvlStr_render,(100,19))
        
        playlvl_str = str(play_lvl)
        playlvlStr_render = game_boldFont.render(playlvl_str, False, BLACK)
        SCREEN.blit(playlvlStr_render,(300,172))

        ## PLAYER HP label 
        playHp_str = str(player_hp) 
        playHpStr_render = game_boldFont.render(playHp_str, False, BLACK)
        SCREEN.blit(playHpStr_render,(221,219))

        maxHp_str = str(max_hp)
        maxHpStr_render = game_boldFont.render(maxHp_str, False, BLACK)
        SCREEN.blit(maxHpStr_render,(297,218))

        #print(attk_name)
        #print(enemy_hp)
        #print(dealt_dmg)

        #-----HP BAR-----#
        playerBar_hp = pygame.Rect(237,207,player_hp,7)
        pygame.draw.rect(SCREEN, GREEN, playerBar_hp)

        enemyBar_hp = pygame.Rect(78,54,enemy_hp,7)
        pygame.draw.rect(SCREEN, GREEN, enemyBar_hp)

        if seq_intro1 == True:

            ##INTRO
            if RESPAWN_route02 == True :
                text_01_str = 'Wild '+ str(rand_enemy_choice[0])
                text_01 = game_font.render(text_01_str, False, (0,0,0))
            if RESPAWN_veridian == True :
                text_01_str = 'Wild '+ str(rand_enemy_choice_2[0])
                text_01 = game_font.render(text_01_str, False, (0,0,0))

            text_01b = game_font.render("appeared !", False, (0,0,0))

            SCREEN.blit(text_01,(30,300))
            SCREEN.blit(text_01b,(30,340))

            pygame.draw.rect(SCREEN, WHITE, cover1_rect)
            pygame.draw.rect(SCREEN, WHITE, cover1b_rect)


            if player_pos[0] >= 0 and player_pos[0] < 45 :
                player_pos[0] += move_vel
            if enemy_pos[0] <= 400 and enemy_pos[0] > 250 :
                enemy_pos[0] -= move_vel

            ##### UNCOVER STATEMENTS

            cover1_rect.width -= uncover_vel
            cover1_rect.left  += uncover_vel

            if cover1_rect.width <= 0 :

                cover1_rect.width = 0
                cover1_rect.left = 0

                cover1b_rect.width -= uncover_vel
                cover1b_rect.left  += uncover_vel

                if cover1b_rect.width <= 0:

                    cover1b_rect.width = 280
                    cover1b_rect.left = (WIDTH/2)-170

                    cover1_rect.width = 280
                    cover1_rect.left = (WIDTH/2)-150
                    #print(cover1_rect.width)

                    #pygame.time.wait(2000)
                    seq_intro1 = False
        
                    seq_intro2 = True  

        if seq_intro2 == True:

            SCREEN.blit(text_02,(30,300))
            SCREEN.blit(text_02b,(30,340))
            pygame.draw.rect(SCREEN, WHITE, cover1_rect)
            pygame.draw.rect(SCREEN, WHITE, cover1b_rect)

            ##### UNCOVER STATEMENTS

            cover1_rect.width -= uncover_vel
            cover1_rect.left  += uncover_vel

            if cover1_rect.width <= 0:
                
                cover1_rect.width = 0
                cover1_rect.left = 0

                cover1b_rect.width -= uncover_vel
                cover1b_rect.left  += uncover_vel

                if cover1b_rect.width <= 0:

                    cover1b_rect.width = 320
                    cover1b_rect.left = (WIDTH/2)-183

                    cover1_rect.width = 300
                    cover1_rect.left = (WIDTH/2)-130
                    #print(cover1_rect.width)

                
                    #pygame.time.wait(2000)
                    MAIN_MENU = True
                    scene = 1
                    seq_intro2 = False

                                
            
    if scene == 1 and MAIN_MENU == True:

        SCREEN.blit(backg_image2,(0,0))

        if RESPAWN_veridian == True :
            SCREEN.blit(rand_enemy_choice_2[1],(enemy_pos[0],enemy_pos[1]))
        
        if RESPAWN_route02 == True :
            SCREEN.blit(rand_enemy_choice[1],(enemy_pos[0],enemy_pos[1]))

        ## LVL 
        enemylvl_str = str(enemy_lvl)
        enemylvlStr_render = game_boldFont.render(enemylvl_str, False, BLACK)
        SCREEN.blit(enemylvlStr_render,(100,19))

        playlvl_str = str(play_lvl)
        playlvlStr_render = game_boldFont.render(playlvl_str, False, BLACK)
        SCREEN.blit(playlvlStr_render,(300,173))

        ## PLAYER HP label 
        playHp_str = str(player_hp) 
        playHpStr_render = game_boldFont.render(playHp_str, False, BLACK)
        SCREEN.blit(playHpStr_render,(221,219))

        maxHp_str = str(max_hp)
        maxHpStr_render = game_boldFont.render(maxHp_str, False, BLACK)
        SCREEN.blit(maxHpStr_render,(297,218))

        #-----HP BAR-----#
        playerBar_hp = pygame.Rect(237,207,player_hp,7)
        pygame.draw.rect(SCREEN, GREEN, playerBar_hp)

        enemyBar_hp = pygame.Rect(78,54,enemy_hp,7)
        pygame.draw.rect(SCREEN, GREEN, enemyBar_hp)
        
 
        if inv.get('TAILWHIP') > 0:
            SCREEN.blit(text_03,(160,289))
            pygame.draw.rect(SCREEN, BLACK, TAILWHIP_button)

        if inv.get('GROWL') > 0:
            SCREEN.blit(text_04,(160,309))
            pygame.draw.rect(SCREEN, BLACK, GROWL_button)
            
        if inv.get('THUNDERSHOCK') > 0:
            SCREEN.blit(text_05,(160,329))
            pygame.draw.rect(SCREEN, BLACK, THUNDERSHOCK_button)

        #-----ATTACK STATS-----#
        if TAILWHIP_button.collidepoint(mouse_pos) and inv.get('TAILWHIP') > 0:
            type1_str = str(type_poke[1])
            typeStr1_render = ATK_FONT.render(type1_str, False, BLACK)
            SCREEN.blit(typeStr1_render,(32,216))    

            attkStats1_str = str(inv.get('TAILWHIP')) + '  ' + str(max_tackle)
            attkStats1_render= game_boldFont.render(attkStats1_str, False, BLACK)
            SCREEN.blit(attkStats1_render,(124,240))


        if GROWL_button.collidepoint(mouse_pos) and inv.get('GROWL') > 0:
            type2_str = str(type_poke[1])
            typeStr2_render = ATK_FONT.render(type2_str, False, BLACK)
            SCREEN.blit(typeStr2_render,(32,216))

            attkStats2_str = str(inv.get('GROWL')) + '  ' + str(max_shock)
            attkStats2_render= game_boldFont.render(attkStats2_str, False, BLACK)
            SCREEN.blit(attkStats2_render,(124,240))


        if THUNDERSHOCK_button.collidepoint(mouse_pos) and inv.get('THUNDERSHOCK') > 0 :
            type2_str = str(type_poke[0])
            typeStr2_render = ATK_FONT.render(type2_str, False, BLACK)
            SCREEN.blit(typeStr2_render,(32,216))

            attkStats3_str = str(inv.get('THUNDERSHOCK')) + '  ' + str(max_electburst)
            attkStats3_render= game_boldFont.render(attkStats3_str, False, BLACK)
            SCREEN.blit(attkStats3_render,(122,240))



    if scene == 2 and MAIN_MENU == False:
     
        SCREEN.blit(backg_image1,(0,0))
        SCREEN.blit(play_sprite,(player_pos[0],player_pos[1]))

        if RESPAWN_veridian == True :
            SCREEN.blit(rand_enemy_choice_2[1],(enemy_pos[0],enemy_pos[1]))
        
        if RESPAWN_route02 == True :
            SCREEN.blit(rand_enemy_choice[1],(enemy_pos[0],enemy_pos[1]))

        ## LVL
        enemylvl_str = str(enemy_lvl)
        enemylvlStr_render = game_boldFont.render(enemylvl_str, False, BLACK)
        SCREEN.blit(enemylvlStr_render,(100,19))
        
        playlvl_str = str(play_lvl)
        playlvlStr_render = game_boldFont.render(playlvl_str, False, BLACK)
        SCREEN.blit(playlvlStr_render,(300,172))

        ## PLAYER HP label 
        playHp_str = str(player_hp) 
        playHpStr_render = game_boldFont.render(playHp_str, False, BLACK)
        SCREEN.blit(playHpStr_render,(221,219))

        maxHp_str = str(max_hp)
        maxHpStr_render = game_boldFont.render(maxHp_str, False, BLACK)
        SCREEN.blit(maxHpStr_render,(297,218))

        #print(attk_name)
        #print(enemy_hp)
        #print(dealt_dmg)

        #-----HP BAR-----#
        playerBar_hp = pygame.Rect(237,207,player_hp,7)
        pygame.draw.rect(SCREEN, GREEN, playerBar_hp)

        enemyBar_hp = pygame.Rect(78,54,enemy_hp,7)
        pygame.draw.rect(SCREEN, GREEN, enemyBar_hp)

        ##PLAYER ATTACK SEQ
        if seq_1 == True:


            text_06_str = (play_pok) + ' used'
            text_06 = game_font.render(text_06_str, False, BLACK)

            text_06b_str = (attk_name) +' !'
            text_06b = game_font.render(text_06b_str, False, BLACK)

            SCREEN.blit(text_06,(30,300))
            SCREEN.blit(text_06b,(30,340))



            pygame.draw.rect(SCREEN, WHITE, cover1_rect)
            pygame.draw.rect(SCREEN, WHITE, cover1b_rect)

            ##### UNCOVER STATEMENTS

            cover1_rect.width -= uncover_vel
            cover1_rect.left  += uncover_vel

            if cover1_rect.width <= 0:
                
                cover1_rect.width = 0
                cover1_rect.left = 0

                cover1b_rect.width -= uncover_vel
                cover1b_rect.left  += uncover_vel

                if cover1b_rect.width <= 0:

                    cover1_rect.width = 280
                    cover1_rect.left = (WIDTH/2)-150
                    #print(cover1_rect.width)

                    cover1b_rect.width = 320
                    cover1b_rect.left = (WIDTH/2)-183
                
                    #pygame.time.wait(2000)
                    seq_1 = False
        
                    seq_2 = True   

        if seq_2 == True:
            
            #------ENEMY TEXT------#
            randAtk_enemy = ''
            if attk_name == 'TAILWHIP':
                if RESPAWN_route02 == True :
                    if (rand_enemy_choice[0]) == 'ONIX':
                        randAtk_enemy = onixAtk_list[0]
                    elif (rand_enemy_choice[0]) == 'CHARIZARD':
                        randAtk_enemy = charizardAtk_list[1]
                if RESPAWN_veridian == True :
                    if (rand_enemy_choice_2[0]) == 'ARTICUNO':
                        randAtk_enemy = articunoAtk_list[0]
                    elif (rand_enemy_choice_2[0]) == 'MEWTO':
                        randAtk_enemy = mewtoAtk_list[1]
            if attk_name == 'GROWL':
                if RESPAWN_route02 == True :
                    if (rand_enemy_choice[0]) == 'ONIX':
                        randAtk_enemy = onixAtk_list[1]
                    elif (rand_enemy_choice[0]) == 'CHARIZARD':
                        randAtk_enemy = charizardAtk_list[0]
                if RESPAWN_veridian == True :
                    if (rand_enemy_choice_2[0]) == 'ARTICUNO':
                        randAtk_enemy = articunoAtk_list[1]
                    elif (rand_enemy_choice_2[0]) == 'MEWTO':
                        randAtk_enemy = mewtoAtk_list[0]
            
            if attk_name == 'THUNDERSHOCK':
                if RESPAWN_route02 == True :
                    if (rand_enemy_choice[0]) == 'ONIX':
                        randAtk_enemy = onixAtk_list[0]
                    elif (rand_enemy_choice[0]) == 'CHARIZARD':
                        randAtk_enemy = charizardAtk_list[1]
                if RESPAWN_veridian == True :
                    if (rand_enemy_choice_2[0]) == 'ARTICUNO':
                        randAtk_enemy = articunoAtk_list[0]
                    elif (rand_enemy_choice_2[0]) == 'MEWTO':
                        randAtk_enemy = mewtoAtk_list[1]


            print(randAtk_enemy)

            if RESPAWN_route02 == True :
                text_07_str = (rand_enemy_choice[0]) + ' used'
                text_07 = game_font.render(text_07_str, False, BLACK)

                text_07b_str = (randAtk_enemy) +' !'
                text_07b = game_font.render(text_07b_str, False, BLACK)

            if RESPAWN_veridian == True :
                text_07_str = (rand_enemy_choice_2[0]) + ' used'
                text_07 = game_font.render(text_07_str, False, BLACK)

                text_07b_str = (randAtk_enemy) +' !'
                text_07b = game_font.render(text_07b_str, False, BLACK)
                

            SCREEN.blit(text_07,(30,300))
            pygame.draw.rect(SCREEN, WHITE, cover2_rect)

            SCREEN.blit(text_07b,(30,340))
            pygame.draw.rect(SCREEN, WHITE, cover2b_rect)
            

            ##### UNCOVER STATEMENTS
            cover2_rect.width -= uncover_vel
            cover2_rect.left  += uncover_vel

            if cover2_rect.width <= 0:

                cover2_rect.width = 0
                cover2_rect.left = 0

                cover2b_rect.width -= uncover_vel
                cover2b_rect.left  += uncover_vel
            
                #-----ENEMY MOVE----#
                ##ONIX
                print(randAtk_enemy)
                if randAtk_enemy == 'ROCKTHROW' or randAtk_enemy == 'FIRESPIN' or randAtk_enemy == 'BLIZZARD' or randAtk_enemy == 'AMNESIA'  :
                    invert = -1
                    enemy_pos[0] -= move_vel2
                    enemy_pos[1] += move_vel2/2
                    if enemy_pos[0] < 50 or enemy_pos[1] > 180 :
                        move_vel2 = move_vel2*invert
                    elif enemy_pos[0] > 200 or enemy_pos[1] < 20 :
                        move_vel2 = move_vel2*invert
                        #print(move_vel2)

                if randAtk_enemy == 'TACKLE' or randAtk_enemy == 'DRANGONCLAW'or randAtk_enemy == 'LASERFOCUS' or randAtk_enemy == 'ICEBEAM' :
                    #print('USEMEEEEEEEEEEEEEEEEEE')
                    invert = -1
                    enemy_pos[0] -= move_vel
                    enemy_pos[1] += move_vel/2
                    if enemy_pos[0] < 200 or enemy_pos[1] > 300 :
                        move_vel = move_vel*invert
                    elif enemy_pos[0] > 400 or enemy_pos[1] < 40 :
                        move_vel = 0 ###move_vel*invert
                        #print(move_vel)


                #####################
                if cover2b_rect.width <= 0:
                    #print(cover2_rect.width)
                    cover2_rect.width = 280
                    cover2_rect.left= (WIDTH/2)-150

                    cover2b_rect.width = 300
                    cover2b_rect.left= (WIDTH/2)-183

                    enemyAtk_dmg = random.randint(10, 80)
                    player_hp = player_hp - enemyAtk_dmg

                    #pygame.time.wait(1000)
                    move_vel = 8
                    seq_2 = False 

                    MAIN_MENU = True
                    scene = 1

    if scene == 3 and MAIN_MENU == False:
          
        SCREEN.blit(backg_image1,(0,0))
        SCREEN.blit(play_sprite,(player_pos[0],player_pos[1]))

        if RESPAWN_veridian == True :
            SCREEN.blit(rand_enemy_choice_2[1],(enemy_pos[0],enemy_pos[1]))
        
        if RESPAWN_route02 == True :
            SCREEN.blit(rand_enemy_choice[1],(enemy_pos[0],enemy_pos[1]))


        ## LVL
        enemylvl_str = str(enemy_lvl)
        enemylvlStr_render = game_boldFont.render(enemylvl_str, False, BLACK)
        SCREEN.blit(enemylvlStr_render,(100,19))
        
        playlvl_str = str(play_lvl)
        playlvlStr_render = game_boldFont.render(playlvl_str, False, BLACK)
        SCREEN.blit(playlvlStr_render,(300,173))

        ## PLAYER HP label 
        playHp_str = str(player_hp) 
        playHpStr_render = game_boldFont.render(playHp_str, False, BLACK)
        SCREEN.blit(playHpStr_render,(221,219))

        maxHp_str = str(max_hp)
        maxHpStr_render = game_boldFont.render(maxHp_str, False, BLACK)
        SCREEN.blit(maxHpStr_render,(297,218))

        #print(attk_name)
        #print(enemy_hp)
        #print(dealt_dmg)

        #-----HP BAR-----#
        playerBar_hp = pygame.Rect(237,207,player_hp,7)
        pygame.draw.rect(SCREEN, GREEN, playerBar_hp)
    
    if seq_3 == True:

        #------CRITICAL TEXT------#
        text_08_str = 'This is a'
        text_08 = game_font.render(text_08_str, False, BLACK)

        text_08b_str = 'CRITICAL HIT !'
        text_08b = game_font.render(text_08b_str, False, BLACK)


        SCREEN.blit(text_08,(30,300))
        pygame.draw.rect(SCREEN, WHITE, cover3_rect)

        
        SCREEN.blit(text_08b,(30,340))
        pygame.draw.rect(SCREEN, WHITE, cover3b_rect)

        cover3_rect.width -= uncover_vel
        cover3_rect.left  += uncover_vel

        if cover3_rect.width <= 0:

            cover3_rect.width = 0
            cover3_rect.left = 0

            cover3b_rect.width -= uncover_vel
            cover3b_rect.left  += uncover_vel

            if cover3b_rect.width <= 0:

                cover3_rect.width = 280
                cover3_rect.left = (WIDTH/2)-150
                #print(cover3_rect.width)

                cover3b_rect.width = 280
                cover3b_rect.left = (WIDTH/2)-170
                #print(cover3_rect.width)

                #pygame.time.wait(2000)
                seq_3 = False

                seq_4 = True   

    if seq_4 == True: 

        #------RESTART TEXT------#
        text_09_str = 'Do you want'
        text_09 = game_font.render(text_09_str, False, BLACK)

        text_09b_str = 'to RESTART ?'
        text_09b = game_font.render(text_09b_str, False, BLACK)

        SCREEN.blit(text_09,(30,300))
        pygame.draw.rect(SCREEN, WHITE, cover3_rect)

        SCREEN.blit(text_09b,(30,340))
        pygame.draw.rect(SCREEN, WHITE, cover3b_rect)

        cover3_rect.width -= uncover_vel
        cover3_rect.left  += uncover_vel

        if cover3_rect.width <= 0:

            cover3_rect.width = 0
            cover3_rect.left  = 0

            cover3b_rect.width -= uncover_vel
            cover3b_rect.left  += uncover_vel

            if cover3b_rect.width <= 0:

                cover3b_rect.width = 280
                cover3b_rect.left = (WIDTH/2)-170

                cover3_rect.width = 280
                cover3_rect.left = (WIDTH/2)-170

                #pygame.time.wait(2000)
                #print(cover3_rect.width)

                seq_4 = False

                seq_5 = True
    
    if seq_5 == True:

        pygame.draw.rect(SCREEN, BLACK, RESTART_button)
        pygame.draw.rect(SCREEN, BLACK, EXIT_button)

        text_10_str = 'REPLAY'
        text_10 = game_font.render(text_10_str, False, BLACK)
        SCREEN.blit(text_10, (70,300))

        text_11_str = 'EXIT'
        text_11 = game_font.render(text_11_str, False, BLACK)
        SCREEN.blit(text_11, (70,333))

        print(seq_1,seq_2,seq_3,seq_4,seq_5,seq_intro1,seq_intro2)
        if click == True:
            if RESTART_button.collidepoint(mouse_pos) and MAIN_MENU == False:
                #inv['TAILWHIP'] = 2
                #inv['GROWL'] = 2
                #inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 1

                player_hp = 117 
                enemy_hp = 117 

                pygame.time.wait(1000)
                MAIN_MENU = True
                scene = 1
                seq_5 = False
            if EXIT_button.collidepoint(mouse_pos) and MAIN_MENU == False:
                inv['TAILWHIP'] = 2
                inv['GROWL'] = 2
                #inv['THUNDERSHOCK'] = inv.get('THUNDERSHOCK') + 1

                player_hp = 117 
                enemy_hp = 117 

                block_x1.width = 50
                block_x2.width = 50
                block_x3.width = 50
                block_x4.width = 50
                block_x5.width = 50
                block_x6.width = 50 
                block_x7.width = 50 
                block_x8.width = 50
                block_y1.width = 50 
                block_y2.width = 50
                block_y3.width = 50
                block_y4.width = 50
                block_y5.width = 50
                block_y6.width = 50


                rand_prob = random.random()
                rand_enemy_choice = random.choice(list(enemy_dict.items()))
                rand_enemy_choice_2 = random.choice(list(enemy_dict_2.items()))
                print(rand_enemy_choice[0])

                pygame.time.wait(1000)
                FIRST_SQUARE = True

                if RESPAWN_veridian == True :
                    scene = 6

                if RESPAWN_route02 == True :
                    scene = 4

                seq_5 = False
                
                #game = False
                #sys.exit()







































    if scene == 4 and MAIN_MENU == False :

        roaming_zone = pygame.Rect(map_pos[0] + 160,map_pos[1] + 160,150,60)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone)

        player_collider = pygame.Rect(roam_pos[0],roam_pos[1],25,25)
        pygame.draw.rect(SCREEN, WHITE, player_collider)

        controlRoom_collider = pygame.Rect(map_pos[0]+120, map_pos[1]+60, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, controlRoom_collider)
        
        SCREEN.blit(backg_image3,(map_pos[0], map_pos[1]))

        #print(AIM_DOWN,AIM_UP,AIM_L,AIM_R)
        if AIM_R == True:

            SCREEN.blit(R_LIST[img_index],(roam_pos[0],roam_pos[1]))  
            
            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(R_LIST):
                    img_index = 0
                SCREEN.blit(R_LIST[img_index], (roam_pos[0],roam_pos[1])) 
            
            
        if AIM_L == True:

            SCREEN.blit(L_LIST[img_index],(roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(L_LIST[img_index], (roam_pos[0],roam_pos[1]))  


        if AIM_UP == True:

            SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  
                
        
        if AIM_DOWN == True:

            SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(DOWN_LIST):
                    img_index = 0
                SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1])) 



        #--------COLLIDER TO CONTROL ROOM---------#
        
        if player_collider.colliderect(controlRoom_collider) :

            SCREEN.blit(terminal_post, (0, 265))  
            print('COLLIDED')

            ##########  TRAVEL TO CONTROL ROOM 

            travel_string = 'Travel to '
            travel_string2 = 'CONTROL ROOM'
            travel_render = game_font.render(travel_string, False, BLACK)
            travel_render2 = game_font.render(travel_string2, False, BLACK)
            SCREEN.blit(travel_render, (30, 300))
            SCREEN.blit(travel_render2, (30, 340))


            pygame.draw.rect(SCREEN, WHITE, cover4_rect)
            pygame.draw.rect(SCREEN, WHITE, cover4b_rect)

             
            ##### UNCOVER STATEMENTS

        
            cover4_rect.width -= uncover_vel
            cover4_rect.left  += uncover_vel

            if cover4_rect.width < 0:
                
                cover4_rect.width = 0
                cover4_rect.left = 0

                cover4b_rect.width -= uncover_vel
                cover4b_rect.left  += uncover_vel

                if cover4b_rect.width <= 0:

                    cover4_rect.width = 0
                    cover4_rect.left = (WIDTH/2)-150
                    #print(cover1_rect.width)

                    cover4b_rect.width = 0
                    cover4b_rect.left = (WIDTH/2)-183
                

                    transition_controlRoom.top -= uncover_vel
                    pygame.draw.rect(SCREEN, BLACK, transition_controlRoom)

                    if transition_controlRoom.top <= 0 :
                        
                        transition_controlRoom.top = 0
                        print(transition_controlRoom.top)
                        print('SCENE 5 READY')

                        roam_pos[0] = (WIDTH/2)-40
                        roam_pos[1] = (HEIGHT/2)+80
                        roam_vel = 1

                        cover4_rect.width = 300
                        cover4_rect.left = (WIDTH/2)-150
                        #print(cover1_rect.width)

                        cover4b_rect.width = 360
                        cover4b_rect.left = (WIDTH/2)-183
                        
                        #pygame.time.wait(1000)

                        #####
                        scene = 5
                        MAIN_MENU = False


        #print(roam_vel)
        ###COLLIDER ROAMING ZONE

        if player_collider.colliderect(roaming_zone) and rand_prob >= 0.01 :

            rand_prob = random.random()
        
        #print(rand_prob)
        #print(seq_1,seq_2,seq_3,seq_4,seq_5,seq_intro1,seq_intro2)

        #-----------BATTLE TRANSITIONS----------#
        if player_collider.colliderect(roaming_zone) and rand_prob <= 0.01 :
            #print(rand_prob)


            print('SPOTTED')
            roam_vel = 0
            ########### transition
            if FIRST_SQUARE == True:
                pygame.draw.rect(SCREEN, BLACK, block_y1)
                block_y1.height += block_vel

                if block_y1.height >= HEIGHT:
                    block_y1.height = HEIGHT

                    #print('STEP 1',block_y1.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x1)
                    block_x1.width += block_vel

                    if block_x1.width >= WIDTH:
                        block_x1.width = WIDTH

                        #print('STEP 2',block_x1.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y2)
                        block_y2.height -= block_vel
                        #print('STEP 3',block_y2.height )
                        if block_y2.height <= -HEIGHT:
                            block_y2.height = -HEIGHT
                            #print('STEP 3',block_y2.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x2)
                            block_x2.width -= block_vel
                            if block_x2.width <= -WIDTH:
                                block_x2.width = -WIDTH
                                #print('STEP 4', block_x2.width)
                                SECOND_SQUARE = True 
                
                
            if SECOND_SQUARE == True:
                #print(SECOND_SQUARE)
                pygame.draw.rect(SCREEN, BLACK, block_y3)
                block_y3.height += block_vel

                if block_y3.height >= HEIGHT-50:
                    block_y3.height = HEIGHT

                    #print('STEP 1',block_y3.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x3)
                    block_x3.width += block_vel

                    if block_x3.width >= WIDTH:
                        block_x3.width = WIDTH

                        #print('STEP 2',block_x3.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y4)
                        block_y4.height -= block_vel
                        
                        if block_y4.height <= -HEIGHT:
                            block_y4.height = -HEIGHT
                            #print('STEP 3',block_y4.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x4)
                            block_x4.width -= block_vel
                            if block_x4.width <= -WIDTH:
                                block_x4.width = -WIDTH
                                #print('STEP 4', block_x4.width)
                                THIRD_SQUARE = True
            
            if THIRD_SQUARE == True:
                #print(SECOND_SQUARE)
                pygame.draw.rect(SCREEN, BLACK, block_y5)
                block_y5.height += block_vel

                if block_y5.height >= HEIGHT-100:
                    block_y5.height = HEIGHT

                    #print('STEP 1',block_y5.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x5)
                    block_x5.width += block_vel

                    if block_x5.width >= WIDTH:
                        block_x5.width = WIDTH

                        #print('STEP 2',block_x5.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y6)
                        block_y6.height -= block_vel
                        
                        if block_y6.height <= -HEIGHT:
                            block_y6.height = -HEIGHT
                            #print('STEP 3',block_y6.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x6)
                            block_x6.width -= block_vel
                            if block_x6.width <= -WIDTH:
                                block_x6.width = -WIDTH
                                #print('STEP 4', block_x6.width)
                                FINAL_SQUARE = True
                
            if FINAL_SQUARE == True:
                pygame.draw.rect(SCREEN, BLACK, block_x7)
                block_x7.width += block_vel
                if block_x7.width >= WIDTH:
                    pygame.draw.rect(SCREEN, BLACK, block_x8)
                    block_x8.width -= block_vel
                    if block_x8.width <= -WIDTH:
                        block_x8.width = -WIDTH
                        print('BATLLE READY')

                        pygame.time.wait(1000)

                        FIRST_SQUARE = False
                        SECOND_SQUARE = False     
                        THIRD_SQUARE = False
                        seq_1 = True
                        seq_intro1 = True
                        scene = 0
                        FINAL_SQUARE = False

                        RESPAWN_route02 = True
                        RESPAWN_veridian = False

                        roam_pos[0] = (WIDTH/2)-150
                        roam_pos[1] = (HEIGHT/2)
                        roam_vel = 1


    ############### CONTROL ROOM #####################

    if scene == 5 and MAIN_MENU == False :
        #####3

        #SCREEN.blit(backg_image4,(0, 0))

        veridian_collider = pygame.Rect(map2_pos[0]+190, map2_pos[1]+40, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, veridian_collider)

        route02_collider = pygame.Rect((WIDTH/2)-25,310,50,50)
        pygame.draw.rect(SCREEN, WHITE, route02_collider)
            
        player_collider = pygame.Rect(roam_pos[0],roam_pos[1],25,25)
        pygame.draw.rect(SCREEN, WHITE, player_collider)
        
        SCREEN.blit(backg_image4,(0, 0))


        if AIM_R == True:

            SCREEN.blit(R_LIST[img_index],(roam_pos[0],roam_pos[1]))  
            
            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(R_LIST):
                    img_index = 0
                SCREEN.blit(R_LIST[img_index], (roam_pos[0],roam_pos[1])) 
            
            
        if AIM_L == True:

            SCREEN.blit(L_LIST[img_index],(roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(L_LIST[img_index], (roam_pos[0],roam_pos[1]))  


        if AIM_UP == True:

            SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  
                
        
        if AIM_DOWN == True:

            SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(DOWN_LIST):
                    img_index = 0
                SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1])) 



        #-------CLIP IN TRANSITIONS-------#
        transition_controlRoom.top -= uncover_vel
        pygame.draw.rect(SCREEN, BLACK, transition_controlRoom)

        if transition_controlRoom.top + transition_controlRoom.height <= 0 :
            
            transition_controlRoom.top = -600
            print(transition_controlRoom.top)


        #-----TRANSITION TO VERIDIAN-----#

        if player_collider.colliderect(veridian_collider) :

            SCREEN.blit(terminal_post, (0, 265))  
            print('COLLIDED')

            ##########  TRAVEL TO CONTROL ROOM 

            travel_string = 'Travel to '
            travel_string2 = 'VERIDIAN FOREST'
            travel_render = game_font.render(travel_string, False, BLACK)
            travel_render2 = game_font.render(travel_string2, False, BLACK)
            SCREEN.blit(travel_render, (30, 300))
            SCREEN.blit(travel_render2, (30, 340))


            pygame.draw.rect(SCREEN, WHITE, cover5_rect)
            pygame.draw.rect(SCREEN, WHITE, cover5b_rect)

            
            ##### UNCOVER STATEMENTS
        
            cover5_rect.width -= uncover_vel
            cover5_rect.left  += uncover_vel

            if cover5_rect.width < 0:
                
                cover5_rect.width = 0
                cover5_rect.left = 0

                cover5b_rect.width -= uncover_vel
                cover5b_rect.left  += uncover_vel

                if cover5b_rect.width <= 0:

                    cover5_rect.width = 0
                    cover5_rect.left = (WIDTH/2)-150
                    #print(cover1_rect.width)

                    cover5b_rect.width = 0
                    cover5b_rect.left = (WIDTH/2)-183
                
                    
                    transition_veridian.top -= uncover_vel
                    pygame.draw.rect(SCREEN, BLACK, transition_veridian)

                    if transition_veridian.top <= 0 :
                        
                        transition_veridian.top = 400
                        print(transition_veridian.top)
                        print('SCENE 6 READY')

                        roam_pos[0] = (WIDTH/2)
                        roam_pos[1] = 300
                        roam_vel = 1


                        cover5_rect.width = 300
                        cover5_rect.left = (WIDTH/2)-150
                        #print(cover1_rect.width)

                        cover5b_rect.width = 360
                        cover5b_rect.left = (WIDTH/2)-183
                            
                        #pygame.time.wait(1000)
                        
                        #####
                        scene = 6
                        MAIN_MENU = False

                    #################

        ### BACK TO ROUTE 02 ###
        if player_collider.colliderect(route02_collider) :

            print('COLLIDED')
            pygame.draw.rect(SCREEN, BLACK, transition_controlRoom2)
            transition_controlRoom2.top -= uncover_vel 


            print(transition_controlRoom2.top)
                
            if transition_controlRoom2.top <= 0 :
                transition_controlRoom2.top = 400
                print(transition_controlRoom2.top)

                roam_pos[0] = (WIDTH/2)+40
                roam_pos[1] = (HEIGHT/2)-100
                roam_vel = 1

                map_pos[0] = 0
                map_pos[1] = 0

                map3_pos[0] = 0
                map3_pos[1] = -470
                        

                scene = 4
                MAIN_MENU = False












    ############# VERIDIAN FOREST ####################

    #print(scene, MAIN_MENU)
    if scene == 6 and MAIN_MENU == False :
        ###########################################################
        #SCREEN.blit(backg_image5, (map3_pos[0], map3_pos[1]))
            
               
        roaming_zone2 = pygame.Rect(map3_pos[0] + 360, map3_pos[1], 80, 170)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone2)

        roaming_zone3 = pygame.Rect(map3_pos[0] + 445, map3_pos[1] + 190, 50, 170)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone3)

        roaming_zone4 = pygame.Rect(map3_pos[0] + 100, map3_pos[1] + 140, 150, 40)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone4)

        roaming_zone5 = pygame.Rect(map3_pos[0] + 25, map3_pos[1] + 160, 30, 60)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone5)

        roaming_zone6 = pygame.Rect(map3_pos[0] + 145, map3_pos[1] + 350, 20, 100)
        pygame.draw.rect(SCREEN, WHITE, roaming_zone6)

        roaming_list = [ roaming_zone3, roaming_zone4, roaming_zone5, roaming_zone6 ]

        #SCREEN.blit(backg_image5, (map3_pos[0], map3_pos[1]))
        backTo_CR_collider = pygame.Rect(map3_pos[0]+(WIDTH/2)+80,map3_pos[1]+550, 50, 50)
        pygame.draw.rect(SCREEN, WHITE, backTo_CR_collider)

        player_collider = pygame.Rect(roam_pos[0],roam_pos[1],25,25)
        pygame.draw.rect(SCREEN, WHITE, player_collider)

        SCREEN.blit(backg_image5, (map3_pos[0], map3_pos[1]))


        if AIM_R == True:

            SCREEN.blit(R_LIST[img_index],(roam_pos[0],roam_pos[1]))  
            
            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(R_LIST):
                    img_index = 0
                SCREEN.blit(R_LIST[img_index], (roam_pos[0],roam_pos[1])) 
            
            
        if AIM_L == True:

            SCREEN.blit(L_LIST[img_index],(roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(L_LIST[img_index], (roam_pos[0],roam_pos[1]))  


        if AIM_UP == True:

            SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(UP_LIST):
                    img_index = 0
                SCREEN.blit(UP_LIST[img_index], (roam_pos[0],roam_pos[1]))  
                
        
        if AIM_DOWN == True:

            SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1]))  

            img_timer += 1
            if img_timer >= 4 :
                img_timer = 0
                img_index += frame_speed
                if img_index >= len(DOWN_LIST):
                    img_index = 0
                SCREEN.blit(DOWN_LIST[img_index], (roam_pos[0],roam_pos[1])) 


        
        #-------CLIP IN TRANSITIONS-------#
        transition_veridian2.top -= uncover_vel
        pygame.draw.rect(SCREEN, BLACK, transition_veridian2)
        
        if transition_veridian2.top + transition_veridian2.height <= -800 :
            
            transition_veridian2.top = -900
        
        #print(transition_veridian2.top)



        
        ### BACK TO CONTROL ROOM 
        if player_collider.colliderect(backTo_CR_collider) :

            pygame.draw.rect(SCREEN, BLACK, transition_controlRoom2)
            transition_controlRoom2.top -= uncover_vel 


            print(transition_controlRoom2.top)
                
            if transition_controlRoom2.top <= 0 :
                transition_controlRoom2.top = 400
                print(transition_controlRoom2.top)

                roam_pos[0] = (WIDTH/2)+40
                roam_pos[1] = (HEIGHT/2)-100
                roam_vel = 1
                        
                scene = 5
                MAIN_MENU = False
            #print('COLLIDED')


        if player_collider.collidelist(roaming_list) != -1 and rand_prob2 >= 0.01 :

            rand_prob2 = random.random()
        
        print(rand_prob2)
        #print(seq_1,seq_2,seq_3,seq_4,seq_5,seq_intro1,seq_intro2)

        #-----------BATTLE TRANSITIONS----------#
        if player_collider.collidelist(roaming_list) != -1 and rand_prob2 <= 0.01 :

            print(rand_prob2)
            print('SPOTTED')

            roam_vel = 0
            ########### transition
            if FIRST_SQUARE == True:
                pygame.draw.rect(SCREEN, BLACK, block_y1)
                block_y1.height += block_vel

                if block_y1.height >= HEIGHT:
                    block_y1.height = HEIGHT

                    #print('STEP 1',block_y1.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x1)
                    block_x1.width += block_vel

                    if block_x1.width >= WIDTH:
                        block_x1.width = WIDTH

                        #print('STEP 2',block_x1.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y2)
                        block_y2.height -= block_vel
                        #print('STEP 3',block_y2.height )
                        if block_y2.height <= -HEIGHT:
                            block_y2.height = -HEIGHT
                            #print('STEP 3',block_y2.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x2)
                            block_x2.width -= block_vel
                            if block_x2.width <= -WIDTH:
                                block_x2.width = -WIDTH
                                #print('STEP 4', block_x2.width)
                                SECOND_SQUARE = True 
                
                
            if SECOND_SQUARE == True:
                #print(SECOND_SQUARE)
                pygame.draw.rect(SCREEN, BLACK, block_y3)
                block_y3.height += block_vel

                if block_y3.height >= HEIGHT-50:
                    block_y3.height = HEIGHT

                    #print('STEP 1',block_y3.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x3)
                    block_x3.width += block_vel

                    if block_x3.width >= WIDTH:
                        block_x3.width = WIDTH

                        #print('STEP 2',block_x3.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y4)
                        block_y4.height -= block_vel
                        
                        if block_y4.height <= -HEIGHT:
                            block_y4.height = -HEIGHT
                            #print('STEP 3',block_y4.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x4)
                            block_x4.width -= block_vel
                            if block_x4.width <= -WIDTH:
                                block_x4.width = -WIDTH
                                #print('STEP 4', block_x4.width)
                                THIRD_SQUARE = True
            
            if THIRD_SQUARE == True:
                #print(SECOND_SQUARE)
                pygame.draw.rect(SCREEN, BLACK, block_y5)
                block_y5.height += block_vel

                if block_y5.height >= HEIGHT-100:
                    block_y5.height = HEIGHT

                    #print('STEP 1',block_y5.height )
                    pygame.draw.rect(SCREEN, BLACK, block_x5)
                    block_x5.width += block_vel

                    if block_x5.width >= WIDTH:
                        block_x5.width = WIDTH

                        #print('STEP 2',block_x5.width )
                        pygame.draw.rect(SCREEN, BLACK, block_y6)
                        block_y6.height -= block_vel
                        
                        if block_y6.height <= -HEIGHT:
                            block_y6.height = -HEIGHT
                            #print('STEP 3',block_y6.height )

                            pygame.draw.rect(SCREEN, BLACK, block_x6)
                            block_x6.width -= block_vel
                            if block_x6.width <= -WIDTH:
                                block_x6.width = -WIDTH
                                #print('STEP 4', block_x6.width)
                                FINAL_SQUARE = True
                
            if FINAL_SQUARE == True:
                pygame.draw.rect(SCREEN, BLACK, block_x7)
                block_x7.width += block_vel
                if block_x7.width >= WIDTH:
                    pygame.draw.rect(SCREEN, BLACK, block_x8)
                    block_x8.width -= block_vel
                    if block_x8.width <= -WIDTH:
                        block_x8.width = -WIDTH
                        print('BATLLE READY')

                        pygame.time.wait(1000)
                        
                        FIRST_SQUARE = False
                        SECOND_SQUARE = False     
                        THIRD_SQUARE = False
                        seq_1 = True
                        seq_intro1 = True
                        scene = 0
                        FINAL_SQUARE = False

                        RESPAWN_veridian = True
                        RESPAWN_route02 = False
                    
                        roam_pos[0] = (WIDTH/2)
                        roam_pos[1] = (HEIGHT/2)+150

                        roam_vel = 1
        
















    #print(FIRST_SQUARE,SECOND_SQUARE,THIRD_SQUARE,FINAL_SQUARE)
    #print(seq_1,seq_2)


    pygame.display.update()
    ################################################
    # END
    ################################################
pygame.quit()
