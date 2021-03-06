import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data)
all_states = data.state.to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # print(answer_state)
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_data_frame = pandas.DataFrame(missing_states)
        missing_states_data_frame.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_row = data[data.state == answer_state]
        t.goto(int(data_row.x), int(data_row.y))
        t.write(answer_state)

