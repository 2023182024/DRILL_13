from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}
    GROUND_Y = 30
    GRAVITY = 0.65
    BOUNCE_SPEED = 11

    def __init__(self, x, y, velocity, ball_type=1):
        if ball_type not in Ball.images:
            image_name = 'ball21x21.png' if ball_type == 1 else 'ball41x41.png'
            Ball.images[ball_type] = load_image(image_name)
        self.x, self.y = x, y
        self.velocity = velocity
        self.vertical_velocity = 0
        self.image = Ball.images[ball_type]
        self.radius = self.image.w // 2

    def update(self):
        self.x += self.velocity
        self.vertical_velocity -= self.GRAVITY
        self.y += self.vertical_velocity

        # Fireballs bounce off the ground instead of disappearing below it.
        ground_y = self.GROUND_Y + self.radius
        if self.y <= ground_y:
            self.y = ground_y
            self.vertical_velocity = self.BOUNCE_SPEED

        if self.x < -self.radius or self.x > get_canvas_width() + self.radius:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
