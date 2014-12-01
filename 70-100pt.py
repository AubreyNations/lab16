# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='#BFF5ED')
rocket1 = drawpad.create_rectangle(400,585,405,590, fill="black")
player = drawpad.create_oval(390,580,410,600, fill="#35B0FC", outline="#35B0FC")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red", outline="red")
rocket1Fired = False

direction = 5
direction2 = -1


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        
    
    
    def animate(self):
        global drawpad
        global enemy
        global direction2
        global direction
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)

        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        
        if rocket1Fired == True:
            drawpad.move(rocket1, 0, -10)
        if self.collisionDetect() == True:
            drawpad.delete(enemy)
        if ry2<0:
            rocket1Fired = False
            drawpad.move(rocket1, (px1-rx1), (py1-ry1))
            self.rockets = (self.rockets) - 1
            self.rocketsTxt.configure(text=self.rockets)
        drawpad.after(10,self.animate)

    def key(self, event):
        global player
        global drawpad
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(player)
        
        if event.char == " ":
            rocket1Fired = True
        if event.char == "w":
            if y1>0:
                drawpad.move(player,0,-20)
                drawpad.move(rocket1,0,-20)
        elif event.char == "d":
            if x2<800:
                drawpad.move(player,20,0)
                drawpad.move(rocket1,20,0)
        elif event.char == "a":
            if x1>0:
                drawpad.move(player,-20,0)
                drawpad.move(rocket1,-20,0)
        elif event.char == "s":
            if y2<600:
                drawpad.move(player,0,20)
                drawpad.move(rocket1,0,20)
            
    
    def collisionDetect(self):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if (rx1>=x1 and rx2<=x2) and (ry1>=y1 and ry2<=y2):
            return True
        else:
            return False
app = myApp(root)
root.mainloop()