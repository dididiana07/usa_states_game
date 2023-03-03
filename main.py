from turtle import Screen, textinput, Turtle
import pandas as pd

background_pic_united_states = "us-states-game-start/blank_states_img.gif"

screen = Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
screen.bgpic(background_pic_united_states)
screen.tracer(0)

root = screen.getcanvas()
canvas = root.winfo_toplevel()


def close_window():
    global its_running
    its_running = False


canvas.protocol("WM_DELETE_WINDOW", close_window)

data = pd.read_csv("us-states-game-start/50_states.csv")
total_states = len(data)
guessed_states = 0


def check_state(state, csv_file_states):
    """Checks if the state is found on the file and return the coordinates."""
    list_states = []
    for states in csv_file_states.state:
        list_states.append(states)
    if state in list_states:
        index = list_states.index(state)
        return csv_file_states.iloc[index].x, csv_file_states.iloc[index].y


def add_state_to_map(state_name, x_cord, y_cord):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.color("black")
    text.setpos(x_cord, y_cord)
    text.write(f"{state_name}", font=("Arial", 10, "normal"))


its_running = True
show_textinput = True

guessed = []

while its_running:
    screen.update()
    if show_textinput:
        try:
            ask_state = textinput(f"{guessed_states}/{total_states} states.", "Enter a state:").title()
            if check_state(ask_state, data) and ask_state not in guessed:
                guessed_states += 1
                add_state_to_map(ask_state, check_state(ask_state, data)[0], check_state(ask_state, data)[1])
                guessed.append(ask_state)
        except AttributeError:
            pass
    elif guessed_states == total_states:
        show_textinput = False
    if not its_running:
        break
