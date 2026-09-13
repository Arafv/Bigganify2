import webbrowser

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.core.clipboard import Clipboard
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup


# =========================================================
# BIGGANIFY
# =========================================================

Window.clearcolor = (0.015, 0.025, 0.06, 1)

WHATSAPP_LINK = (
    "https://chat.whatsapp.com/"
    "GNnF87XGprt9eZ51o9cz8r"
    "?s=cl&p=a&mlu=4&ilr=4"
)


# =========================================================
# COLORS
# =========================================================

BG = (0.015, 0.025, 0.06, 1)
WHITE = (0.94, 0.97, 1, 1)
BLUE = (0.10, 0.65, 1, 1)
CYAN = (0.15, 0.90, 1, 1)
GREEN = (0.10, 0.85, 0.45, 1)
MUTED = (0.55, 0.70, 0.90, 1)


# =========================================================
# CLICKABLE TEXT BUTTON
# =========================================================

class TextButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)

        self.color = WHITE
        self.font_size = dp(15)


# =========================================================
# MAIN APP
# =========================================================

class BigganifyApp(App):

    def build(self):

        root = FloatLayout()

        # =================================================
        # SCROLL AREA
        # =================================================

        scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False
        )

        content = BoxLayout(
            orientation="vertical",
            padding=(dp(20), dp(18), dp(20), dp(100)),
            spacing=dp(18),
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        # =================================================
        # HEADER
        # =================================================

        header = BoxLayout(
            size_hint_y=None,
            height=dp(70),
            spacing=dp(12)
        )

        logo = Image(
            source="bigganify.jpg",
            size_hint_x=None,
            width=dp(65),
            allow_stretch=True
        )

        header.add_widget(logo)

        title_box = BoxLayout(
            orientation="vertical"
        )

        title = Label(
            text="[b]Bigganify[/b]",
            markup=True,
            font_size=dp(28),
            color=WHITE,
            halign="left"
        )

        subtitle = Label(
            text="CODE  •  LEARN  •  BUILD  •  GROW",
            font_size=dp(10),
            color=CYAN,
            halign="left"
        )

        title_box.add_widget(title)
        title_box.add_widget(subtitle)

        header.add_widget(title_box)

        # THREE DOT
        dots = TextButton(
            text="⋮",
            font_size=dp(30),
            size_hint_x=None,
            width=dp(45)
        )

        dots.bind(on_release=self.show_menu)

        header.add_widget(dots)

        content.add_widget(header)

        # =================================================
        # HERO
        # =================================================

        hero = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(240),
            spacing=dp(10)
        )

        hero_text = BoxLayout(
            orientation="vertical",
            spacing=dp(8)
        )

        badge = Label(
            text="[b]💻  PROGRAMMING COMMUNITY[/b]",
            markup=True,
            color=CYAN,
            font_size=dp(11),
            halign="left"
        )

        welcome = Label(
            text="[b]Welcome to\nBigganify Buildlab![/b]",
            markup=True,
            font_size=dp(27),
            color=WHITE,
            halign="left",
            valign="middle"
        )

        welcome.bind(
            size=lambda x, y: setattr(x, "text_size", y)
        )

        description = Label(
            text="Learn. Code. Build.\nShare your ideas with others.",
            font_size=dp(14),
            color=MUTED,
            halign="left"
        )

        hero_text.add_widget(badge)
        hero_text.add_widget(welcome)
        hero_text.add_widget(description)

        hero.add_widget(hero_text)

        hero_logo = Image(
            source="bigganify.jpg",
            size_hint_x=0.42,
            allow_stretch=True
        )

        hero.add_widget(hero_logo)

        content.add_widget(hero)

        # =================================================
        # QUICK ACTIONS
        # =================================================

        section = Label(
            text="[b]Explore Bigganify[/b]",
            markup=True,
            color=WHITE,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(40),
            halign="left"
        )

        content.add_widget(section)

        # NO BOXES — JUST EMOJI + TEXT
        actions = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(220),
            spacing=dp(3)
        )

        actions_data = [
            ("💻", "Programming", "Learn coding & programming"),
            ("🧠", "Problem Solving", "Improve your logic"),
            ("🚀", "Projects & Ideas", "Build something cool"),
            ("👥", "Community", "Share • Help • Learn")
        ]

        for emoji, title_text, subtitle_text in actions_data:

            row = Button(
                background_normal="",
                background_down="",
                background_color=(0, 0, 0, 0),
                size_hint_y=None,
                height=dp(52)
            )

            row.text = (
                f"{emoji}   [b]{title_text}[/b]   "
                f"[color=#8AAAD0]{subtitle_text}[/color]"
            )

            row.markup = True
            row.color = WHITE
            row.font_size = dp(15)

            # Make every row clickable
            row.bind(
                on_release=lambda btn, t=title_text:
                self.action_clicked(t)
            )

            actions.add_widget(row)

        content.add_widget(actions)

        # =================================================
        # ABOUT
        # =================================================

        about_title = Label(
            text="[b]✨ About Bigganify[/b]",
            markup=True,
            color=WHITE,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(40),
            halign="left"
        )

        content.add_widget(about_title)

        about = Label(
            text=(
                "Bigganify is a programming community where "
                "curious minds can learn, share knowledge, "
                "solve problems and build amazing things.\n\n"
                "🐍 Python   🌐 Web Dev   📱 App Dev   "
                "⚙️ C++   🟨 JavaScript"
            ),
            color=MUTED,
            font_size=dp(14),
            halign="left",
            valign="top",
            size_hint_y=None,
            height=dp(140)
        )

        about.bind(
            size=lambda x, y: setattr(x, "text_size", y)
        )

        content.add_widget(about)

        # =================================================
        # WHATSAPP
        # =================================================

        join_title = Label(
            text="[b]🟢 Join the Bigganify Group[/b]",
            markup=True,
            color=WHITE,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(45),
            halign="left"
        )

        content.add_widget(join_title)

        join_button = Button(
            text="💬   [b]JOIN WHATSAPP GROUP[/b]   →",
            markup=True,
            font_size=dp(16),
            color=WHITE,
            size_hint_y=None,
            height=dp(60),
            background_normal="",
            background_down="",
            background_color=(0.05, 0.45, 0.25, 1)
        )

        join_button.bind(
            on_release=lambda x: webbrowser.open(WHATSAPP_LINK)
        )

        content.add_widget(join_button)

        # =================================================
        # FOOTER
        # =================================================

        footer = Label(
            text="💙 Together we code • Together we learn • Together we grow",
            color=(0.4, 0.65, 0.9, 1),
            font_size=dp(11),
            size_hint_y=None,
            height=dp(40)
        )

        content.add_widget(footer)

        scroll.add_widget(content)
        root.add_widget(scroll)

        # =================================================
        # BOTTOM NAVIGATION
        # =================================================

        nav = BoxLayout(
            size_hint=(1, None),
            height=dp(68),
            pos_hint={"x": 0, "y": 0},
            padding=(dp(5), dp(5)),
            spacing=dp(2)
        )

        nav_items = [
            ("🏠", "Home"),
            ("💬", "Chat"),
            ("📚", "Resources"),
            ("👥", "Members"),
            ("⋮", "More")
        ]

        for emoji, name in nav_items:

            button = TextButton(
                text=f"{emoji}\n{name}",
                font_size=dp(11),
                color=MUTED
            )

            button.bind(
                on_release=lambda btn, n=name:
                self.nav_clicked(n)
            )

            nav.add_widget(button)

        root.add_widget(nav)

        return root

    # =====================================================
    # ACTION CLICK
    # =====================================================

    def action_clicked(self, name):

        messages = {
            "Programming":
                "💻 Programming\n\nLearn and discuss programming.",

            "Problem Solving":
                "🧠 Problem Solving\n\n"
                "Improve your logic and coding skills.",

            "Projects & Ideas":
                "🚀 Projects & Ideas\n\n"
                "Share your projects and creative ideas.",

            "Community":
                "👥 Community\n\n"
                "Learn, help and connect with other programmers."
        }

        self.popup(
            messages.get(name, "Bigganify")
        )

    # =====================================================
    # NAVIGATION CLICK
    # =====================================================

    def nav_clicked(self, name):

        if name == "Home":
            self.popup("🏠 You are already on the Home page.")

        elif name == "Chat":
            webbrowser.open(WHATSAPP_LINK)

        elif name == "Resources":
            self.popup(
                "📚 Resources\n\n"
                "Programming resources will be available here."
            )

        elif name == "Members":
            self.popup(
                "👥 Members\n\n"
                "Bigganify community members."
            )

        elif name == "More":
            self.show_menu(None)

    # =====================================================
    # THREE DOT MENU
    # =====================================================

    def show_menu(self, button):

        layout = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
            padding=dp(12)
        )

        join = TextButton(
            text="💬  Join WhatsApp Group",
            size_hint_y=None,
            height=dp(50)
        )

        copy = TextButton(
            text="🔗  Copy Group Link",
            size_hint_y=None,
            height=dp(50)
        )

        close = TextButton(
            text="✕  Close",
            size_hint_y=None,
            height=dp(50)
        )

        layout.add_widget(join)
        layout.add_widget(copy)
        layout.add_widget(close)

        popup = Popup(
            title="Bigganify",
            content=layout,
            size_hint=(0.82, None),
            height=dp(220)
        )

        join.bind(
            on_release=lambda x: (
                popup.dismiss(),
                webbrowser.open(WHATSAPP_LINK)
            )
        )

        copy.bind(
            on_release=lambda x: (
                Clipboard.copy(WHATSAPP_LINK),
                popup.dismiss()
            )
        )

        close.bind(
            on_release=popup.dismiss
        )

        popup.open()

    # =====================================================
    # POPUP
    # =====================================================

    def popup(self, message):

        close = Button(
            text="OK",
            size_hint_y=None,
            height=dp(45)
        )

        box = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        box.add_widget(
            Label(
                text=message,
                font_size=dp(15),
                halign="center"
            )
        )

        box.add_widget(close)

        popup = Popup(
            title="Bigganify",
            content=box,
            size_hint=(0.82, None),
            height=dp(230)
        )

        close.bind(on_release=popup.dismiss)

        popup.open()


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    BigganifyApp().run()