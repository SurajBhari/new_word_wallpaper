from calendar import c
from turtle import color
from PIL import Image,ImageFilter, ImageFont, ImageDraw 
from json import loads, dump
from random import randint, choice
import textwrap

height = 2400
width = 1080

number_of_images_to_render = 20
count = 0 


dictionary = {}
with open("dictionary.json", "r") as f:
    dictionary = loads(f.read())

print("Dictionary loaded")
print(len(dictionary.keys()))

while count<number_of_images_to_render:
    word = str(choice(list(dictionary.keys())))
    meaning = dictionary[word]
    del dictionary[word]
    if not meaning["MEANINGS"]: 
        continue
    if not meaning["SYNONYMS"]:
        continue
    if not meaning["ANTONYMS"]:
        continue
    
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    img = Image.new('RGB', (width, height), color = (r,g,b))
    # find complimentry color 
    tr, tg, tb = 255-r, 255-g, 255-b
    mea = meaning["MEANINGS"][list(meaning["MEANINGS"].keys())[0]]
    litreal_meaning = mea[1]
    noun_or_verb = mea[0]
    synonyms = "\n".join(meaning["SYNONYMS"])
    antonyms = "\n".join(meaning["ANTONYMS"])
    
    draw = ImageDraw.Draw(img) 
    #Render the word in center
    headfont = ImageFont.truetype(r'D:\global\Poppins-ExtraBold.ttf', 80) 
    otherfont = ImageFont.truetype(r'D:\global\Poppins-Regular.ttf', 60)
    x,y = ((width/2)-500, height/6)
    draw.text((x,y), word, font = headfont, fill=(tr,tg,tb)) 
    #Wrap the litreal_meaning
    y += 200
    draw.text((x,y), noun_or_verb, font = otherfont, fill=(tr,tg,tb)) 
    y += 100
    x+= 50
    # word wrap 
    for i in textwrap.wrap(litreal_meaning, width=30):
        draw.text((x,y), i, font = otherfont, fill=(tr,tg,tb)) 
        y += 100
    x-= 50
    if synonyms:
        y+=100
        draw.text((x,y), "S:", font = otherfont, fill=(tr,tg,tb))  
        x += 50
        y += 100 
        draw.text((x,y), synonyms, font = otherfont, fill=(tr,tg,tb))
        y += 100*len(synonyms.split("\n"))
        x -= 50
    if antonyms:
        y+=100
        draw.text((x,y), "A:", font = otherfont, fill=(tr,tg,tb))  
        x += 50
        y += 100 
        draw.text((x,y), antonyms, font = otherfont, fill=(tr,tg,tb))
        y += 100*len(antonyms.split("\n"))
        x -= 50
    
    count += 1
    print(count)
    with open(f"output/{word}.png", "wb") as f:
        img.save(f)
    