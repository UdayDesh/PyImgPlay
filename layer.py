from PIL import Image
import numpy as np
import sys

def trans_paste(bg_img,fg_img,box=(0,0)):
    fg_img_trans = Image.new("RGBA",bg_img.size)
    fg_img_trans.paste(fg_img,box,mask=fg_img)
    new_img = Image.alpha_composite(bg_img,fg_img_trans)
    return new_img

def own_method():    
    bg_img = Image.open("cloud.png")
    fg_img = Image.open("coco.png")
    coco_box = (70,135,70+122,135+120)
    fg_img = fg_img.resize(fg_img.size,0,coco_box)
    fg_img.show()
    merged_img = trans_paste(bg_img,fg_img,(250,100))
    merged_img.show()
    img2=Image.open("frame.png")
    merged_img = trans_paste(merged_img,img2,(50,100))
    merged_img.show()
    img3=Image.open("car.png")
    s=img3.size
    img3=img3.resize((int(s[0]/4),int(s[1]/4)))
    merged_img = trans_paste(merged_img,img3,(170,270))
    merged_img.show()
    merged_img.save('Merged_own.png','PNG')

def bulk_method(set_of_files):    
    merged_img = Image.new("RGBA",(1000,1000))#Blank transparent image
    loc = 0
    for i in set_of_files:
        temp=Image.open(i).resize((150,150))
        merged_img = trans_paste(merged_img,temp,(loc,loc))
        loc = loc + 100
        merged_img.show()
    merged_img.save('MergedBulk.png','PNG')

if __name__ == "__main__":
    print(f"Number of Images: {len(sys.argv) - 1}")
    sof=list()
    for i, arg in enumerate(sys.argv):
        if (i == 0): continue
        print(f"File {i:>6}: {arg}")
        sof.append(arg)
    print(sof)
    print("Bulk method - placing images in given order")
    bulk_method(sof)
    print("Own method - placing images in order")
    own_method()
    
