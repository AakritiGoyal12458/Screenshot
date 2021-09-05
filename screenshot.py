#taking screenshot with python
##1st black n white
##2nd coloured


##we need pyautogui
##so pip install pyautogui
##ImageGrab:black and white always
##for coloured (r,g,b - red , green , blue ) 0,0,0 to 255,255,255


import time
from PIL import Image,ImageGrab


def takescreenshot():#make a function
    image=ImageGrab.grab()
    image.show()
    return image

if __name__=="__main__":
    time.sleep(3)
    
    image=takescreenshot()
    data=image.load()
    print(data)
    #make  image colourfull from 0 to 255

    for i in range(35,56):
        for j in range(0,255):
            data
        
    

