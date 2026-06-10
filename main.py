from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from random import randint

Window.size = (360, 640)
Window.clearcolor = (0, 0, 0, 1)

CELL = 20
W, H = 360, 640


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.reset()

        Window.bind(on_touch_move=self.on_touch_move)
        Clock.schedule_interval(self.update, 0.12)

    def reset(self):
        self.snake = [(160, 300)]
        self.direction = (CELL, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        return (
            randint(0, (W // CELL) - 1) * CELL,
            randint(0, (H // CELL) - 1) * CELL
        )

    def on_touch_move(self, window, touch):
        if self.game_over:
            return

        dx, dy = touch.dx, touch.dy

        if abs(dx) > abs(dy):
            if dx > 0:
                self.direction = (CELL, 0)
            else:
                self.direction = (-CELL, 0)
        else:
            if dy > 0:
                self.direction = (0, CELL)
            else:
                self.direction = (0, -CELL)

    def update(self, dt):
        if self.game_over:
            return

        x, y = self.snake[0]
        dx, dy = self.direction
        new_head = (x + dx, y + dy)

        # đụng tường
        if new_head[0] < 0 or new_head[0] >= W or new_head[1] < 0 or new_head[1] >= H:
            self.game_over = True
            return

        # đụng thân
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()

        self.draw()

    def draw(self):
        self.canvas.clear()

        with self.canvas:
            # food
            Color(1, 0, 0)
            Rectangle(pos=self.food, size=(CELL, CELL))

            # snake
            Color(0, 1, 0)
            for part in self.snake:
                Rectangle(pos=part, size=(CELL, CELL))


class SnakeApp(App):
    def build(self):
        return SnakeGame()


SnakeApp().run()
