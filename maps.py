from turtle import Turtle, Screen
IMAGE = "blank_states_img.gif"
FONT = ("Arial", 10, "normal")
SCORE_FONT = ("Arial", 25, "normal")


class Maps:
    """It controls the mapping of states"""
    def __init__(self):
        self.places = Turtle()
        self.places.shape("square")
        self.places.shapesize(0.1)
        self.places.penup()
        self.score = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.win = Turtle()
        self.win.hideturtle()
        self.win.penup()
        self.input = ""
        self.screen = Screen()
        self.screen.title("Find the States")
        self.bg = Turtle()
        self.screen.addshape(IMAGE)
        self.bg.shape(IMAGE)

    def user_input(self):
        """Gets the user input"""
        self.input = self.screen.textinput(title="States", prompt="Enter the names of states in america or enter 'exit' to exit the game:")
        if self.input.lower() == "exit":
            return "exit"
        return self.input

    def exit(self):
        """Exits turtle's Screen"""
        self.screen.exitonclick()

    def place_on_map(self, place, x_cor, y_cor):
        """Place the answer in map"""
        # self.places = Turtle()
        self.places.goto(x_cor, y_cor)
        self.places.write(place, align="center", font=FONT)

    def scores(self, found):
        """Creates the scoreboard"""
        self.score.goto(250, 220)
        self.score.clear()
        self.score.write(f"{found}/50", align="center", font=SCORE_FONT)

    def winner(self):
        """Displays the 'You Win'"""
        self.win.goto(0, 0)
        self.win.write("You win", align="center", font=("Arial", 50, "normal"))
