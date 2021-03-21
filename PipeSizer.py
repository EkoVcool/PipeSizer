# -*- coding: utf-8 -*-
"""
Pipe Sizer v0.2

Created on Fri Jan 22 10:22:24 2021

@author: erik
"""

from tkinter import *

pi =3.14159

top = Tk()
top.title('PIPE SIZER')
top.geometry('256x125')
    
options = ["PVC","HDPE"]

pipetype = StringVar()
pipetype.set("PVC")
drop = OptionMenu(top,pipetype,*options)
drop.grid(row=3,column=3,columnspan=2,sticky='W')
drop.config(width = 5,height = 1)

top.iconbitmap('C:/Program Files/Pipe Sizer/icons8-piping-96.ico')

L1 = Label(top, text = "Flowrate:").grid(row=1,column=0,sticky='W')
L2 = Label(top, text = "Velocity:").grid(row=2,column=0,sticky='W')
L3 = Label(top, text = "Pipe Dia.:").grid(row=3,column=0,sticky='W')


v = StringVar()
u = StringVar()
t = StringVar()
r = StringVar()


E1 = Entry(top, textvariable=v, justify=CENTER,width=20).grid(row=1,column=1,sticky='W')
E2 = Entry(top, textvariable=u, justify=CENTER,width=20).grid(row=2,column=1,sticky='W')
E3 = Entry(top, textvariable=t, justify=CENTER,width=20).grid(row=3,column=1,sticky='W')

L4 = Label(top, textvariable=r, fg='red',wraplength=250).grid(row=4,column=0,rowspan=2,columnspan=4,sticky='W')
L5 = Label(top, text = 'Gravity: 2ft/s   Suction: 3ft/s   Discharge: 5ft/s').grid(row=7,column=0,columnspan=4,sticky='W')


#Creates a class object for keeping track of pipe size data
class PipeSize:
    def __init__(self,standard,metric,decimal,area):
        self.standard = standard
        self.metric = metric
        self.decimal = decimal
        self.area = area
        
#Creates a master list of pipe size objects using the PipeSize class
def PipeType(pipetype):
    #List of Standard Schedule 80 interior pipe diameters
    pipestandarddiam = [0.526,0.722,0.936,1.255,1.476,1.913,2.290,2.864,3.786,5.709,7.565,9.493,11.294,12.41,14.213,16.014,17.814,21.418]
    pipestandarddiamHDPE = [2.08,3.07,3.95,5.81,7.57,9.43,11.19,12.29,14.04,15.80,17.55,19.31,21.06,24.57,26.33,28.08,31.60,36.86,42.13]
    
    PipeList = []

    if pipetype == 'PVC':
        
        #Calculates areas based on the standard pipe diameter list and adds them to a new list
        a = 0
        pipestandarea = []
        while a < len(pipestandarddiam):  
            pipestandarea.append(pi*((pipestandarddiam[a]/2)/12)**2)
            a = a + 1
        
        del PipeList[:]
        PipeList.append(PipeSize('1/2', '15mm', 0.5, pipestandarea[0]))
        PipeList.append(PipeSize('3/4', '20mm', 0.75, pipestandarea[1])) 
        PipeList.append(PipeSize('1', '25mm', 1, pipestandarea[2]))
        PipeList.append(PipeSize('1-1/4', '32mm', 1.25, pipestandarea[3]))        
        PipeList.append(PipeSize('1-1/2', '40mm', 1.5, pipestandarea[4]))
        PipeList.append(PipeSize('2', '50mm', 2, pipestandarea[5]))
        PipeList.append(PipeSize('2-1/2', '65mm', 2.5, pipestandarea[6]))
        PipeList.append(PipeSize('3', '80mm', 3, pipestandarea[7]))
        PipeList.append(PipeSize('4', '100mm', 4, pipestandarea[8]))
        PipeList.append(PipeSize('6', '150mm', 6, pipestandarea[9]))
        PipeList.append(PipeSize('8', '200mm', 8, pipestandarea[10]))
        PipeList.append(PipeSize('10', '250mm', 10, pipestandarea[11]))
        PipeList.append(PipeSize('12', '300mm', 12, pipestandarea[12]))
        PipeList.append(PipeSize('14', '350mm', 14, pipestandarea[13]))
        PipeList.append(PipeSize('16', '400mm', 16, pipestandarea[14]))
        PipeList.append(PipeSize('18', '450mm', 18, pipestandarea[15]))
        PipeList.append(PipeSize('20', '500mm', 20, pipestandarea[16]))
        PipeList.append(PipeSize('24', '600mm', 24, pipestandarea[17]))

    elif pipetype == 'HDPE':
        
        a0 = 0
        pipestandareaHDPE = []
        while a0 < len(pipestandarddiamHDPE):  
            pipestandareaHDPE.append(pi*((pipestandarddiamHDPE[a0]/2)/12)**2)
            a0 = a0 + 1
    
        del PipeList[:]
        PipeList.append(PipeSize('2', '50mm', 2, pipestandareaHDPE[0]))
        PipeList.append(PipeSize('3', '80mm', 3, pipestandareaHDPE[1]))
        PipeList.append(PipeSize('4', '100mm', 4, pipestandareaHDPE[2]))
        PipeList.append(PipeSize('6', '150mm', 6, pipestandareaHDPE[3]))
        PipeList.append(PipeSize('8', '200mm', 8, pipestandareaHDPE[4]))
        PipeList.append(PipeSize('10', '250mm', 10, pipestandareaHDPE[5]))
        PipeList.append(PipeSize('12', '300mm', 12, pipestandareaHDPE[6]))
        PipeList.append(PipeSize('14', '350mm', 14, pipestandareaHDPE[7]))
        PipeList.append(PipeSize('16', '400mm', 16, pipestandareaHDPE[8]))
        PipeList.append(PipeSize('18', '450mm', 18, pipestandareaHDPE[9]))
        PipeList.append(PipeSize('20', '500mm', 20, pipestandareaHDPE[10]))
        PipeList.append(PipeSize('22', '550mm', 22, pipestandareaHDPE[11]))
        PipeList.append(PipeSize('24', '600mm', 24, pipestandareaHDPE[12]))
        PipeList.append(PipeSize('28', '700mm', 28, pipestandareaHDPE[13]))
        PipeList.append(PipeSize('30', '750mm', 30, pipestandareaHDPE[14]))
        PipeList.append(PipeSize('32', '800mm', 32, pipestandareaHDPE[15]))
        PipeList.append(PipeSize('36', '900mm', 36, pipestandareaHDPE[16]))
        PipeList.append(PipeSize('42', '1000mm', 42, pipestandareaHDPE[17]))
        PipeList.append(PipeSize('48', '1200mm', 48, pipestandareaHDPE[18]))
        
    return PipeList

