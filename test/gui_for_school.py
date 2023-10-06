import pygame
import sys
import logic


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (200, 200, 200)
BUTTON_TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LocalBank")

# Load a font
font = pygame.font.Font(None, FONT_SIZE)


# Define button properties
buttons = [
    {
        "text": "Login",
        "x": 0,
        "y": 0,
        "rect": None,
        "hovered": False,
        "pressed": False,
    },
    {
        "text": "Register",
        "x": 0,
        "y": 100,
        "rect": None,
        "hovered": False,
        "pressed": False,
    },
    {
        "text": "Exit",
        "x": 0,
        "y": 200,
        "rect": None,
        "hovered": False,
        "pressed": False,
    },
]


     
# Create button rectangles
for button in buttons:
    button["rect"] = pygame.Rect(button["x"], button["y"], BUTTON_WIDTH, BUTTON_HEIGHT)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over any of the buttons
            for button in buttons:
                if button["rect"].collidepoint(event.pos):
                    button["hovered"] = True
                else:
                    button["hovered"] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is over any of the buttons and the left mouse button is pressed
            for button in buttons:
                if button["rect"].collidepoint(event.pos) and event.button == 1:
                    button["pressed"] = True
                    #print(f"Button clicked: {button['text']}")
                    #buttons functions
                    if button["text"] == "Login":
                        logic.login()
                    elif button["text"] == "Register":
                        logic.registration()
                    elif button["text"] == "Exit":
                        exit()
            

    # Clear the screen
    screen.fill((180, 180, 180))

    # Draw the buttons
    for button in buttons:
        if button["hovered"]:
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button["rect"])
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, button["rect"])

        # Draw the button text
        text = font.render(button["text"], True, BUTTON_TEXT_COLOR)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()