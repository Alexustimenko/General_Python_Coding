from PIL import Image,ImageFilter
filecat="img_1.png"
with Image.open(filecat) as imgcat:
    imgcat.load()
imgcat=imgcat.crop((800,0,1650,1281))
imgcat.show()
imgcatgrey=imgcat.convert("L")
imgcatgrey.show()
threshold=57
imgcattreshold=imgcatgrey.point(lambda x: 255 if x>threshold else 0)
imgcattreshold.show()
r,g,b=imgcat.split()
r.show()
g.show()
b.show()
imgcattreshold=b.point(lambda x:255 if x>threshold else 0)
imgcattreshold=imgcattreshold.convert("1")
imgcattreshold.show()
def erode(cycles,image):
    for _ in range(cycles):
        image=image.filter(ImageFilter.MinFilter(3))
    return image
def dilate(cycles,image):
    for _ in range(cycles):
        image=image.filter(ImageFilter.MaxFilter(3))
    return image
step1=erode(12,imgcattreshold)
step1.show()
step2=dilate(58,step1)
step2.show()
catmask=erode(45,step2)
catmask.show()
catmask=catmask.convert("L")
catmask=catmask.filter(ImageFilter.BoxBlur(20))
catmask.show()
blank=imgcat.point(lambda _:0)
catseg=Image.composite(imgcat,blank,catmask)
catseg.show()
filename_monastery = "img_2.png"
with Image.open(filename_monastery) as img_monastery:
    img_monastery.load()

img_monastery.paste(
    imgcat.resize((imgcat.width // 10, imgcat.height // 10)),
    (1300, 750),
    catmask.resize((catmask.width // 10, catmask.height // 10)),
)

img_monastery.show()