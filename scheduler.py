
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import matplotlib
import matplotlib.pyplot as plt
max = 9999999999999999999999999999999
HighestPrior = max
ProccessNumber = -1
MinimumProcessArrivalTime = max
j = 0
Time=0
PAV = []
Position = 0
arrivaldict={}
durationdict={}
prioritydict = {}
#****** Mira's global variables *******
ProcessedProcess = []
ProcessedTime = []
ProcessStartTime=[]
max = 0
element = 0
global Emptive




class Process:

    def __init__(self, name, arrival, remaining):
        self.name = name
        self.arrival = int(arrival)
        self.remaining = int(remaining)

    def do_process(self):
        if (self.remaining == 0):
            return None
        else:
            self.remaining -= 1
            if (self.remaining == 0):
                return None
            else:
                return self.remaining

    def status(self):
        return "Name : {}, arrival: {}, remaining : {}".format(self.name, self.arrival, self.remaining)




def FCFS ():
    global Time
    global max
    global element
    max = int(arrivaldict[0])
    flag = 0

    for i in range(int(numberOfProcesses) ):
        if (int(arrivaldict[i]) > max):
                max = int(arrivaldict[i])

    while 1 :
        for i in range(int(numberOfProcesses)):
            if (int(arrivaldict[i]) <= Time) and (int(durationdict[i]) != 0) and (
                        int(arrivaldict[i]) < int(max) + 1):
                ProcessStartTime.append(Time)
                Time = Time + int(durationdict[i])
                ProcessedProcess.append('P'+str(i))
                ProcessedTime.append(durationdict[i])
                durationdict[i] = 0
                element = element + 1
                flag=1
            else :
                flag=0
        if (flag == 0):
            Time = Time + 1
        if element == int(numberOfProcesses) :
            break
def PR():

    if Emptive.get()=='Non-Preemptive':
            Scheduler()
    if Emptive.get()=='Pre-Emptive':
            PreScheduler()




def checkRR():
    global root5
    global Quantum
    qq=int(Quantum.get())
    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 = durationdict[i].get()
        if (not (temp.isnumeric()) or not (temp2.isnumeric()) or int(temp2) == 0 or not(Quantum.get().isnumeric()) or int(Quantum.get())<=0):
            flag = 0
        else:
            arrivaldict[i] = temp
            durationdict[i] = temp2
    if flag == 0:
        tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
    if (flag == 1):
        RR(qq)
        Draw()
        root5.destroy()
def checkFCFS():
    global root2
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 =durationdict[i].get()
        if (not(temp.isnumeric()) or not(temp2.isnumeric()) or  int(temp2)==0):
            tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")

        else:
            arrivaldict[i]=temp
            durationdict[i]=temp2
    FCFS()
    Draw()
    root2.destroy()
def checkPR():
    global root3
    global Emptive

    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 = durationdict[i].get()
        temp3 = prioritydict[i].get()
        if (not (temp.isnumeric()) or not (temp2.isnumeric()) or int(temp2) == 0 or not (temp3.isnumeric()) ):
            tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
            flag =0

        else:
            arrivaldict[i] = temp
            durationdict[i] = temp2
            prioritydict[i] = temp3
    if (Emptive.get() == "Pre or Non"):
        flag = 0
    if(flag==1):
        PR()
        Draw()
        root3.destroy()
def checkSJF():
    global root4
    global Emptive
    flag = 1
    for i in range(int(numberOfProcesses)):
        temp = arrivaldict[i].get()
        temp2 =durationdict[i].get()
        if (not(temp.isnumeric()) or not(temp2.isnumeric()) or  int(temp2)==0):
            flag =0
        else:
            arrivaldict[i]=temp
            durationdict[i]=temp2
    if(Emptive.get()=="Pre or Non"):
        flag = 0
    if flag == 0:
        tkinter.messagebox.showerror("Error", "ERROR:Please enter a valid input")
    if (flag==1):
        if(Emptive.get()=='Non-Preemptive'):
            SJF(0)
        if (Emptive.get() == 'Pre-Emptive'):
            SJF(1)
        Draw()
        root4.destroy()






