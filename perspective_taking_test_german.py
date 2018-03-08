# PTSOT Version taken from https://github.com/TimDomino/ptsot working with python3
# install the following dependencies:
# 0. check if pip3 (pip for python3) is installed: type "which pip3" or "pip3 -V" on a mac terminal or windows shell
#  -> if it is installed, the installed path should display
#  -> if not follow (https://pip.pypa.io/en/stable/installing/)
# 1. install pip3 (when on osx or windows), apt-get (Linux)
# install the following packages with dependecies by typing the following command on a mac terminal or windows shell
# "python3 -mpip install matplotlib"
# "python3 -mpip install nose"
# "python3 -mpip install pylsl"

# 2. run the task by typing "python3 perspective_taking_test_german.py" on a mac terminal or windows shell

# import matplotlib features
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as lines
import matplotlib.patches as patches
import numpy as np

# import python libraries
import builtins
import math
import sys
import time

# import LSL
from pylsl import StreamInfo, StreamOutlet

##################
# task specifications
##################
TASK_TEXT_1 = " Stellen Sie sich vor, Sie stehen an der Position "
TASK_TEXT_2 = "\n und schauen in Richtung"
TASK_TEXT_3 = " Zeigen Sie nun in Richtung"

TASK_ITEMS = [ ("Blume", "Baum", "Katze", 301), # example
               ("Auto", "Verkehrsampel", "Stoppschild", 123),
               ("Katze", "Baum", "Auto", 237),
               ("Stoppschild", "Katze", "Haus", 83),
               ("Katze", "Blume", "Auto", 156),
               ("Stoppschild", "Baum", "Verkehrsampel", 319),
               ("Stoppschild", "Blume", "Auto", 235),
               ("Verkehrsampel", "Haus", "Blume", 333),
               ("Haus", "Blume", "Stoppschild", 260),
               ("Auto", "Stoppschild", "Baum", 280),
               ("Verkehrsampel", "Katze", "Auto", 48),
               ("Baum", "Blume", "Haus", 26),
               ("Katze", "Haus", "Verkehrsampel", 150)
             ]

TIME_IN_SECONDS = 5 * 60

INSTRUCTION_TEXT = "Dieser Test untersucht Ihre Fähigkeit, sich verschiedene Perspektiven im Raum vorzustellen.\n" + \
                   "In jeder der folgenden Teilaufgaben sehen Sie dasselbe Bild, auf dem eine Vielzahl von \n" + \
                   "Objekten sowie ein „Pfeilkreis“ zu sehen sind. Es wird Ihnen eine Frage über räumlichen \n" + \
                   "Beziehungen zwischen einigen dieser Objekte gestellt. Für die Beantwortung der Frage\n" + \
                   "sollen Sie sich vorstellen, dass Sie an einem der Objekte stehen (das Objekt wird im \n" + \
                   "Zentrum des Kreises angezeigt) und einem anderen Objekt zugewandt sind (dieses Objekt\n" + \
                   "wird über dem Kreis genannt). Sie sollen sich vorstellen am Ort des ersten Objektes zu\n" + \
                   "stehen und in die Richtung des zweiten Objektes zu schauen. Dann sollen Sie einen Pfeil\n" + \
                   "zeichnen, der die Richtung des dritten Objektes anzeigt. Nutzen Sie dafür bitte die\n" + \
                   "Maustaste (linker Mausklick auf den Kreis).   \n\n" + \
                   "Betrachten Sie das unten gezeigte Beispiel. Stellen Sie sich vor, dass Sie an der Blume\n" + \
                   "stehen (“Blume” wird im Zentrum des Kreises angezeigt). Stellen Sie sich nun vor in\n" + \
                   "Richtung des Baumes zu schauen (“Baum” wird über dem Kreis angezeigt). Nun sollen Sie \n" + \
                   "einen Pfeil zeichnen, welcher in Richtung der “Katze” zeigt. Im Beispiel wurde dieser Pfeil\n" + \
                   "bereits für Sie eingezeichnet. \n\n" + \
                   "In den folgenden Teilaufgaben ist es Ihre Aufgabe, die jeweiligen Pfeile einzuzeichnen. Ist \n" + \
                   "die Pfeileinstellung im Beispiel für Sie richtig? Wenn nicht, oder wenn Sie unsicher sind, \n" + \
                   "fragen Sie bitte jetzt die ExperimentalleiterInnen. \n\n" + \
                   "Der Test besteht insgesamt aus 12 Teilaufgaben, eine auf jeder Seite. Bei jeder Teilaufgabe  \n" + \
                   "befindet sich die Darstellung der Objekte am oberen Seitenrand und der „Pfeilkreis“ am\n" + \
                   "unteren. Bitte heben oder drehen Sie den Monitor nicht. Markierungen sind ebenfalls nicht \n" + \
                   "gestattet. Versuchen Sie, möglichst genau die Richtungen zu markieren. Sie können ihre\n" +\
                   "Angabe auch nachbessern. Verwenden Sie jedoch nicht zu viel Zeit mit einzelnen  \n\n" + \
                   "Teilaufgaben. Sie haben für den Test 5 Minuten Zeit. \nBitte nutzen Sie die Leertaste um Ihre Richtungseingabe zu bestätigen.\n"

