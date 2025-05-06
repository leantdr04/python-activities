from states import TitleState
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
us_map = "blank_states_img.gif"
screen.addshape(us_map)
turtle.shape(us_map)

states = TitleState()
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        #optional(list compre) -- missing_states = [states for states in states_list if states not in guessed_states]
        missing_states = []
        for states in states_list:
            if states not in guessed_states:
                missing_states.append(states)
        # missed_states_df = pandas.DataFrame(missing_states) --creating csv file containing  missed states
        # missed_states_df.to_csv("remaining_states_to_know.csv")
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        states_coords = states_data[states_data.state == answer_state]
        x_coord = int(states_coords.x)
        y_coord = int(states_coords.y)
        states.create_title(answer_state, x_coord, y_coord) #or states_coords.state.item() -for state name





screen.exitonclick()
#For making new coords in new images

# def get_mouse_coord(x,y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_coord)
