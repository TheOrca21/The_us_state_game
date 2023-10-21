import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
score = 0
Data = pd.read_csv('50_states.csv')
text = turtle.Turtle()
text.hideturtle()
text.penup()
guessed = []
all_states = Data.state.to_list()
while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 Guessed", prompt="Enter a state name and fill the map").title()
    if answer_state == 'Exit':
        missing = []
        for state in all_states:
            if state not in guessed:
                missing.append(state)
        new_data = pandas.DataFrame(missing)
        break
    if answer_state in all_states and answer_state not in guessed:
        guessed.append(answer_state)
        state = Data[Data.state == answer_state]
        text.goto(int(state.x), int(state.y))
        text.write(f"{answer_state}")
screen.exitonclick()

new_data.to_csv('missed.csv')