# initialize LSL
info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'ptsot')
outlet = StreamOutlet(info)
print("now sending data...")

##################
# main function
##################
def main():

    matplotlib.rcParams['toolbar'] = 'None'
    subject_id = input("Please insert your participant ID: ")
    result_file = open('results-' + str(subject_id) + '.txt', 'w+')
    
    create_test_window(subject_id)
    create_instruction_window()

    builtins.result_file = result_file
    builtins.errors = []
    builtins.task_id = 0
    load_task(builtins.task_id)

    plt.show()


##################
# plot creator functions
##################
def create_instruction_window():
    ins_fig = plt.figure("Versuchsanleitung", figsize = (8.5, 10))
    ins_ax = ins_fig.add_subplot(1, 1, 1)
    ins_ax.text(0.01, 0, INSTRUCTION_TEXT, verticalalignment='center', fontsize=14)
    plt.xticks([])
    plt.yticks([])
    plt.ylim([-1.0, 1.0])
    ins_fig.tight_layout()


def create_test_window(SUBJECT_ID):
    test_fig = plt.figure("Perspective Taking Test - Versuchsperson " + str(SUBJECT_ID), figsize = (10.5, 15))

    # object array subplot
    pic_ax = test_fig.add_subplot(2, 1, 1)
    picture = mpimg.imread('object_array.png')
    plt.xticks([])
    plt.yticks([])
    pic_ax.set_title("Verbleibende Zeit: " + str(TIME_IN_SECONDS))
    pic_ax.imshow(picture)

    # user input subplot
    input_ax = test_fig.add_subplot(2, 1, 2)
    input_ax.axis('equal')

    circle = patches.Circle((0, 0), 1.015, facecolor='none', edgecolor='black', linewidth=3)
    input_ax.add_patch(circle)

    upright_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='black')
    input_ax.add_line(upright_line)
    input_ax.add_line(lines.Line2D((0, -0.03), (1, 0.95), linewidth=3, color='black')) # left arrow wedge
    input_ax.add_line(lines.Line2D((0, 0.03), (1, 0.95), linewidth=3, color='black')) # right arrow wedge

    answer_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='orange')
    input_ax.add_line(answer_line)

    text_bottom = input_ax.text(0.0, -0.15, 'text_bottom', fontsize=14, horizontalalignment='center')
    text_top = input_ax.text(0.0, 1.05, 'text_top', fontsize=14, horizontalalignment='center')
    text_example = input_ax.text(-1.0, 0.58, 'text_example', fontsize=14, horizontalalignment='center')
    text_instruction = input_ax.text(0.0, 1.2, 'text_instruction', fontsize=12, horizontalalignment='center')

    plt.xlim(-1.5, 1.5)
    plt.xticks([])
    plt.ylim(-1.5, 1.5)
    plt.yticks([])
    test_fig.tight_layout()

    # event handling
    builtins.fig = test_fig
    builtins.answer_line = answer_line
    builtins.picture_ax = pic_ax
    builtins.text_bottom = text_bottom
    builtins.text_top = text_top
    builtins.text_example = text_example
    builtins.text_instruction = text_instruction
    test_fig.canvas.mpl_connect('button_press_event', on_click)
    test_fig.canvas.mpl_connect('key_press_event', on_key_press)


