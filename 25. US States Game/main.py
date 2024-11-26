import pandas
import turtle

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = [state.title() for state in data.state.to_list()]
States_Guessed = []

while len(States_Guessed) < 50:
    answer_state = screen.textinput(title=f"{len(States_Guessed)}/50 States Guessed",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in States_Guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("MissedStates.csv")
        break
    if answer_state in states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)
            States_Guessed.append(answer_state)
