from gamelib import*

game = Game(750, 700, "Get Stream Sniped - Speedrun")

#Functions
def daisy_controls():
    daisy.draw()
    walk.draw()
    walk.x = daisy.x
    walk.y = daisy.y
    if (keys.Pressed[K_LEFT] or keys.Pressed[K_a] or
    keys.Pressed[K_RIGHT] or keys.Pressed[K_d] or
    keys.Pressed[K_UP] or keys.Pressed[K_w] or
    keys.Pressed[K_DOWN] or keys.Pressed[K_s]):
        walk.visible = True
        daisy.visible = False
    else:
        walk.visible = False
        daisy.visible = True
        
    if keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
        daisy.x -= 4

    if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
        daisy.x += 4

    if keys.Pressed[K_DOWN] or keys.Pressed[K_s]:
        daisy.y += 4

    if keys.Pressed[K_UP] or keys.Pressed[K_w]:
        daisy.y -= 4

def daisy_lr():
    daisy.draw()
    walk.draw()
    walk.x = daisy.x
    walk.y = daisy.y
    if (keys.Pressed[K_LEFT] or keys.Pressed[K_a] or
    keys.Pressed[K_RIGHT] or keys.Pressed[K_d]):
        walk.visible = True
        daisy.visible = False
    else:
        walk.visible = False
        daisy.visible = True
        
    if keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
        daisy.x -= 4

    if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
        daisy.x += 4

    if walk.visible == True:
        walking.setVolume(75)   
        walking.play()
    else:
        walking.setVolume(0)

def positionObjects(object):
    for i in range(len(object)):
        object[i].resizeBy(-25)
        x = randint(50,750)
        y = randint(100,5000)
        object[i].moveTo(x,-y)
        #s = randint(4,8)
        object[i].setSpeed(4,180)
        object[i].visible = True

def monster_move():
    monster.draw()
    if monster.y <= 100 and monster.x > 250:
        monster.x -= 10
        
    elif monster.x <= 250 and monster.y < 560:
        monster.y += 10

    elif monster.y >= 560 and monster.x < 500:
        monster.x += 10

    elif monster.x >= 500 and monster.y > 100:
        monster.y -= 10


#Main Program
daisy = Animation("Images/DaisyIdle.png", 19, game, 32, 608/19, 3)
daisy.resizeBy(400)
walk = Animation("Images/DaisyWalk.png", 8, game, 32, 256/8,3)
walk.resizeBy(400)

startup = Image("Images/Startupscreen.png", game)
startup.resizeBy(50)
game.setBackground(startup)

start1 = Animation("Images/start1.png", 2, game, 32,14, 12)
start1.resizeBy(1000)
start2 = Animation("Images/start2.png", 2, game, 32,15, 12)
start2.resizeBy(1000)
'''start1.collisionBorder = "rectangle"
start2.collisionBorder = "rectangle"'''

transition = Animation("Images/loading.png", 45, game, 32, 1440/45, 1)
transition.resizeBy(2250)

f = Font(white,30,gray,"Comic Sans")
g = Font(white,16,gray,"Comic Sans")
h = Font(white,11,gray,"Comic Sans")
t = Font(white,22,gray,"Comic Sans")
y = Font(white,40,gray,"Comic Sans")
e = Font(white,20,gray,"Comic Sans")
l = Font(red,30,red,"Comic Sans")
L = Font(red,50,red,"Comic Sans")

daisys = Animation("Images/daisysprites.png", 8, game, 64, 512/8,1)
daisys.resizeBy(600)
daisys.x = 200
daisys.y = 450

drd = Image("Images/roomday.png", game)
drd.resizeTo(game.width,game.height)
drn = Image("Images/roomnoon.png", game)
drn.resizeTo(game.width,game.height)
drnt = Image("images/roomnight.png",game)
drnt.resizeTo(game.width,game.height)

kitchen = Image("images/kitchen.png",game)
kitchen.resizeTo(game.width,game.height)

hallway = Image("images/hallway.png",game)
hallway.resizeTo(500,game.height)

lay = Image("images/lay.png",game)
lay.resizeBy(400)
lay.moveTo(50,325)

call = Sound("sounds/call.wav",0)
call.setVolume(60)
songbk = Sound("sounds/music.mp3",1)
walking = Sound("sounds/footsteps.wav",2)
music = Sound("Sounds/bgmusic.wav", 3)
scarymusic = Sound("Sounds/runmusic.mp3", 4)
emusic = Sound("Sounds/endingmusic.mp3", 5)
knocking = Sound("Sounds/knocking.mp3", 6)
harderknocking = Sound("Sounds/banging.mp3", 7)

