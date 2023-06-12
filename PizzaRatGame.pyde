"""
Claudia Cheuk
Pizza Rat Game
"""

#set variables for moving rat, shirt, bottle, and pizza positions + directions
ratX = 100
ratY = 500
ratJump = 0

botX = 800
botY = 500
botDir = 50

shirtX = 1600
shirtY = 500
shirtDir = 50

pizzaX = 1400
pizzaY = 500
pizzaDir = 50

#game start
startMode = False

def setup():
    size(1200,800)
    rectMode(CENTER)
    textAlign(CENTER)
    frameRate(16)
    
    #load icons
    global rat, bot, shirt, pizza
    rat = loadImage("mouse.png")
    bot = loadImage("bottle.png")
    shirt = loadImage("shirt.png")
    pizza = loadImage("pizza.png")

def draw():
    global ratJump, ratX, ratY, botX, botY, shirtX, shirtY, botDir, shirtDir, startMode, pizzaX, pizzaY, pizzaDir
    
    #background and instructions
    background(255)
    adlery = createFont("Adlery-Pro-Blockletter-trial.ttf", 40)
    textFont(adlery)
    fill(0)
    text("Get the New York mouse to its pizza!", width/2, height/8)
    fill(255,0,0)
    text("Holiday Edition",width/2,height/8+50)
    fill(0,100,0)
    textSize(30)
    text("Press spacebar to start and hold to hop over hurdles!",width/2,height/8+120)
    
    #ground
    fill(100,82,59,90)
    noStroke()
    rect(width/2,700,width,200)
    
    #icons input
    image(rat,ratX,ratY,180,130)
    image(bot,botX,botY,150,120)
    image(shirt,shirtX,shirtY, 150,120)
    image(pizza,pizzaX,pizzaY,150,120)
    
    #gameplay
    if startMode:
        fill(0)
        text("Go!",width/2,height/2)
        #for ratY in range (height/2, 500):
        
        if ratJump == 0:
            ratY += 15
        if ratY > 500:
            ratY = 500
            
        botX -= botDir #bottle starts moving
        shirtX -= shirtDir #shirt starts moving
        
        if botX < -400:
            botX = 1200 #make the bottle come back out again once it disappears
            if pizzaX < 1400:
                botDir = 0
                botX = 1200 #stop showing bottles when pizza comes out
        if shirtX < 0:
            shirtX = 1600 #make the shirt come back out again once it disappears
            if pizzaX < 1200:
                shirtDir = 0 #stop showing shirts when pizza comes out
        if ((ratX == botX) or (ratX == shirtX)) and ratY > 400:
            startMode = False #fail if rat touches bottle or shirt
        if millis() > 15000:
            pizzaX -= pizzaDir #pizza comes out after around 15 seconds of gameplay
            if ratX == pizzaX or pizzaX <= 0: #stop the game if rat catches pizza or misses pizza
                startMode = False
    elif ((ratX == botX) or (ratX == shirtX)) and ratY > 400: #if rat touches shirt or bottle
        fill(255,0,0)
        text("Sorry :( Guess he'll have to stick to leftover crumbs...",width/2,height/2)
    elif ratX == pizzaX and ratY > 400: #if rat catches pizza
        fill(255,108,85)
        text("Congrats! Merry Christmas to the New York mouse!",width/2,height/2)
    elif pizzaX <= 0: #if rat misses pizza
        fill(255,0,0)
        text("Sorry, you missed it :( So close yet so far...",width/2,height/2)
   

def keyPressed():
    global startMode, ratJump, ratX, ratY, botX, botY, shirtX, shirtY
    if key == ' ':
        startMode = True #spacebar starts game
        ratJump = 150 #jump mechanism
        ratY -= ratJump #rat starts jumping
    
def keyReleased():
    global ratJump, ratX, ratY, botX, botY, shirtX, shirtY
    if key == ' ':
        ratJump = 0 #lands when key released