def load_task(INDEX):
    task_id_as_text = str(INDEX) + '.'
    item_tuple = TASK_ITEMS[INDEX]
    located_at = item_tuple[0].replace(' ', '\; ')
    facing_to = item_tuple[1].replace(' ', '\; ')
    pointing_to = item_tuple[2].replace(' ', '\; ')

    instruction_text = task_id_as_text + ' ' + TASK_TEXT_1 + ' $\mathtt{' + located_at + '}$ ' + TASK_TEXT_2 + \
                       ' $\mathtt{' + facing_to + '}$. ' + TASK_TEXT_3 + ' $\mathtt{' + pointing_to + '}$.'
    builtins.text_instruction.set_text(instruction_text)

    # push event marker to LSL
    outlet.push_sample([task_id_as_text])
    
    if INDEX == 0: # example case
        builtins.answer_line.set_data([0.0, -0.86], [0.0, 0.52])
        text_example.set_text('Katze')
    else:
        builtins.answer_line.set_data([0.0, 0.0], [0.0, 1.0])
        text_example.set_text('')

    if INDEX == 1: # first real task, start timer
        timer = builtins.fig.canvas.new_timer(interval=1000)
        timer.add_callback(update_time)
        builtins.start_time = time.time()
        timer.start()
    
    builtins.text_bottom.set_text(item_tuple[0])
    builtins.text_top.set_text(item_tuple[1])
    builtins.fig.canvas.draw()


##################
# callbacks
##################
def on_click(EVENT):
    if EVENT.inaxes is None:
        return
    length = euclidean_distance([0, 0], [EVENT.xdata, EVENT.ydata])
    builtins.answer_line.set_data([0.0, EVENT.xdata/length], [0.0, EVENT.ydata/length])
    builtins.fig.canvas.draw()


def on_key_press(EVENT):
    if EVENT.key == ' ':
        if builtins.task_id > 0: # exclude example
            correct_angle = round(TASK_ITEMS[builtins.task_id][3], 4)
            logged_angle = round(compute_response_line_angle(), 4)
            error = round(angle_difference(correct_angle, logged_angle), 4)
            builtins.result_file.write(str(builtins.task_id) + ',' + str(correct_angle) + ',' + str(logged_angle) + ',' + str(error) + '\n')
            builtins.errors.append(error)

        builtins.task_id += 1

        if builtins.task_id < len(TASK_ITEMS): # move on to the next task
            load_task(builtins.task_id)
        else: # no more tasks, terminate the test
            avg_error = np.mean(builtins.errors)
            builtins.result_file.write('Average Error: ' + str(round(avg_error, 4)))
            builtins.result_file.close()
            print('The test has terminated successfully. Results saved to file ' + builtins.result_file.name + '.')
            sys.exit(0)


def update_time():
    elapsed = max(TIME_IN_SECONDS - round(time.time()-builtins.start_time), 0)
    builtins.picture_ax.set_title("Verbleibende Zeit: " + str(elapsed))
    builtins.fig.canvas.draw()


##################
# math helpers
##################
def compute_response_line_angle():
    answer_line_data = builtins.answer_line.get_data()
    answer_line_endpoint = (answer_line_data[0][1], answer_line_data[1][1])
    upright_endpoint = (0.0, 1.0)
    cosine_value = answer_line_endpoint[0]*upright_endpoint[0] + \
                   answer_line_endpoint[1]*upright_endpoint[1]

    angle = angle_between_normalized_2d_vectors(upright_endpoint, answer_line_endpoint) * 180.0/math.pi

    # convert angle to range (0; 360]
    if angle < 0:
        angle *= -1
    else:
        angle = 360.0 - angle

    return angle


def euclidean_distance(POINT_1, POINT_2):
    return math.sqrt(pow(POINT_1[0]-POINT_2[0], 2) + pow(POINT_1[1]-POINT_2[1], 2))


def angle_between_normalized_2d_vectors(VEC1, VEC2):
    return math.atan2(VEC1[0]*VEC2[1] - VEC1[1]*VEC2[0], VEC1[0]*VEC2[0] + VEC1[1]*VEC2[1])


def angle_difference(ANGLE_1, ANGLE_2):
    phi = math.fmod(abs(ANGLE_2-ANGLE_1), 360)
    distance = 360 - phi if phi > 180 else phi
    return distance


if __name__ == '__main__':
    main()