mgbk = Image("images/mgbk.png",game)
mgbk.resizeTo(game.width,game.height)

hearts = []
for i in range(50):
    heart = Animation("images/heart.png", 3, game, 206/3, 61)
    hearts.append(heart)
positionObjects(hearts)

bhs = []
for i in range(25):
    broken = Animation("images/broken.png",11,game,13090/11,879)
    broken.resizeBy(-93)
    bhs.append(broken)
positionObjects(bhs)

bucket = Image("images/bucket.png",game)
bucket.resizeBy(200)

monster = Animation("images/monster.png",10,game,48,48)
monster.resizeBy(200)
jumpscare = Animation("images/jumpscare.png",8,game,1727/4,497/2,2)
jumpscare.resizeTo(game.width,game.height)

gun = Image("images/GUN.png",game)
bullet = Image("images/bullet.png",game)
bullet.visible = False
gunammo = Animation("images/bullets.png", 5, game, 320/5, 64)

bro = Image("images/bro.png",game)
bro.moveTo(340, 450)
bro.resizeBy(400)

pphole = Image("images/peephole.jpg",game)
pphole.resizeTo(game.width,game.height)

closet = Image("images/closet.png",game)
closet.resizeTo(game.width,game.height)

detect = Image("images/detect.png",game)
detect.resizeBy(200)

findmy = Image("images/findmy.png", game)
findmy.resizeTo(game.width, game.height)
findmy.resizeBy(-30)

key = Image("images/closetkey.png", game)
key.moveTo(520, 330)

end = Image("images/ending.png", game)
end.resizeTo(game.width, game.height)
end.resizeBy(-30)

title = Image("images/title.png",game)
title.resizeBy(1000)

#Start-up Screen        
while not game.over:
    game.processInput()
    startup.draw()
    start1.draw()
    start2.draw()

    if mouse.collidedWith(start1, "rectangle"):
        start2.visible = True
    else:
        start2.visible = False
    if start2.visible and mouse.collidedWith(start2, "rectangle") and mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    transition.draw()
    if transition.f >= 44:
        game.over = True
        transition.visible = False
        
    game.update(30)

game.over = False

#Bedroom
while not game.over:
    game.processInput()
    game.clearBackground("white")
    drd.draw()
    daisy_controls()
    game.drawText("Daisy is a cherished idol who adores her fans.",60,540,f)
    game.drawText("But among them is an obsessed one…",60,580,f)
    '''text1.moveTo(375,600)
    text1.draw()'''

    if daisy.y == 450:
        game.over = True
    
    game.update(30)

daisy.y = 0

game.over = False
#game.collisionBorder = "rectangle"

#Hallway
daisy.y = 0
daisy.resizeBy(-20)
walk.resizeBy(-20)
while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    daisy_controls()
    if keys.Pressed[K_UP] or keys.Pressed[K_w]:
        hallway.y += 2
    if keys.Pressed[K_DOWN] or keys.Pressed[K_s]:
        hallway.y -= 2

    if daisy.y <= 50:
        game.drawText("A fan that has been there since day one",215,200,g)

    if daisy.y <= 200:
        game.drawText("In the corner of the every stream she does,",210,300,g)
        game.drawText("but never comments",210,320,g)

    if daisy.y <= 350:
        game.drawText("But the least she could have done",210,420,g)
        game.drawText("was have a little bit of skepticism...",210,440,g)

    if daisy.y >= 450 and daisy.x == 375 or daisy.y >= 450 and daisy.x == 360 or daisy.y >= 500 and daisy.x == 365 or daisy.y >= 500 and daisy.x == 385:
        game.over = True

    game.update(30)

game.over = False

#Kitchen
daisy.resizeBy(150)
walk.resizeBy(150)
daisy.y = 475
while not game.over:
    game.processInput()
    game.clearBackground("white")
    kitchen.draw()
    daisy_controls()
    lay.draw()
    if lay.y > 200:
        game.drawText("Click to collect items",75,225,f)
    if lay.y > 200 and mouse.LeftClick and mouse.collidedWith(lay):
        lay.moveTo (50, 50)
        lay.resizeTo(100, 100)
    if daisy.y >= 550 and lay.y < 200:
        game.over = True
        
    game.update(30)

game.over = False

#Hallway 2
hallway.y = 300
daisy.y = 500
daisy.resizeBy(-60)
walk.resizeBy(-60)
lay.moveTo (50, 50)
lay.resizeTo(100, 100)

