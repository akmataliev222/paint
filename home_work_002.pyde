def cyrcle():
    ellipse(10, 10, 30, 30)

def setup():
    size(1000, 700)
    background(0, 0, 70)
    fill(255)
    rect(width * 0.081, height * 0.05, width * 0.89, height * 0.87) 

radiuse = 10    

clr = color(255, 0, 0)            
                                    
def draw():
    global clr
    if mouseButton == LEFT:
         
        if mouseX > width * 0.090 and mouseX < width * 0.980 and mouseY > height * 0.085 and mouseY < height * 0.9:
            noStroke()
            fill(clr)
            ellipse(mouseX, mouseY, radiuse, radiuse)
        if mouseX > width * 0.08 and mouseX < width * 0.08 + 25 and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(0, 255, 0)  
       
        if mouseX > width * 0.08 + 25 and mouseX < width * 0.08 + 25 * 2 and mouseY > height * 0.93 and mouseY + height * 0.93:
            clr = color(255, 0, 0)   
        
        if mouseX > width * 0.08 + 50 and mouseX < width * 0.08 + 25 * 3 and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(0, 0, 255 )   
    
        if mouseX > width * 0.08 + 75 and mouseX < width * 0.08 + 25 * 4  and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(180, 160, 210)   
    
        if mouseX > width * 0.08 + 100 and mouseX < width * 0.08 + 25 * 5  and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(84, 78, 77)   
      
        if mouseX > width * 0.08 + 125 and mouseX < width * 0.08 + 25 * 6  and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(125, 125, 10)   
       
        if mouseX > width * 0.08 + 150 and mouseX < width * 0.08 + 25 * 7  and mouseY > height * 0.93 and mouseY + height * 0.93 + 25:
            clr = color(125, 125, 130)   
        
        if mouseX > width * 0.08 and mouseX < width * 0.08 + 25 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(255, 255, 0)   
         
        if mouseX > width * 0.08 + 25  and mouseX < width * 0.08 + 25 * 2 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(255, 0, 190)   
          
        if mouseX > width * 0.08 + 50  and mouseX < width * 0.08 + 25 * 3 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(140, 0, 180)   
           
        if mouseX > width * 0.08 + 75  and mouseX < width * 0.08 + 25 * 4 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(140, 255, 180)   
                 
        if mouseX > width * 0.08 + 100  and mouseX < width * 0.08 + 25 * 5 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(0, 255, 255)    
        
        if mouseX > width * 0.08 + 125  and mouseX < width * 0.08 + 25 * 6 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(200, 170, 140)    
          
        if mouseX > width * 0.08 + 150  and mouseX < width * 0.08 + 25 * 7 and mouseY > height * 0.93 + 25 and mouseY + height * 0.93 + 25:
            clr = color(0, 0, 0)  
             
        if mouseX > width * 0.08 + 175  and mouseX < width * 0.08 + 25 * 8 and mouseY > height * 0.93 and mouseY + height * 0.93 :
            clr = color(255)  
          
        
         
         
         
    if key == "c" or key == "C":
        fill(255)
        rect(width * 0.081, height * 0.05, width * 0.89, height * 0.87)
    fill(0, 255, 0)
    rect(width * 0.08, height * 0.93, 20, 20)
    fill(255, 0, 0)
    rect(width * 0.08 + 25, height * 0.93, 20, 20)
    fill(0, 0, 255)
    rect(width * 0.08 + 25 + 25, height * 0.93, 20, 20)
    fill(180, 160, 210)
    rect(width * 0.08 + 25 * 3, height * 0.93, 20, 20)
    fill(84, 78, 77)
    rect(width * 0.08 + 25 * 4, height * 0.93, 20, 20)
    fill(125, 125, 10)
    rect(width * 0.08 + 25 * 5, height * 0.93, 20, 20)
    fill(125, 125, 130)
    rect(width * 0.08 + 25 * 6, height * 0.93, 20, 20)
    fill(255, 255, 0)
    rect(width * 0.08, height * 0.93 + 25, 20, 20)
    fill(255, 0, 190)
    rect(width * 0.08 + 25, height * 0.93 + 25, 20, 20)
    fill(140, 0, 180)
    rect(width * 0.08 + 25 + 25, height * 0.93 + 25, 20, 20)
    fill(140, 255, 180)
    rect(width * 0.08 + 25 + 25 + 25, height * 0.93 + 25, 20, 20)
    fill(0, 255, 255)
    rect(width * 0.08 + 25 * 4, height * 0.93 + 25, 20, 20)
    fill(200, 170, 140)
    rect(width * 0.08 + 25 * 5, height * 0.93 + 25, 20, 20)
    fill(0, 0, 0)
    rect(width * 0.08 + 25 * 6, height * 0.93 + 25, 20, 20)
    fill(255)
    rect(width * 0.08 + 25 * 7, height * 0.93, 50, 45)
    
    img = loadImage("01.png");
    image(img, 260, 655, 40, 40)   
 

    
def mouseWheel(event):
    global radiuse
    a = event.getCount()
    radiuse += a
    
    
