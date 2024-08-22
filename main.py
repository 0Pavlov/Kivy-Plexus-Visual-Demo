# noinspection PyProtectedMember
from kivy.app import App, Builder
from kivy.clock import Clock
from kivy.properties import (
    ListProperty,
)
from kivy.uix.widget import Widget

Builder.load_string(
    """
<Particle>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Ellipse:
            size: self.size
            pos: self.pos
        Color:
            rgba: 1, 0, 0, .5
        Rectangle:
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
        self.particle = Particle()
        self.add_widget(self.particle)

    def update(self, dt: float) -> None:
        """Updates the screen."""
        pass


class Particle(Widget):
    """Represents the single particle.

    Attributes:
        size (ListProperty): Size of the particle in pixels.
    """
    size = ListProperty([20, 20])


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