while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    lay.draw()
    daisy_controls()
    if keys.Pressed[K_s]:
        hallway.y -= 2
    if keys.Pressed[K_w]:
        hallway.y += 2
    if daisy.y <= 150 and daisy.x == 375 or daisy.y <= 150 and daisy.x == 360 or daisy.y <= 100 and daisy.x == 365 or daisy.y <= 100 and daisy.x == 385:
        game.over = True
        
    game.update(30)
    
game.over = False

#Bedroom Noon
daisy.resizeBy(65)
walk.resizeBy(65)
daisy.y = 400

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("Answer the call",500,15,f)
    daisy_controls()
    call.setVolume(80)
    call.play()
    if daisy.y <= 250 and daisy.x <= 250 or walk.y <= 250 and walk.x <= 250:
        game.over = True
    
    game.update(30)

game.over = False

#Call
while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Hello?'",325,550,t)
    call.setVolume(0)
    daisys.draw()
    if daisys.f >= 5:
        daisys.f = 5
    if mouse.LeftClick:
        game.over = True
    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Yea, Daisy? The stream is starting soon right?'",150,550,t)
    call.setVolume(0)
    if mouse.LeftClick:
        game.over = True

    game.update(30)    


game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Yea, its gonna start up soon'",325,550,t)
    call.setVolume(0)
    daisys.draw()
    if daisys.f >= 3:
        daisys.f = 3
    if mouse.LeftClick:
        game.over = True
    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Alr great! Im gonna get on in a few,'",150,550,t)
    game.drawText("'hope your first stream goes well!'",150,600,t)
    call.setVolume(0)
    if mouse.LeftClick:
        game.over = True
    game.update(30)


game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Awh thanks! Hope you have fun too. Bye'",300,550,t)
    call.setVolume(0)
    daisys.draw()
    if daisys.f >= 4:
        daisys.f = 4
    if mouse.LeftClick:
        game.over = True
    game.update(30)


game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Bye Daisy!-- *hang up*'",150,550,t)
    call.setVolume(0)
    if mouse.LeftClick:
        game.over = True
    game.update(30)


game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drn.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Im nervous but I think I've got this first stream...'",300,550,g)
    game.drawText("'My fans love me what am I worried about lol!'",300,600,g)
    call.setVolume(0)
    daisys.draw()
    if daisys.f >= 2:
        daisys.f = 2
    if mouse.LeftClick:
        game.over = True
    game.update(30)

while not game.over:
    game.processInput()
    transition.draw()
    game.drawText("'Stream start!'",375,200,f)
    if transition.f >= 44:
        game.over = True
        transition.visible = False
        
    game.update(30)

game.over = False

daisy.y = 485

#Minigame
while not game.over:
    game.processInput()
    game.clearBackground("white")
    mgbk.draw()
    daisy_lr()
    bucket.draw()

    bucket.y = daisy.y - 100
    bucket.x = daisy.x
    bucket.y = walk.y - 100
    bucket.x = walk.x

    game.drawText("Win the game to entertain the fans",10,10,t)
    game.drawText("by keeping a score over 200 at the end!",10,40,t)

    for i in range(len(hearts)):
        hearts[i].move()
        if hearts[i].collidedWith(daisy):
            game.score += 10
            hearts[i].visible = False
        game.drawText(game.score,10,650,f)

    for i in range(len(bhs)):
        bhs[i].move()
        if bhs[i].collidedWith(daisy):
            game.score -= 10
            bhs[i].visible = False

    if game.score >= 200:
        game.over = True

    game.update(30)
    
game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    transition.draw()
    if transition.f >= 44:
        game.over = True
        transition.visible = False
        
    game.update(30)

game.over = False

#Bedroom Night
daisy.moveTo (250, 250)
while not game.over:
    game.processInput()
    game.clearBackground("white")
    drnt.draw()
    lay.draw()
    daisy_controls()
    game.drawText("'Ughh... finally ended my stream... Why'd it go for 5 hours?'",300,550,g)
    call.setVolume(0)
    daisys.draw()
    if daisys.f >= 0:
        daisys.f = 0
    if mouse.LeftClick:
        game.over = True
        
    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drnt.draw()
    daisy_controls()
    game.drawText("'I need to get out of my room and stop being a chud already..'",300,550,g)
    daisys.draw()
    if daisys.f >= 6:
        daisys.f = 6
    if mouse.LeftClick:
        game.over = True
    game.update(30)


game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("white")
    drnt.draw()
    daisy_controls()
    game.drawText("Leave the room",500,15,f)
    if daisy.y == 450 or walk.y == 450:
        game.over = True
    game.update(30)

