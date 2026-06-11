from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from random import randint

GRID = 20
SIZE = 20

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.direction = (0, 1)
        self.food = (5, 5)

        Clock.schedule_interval(self.update, 0.2)
        self.bind(pos=self.redraw, size=self.redraw)

    def on_touch_down(self, touch):
        x, y = touch.pos
        if x < self.width / 2:
            self.direction = (-1, 0)
        else:
            self.direction = (1, 0)

    def update(self, dt):
        hx, hy = self.snake[-1]
        dx, dy = self.direction

        new_head = (hx + dx, hy + dy)

        # ăn food
        if new_head == self.food:
            self.food = (randint(0, 19), randint(0, 19))
        else:
            self.snake.pop(0)

        # game over đơn giản
        if new_head in self.snake:
            self.snake = [(10, 10), (10, 11), (10, 12)]

        self.snake.append(new_head)
        self.redraw()

    def redraw(self, *args):
        self.canvas.clear()

        with self.canvas:
            # food
            Color(1, 0, 0)
            Rectangle(pos=(self.food[0]*SIZE, self.food[1]*SIZE), size=(SIZE, SIZE))

            # snake
            Color(0, 1, 0)
            for x, y in self.snake:
                Rectangle(pos=(x*SIZE, y*SIZE), size=(SIZE, SIZE))


class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == "__main__":
    SnakeApp().run()