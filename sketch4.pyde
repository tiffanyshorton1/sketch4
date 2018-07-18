def setup():
    size (600, 800)
    beyImage = loadImage("beyonce.jpg")
    image(beyImage, 0, 0)

    loadPixels()
    
    for i in range(len(pixels)):
        currentPixel = pixels [i]
        pixelRed = red (currentPixel)
        pixelGreen = green (currentPixel)
        pixelBlue = blue (currentPixel)
        range(pixelRed) = 
    
        


    updatePixels()
