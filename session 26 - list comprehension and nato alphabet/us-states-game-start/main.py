import pandas as pd
import turtle

data = pd.read_csv('50_states.csv')
print(data.state)
image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title('US State Game')
screen.addshape(image)
turtle.shape(image)

# turtle.penup()
# screen.tracer(0)
# still_guess = True
# score = 0
# titlee = ''
# correct_answer = []
# while still_guess:
#     screen.update()
#     if score == 0:
#         titlee = 'guess the state'
#     answer_state = screen.textinput(title=titlee, prompt='what state?').title()
#     for i in data.state:
#         if i == answer_state:
#             x = int(data[data.state == answer_state].x)
#             y = int(data[data.state == answer_state].y)
#             turtle.goto(x, y)
#             turtle.write(answer_state)
#             turtle.goto(0, 0)
#             if answer_state not in correct_answer:
#                 correct_answer.append(answer_state)
#                 score += 1
#             titlee = f'{score}/50 state correct'
#     if len(correct_answer) == 50:
#         turtle.write('you are at the end of the state, you win!')
#         still_guess = False

# other way
all_states = data.state.to_list()
correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 state correct", prompt='what state?').title()
    if answer_state == 'Exit':
        # for state in all_states:
        #     if state not in correct_answer:
        #         missing_state.append(state)

        # simplify code with list comprehension
        missing_state = [state for state in all_states if state not in correct_answer]
        df = pd.DataFrame(missing_state)
        df.to_csv('state_to_learn.csv')
        break
    if answer_state in all_states:
        correct_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stack_data = data[data.state == answer_state]
        t.goto(int(stack_data.x), int(stack_data.y))
        t.write(answer_state)



