import arcade, math
from screeninfo import get_monitors

# Get the primary monitor's width and height
monitor = get_monitors()[0]
SCREEN_WIDTH = monitor.width
SCREEN_HEIGHT = monitor.height

SCREEN_TITLE = "3D snake"

class Circle:
    def __init__(self, tx, ty, size, color, speed, angle):
        self.x, self.y = 0, 0
        self.tx, self.ty = tx, ty
        self.size = size
        self.color = color
        self.speed = speed
        self.angle = angle

    def draw(self):
        
        # Moving squares smoothly
        self.x += (self.tx - self.x) / self.speed
        self.y += (self.ty - self.y) / self.speed

        # Drawing squares
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color, self.angle)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
        self.colors = [(255, 0  , 0  ), # Red
                  (0  , 255, 0  ), # Green
                  (0  , 0  , 255), # Blue
                  (255, 255, 0  ), # Yellow
                  (0  , 255, 255), # Cyan
                  (255, 0  , 255), # Magenta
                  (255, 165, 0  ), # Orange
                  (128, 0  , 128), # Purple
                  (255, 192, 203), # Pink
                  (165, 42 , 42 )  # Brown
        ]
        self.color = self.colors[0]
        self.mousex = 0
        self.mousey = 0
        self.worm = [Circle(0, 300, 40, arcade.color.BLACK, 1, 0)]
        for i in range(1, 101):
            size = 50 - i % 15
            color = (self.color[0]/i, self.color[1]/i, self.color[2]/i)
            speed = i / 1.5
            self.worm.append(Circle(0, 300, size, color, speed, 0))
        self.speedx, self.speedy = 1, 1

    def on_draw(self):
        arcade.start_render()

        # Moving the worm
        count = 5
        for segment in self.worm[::-1]:
            
            # updating the color
            segment.color = (self.color[0] / ((count % 15)+1),
                             self.color[1] / ((count % 15)+1),
                             self.color[2] / ((count % 15)+1)
            )
            count += 1

            # Rotating the worm based on its speed
            dist_x = self.mousex - segment.tx
            dist_y = self.mousey - segment.ty
            distance = math.sqrt(dist_x**2 + dist_y**2)
            if distance > 0:
                segment.angle -= (distance / 150) / 3

            # Making the mouse position as the worm's target
            segment.tx += dist_x / 50
            segment.ty += dist_y / 50
            segment.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mousex = x
        self.mousey = y

    def on_key_press(self, key, modifiers):
        if   key == arcade.key.KEY_1: self.color = self.colors[0]
        elif key == arcade.key.KEY_2: self.color = self.colors[1]
        elif key == arcade.key.KEY_3: self.color = self.colors[2]
        elif key == arcade.key.KEY_4: self.color = self.colors[3]
        elif key == arcade.key.KEY_5: self.color = self.colors[4]
        elif key == arcade.key.KEY_6: self.color = self.colors[5]
        elif key == arcade.key.KEY_7: self.color = self.colors[6]
        elif key == arcade.key.KEY_8: self.color = self.colors[7]
        elif key == arcade.key.KEY_9: self.color = self.colors[8]
        elif key == arcade.key.KEY_0: self.color = self.colors[9]

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
