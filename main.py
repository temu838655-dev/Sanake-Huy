        from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ListProperty
from random import randint
from kivy.core.window import Window

class SnakeGame(Widget):
    snake = ListProperty([(10, 10), (10, 11), (10, 12)])
    food = ListProperty([5, 5])
    direction = ListProperty([0, 1])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.2)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up' and self.direction != [0, -1]: self.direction = [0, 1]
        elif keycode[1] == 'down' and self.direction != [0, 1]: self.direction = [0, -1]
        elif keycode[1] == 'left' and self.direction != [1, 0]: self.direction = [-1, 0]
        elif keycode[1] == 'right' and self.direction != [-1, 0]: self.direction = [1, 0]
        return True

    def update(self, dt):
        new_head = (self.snake[-1][0] + self.direction[0], self.snake[-1][1] + self.direction[1])
        if new_head == tuple(self.food):
            self.food = [randint(0, 19), randint(0, 19)]
        else:
            self.snake.pop(0)
        self.snake.append(new_head)

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == '__main__':
    SnakeApp().run()
    
