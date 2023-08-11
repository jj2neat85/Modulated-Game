def view(window, background, bg_image, player, objects, offset_x):

    window.fill((255, 0, 255))

# Draw each background tile on the window
    for tile in background:
        print(tile)
        window.blit(bg_image, tile)

# Draw the player sprite
    #player.draw(window, offset_x)
        