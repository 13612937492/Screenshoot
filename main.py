import pyautogui
from PIL import ImageGrab

image = ImageGrab.grab(bbox=(0,0,700,800))
image.save('sc.png')