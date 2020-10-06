from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import (
    SpecificBackgroundColorBehavior,
    RectangularElevationBehavior,
)
from kivy.properties import (
    ListProperty,
    StringProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.core.window import Window
from kivy.clock import Clock

from kivymd.uix.button import MDIconButton, MDFloatingActionButton

class MDActionBottomAppBarButton(MDFloatingActionButton):
    _scale_x = NumericProperty(1)
    _scale_y = NumericProperty(1)


class Header(
    ThemableBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    """
    :Events:
        `on_action_button`
            Method for the button used for the :class:`~MDBottomAppBar` class.
    """

    left_action_items = ListProperty()
    """The icons on the left of the toolbar.
    To add one, append a list like the following:

    .. code-block:: kv

        left_action_items: [`'icon_name'`, callback]

    where `'icon_name'` is a string that corresponds to an icon definition and
    ``callback`` is the function called on a touch release event.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """The icons on the left of the toolbar.
    Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """Text toolbar.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    md_bg_color = ListProperty([0, 0, 0, 0])
    """Color toolbar.
    
    :attr:`md_bg_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    anchor_title = StringProperty("left")

    mode = OptionProperty(
        "center", options=["free-end", "free-center", "end", "center"]
    )
    """Floating button position. Onle for :class:`~MDBottomAppBar` class.
    Available options are: `'free-end'`, `'free-center'`, `'end'`, `'center'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    round = NumericProperty("10dp")
    """
    Rounding the corners at the notch for a button.
    Onle for :class:`~MDBottomAppBar` class.

    :attr:`round` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'10dp'`.
    """

    icon = StringProperty("android")
    """
    Floating button. Onle for :class:`~MDBottomAppBar` class.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ListProperty()
    """
    Color action button. Onle for :class:`~MDBottomAppBar` class.

    :attr:`icon_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    type = OptionProperty("top", options=["top", "bottom"])
    """
    When using the :class:`~MDBottomAppBar` class, the parameter ``type``
    must be set to `'bottom'`:

    .. code-block:: kv

        MDBottomAppBar:

            MDToolbar:
                type: "bottom"
    
    Available options are: `'top'`, `'bottom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    #bg_color = get_color_from_hex('3AB054')

    _shift = NumericProperty("3.5dp")
    _angle_start = NumericProperty(90)
    _angle_end = NumericProperty(270)

    def __init__(self, **kwargs):
        self.action_button = MDActionBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")
        self.action_button.bind(
            on_release=lambda x: self.dispatch("on_action_button")
        )
        self.action_button.x = Window.width / 2 - self.action_button.width / 2
        self.action_button.y = (
            (self.center[1] - self.height / 2)
            + self.theme_cls.standard_increment / 2
            + self._shift
        )
        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color
        Window.bind(on_resize=self._on_resize)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )

    def on_action_button(self, *args):
        pass

    def on_md_bg_color(self, instance, value):
        if self.type == "bottom":
            self.md_bg_color = [0, 0, 0, 0]

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def on_right_action_items(self, instance, value):
        self.update_action_bar(self.ids["right_actions"], value)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            action_bar.add_widget(
                MDIconButton(
                    icon=item[0],
                    on_release=item[1],
                    opposite_colors=True,
                    text_color=self.specific_text_color,
                    theme_text_color="Custom",
                )
            )
        action_bar.width = new_width

    def update_action_bar_text_colors(self, instance, value):
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
        for child in self.ids["right_actions"].children:
            child.text_color = self.specific_text_color

    def _on_resize(self, instance, width, height):
        if self.mode == "center":
            self.action_button.x = width / 2 - self.action_button.width / 2
        else:
            self.action_button.x = width - self.action_button.width * 2

    def on_icon(self, instance, value):
        self.action_button.icon = value

    def on_icon_color(self, instance, value):
        self.action_button.md_bg_color = value

    def on_mode(self, instance, value):
        def set_button_pos(*args):
            self.action_button.x = x
            self.action_button.y = y
            self.action_button._hard_shadow_size = (0, 0)
            self.action_button._soft_shadow_size = (0, 0)
            anim = Animation(_scale_x=1, _scale_y=1, d=0.05)
            anim.bind(on_complete=self.set_shadow)
            anim.start(self.action_button)

        if value == "center":
            self.set_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
        elif value == "end":

            self.set_notch()
            x = Window.width - self.action_button.width * 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
            self.right_action_items = []
        elif value == "free-end":
            self.remove_notch()
            x = Window.width - self.action_button.width - dp(10)
            y = self.action_button.height + self.action_button.height / 2
        elif value == "free-center":
            self.remove_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = self.action_button.height + self.action_button.height / 2
        self.remove_shadow()
        anim = Animation(_scale_x=0, _scale_y=0, d=0.05)
        anim.bind(on_complete=set_button_pos)
        anim.start(self.action_button)

    def remove_notch(self):
        self._angle_start = 0
        self._angle_end = 0
        self.round = 0
        self._shift = 0

    def set_notch(self):
        self._angle_start = 90
        self._angle_end = 270
        self.round = dp(10)
        self._shift = dp(3.5)

    def remove_shadow(self):
        self.action_button._hard_shadow_size = (0, 0)
        self.action_button._soft_shadow_size = (0, 0)

    def set_shadow(self, *args):
        self.action_button._hard_shadow_size = (dp(112), dp(112))
        self.action_button._soft_shadow_size = (dp(112), dp(112))

class HeaderWithIcon(
    ThemableBehavior,
    RectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
    BoxLayout,
):
    """
    :Events:
        `on_action_button`
            Method for the button used for the :class:`~MDBottomAppBar` class.
    """

    left_action_items = ListProperty()
    """The icons on the left of the toolbar.
    To add one, append a list like the following:

    .. code-block:: kv

        left_action_items: [`'icon_name'`, callback]

    where `'icon_name'` is a string that corresponds to an icon definition and
    ``callback`` is the function called on a touch release event.

    :attr:`left_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    right_action_items = ListProperty()
    """The icons on the left of the toolbar.
    Works the same way as :attr:`left_action_items`.

    :attr:`right_action_items` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title = StringProperty()
    """Text toolbar.

    :attr:`title` is an :class:`~kivy.properties.StringProperty`
    and defaults to `''`.
    """

    md_bg_color = ListProperty([0, 0, 0, 0])
    """Color toolbar.
    
    :attr:`md_bg_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[0, 0, 0, 0]`.
    """

    anchor_title = StringProperty("left")

    mode = OptionProperty(
        "center", options=["free-end", "free-center", "end", "center"]
    )
    """Floating button position. Onle for :class:`~MDBottomAppBar` class.
    Available options are: `'free-end'`, `'free-center'`, `'end'`, `'center'`.

    :attr:`mode` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'center'`.
    """

    round = NumericProperty("10dp")
    """
    Rounding the corners at the notch for a button.
    Onle for :class:`~MDBottomAppBar` class.

    :attr:`round` is an :class:`~kivy.properties.NumericProperty`
    and defaults to `'10dp'`.
    """

    icon = StringProperty("android")
    """
    Floating button. Onle for :class:`~MDBottomAppBar` class.

    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `'android'`.
    """

    icon_color = ListProperty()
    """
    Color action button. Onle for :class:`~MDBottomAppBar` class.

    :attr:`icon_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    type = OptionProperty("top", options=["top", "bottom"])
    """
    When using the :class:`~MDBottomAppBar` class, the parameter ``type``
    must be set to `'bottom'`:

    .. code-block:: kv

        MDBottomAppBar:

            MDToolbar:
                type: "bottom"
    
    Available options are: `'top'`, `'bottom'`.

    :attr:`type` is an :class:`~kivy.properties.OptionProperty`
    and defaults to `'top'`.
    """

    #bg_color = get_color_from_hex('3AB054')

    _shift = NumericProperty("3.5dp")
    _angle_start = NumericProperty(90)
    _angle_end = NumericProperty(270)

    def __init__(self, **kwargs):
        self.action_button = MDActionBottomAppBarButton()
        super().__init__(**kwargs)
        self.register_event_type("on_action_button")
        self.action_button.bind(
            on_release=lambda x: self.dispatch("on_action_button")
        )
        self.action_button.x = Window.width / 2 - self.action_button.width / 2
        self.action_button.y = (
            (self.center[1] - self.height / 2)
            + self.theme_cls.standard_increment / 2
            + self._shift
        )
        if not self.icon_color:
            self.icon_color = self.theme_cls.primary_color
        Window.bind(on_resize=self._on_resize)
        self.bind(specific_text_color=self.update_action_bar_text_colors)
        Clock.schedule_once(
            lambda x: self.on_left_action_items(0, self.left_action_items)
        )
        Clock.schedule_once(
            lambda x: self.on_right_action_items(0, self.right_action_items)
        )

    def on_action_button(self, *args):
        pass

    def on_md_bg_color(self, instance, value):
        if self.type == "bottom":
            self.md_bg_color = [0, 0, 0, 0]

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def on_right_action_items(self, instance, value):
        self.update_action_bar(self.ids["right_actions"], value)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            action_bar.add_widget(
                MDIconButton(
                    icon=item[0],
                    on_release=item[1],
                    opposite_colors=True,
                    text_color=self.specific_text_color,
                    theme_text_color="Custom",
                )
            )
        action_bar.width = new_width

    def update_action_bar_text_colors(self, instance, value):
        for child in self.ids["left_actions"].children:
            child.text_color = self.specific_text_color
        for child in self.ids["right_actions"].children:
            child.text_color = self.specific_text_color

    def _on_resize(self, instance, width, height):
        if self.mode == "center":
            self.action_button.x = width / 2 - self.action_button.width / 2
        else:
            self.action_button.x = width - self.action_button.width * 2

    def on_icon(self, instance, value):
        self.action_button.icon = value

    def on_icon_color(self, instance, value):
        self.action_button.md_bg_color = value

    def on_mode(self, instance, value):
        def set_button_pos(*args):
            self.action_button.x = x
            self.action_button.y = y
            self.action_button._hard_shadow_size = (0, 0)
            self.action_button._soft_shadow_size = (0, 0)
            anim = Animation(_scale_x=1, _scale_y=1, d=0.05)
            anim.bind(on_complete=self.set_shadow)
            anim.start(self.action_button)

        if value == "center":
            self.set_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
        elif value == "end":

            self.set_notch()
            x = Window.width - self.action_button.width * 2
            y = (
                (self.center[1] - self.height / 2)
                + self.theme_cls.standard_increment / 2
                + self._shift
            )
            self.right_action_items = []
        elif value == "free-end":
            self.remove_notch()
            x = Window.width - self.action_button.width - dp(10)
            y = self.action_button.height + self.action_button.height / 2
        elif value == "free-center":
            self.remove_notch()
            x = Window.width / 2 - self.action_button.width / 2
            y = self.action_button.height + self.action_button.height / 2
        self.remove_shadow()
        anim = Animation(_scale_x=0, _scale_y=0, d=0.05)
        anim.bind(on_complete=set_button_pos)
        anim.start(self.action_button)

    def remove_notch(self):
        self._angle_start = 0
        self._angle_end = 0
        self.round = 0
        self._shift = 0

    def set_notch(self):
        self._angle_start = 90
        self._angle_end = 270
        self.round = dp(10)
        self._shift = dp(3.5)

    def remove_shadow(self):
        self.action_button._hard_shadow_size = (0, 0)
        self.action_button._soft_shadow_size = (0, 0)

    def set_shadow(self, *args):
        self.action_button._hard_shadow_size = (dp(112), dp(112))
        self.action_button._soft_shadow_size = (dp(112), dp(112))
