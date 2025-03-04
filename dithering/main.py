import numpy as np
import pygame

TITLE = "Floyd Steinberg dithering"

running = False

screen = None

new_image = None

def round_color(frag, factor):
    return round(factor * frag / 255) * (255/factor)


def setup():
    global running
    global screen
    global new_image

    # Paste image path here
    image_name = "private_nab_mus.png"
    image = pygame.image.load("img/" + image_name)
    w, h = image.get_size()
    scale = 1
    
    image = pygame.transform.scale(image, (w * scale, h * scale))

    image_width, image_height = image.get_size()

    screen = pygame.display.set_mode((image_width * 2, image_height))
    pygame.display.set_caption(TITLE)
    running = True

    screen.blit(image, (0,0))
    pygame.display.flip()

    image = pygame.transform.grayscale(image)
    new_image = pygame.Surface((w * scale,h * scale))

    print("Processing...")
    for y in range(image_height - 1):
        for x in range(1, image_width - 1):
            color = image.get_at((x, y))

            old_r, old_g, old_b, a = color

            new_r = round_color(old_r, 2)
            new_g = round_color(old_g, 2)
            new_b = round_color(old_b, 2)

            new_image.set_at((x, y), (new_r,new_g,new_b,a))

            err_r = old_r - new_r
            err_g = old_g - new_g
            err_b = old_b - new_b
            err_color = (err_r, err_g, err_b, 0)

            for dx, dy, factor in [(1, 0, 7/16), (-1, 1, 3/16), (0, 1, 5/16), (1, 1, 1/16)]:
                c = image.get_at((x + dx, y + dy))
                new_c = np.add(c, np.multiply(err_color, factor))
                
                # Convertir en valeurs valides et entières
                new_c = tuple(int(min(max(c, 0), 255)) for c in new_c)
                new_image.set_at((x + dx, y + dy), new_c)  # Garder la composante alpha inchangée
        screen.blit(new_image, (image_width, 0))
        pygame.display.flip()
    print("Job done.")

def check_inputs():
    global running 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in {pygame.K_ESCAPE, pygame.K_q}:
                running = False


def main():
    setup()

    while running:
        check_inputs()
    
    response = input("Save newly processed image ? (y/n): ")

    if response == "y":
        name = input("Give a name to the file (no extension)\nName : ")
        pygame.image.save(new_image, name + ".png")
    else:
        print("OK")

if __name__ == '__main__':
    main()
