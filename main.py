import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the State in US")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state= []
ok = True
while len(guessed_state) < 50 and ok:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50 States correct" , prompt="What's another state's name ? ").title()
    if answer_state == "Exit":
        missing_State = []
        for state in all_state:
            if state not in guessed_state:
                missing_State.append(state)
        new_data = pandas.DataFrame(missing_State)
        new_data.to_csv("states_to_learn")
        ok = False
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(answer_state)



data.to_csv("missing_state.csv")