def SJF_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global emptive
    global checkk
    global root4
    global Emptive
    checkk= IntVar()
    arrivaldict = {}
    durationdict = {}
    root4 = Tk()
    root4.title("SJF Scheduler")
    root4.geometry("300x300")
    Plabel = Label(root4, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    arrival = Label(root4, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)

    duration = Label(root4, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)


    for i in range(int(numberOfProcesses)):
        label = Label(root4, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root4, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root4, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)

    Emptive = Combobox(root4, values=['Pre-Emptive', 'Non-Preemptive'], width=15)
    Emptive.set("Pre or Non")
    Emptive.grid(columnspan=12)

    buuton = Button(root4, text="OK", command=checkSJF)
    buuton.grid(columnspan=12)
def RR_Page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global root5
    global Quantum
    arrivaldict = {}
    durationdict = {}
    root5 = Tk()
    root5.title("RR Scheduler")
    root5.geometry("300x300")
    Plabel = Label(root5, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    arrival = Label(root5, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)

    duration = Label(root5, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)

    for i in range(int(numberOfProcesses)):
        label = Label(root5, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root5, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root5, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)
    label8= Label(root5,text="Quantum Time:")
    label8.grid(row=i+2)
    Quantum = Entry(root5)
    Quantum.grid(row=i+2,column=2,columnspan=12)

    buuton = Button(root5, text="OK",command=checkRR)
    buuton.grid(columnspan=12)

def PR_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global prioritydict
    global root3
    global Emptive
    arrivaldict = {}
    durationdict = {}
    prioritydict = {}
    root3 = Tk()
    root3.title("PR Scheduler")
    root3.geometry("450x400")
    Plabel = Label(root3, text="Process Name", )
    Plabel.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
    arrival = Label(root3, text="Arrival Time")
    arrival.grid(row=0, column=4, columnspan=3, padx=10, pady=5)
    duration = Label(root3, text="Duration")
    duration.grid(row=0, column=8, columnspan=3, padx=10, pady=5)
    priority = Label(root3,text="Priority")
    priority.grid(row=0, column=12, columnspan=3 , padx=10,pady=5)
    for i in range(int(numberOfProcesses)):
        label = Label(root3, text='P' + str(i))
        label.grid(row=i + 1, column=0, columnspan=3, padx=10, pady=5)
        arrivaldict[i] = Entry(root3, width=10)
        arrivaldict[i].grid(row=i + 1, column=4, columnspan=3, padx=20, pady=5)

        durationdict[i] = Entry(root3, width=10)
        durationdict[i].grid(row=i + 1, column=8, columnspan=3, padx=20, pady=5)

        prioritydict[i] = Entry(root3, width=10)
        prioritydict[i].grid(row=i + 1, column=12, columnspan=3, padx=20, pady=5)

    Emptive = Combobox(root3, values=['Pre-Emptive', 'Non-Preemptive'], width=15)
    Emptive.set("Pre or Non")
    Emptive.grid(columnspan=16)
    buuton = Button(root3, text="OK", command=checkPR)
    buuton.grid(columnspan=18)
def FCFCS_page():
    global numberOfProcesses
    global entryq
    global arrivaldict
    global durationdict
    global root2
    arrivaldict = {}
    durationdict = {}
    root2 = Tk()
    root2.title("FCFS Scheduler")
    root2.geometry("300x300")
    Plabel = Label(root2, text="Process Name",)
    Plabel.grid(row=0, column=0,columnspan= 3, padx=10,pady=5)
    arrival = Label(root2,text="Arrival Time")
    arrival.grid(row=0, column=4 ,columnspan=3,padx=10,pady=5)
    duration = Label(root2, text="Duration")
    duration.grid(row=0, column=8,columnspan=3,padx=10,pady=5)



    for i in range(int(numberOfProcesses)):
        label = Label(root2, text='P' + str(i))
        label.grid(row=i+1, column=0,columnspan= 3, padx=10,pady=5)
        arrivaldict[i] = Entry(root2, width=10)
        arrivaldict[i].grid(row=i+1, column=4,columnspan= 3, padx=20,pady=5)


        durationdict[i] = Entry(root2, width=10)
        durationdict[i].grid(row=i+1, column=8,columnspan= 3, padx=20,pady=5)

    buuton = Button(root2,text="OK",command=checkFCFS)
    buuton.grid(columnspan=12)






def mainpage():
    global root
    global technique
    global number
    global NumberOfProcesses
    root = Tk()
    root.title("Scheduler")
    root.geometry("300x300")

    upperframe = Frame()
    upperframe.pack()
    lowerframe = Frame()
    lowerframe.pack(side=BOTTOM)

    choices=["FCFS","SJF","PR","RR"]
    technique = Combobox(root, values=choices, width=15)
    technique.set("Choose..")



    label_1 = Label(upperframe, text="No. of processes")
    label_2 = Label(root, text="Select a technique",width=200)
    button_1 = Button(root, text="OK" ,command=showtype)
    number = Entry(upperframe)
    menu = Menu(root)
    label_1.pack(side=LEFT)
    number.pack(side=RIGHT)
    label_2.pack()
    technique.pack()
    button_1.pack()

def showtype():
    global numberOfProcesses
    global number
    global root
    if(not((number.get()).isnumeric()) or int(number.get())==0 or technique.get()=="Choose.."):
        tkinter.messagebox.showerror("Error","ERROR:Please enter a valid input")
    else:
        numberOfProcesses = int(number.get())
        if(technique.get() == "FCFS"):
            FCFCS_page()

        if(technique.get() == "PR"):
            PR_page()

        if (technique.get() == "SJF"):
            SJF_page()
        if(technique.get() == "RR"):
            RR_Page()

        #root.withdraw()

def SJF(preemptive): # 1 if preemptive,0 if non preemptive
    global number
    global  Time
    global durationdict
    global arrivaldict
    global ProcessStartTime
    global ProcessedProcess
    global ProcessedTime
    last_process_name = ''
    number_of_done = 0
    time = 0
    processes = []
    processes_queue = []
    last_appended = 0
    do_flag = 0
    done_flag = 0

    for index in range(int(number.get())):  # looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
        processes.append(Process('P'+ str(index), arrivaldict[index], durationdict[index]))
    processes.sort(key=lambda x: x.arrival)  # sort proccesses according to arrival time
    while (1):
        for index in range(last_appended, len(processes)):
            if (time == processes[index].arrival):
                processes_queue.append(processes[index])
                last_appended = index
                # print(processes_queue[last_appended].status())
            else:
                last_appended = index
                break
        if (len(processes_queue) == 0):
            if (do_flag == 0):
                time += 1
                continue
            elif (number_of_done != len(processes)):
                time += 1
                continue
            else:
                break
        if (processes_queue[0].name != last_process_name):  # process changed
            ProcessedProcess.append(processes_queue[0].name)
            ProcessStartTime.append(time)
            ProcessedTime.append(0)
        # print(processes_queue[0].status(),"time :",time)
        last_process_name = processes_queue[0].name
        if ((done_flag == 1) or (preemptive)):
            processes_queue.sort(key=lambda x: x.remaining)
            done_flag = 0
        if (processes_queue[0].remaining == 0):
            done_flag = 1
            #print("process", processes_queue[0].name, "is done")
            processes_queue.remove(processes_queue[0])
            number_of_done += 1
            if (len(processes_queue) != 0):
                processes_queue[0].do_process()
                ProcessedTime[-1] += 1
                do_flag = 1
            # print(time, processes_queue[0].name, " ", end="")
        else:
            processes_queue[0].do_process()
            ProcessedTime[-1] += 1
            do_flag = 1
        #  print(time,processes_queue[0].name," ",end = "")
        time += 1

    numberofprocess = len(ProcessedProcess)
    Time = time



def Scheduler():
    global Time
    global HighestPrior
    global ProccessNumber
    global numberOfProcesses
    global MinimumProcessArrivalTime
    global j
    while j < numberOfProcesses:
        for i in range(numberOfProcesses):
            if int(arrivaldict[i]) <= Time and int(durationdict[i]) != 0 and int(
                    prioritydict[i]) < HighestPrior:
                ProccessNumber = i
                HighestPrior = int(prioritydict[i])
            if (int(arrivaldict[i]) < MinimumProcessArrivalTime and int(durationdict[i]) != 0):
                MinimumProcessArrivalTime = int(arrivaldict[i])
        if ProccessNumber == -1:
            Time = MinimumProcessArrivalTime
        else:
            ProcessStartTime.append(Time)
            Time = Time + int(durationdict[ProccessNumber])
            ProcessedProcess.append("P" + str(ProccessNumber))
            ProcessedTime.append(int(durationdict[ProccessNumber]))
            durationdict[ProccessNumber] = 0
            HighestPrior = max
            ProccessNumber = -1
            MinimumProcessArrivalTime = max
            j = j + 1



def PreScheduler():
    global durationdict
    global Time
    global prioritydict
    global HighestPrior
    global ProccessNumber
    global numberOfProcesses
    global arrivaldict
    global MinimumProcessArrivalTime
    global j
    global PAV
    global Position
    global number
    global ProcessedProcess
    global ProcessStartTime
    global ProcessedTime
    PAV.clear()
    ProcessedProcess.clear()
    ProcessedTime.clear()
    ProcessStartTime.clear()
    Position=0
    HighestPrior=max
    Time=0
    ProccessNumber=-1
    x=int(number.get())
    for i in range(x):
        PAV.append(arrivaldict[i])
    PAV=sorted(PAV)
    PAV=list(dict.fromkeys(PAV))
    flag = 0
    if int(PAV[Position]) ==0:

        if (Position == (len(PAV) - 1)):
            flag = 1
        else:
            Position = Position+1
    while j < numberOfProcesses:
        for i in range(numberOfProcesses):
            if int(arrivaldict[i]) <= Time and int(durationdict[i]) != 0 and int(
                    prioritydict[i]) < HighestPrior:
                ProccessNumber = i
                HighestPrior = int(prioritydict[i])
            if (int(arrivaldict[i]) < MinimumProcessArrivalTime and int(durationdict[i]) != 0):
                MinimumProcessArrivalTime = int(arrivaldict[i])
        if ProccessNumber == -1:
            Time = int(PAV[Position])
            if (Position == (len(PAV) - 1)):
                flag = 1
            if (flag == 0):
                Position = Position + 1
                continue
        else:
            if(Time+int(durationdict[ProccessNumber])<int(PAV[Position]) or flag == 1):
                ProcessStartTime.append(Time)
                Time = Time + int(durationdict[ProccessNumber])
                ProcessedProcess.append("P" + str(ProccessNumber))
                ProcessedTime.append(int(durationdict[ProccessNumber]))
                durationdict[ProccessNumber] = 0
                HighestPrior = max
                ProccessNumber = -1
                MinimumProcessArrivalTime = max
                j = j + 1

            else:
                ProcessStartTime.append(Time)
                ProcessedTime.append(int(PAV[Position])-Time)
                durationdict[ProccessNumber] = str(int(durationdict[ProccessNumber]) -(int(PAV[Position])-Time))
                Time = int(PAV[Position])
                ProcessedProcess.append("P" + str(ProccessNumber))
                HighestPrior = 99999999999999999999999999
                ProccessNumber = -1
                MinimumProcessArrivalTime = 99999999999999999999999999
                if (Position == (len(PAV) - 1)):
                    flag = 1
                if (flag == 0):
                    Position = Position + 1






def RR(timeQuantum):
    global Time
    global ProcessedTime
    global ProcessedProcess
    global ProcessStartTime
    last_process_name = ''
    processes = []
    processes_queue = []
    time = 0
    last_appended = 0
    untilTime = 0
    number_of_done = 0
    for index in range(int(number.get())):  # looping in the txt file,adding string in a list then splitting the strings then appending objects in a list
        processes.append(Process('P'+ str(index), arrivaldict[index], durationdict[index]))
    processes.sort(key=lambda x: x.arrival)  # sort proccesses according to arrival time
    while (1):
        for index in range(last_appended, len(processes)):
            if (time == processes[index].arrival):
                processes_queue.append(processes[index])
                last_appended = index
                # print(processes_queue[last_appended].status())
            else:
                last_appended = index
                break
        #print('untilTime ', untilTime)
        if (len(processes_queue) != 0):  # process queue has something

            if (untilTime == timeQuantum):  # timeQuantum is reached
                processes_queue.append(processes_queue.pop(0))  # first goes last
                untilTime = 0
            if (processes_queue[0].name != last_process_name):  # process changed
                ProcessedProcess.append(processes_queue[0].name)
                ProcessStartTime.append(time)
                ProcessedTime.append(0)
            # print(processes_queue[0].status(),"time :",time)
            last_process_name = processes_queue[0].name
            if (processes_queue[0].do_process() != None):  # top process still has remainnig BT
                ProcessedTime[-1] += 1
                #print(processes_queue[0].status(), ' time ', time)
            else:  # top process has finished
                #print("process", processes_queue[0].name, "is done")
                ProcessedTime[-1] += 1
                processes_queue.pop(0)
                untilTime = -1
                number_of_done += 1
        elif ((number_of_done == len(processes))):  # nothing in the process queue but all process were executed
            break
        else:  # gap
            untilTime = -1
        untilTime += 1
        untilTime = (untilTime % (timeQuantum + 1))  # untilTime goes 1..timeQuantum,1..
        time += 1
    numberofprocess = len(ProcessedProcess)
    Time = time







def Draw():
    ytick=[]
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()

    # Setting Y-axis limits
    gnt.set_ylim(0, int(len(ProcessedProcess))+2)
    # Setting X-axis limits
    gnt.set_xlim(0, int(Time) * 1.25)
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Process Numbers ')
    # Labelling tickes of y-axis
    for i in range(len(ProcessedProcess)):
        ytick.append(i+1)
    gnt.set_yticklabels(ProcessedProcess)
    gnt.set_yticks(ytick)
    # Setting graph attribute
    gnt.grid(True)

    # Declaring a bar in schedule
    for i in range(len(ProcessedProcess)):

        gnt.broken_barh([(int(ProcessStartTime[i]), int(ProcessedTime[i]))], (i ,1 ), facecolors=('black'))
    plt.show()







mainpage()

root.mainloop()










































