#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "masperet-gabay-preview-v2.jpg"
W,H = 1200,630

def font(size):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    return ImageFont.truetype(p,size)

def write(draw,pt,value,size,fill,outline="#16365e",stroke=0):
    draw.text(pt,value,font=font(size),anchor="mm",direction="rtl",
              fill=fill,stroke_fill=outline,stroke_width=stroke)

def rounded(draw,rect,r,fill,outline=None,width=1):
    draw.rounded_rectangle(rect,radius=r,fill=fill,outline=outline,width=width)

def sticker(draw,rect,r,fill):
    x0,y0,x1,y1=rect
    rounded(draw,(x0+5,y0+8,x1+5,y1+8),r,"#1a5b81")
    rounded(draw,rect,r,fill,"#ffffff",8)
    rounded(draw,(x0+12,y0+10,x1-12,y0+17),5,"#ffffff8a")

def face(layer,name,cx,y,width):
    path=ROOT/"assets"/f"{name}-face.webp"
    if not path.is_file():
        raise FileNotFoundError(f"Original game character is required: {path}")
    pic=Image.open(path).convert("RGBA")
    scale=min(width/pic.width,width*1.04/pic.height)
    pic=pic.resize((round(pic.width*scale),round(pic.height*scale)),Image.Resampling.LANCZOS)
    shadow=Image.new("RGBA",pic.size,(16,48,82,0))
    shadow.putalpha(pic.getchannel("A").filter(ImageFilter.GaussianBlur(12)))
    px=round(cx-pic.width/2)
    layer.alpha_composite(shadow,(px+9,y+12))
    layer.alpha_composite(pic,(px,y))

def create():
    im=Image.new("RGB",(W,H))
    pixels=im.load()
    for y in range(H):
        for x in range(W):
            dist=((x-600)**2/1100000+(y-205)**2/400000)**.5
            pixels[x,y]=(min(255,int(35+35*min(1,dist)+.05*y)),
                         int(193+23*(1-min(1,dist))),
                         int(249-8*min(1,dist)))
    im=im.convert("RGBA");d=ImageDraw.Draw(im,"RGBA")
    cx,cy=600,235
    for i in range(20):
        a=i*math.pi/10
        d.polygon([(cx,cy),(cx+1400*math.cos(a-.045),cy+1400*math.sin(a-.045)),
                   (cx+1400*math.cos(a+.045),cy+1400*math.sin(a+.045))],
                  fill=(255,255,255,30))
    rng=random.Random(9)
    for _ in range(50):
        x,y=rng.randrange(22,1178),rng.randrange(20,535)
        if 330<x<880 and 66<y<380: continue
        d.ellipse((x,y,x+8,y+8),fill=rng.choice(["#ffffffaa","#ffcf47","#b8ffeb","#79dfff"]))
    for x in [8,1166]:
        rounded(d,(x,10,x+24,295),10,"#ffffff","#17486b",5)
        for y in range(28,283,39):
            d.polygon([(x+3,y+18),(x+21,y),(x+21,y+20),(x+3,y+38)],
                      fill="#e54758" if y%2 else "#2e93d0")
        d.ellipse((x-2,0,x+26,20),fill="#dce8f3",outline="#17486b",width=3)
    d.ellipse((39,57,379,399),fill="#ffffff",outline="#1463a0",width=11)
    d.ellipse((50,68,368,388),fill="#9beafe")
    d.ellipse((821,57,1161,399),fill="#ffffff",outline="#1463a0",width=11)
    d.ellipse((832,68,1150,388),fill="#fff0a7")
    rounded(d,(82,315,337,466),76,"#182b4b","#ffffff",7)
    rounded(d,(867,315,1118,466),78,"#19314f","#ffffff",7)
    d.polygon([(970,333),(998,333),(1007,432),(979,450),(958,433)],fill="#ee4855")
    d.polygon([(970,333),(986,357),(998,333)],fill="#ffffff")
    face(im,"avi",210,67,275)
    face(im,"koko",990,67,280)
    d=ImageDraw.Draw(im,"RGBA")
    sticker(d,(354,94,846,356),63,"#123b68")
    rounded(d,(380,115,820,336),46,"#102e58")
    write(d,(600,177),"מספרת",91,"#ffffff","#102d52",2)
    write(d,(600,284),"גבאי",121,"#ffd44b","#102d52",4)
    rounded(d,(452,345,749,358),7,"#ffffff")
    for x in range(459,735,28):
        d.polygon([(x,345),(x+10,345),(x+3,358),(x-7,358)],
                  fill="#eb4557" if (x//28)%2 else "#3289cd")
    tiles=[
       (58,372,410,522,"#a0f4cf","טמפל מספרה","RUN"),
       (424,372,776,522,"#ffe18a","אבן נייר ומספריים","RPS"),
       (790,372,1142,522,"#76d8ff","ציפור מספרה","FLAPPY")
    ]
    for j,(x0,y0,x1,y1,c,label,mini) in enumerate(tiles):
        sticker(d,(x0,y0,x1,y1),39,c)
        d.ellipse((x0+20,y0+23,x0+70,y0+73),fill="#ffffffb0")
        if j==0:
            d.ellipse((x0+34,y0+35,x0+57,y0+54),fill="#194e62")
            d.line((x0+65,y0+50,x0+80,y0+42),fill="#174965",width=7)
        elif j==1:
            d.ellipse((x0+27,y0+28,x0+59,y0+60),fill="#f2c2a0",outline="#174965",width=5)
            d.line((x0+41,y0+25,x0+41,y0+42),fill="#174965",width=5)
        else:
            d.ellipse((x0+28,y0+25,x0+65,y0+62),fill="#158bd0",outline="#174965",width=4)
            d.polygon([(x0+61,y0+43),(x0+77,y0+46),(x0+61,y0+53)],fill="#e6aa25")
        write(d,((x0+x1)//2,y0+44),mini,19,"#17516f")
        write(d,((x0+x1)//2,y0+108),label,35 if j!=1 else 28,"#14395c")
    rounded(d,(226,548,974,614),23,"#f54251","#ffffff",7)
    d.polygon([(226,570),(194,578),(225,598)],fill="#d42d44")
    d.polygon([(974,570),(1006,578),(975,598)],fill="#d42d44")
    write(d,(600,580),"העיקר הבריאות והתסרוקת",37,"#ffffff","#a52a41",1)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    im.convert("RGB").save(OUT,"JPEG",quality=87,optimize=True,subsampling=0)
    print(f"Created: {OUT} ({OUT.stat().st_size} bytes)")

if __name__=="__main__":
    create()