def PipeArea(PipeList):
    a0 = 0
    pipestandarea = []
    while a0 < len(PipeList):
        pipestandarea.append(PipeList[a0].area)
        a0 = a0 + 1
    return pipestandarea

def PipeSizeS(PipeList):
    a1 = 0
    pipesizestandard = []
    while a1 < len(PipeList):  
        pipesizestandard.append(PipeList[a1].standard)
        a1 = a1 + 1
    return pipesizestandard
    
def PipeSizeD(PipeList):    
    a2 = 0
    pipesizedecimal =[]
    while a2 < len(PipeList):  
        pipesizedecimal.append(PipeList[a2].decimal)
        a2 = a2 + 1
    return pipesizedecimal

#Creating a dictionary from the area list for key reference information
def PipeDictArea(PipeList):    
    z1 = 1        
    pipedictarea = {PipeList[0].area : 0}   
    while z1 < len(PipeList):    
        pipedictarea[PipeList[z1].area] = z1 
        z1 = z1 + 1
    return pipedictarea

#Creating a dictionary from the standard list for key reference information        
def PipeDictS(PipeList):
    z2 = 1
    pipedictstandard = {PipeList[0].standard : 0}   
    while z2 < len(PipeList):    
        pipedictstandard[PipeList[z2].standard] = z2 
        z2 = z2 + 1
    return pipedictstandard
        
#Creating a dictionary from the decimal for key reference information
def PipeDictD(PipeList):
    z3 = 1
    pipedictdecimal = {PipeList[0].decimal : 0}   
    while z3 < len(PipeList):    
        pipedictdecimal[PipeList[z3].decimal] = z3 
        z3 = z3 + 1
    return pipedictdecimal
        
#Function to compare a calculated output to a list of numbers
def closest(x,y):
    return x[min(range(len(x)), key = lambda i: abs(x[i]-y))]

##################################################################################################################

