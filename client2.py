import pygame
from button import Button
from network import Network
from board import Board
from timer import Timer
from sounds import Sounds



def main():
    pygame.init()


    width = 500
    height = 700
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")
    bottomheight = 200
    lastX = 0
    lastY = 0

    lastX2 = 0
    lastY2 = 0

    barriers = []


    bg = pygame.image.load("images and audio/cube background3.jpg")
    bg = pygame.transform.scale(bg, (width, height-bottomheight))#500,500

    blackBg = pygame.image.load("images and audio/black bg.jpg")
    blackBg = pygame.transform.scale(blackBg, (width, bottomheight))#500,200

    # brick = pygame.image.load("D:/‏‏הורדות/black brick.jpg")
    # brick = pygame.transform.scale(brick, (50, 50))

    redCube = pygame.image.load("images and audio/‏‏Box cop.png")
    redCube = pygame.transform.scale(redCube, (40, 40))
    blackCube = pygame.image.load("images and audio/‏‏Box - עותק.png")
    blackCube = pygame.transform.scale(blackCube, (40, 40))

    muteImage = pygame.image.load("D:\‏‏הורדות\mute.jpg")
    muteImage = pygame.transform.scale(muteImage, (50, 50))

    # Create a mute button and display it on the screen
    mute_button = pygame.Rect(450, 500, 50, 50)
    mute_button_color = (255, 0, 0)

    # load start and exit button images
    start_img = pygame.image.load("images and audio/start_btn.png").convert_alpha()
    start_img = pygame.transform.scale(start_img, (100, 50))
    exit_img = pygame.image.load("images and audio/exit_btn.png").convert_alpha()
    exit_img = pygame.transform.scale(exit_img, (100, 50))

    # create button instances
    start_button = Button(50, 200, 100, 50, "hi")
    exit_button = Button(350, 200, 100, 50, "hi")

    # Creating an instance of the Sounds class
    sounds = Sounds()

    # Toggle the music mute status
    sounds.toggle_music_mute()






    musicFlag = False
    run = True
    gameStart = False
    gameEnd = False
    myScore =0
    enemyScore = 0
    showTutorialScreen(win)
    introScreen(win,start_button,exit_button,start_img,exit_img)
    n = Network()#network
    p = n.getP()#player

    timer = Timer()
    timer.star_Timer()

    board_map = [[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
                 ]
    '''

    board_map = [[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
                 [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
                 ]

    board_map = [[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
                 ]



    '''
    board_width = 50
    board_height = 50
    board1 = Board(board_width, board_height, board_map)

    clock = pygame.time.Clock()

    ready_button = Button(0, 500, 100, 50, "Ready")
    client_ready = False

    while run:

        clock.tick(60)# fps=80
        p2=n.send(p)

        # colusion
        if p.rect.colliderect(p2.rect):

            if p.password == 1234:
                p.x, p.y = 0, (height - bottomheight - p.height) / 2


            if p.password==4321:
                p.x, p.y = width - p.width, (height - bottomheight - p.height) / 2

            # switch the colors of the two rectangles
            p.color, p2.color = p2.color, p.color
            p.update()
            p2.update()

        #scoring system
            if p.color == (255, 0, 0):
                enemyScore += 1

            if p2.color == (255, 0, 0):
                myScore += 1
                sounds.play_sound_point()


        # board borders
        if p.x > width - p.width:
            p.x = width - p.width
            p.update()
        if p.x < 0:
            p.x = 0
            p.update()
        if p.y > height-bottomheight - p.height:
            p.y = height-bottomheight - p.height
            p.update()
        if p.y < 0:
            p.y = 0
            p.update()


        lastX = p.x
        lastY = p.y

        lastX2 = p2.x
        lastY2 = p2.x
        if p.isReady and p2.isReady and p.connected and p2.connected:
            p.move()

        for i in range(len(board_map)):
            for j in range(len(board_map[0])):
                if board_map[i][j] == 1:
                    barrier2 = pygame.Rect(j * int(width/len(board_map)), i * int(((height-bottomheight)/len(board_map[0]))), board1.width, board1.height)
                    barriers.append(barrier2)

        for bar in barriers:
            if bar.colliderect(p.rect):
                p.x = lastX
                p.y = lastY
                p.update()

            if bar.colliderect(p2.rect):
                p2.x = lastX2
                p2.y = lastY2
                p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if p.isReady and p2.isReady and p.connected and p2.connected:
                timer.change_Timer(event)

            if timer.time_Up() and myScore<enemyScore:
                small_font = pygame.font.Font('freesansbold.ttf', 26)
                lose_text = small_font.render("You lost", True, (255, 255, 255))
                win.blit(lose_text, (50, 650))
                pygame.display.update()
                pygame.time.wait(3000)

            if timer.time_Up() and myScore>=enemyScore:
                small_font = pygame.font.Font('freesansbold.ttf', 26)
                win_text = small_font.render("You win", True, (255, 255, 255))
                win.blit(win_text, (50, 650))
                pygame.display.update()
                pygame.time.wait(3000)


            #game ends
            if timer.time_Up():
                gameEnd =True
                gameStart=False
                ready_button.color = (255,0,0)
                client_ready = False
                p.isReady = False
                p2.isReady= False
                timer.set_Timer()
                myScore = 0
                enemyScore = 0

                if p.password == 1234:
                    p.x, p.y = 0, (height - bottomheight - p.height) / 2
                    p.update()


                elif p.password == 4321:
                    p.x, p.y = width - p.width, (height - bottomheight - p.height) / 2
                    p.update()
                pygame.display.update()

            # button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ready_button.rect.collidepoint(event.pos) :
                    client_ready = True
                    ready_button.set_pressed()
                    p.isReady = True


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and mute_button.collidepoint(event.pos):#clicked the button
                    sounds.toggle_music_mute()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    gameStart=True
                    gameEnd = False



                    # Calling the play_sound() method
                    if musicFlag==False:
                        sounds.play_sound()
                        musicFlag=True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.rect.collidepoint(event.pos):
                    run = False
                    pygame.quit()


        if gameStart==True:
            redrawWindow(win, bg, blackBg, p, p2, board1, timer, ready_button, client_ready,myScore,enemyScore,mute_button_color,mute_button,muteImage,redCube,blackCube)
        if gameEnd == True:
            introScreen(win,start_button,exit_button,start_img,exit_img)

def introScreen(win,start_button,exit_button,start_img,exit_img):

    win.fill((202, 228, 241))
    start_button.draw(win)
    exit_button.draw(win)
    win.blit(start_img,(50,200))
    win.blit(exit_img,(350,200))
    pygame.display.update()



def redrawWindow(win, bg, blackBg, player, player2, board1, timer, ready_button, client_ready,myScore,enemyScore,mute_button_color,mute_button,muteImage,redCube,blackCube):
    small_font = pygame.font.Font('freesansbold.ttf', 26)
    win.fill((255, 255, 255))
    win.blit(bg, (0, 0))
    win.blit(blackBg, (0, 500))
    board1.draw(win)
    player.draw(win)
    player2.draw(win)
    pygame.draw.rect(win, mute_button_color, mute_button)
    win.blit(muteImage, (450, 500))

    # PRINT TIME
    timer_text = small_font.render(f"Game Ends in:{timer.text}", True, (255, 255, 255))
    win.blit(timer_text, (250, 650))

    myScore_text = small_font.render(f"your score is:{myScore}", True, (255, 255, 255))
    win.blit(myScore_text, (0, 560))

    enemyScore_text = small_font.render(f"enemy score is:{enemyScore}", True, (255, 255, 255))
    win.blit(enemyScore_text, (0, 600))

    if player.isReady and player2.isReady and not player2.connected:
        disconnected_text = small_font.render("player 2 disconnected", True, (255, 0, 0))
        win.blit(disconnected_text, (220, 560))


    if player.color == (255, 0, 0):
        win.blit(redCube, (player.x, player.y))
        cop_text = small_font.render("You are the cop", True, (0, 0, 255))
        win.blit(cop_text, (160, 510))
    else:
        win.blit(blackCube, (player.x, player.y))

    if player2.color == (255, 0, 0):
        win.blit(redCube, (player2.x, player2.y))
        prisoner_text = small_font.render("You are the prisoner", True, (255, 165, 0))
        win.blit(prisoner_text, (160, 510))
    else:
        win.blit(blackCube, (player2.x, player2.y))

    # Draw the ready button
    if client_ready:
        ready_button.text = "Ready!"
        ready_button.draw(win)
    else:
        ready_button.text = "Ready?"
        ready_button.draw(win)

    pygame.display.update()


def showTutorialScreen(win):
    """
    Displays a tutorial screen to guide new players.
    """
    tutorial_img = pygame.image.load("C:/Users/user 2017/OneDrive\Pictures/img/tutorialScreen.jpg")

    # Display the tutorial screen until the player closes it or presses a key
    tutorial_displayed = True
    while tutorial_displayed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                tutorial_displayed = False

        # Draw the tutorial image on the window
        win.blit(tutorial_img, (0, 0))
        pygame.display.update()
main()