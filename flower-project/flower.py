from graphics import graphics

flower_color = "purple"

def main():
    print("Let's draw a flower!")
    myCanvas = graphics(500, 500, "Flower")
    # grass
    myCanvas.rectangle(0, 400, 500, 100, "green")
    # sky
    myCanvas.rectangle(0, 0, 500, 400, "light blue")
    # straw
    myCanvas.line(250, 200, 250, 450, "dark green", 5)
    # leafs
    myCanvas.triangle(250, 150, 250, 250, 400, 200, flower_color)
    myCanvas.triangle(250, 150, 250, 250, 100, 200, flower_color)
    myCanvas.triangle(300, 200, 200, 200, 250, 50, flower_color)
    myCanvas.triangle(300, 200, 200, 200, 250, 350, flower_color)
    # flower middle
    myCanvas.ellipse(250, 200, 75, 75, "orange")
    # all done, now draw it all
    myCanvas.draw()

main()