#Function used to calculate the recommended pipe diameter based on system flowrate and desired water velocity
def find_diam(flowrate_input,velocity_input,pipe_list):
 
    #Flowrate and velocity input prompts
    #flowrate_input = str(input('Enter the flowrate through pipe (gpm):   '))
    #velocity_input = str(input('Enter the desired velocity through pipe (ft/s):   '))
    
    PipeList = pipe_list
    pipestandarea = PipeArea(pipe_list)
    pipedictarea = PipeDictArea(pipe_list)

    #Code that checks to make sure the inputs are positive numbers and give error message if inputs aren't
    k = 0
    j = 0
    l = 0
    while k < 1 and j < 1 and l < 1:
        #Checks to make sure the flowrate input is a number
        try:
            float(flowrate_input)
        except:
            r.set('ERROR: Flowrate must be a number.')
            return
        else:
            flowrate_input = float(flowrate_input)
            k = 1
        #Checks to make sure the velocity input is a number   
        try:
            float(velocity_input)
        except:
            r.set('ERROR: Velocity must be a number.')
            return
        else:
            velocity_input = float(velocity_input)
            j = 1
        #Checks to see if both velocity and flowrate are possitive numbers    
        if flowrate_input > 0 and velocity_input > 0:
            l = 1
        else:
            r.set('ERROR: Numbers must be POSITIVE.')
            return
    
    #Converts flowrate input from gallons per minute to cubic feet per second
    flowrate_convert = flowrate_input/448.83
    
    #Converts flowrat input from gallons per minute to cubit meters per hour
    flowrate_convertm = flowrate_input/4.402868
    
    #Calculates the needed area of the pipe based on the inputs using equation Q=VA
    exact_area = flowrate_convert/velocity_input
    
    #Uses the closest function to determine which standard pipe area is closest to the needed area calculated
    recommended_area = closest(pipestandarea, exact_area)
    
    #Uses the recommended standardized pipe size area to calculate the water velocity through this new area
    vel_recom_dia = flowrate_convert/recommended_area
    
    #Converts the new water velocity from feet per second to meters per second
    velocity_convertm = vel_recom_dia*0.3048
    
    #Compares the recommended pipe area to the areas in the pipe area dictionary to find its key
    res = None 
    if recommended_area in set(pipestandarea).intersection(pipedictarea): 
        res = pipedictarea[recommended_area] 
    
    
    if vel_recom_dia <= 6: 
        
        v.set('%dgpm [%dCMH]' %(flowrate_input, flowrate_convertm))
        t.set('%sinch [%s]' %(PipeList[res].standard,PipeList[res].metric))
        u.set('%.1fft/s [%.1fm/s]' %(vel_recom_dia, velocity_convertm))
        
    else:
        res = abs(res + 1)
        vel_recom_dia = flowrate_convert/pipestandarea[res]
        velocity_convertm = vel_recom_dia*0.3048
        
        v.set('%dgpm [%dCMH]' %(flowrate_input, flowrate_convertm))
        t.set('%sinch [%s]' %(PipeList[res].standard,PipeList[res].metric))
        u.set('%.1fft/s [%.1fm/s]' %(vel_recom_dia, velocity_convertm))
        
    return

##################################################################################################################

#Function used to calculate the water velocity base on specified flowrate and pipe diameter             
def find_velo(flowrate_input,pipe_diam_input,pipe_list):
    
    PipeList = pipe_list
    pipestandarea = PipeArea(pipe_list)
    pipesizestandard = PipeSizeS(pipe_list)
    pipesizedecimal = PipeSizeD(pipe_list)
    PipeDictStandard = PipeDictS(pipe_list)
    PipeDictDecimal = PipeDictD(pipe_list)
    
    #Code that checks to make sure the inputs are positive numbers and give error message if inputs aren't
    k = 0
    j = 0
    l = 0
    res = None
    while k < 1 and j < 1 and l < 1:
        
        #Checks to make sure the pipe size input is valid
        try:
            float(pipe_diam_input)
        except:
            if pipe_diam_input in set(pipesizestandard).intersection(PipeDictStandard): 
                res = PipeDictStandard[pipe_diam_input]
                k = 1
            else:
                r.set('ERROR: Invalid pipe diameter.')
                return
        else:
            pipe_diam_input = float(pipe_diam_input)
            if pipe_diam_input in set(pipesizedecimal).intersection(PipeDictDecimal): 
                res = PipeDictDecimal[pipe_diam_input]
                k = 1
            else:
                r.set('ERROR: Invalid pipe diameter.')
                return
            
        #Checks to make sure the flowrate input is a number   
        try:
            float(flowrate_input)
        except:
            r.set('ERROR: Flowrate must be a number.')
            return
        else:
            flowrate_input = float(flowrate_input)
            j = 1
        #Checks to see if velocity is a positive number  
        if flowrate_input > 0:
            l = 1
        else:
            r.set('ERROR: Numbers must be POSITIVE.')
            return
    
    #Converts flowrate input from gallons per minute to cubic feet per second
    flowrate_convert = flowrate_input/448.83
    
    #Converts flowrat input from gallons per minute to cubit meters per hour
    flowrate_convertm = flowrate_input/4.402868
    
    #Calculates the velocity of the pipe based on the inputs using equation Q=VA
    velocity_calc = flowrate_convert/pipestandarea[res]
    
    #Converts the new water velocity from feet per second to meters per second
    velocity_convertm = velocity_calc*0.3048
    
    v.set('%dgpm [%dCMH]' %(flowrate_input, flowrate_convertm))
    t.set('%sinch [%s]' %(PipeList[res].standard,PipeList[res].metric))
    u.set('%.1fft/s [%.1fm/s]' %(velocity_calc, velocity_convertm))
    
    return

