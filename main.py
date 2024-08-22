# noinspection PyProtectedMember
from kivy.app import App, Builder
from kivy.clock import Clock
from kivy.properties import (
    ListProperty,
    NumericProperty,
)
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from random import choice, randint

Builder.load_string(
    """
<Particle>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            size: self.size
            pos: self.pos
    """
)


class Plexus(Widget):
    """Main class for the demo.

    This class contains all the demo logic and serves as the root widget.
    """

    def __init__(self, **kwargs):
        """Initializes the Plexus instance.

        Does stuff on the app's startup.
        """
        super(Plexus, self).__init__(**kwargs)
        self.particles = []
        for _ in range(25):
            particle = Particle()
            # Assign random velocity
            particle.velocity_x = choice([-3, -2, -1, 1, 2, 3])
            particle.velocity_y = choice([-3, -2, -1, 1, 2, 3])
            # Assign random position
            particle.pos = [
                randint(0, 1000),
                randint(0, 1000)
            ]
            self.particles.append(particle)
            self.add_widget(particle)

    # noinspection PyUnusedLocal
    def update(self, dt: float) -> None:
        """Updates the screen."""
        for particle in self.particles:
            particle.move()

        self.canvas.after.clear()  # Clear previous lines
        with self.canvas.after:
            for i in range(len(self.particles)):
                for j in range(i + 1, len(self.particles)):
                    p1 = self.particles[i]
                    p2 = self.particles[j]
                    distance = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
                    connect_distance = 200
                    if distance < connect_distance:
                        line_width = 3 * (1 - distance / connect_distance)
                        Color(1, 1, 1, 0.3)
                        Line(
                            points=[p1.x + 10, p1.y + 10, p2.x + 10, p2.y + 10],
                            width=line_width
                        )


class Particle(Widget):
    """Represents the single particle.

    Attributes:
        size (ListProperty): Size of the particle in pixels.
        velocity_x (NumericProperty): Particle's x-axis velocity.
        velocity_y (NumericProperty): Particle's y-axis velocity.

    Methods:
        move(): Moves the particle and handles collisions with the parent's boundaries.
    """
    size = ListProperty([20, 20])
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self) -> None:
        """Moves the particle and handles collisions with the parent's boundaries.

        This method updates the particle's position based on its velocity.
        It then checks if the particle has collided with the edges of its parent
        widget. If a collision is detected, the particle's velocity is reversed
        to simulate bouncing behavior.
        """
        # Apply velocity
        self.pos[0] += self.velocity_x
        self.pos[1] += self.velocity_y

        # Bounce off sides
        if self.pos[0] < self.parent.x:
            self.velocity_x = abs(self.velocity_x)
        elif self.pos[0] + self.size[0] > self.parent.width:
            self.velocity_x = abs(self.velocity_x) * -1

        # Bounce off top and bottom
        if self.pos[1] < self.parent.y:
            self.velocity_y = abs(self.velocity_y)
        elif self.pos[1] + self.size[1] > self.parent.height:
            self.velocity_y = abs(self.velocity_y) * -1


class PlexusApp(App):
    """Main application class for the demo.

    This class is responsible for setting up the game window and initializing the demo
    logic. It inherits from Kivy's App class, which provides the main event loop and
    window management.

    Methods:
        build(): Initializes the demo by creating an instance of Plexus and scheduling
        its update method to be called at regular intervals.
    """

    def build(self) -> Plexus:
        """Builds the Plexus application.

        Initializes the demo and sets the update interval.

        Returns:
            Plexus: The demo instance. Root widget object.
        """
        root = Plexus()
        Clock.schedule_interval(root.update, 1.0 / 120.0)
        return root


if __name__ == '__main__':
    PlexusApp().run()