game.over = False


daisy.y = 0
daisy.resizeBy(-25)
walk.resizeBy(-25)
hallway.y = 400
while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    game.drawText("?",500, 15,f)
    daisy_controls()
    if keys.Pressed[K_s]:
        hallway.y -= 2
    if keys.Pressed[K_w]:
        hallway.y += 2
    if daisy.y <= 50:
        game.drawText("There's someone at the door",215,200,g)

    if daisy.x >= 520 and daisy.y <= 520:
        game.drawText("Look through keyhole? Left click", 350, 350, t)

    if mouse.LeftClick:
        game.over = True

    game.update(30)                                                                                                                                             

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()
    
    game.drawText("*knock knock knock*",250,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'Yo, Daisy are you home?'",300,100,t)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:

    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'Bro? What are you doing here!'",200,100,f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:

    game.processInput()

    game.clearBackground("black")

    pphole.draw()

    bro.draw()

    game.drawText("Daisy:'I thought you-'",200,100,f)

    if mouse.LeftClick:

        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'Shh shut up its cold out here, can you let me innn??'",0,100,f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)
    
game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'What?-'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'I SAID OPEN SESAME ALREADY'",50,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'Holy yap, calm down-'",200,100,f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'...'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'O-Oh my god!! Did you hurt your feet getting here..!?'",0,100,e)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'...'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'UHM'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'YES?'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("Daisy:'Omg hold on you need bandages!'",200,100,f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    pphole.draw()
    bro.draw()

    game.drawText("'WAIT-'",200,100,y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    game.drawText("Go 'find bandages'",400, 15,f)
    daisy_controls()

    if keys.Pressed[K_s]:
        hallway.y -= 2

    if keys.Pressed[K_w]:
        hallway.y += 2

    if daisy.y >= 350:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    findmy.draw()

    game.drawText("Im not that stupid", 230, 600, y)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    findmy.draw()

    game.drawText("Calling the police obviously.", 230, 600, f)

    game.drawText("But just incase...", 230, 650, f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()

    game.drawText("Find the closet key",400, 15,f)

    daisy_controls()

    if keys.Pressed[K_s]:
        hallway.y -= 2

    if keys.Pressed[K_w]:
        hallway.y += 2

    if daisy.y >= 500 and daisy.x == 375 or daisy.y >= 500 and daisy.x == 360 or daisy.y >= 500 and daisy.x == 365 or daisy.y >= 500 and daisy.x == 385:
        game.over = True

    game.update(30)

game.over = False

daisy.y = 475
daisy.resizeBy(80)
walk.resizeBy(80)

while not game.over:
    game.processInput()
    game.clearBackground("white")
    kitchen.draw()
    key.draw()
    daisy_controls()

    if key.y > 100:
        game.drawText("Find the closet key",400, 15,f)

    if key.y > 100 and mouse.LeftClick and mouse.collidedWith(key):
        key.moveTo (50, 50)

    if daisy.y >= 550:
        game.over = True

    game.update(30)

game.over = False

hallway.y = 300

daisy.y = 500
daisy.resizeBy(-50)
walk.resizeBy(-50)

key.moveTo (50, 50)

while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    key.draw()

    #print(mouse.x)
    #print(mouse.y)

    game.drawText("Unlock the closet",500,15,f)

    daisy_controls()

    if keys.Pressed[K_s]:
        hallway.y -= 2
        
    if keys.Pressed[K_w]:
        hallway.y += 2

    if daisy.x >= 520 and daisy.y <= 445:
        game.drawText("Unlock? *Left Click*", 350, 460, t)
        if mouse.LeftClick:
            game.over = True

    game.update(30)



game.over = False



gun.resizeBy(120)
gun.moveTo(270, 420)

while not game.over:
    game.processInput()
    game.clearBackground("black")
    closet.draw()
    gun.draw()

    game.drawText("Take the gun",400, 15,l)

    if mouse.LeftClick and mouse.collidedWith(gun):
        game.over = True

    game.update(30)



gun.visible = False
game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    closet.draw()

    if mouse.LeftClick and gun.visible == False:
        game.over = True

    game.update(30)



game.over = False



hallway.y = 300

daisy.moveTo(520, 445)
daisy.resizeBy(-10)
walk.resizeBy(-10)

monster.moveTo(100, 500)

daisy.ammo = 3

while not game.over:
    game.processInput()
    game.clearBackground("black")
    hallway.draw()
    #print(mouse.x)
    #print(mouse.y)
    bullet.draw()
    bullet.move()
    gun.draw()
    daisy_controls()
    monster_move()
    gunammo.draw()

    scarymusic.play(True, 0)

    gun.y = daisy.y
    gun.x = daisy.x + 50
    gun.y = walk.y
    gun.x = walk.x + 50

    game.drawText("KILL IT ",100,15,l)
    game.drawText("Left click to shoot",100,60,f)
    
    if daisy.ammo == 3:
        gunammo.f = 0
    if daisy.ammo == 2:
        gunammo.f = 1
    if daisy.ammo == 1:
        gunammo.f = 2
    if daisy.ammo == 0:
        gunammo.f = 4
        
                    
    if keys.Pressed[K_s]:
        hallway.y -= 2
    if keys.Pressed[K_w]:
        hallway.y += 2
        
    if mouse.LeftClick and bullet.visible == False and daisy.ammo >=1:
        bullet.visible = True
        bullet.moveTo(gun.x, gun.y)
        bullet.setSpeed(8, 270)
        #replace 270 with s
        #s = mouse.x,mouse.y
        daisy.ammo -= 1

    if bullet.visible == True:
        bullet.move()

    if bullet.x > game.width:
        bullet.visible = False
        bullet.moveTo(gun.x, gun.y)

    if bullet.collidedWith(monster):
        bullet.visible = False
        monster.visible = False
       
    elif daisy.collidedWith(monster) or walk.collidedWith(monster) or daisy.ammo == 0 and bullet.visible == False and monster.visible:
        game.clearBackground(black)
        jumpscare.visible = True
        jumpscare.draw()
        daisy.ammo = 0
        game.drawText("you dide", 290, 100, L)
        game.drawText("Press [SPACE] to retry!", 220, 400, l)
        if monster.y <= 100 and monster.x > 250:
            monster.x += 10
        
        elif monster.x <= 250 and monster.y < 560:
            monster.y -= 10

        elif monster.y >= 560 and monster.x < 500:
            monster.x -= 10

        elif monster.x >= 500 and monster.y > 100:
            monster.y += 10

            
        if keys.Pressed[K_LEFT] or keys.Pressed[K_a]:
            daisy.x += 5
            walking.setVolume(0)
        if keys.Pressed[K_RIGHT] or keys.Pressed[K_d]:
            daisy.x -= 5
            walking.setVolume(0)
        if keys.Pressed[K_DOWN] or keys.Pressed[K_s]:
            daisy.y -= 5
            walking.setVolume(0)
        if keys.Pressed[K_UP] or keys.Pressed[K_w]:
            daisy.y += 5
            walking.setVolume(0)
            
        if jumpscare.f >= 7:
            jumpscare.f = 1

            if jumpscare.f == 1 and not keys.Pressed[K_SPACE]:
                game.wait(K_SPACE)

                if keys.Pressed[K_SPACE]:
                    hallway.y = 300
                    daisy.moveTo(520, 300)
                    monster.moveTo(500, 100)
                    daisy.ammo = 3

                    jumpscare.f = 0
                    jumpscare.visible = False
                  
    if daisy.x >= 520 and daisy.y <= 220 and monster.visible == False:
        game.drawText("exit? - Leftclick", 350, 350, t)
        if mouse.LeftClick:
            game.over = True    
        
    game.update(30)

game.over = False

transition.f = 0

while not game.over:
    game.processInput()
    transition.draw()

    transition.f += 1
    
    if transition.f >= 44:
        game.over = True
        transition.visible = False
        
    game.update(30)

game.over = False

#Ending
scarymusic.setVolume(0)
emusic.play(True, 0)
emusic.setVolume(100)

while not game.over:
    game.processInput()
    game.clearBackground("black")
    end.draw()
    emusic.play(True, 0)
    
    game.drawText("Woaw you saved Daisy!.", 230, 600, f)

    game.drawText("She's so happy look at her", 230, 650, f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)
    
game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    end.draw()
    emusic.play(True, 0)

    game.drawText("After that day, Daisy stayed over at her brothers house", 100, 620, t)

    game.drawText("Until she got a new apartment, and job", 100, 650, f)

    if mouse.LeftClick:
        game.over = True

    game.update(30)

game.over = False

while not game.over:
    game.processInput()
    game.clearBackground("black")
    end.draw()
    emusic.play(True, 0)

    game.drawText("Good Job", 350, 610, y)
    game.drawText("Press [SPACE] to quit", 100, 650, t)

    if keys.Pressed[K_SPACE]:
        game.over = True

    game.update(30)
    
game.quit()
