"""CSC 161 Lab: Objects & Graphics

This program creates a GUI to draw a house.

Borja Rojo
Lab Section TR 2:00-3:15pm
Fall 2016
"""

import graphics


def main():
    # Create window
    window = graphics.GraphWin("Making a House", 600, 600)

    # Step 1: Draw the frame
    click1 = window.getMouse()
    click2 = window.getMouse()
    frame = graphics.Rectangle(click1, click2)
    frame.draw(window)

    # Step 2: Draw the door
    click3 = window.getMouse()

    houseWidth = click1.getX() - click2.getX()
    doorWidth = houseWidth / 5

    doorBottomRightX = click3.getX() - doorWidth / 2
    doorBottomRightY = click1.getY()
    doorBottomRight = graphics.Point(doorBottomRightX, doorBottomRightY)

    doorTopLeftX = click3.getX() + doorWidth / 2
    doorTopLeftY = click3.getY()
    doorTopLeft = graphics.Point(doorTopLeftX, doorTopLeftY)

    door = graphics.Rectangle(doorBottomRight, doorTopLeft)
    door.draw(window)

    # Step 4: Draw the window (fenetre is window in French)
    click4 = window.getMouse()
    fenetreWidth = doorWidth * 3 / 4

    fenetreBottomLeftX = click4.getX() - fenetreWidth / 2
    fenetreBottomLeftY = click4.getY() + fenetreWidth / 2
    fenetreBottomLeft = graphics.Point(fenetreBottomLeftX,
                                       fenetreBottomLeftY)

    fenetreTopRightX = click4.getX() + fenetreWidth / 2
    fenetreTopRightY = click4.getY() - fenetreWidth / 2
    fenetreTopRight = graphics.Point(fenetreTopRightX, fenetreTopRightY)

    fenetre = graphics.Rectangle(fenetreBottomLeft, fenetreTopRight)
    fenetre.draw(window)

    # Step 5: Draw the roof
    click5 = window.getMouse()
    rightSide = graphics.Line(graphics.Point(click1.getX(), click2.getY()),
                              click5)
    leftSide = graphics.Line(click5, click2)

    rightSide.draw(window)
    leftSide.draw(window)

    window.getMouse()

main()
