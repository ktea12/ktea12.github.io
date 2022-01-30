from typing_extensions import IntVar
from matplotlib import pyplot as plt
import tkinter

root=tkinter.Tk()
root.title("Mood Tracker")
root.geometry("1000x500")

WIDTH = 20
HEIGHT = 10

class moodgraph: #create class for graphing moods

    def __init__(self, morning, noon, night, ): #getter function, getting values: time of day, and level of mood
        self.tmorn = morning #level of mood in the morning
        self.tnoon = noon #level of mood at noon
        self.tnight = night #level of mood at night
        self.moodscore = [self.tmorn, self.tnoon, self.tnight]
        self.time_of_day = ['Morning', 'Noon', 'Night']
        self.morntf = None
        self.noontf = None
        self.nighttf = None

#Added attributes in the class called morningtf, noontf and nighttf
#these attributes are linking to the text field from the tkinter (morning, noon and night text fields)

    def update_inputs(self):
        morning2 = int(morning.get())
        noon2 = int(noon.get())
        night2 = int(night.get())

        self.moodscore = [morning2,noon2,night2]

    def graph_mood_score(self):
        self.update_inputs()
        plt.plot(self.time_of_day, self.moodscore)
        plt.xlabel('Time of Day')
        plt.ylabel('Mood Level')
        plt.title('Mood Level over Time')
        plt.show()


label =tkinter.Label (text="Welcome to Mood track.")
label.grid(row=1, column=4, pady=20)
label =tkinter.Label (text="What Level is your Mood at?")
label.grid(row=1, column=5, pady=20)

button0=tkinter.Button(root, text="0\n\nVery Bad", width=WIDTH, height=HEIGHT, bg="red")
button0.grid(row=2, column=2, padx=7, pady=10)

button1=tkinter.Button(root, text="1\n\nBad and Unproductive", width=WIDTH, height=HEIGHT, bg="orange")
button1.grid(row=2,column=3, padx=7, pady=10)

button2=tkinter.Button(root, text="2\n\nBad but Productive", width=WIDTH, height=HEIGHT, bg="yellow")
button2.grid(row=2,column=4, padx=7, pady=10)

button3=tkinter.Button(root, text="3\n\nNormal", width=WIDTH, height=HEIGHT, bg="dark green")
button3.grid(row=2,column=5, padx=7, pady=10)

button4=tkinter.Button(root, text="4\n\nGood Mood", width=WIDTH, height=HEIGHT, bg="green")
button4.grid(row=2,column=6, padx=7, pady=10)

button5=tkinter.Button(root, text="5\n\nVery Good Mood", width=WIDTH, height=HEIGHT, bg="light green")
button5.grid(row=2,column=7, padx=7, pady=10)


morning2 = IntVar("1")

label =tkinter.Label (text="Morning Mood? ")
label.grid(row=3, column=4, pady=20)
morning = tkinter.Entry(font=40, textvariable = morning2, width=15)
morning.grid(row=3, column=5, pady=20)

afternoon2 = IntVar("2")

label =tkinter.Label (text="Mood at noon? ")
label.grid(row=4, column=4, pady=20)
noon = tkinter.Entry(font=40, width=15, textvariable=afternoon2)
noon.grid(row=4, column=5, pady=20)


night2 = IntVar("3")
label =tkinter.Label (text="Mood at night? ")
label.grid(row=5, column=4, pady=20)
night = tkinter.Entry(textvariable = night2, font=40, width=15)
night.grid(row=5, column=5, pady=20)

# morning2 = int(morning.get())
# noon2 = int(noon.get())
# night2 = int(night.get())
# moodlevel = [morning2,afternoon2,night2]
# mood=moodgraph(morning2,noon2,night2)

mood=moodgraph(0,0,0)

mood.morntf = morning
mood.noontf = noon
mood.nighttf = night

graph =tkinter.Button(text="Plot Graph", command=mood.graph_mood_score)
graph.grid(row=6, column=5, pady=20) #Fuction graph : -> get values that was entered in the field and graph in the matplot


root.mainloop() #for window display