##################################################################################################################

#Function used to calculate the system flowrate based on specified water velocity and pipe diameter   
def find_flow(velocity_input,pipe_diam_input,pipe_list):
    
    PipeList = pipe_list
    pipestandarea = PipeArea(pipe_list)
    pipesizestandard = PipeSizeS(pipe_list)
    pipesizedecimal = PipeSizeD(pipe_list)
    PipeDictStandard = PipeDictS(pipe_list)
    PipeDictDecimal = PipeDictD(pipe_list)
    
    
    #Code that checks to make sure the inputs are positive numbers and give error message if inputs aren't
    k = 0
    j = 0
    l = 0
    res = None
    while k < 1 and j < 1 and l < 1:
        
        #Checks to make sure the pipe size input is valid
        try:
            float(pipe_diam_input)
        except:
            if pipe_diam_input in set(pipesizestandard).intersection(PipeDictStandard): 
                res = PipeDictStandard[pipe_diam_input]
                k = 1
            else:
                r.set('ERROR: Invalid pipe diameter.')
                return
        else:
            pipe_diam_input = float(pipe_diam_input)
            if pipe_diam_input in set(pipesizedecimal).intersection(PipeDictDecimal): 
                res = PipeDictDecimal[pipe_diam_input]
                k = 1
            else:
                r.set('ERROR: Invalid pipe diameter.')
                return
            
        #Checks to make sure the velocity input is a number   
        try:
            float(velocity_input)
        except:
            r.set('ERROR: Velocity must be a number.')
            return
        else:
            velocity_input = float(velocity_input)
            j = 1
        #Checks to see if velocity is a positive number  
        if velocity_input > 0:
            l = 1
        else:
            r.set('ERROR: Numbers must be POSITIVE.')
            return
        
    #Calculates the flowrate of the pipe based on the inputs using equation Q=VA
    flowrate_calc = velocity_input*pipestandarea[res]
    
    #Converts flowrate input from gallons per minute to cubic feet per second
    flowrate_convert = flowrate_calc*448.83
    
    #Converts flowrat input from gallons per minute to cubit meters per hour
    flowrate_convertm = flowrate_convert/4.402868
    
    #Converts the new water velocity from feet per second to meters per second
    velocity_convertm = velocity_input*0.3048
    
    v.set('%dgpm [%dCMH]' %(flowrate_convert, flowrate_convertm))
    t.set('%sinch [%s]' %(PipeList[res].standard,PipeList[res].metric))
    u.set('%.1fft/s [%.1fm/s]' %(velocity_input, velocity_convertm))
    
    
##################################################################################################################    


def Clear():
    v.set('')
    u.set('')
    t.set('')
    r.set('')

def Calculate():
    PipeList = PipeType(pipetype.get())
    B1.focus_set()
    m = v.get()
    n = u.get()
    o = t.get()

    if len(m) != 0 and len(n) != 0 and len(o) == 0:
        find_diam(m,n,PipeList)
        
    elif len(m) != 0 and len(n) == 0 and len(o) != 0:
        find_velo(m,o,PipeList)
        
    elif len(m) == 0 and len(n) != 0 and len(o) != 0:
        find_flow(n,o,PipeList)
        
    else:
        Clear()
        return
    
B1 = Button(top, text='Calculate', command=Calculate,width=9,height=1, bg = 'deep sky blue')
B1.grid(row=1, column=3,sticky='W')
B2 = Button(top, text='Clear', command=Clear,width=9,height=1, bg = 'indian red')
B2.grid(row=2, column=3,sticky='W')

top.bind('<Return>', lambda event=None: B1.invoke())
top.bind('<Delete>', lambda event=None: B2.invoke())

top.mainloop()