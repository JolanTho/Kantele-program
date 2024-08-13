# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:11:43 2024

@author: thomasj2
"""
import customtkinter as ctk
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


app = ctk.CTk() #creation of the window.
app.geometry("800x800") # Set the size of the window.


def linear_mass(StringNumber,Diameter,Density): # Calcul of linear mass.
    Mlin = []
    for i in range (StringNumber):
        a = m.pi*(pow(Diameter[i]/2,2))*Density # Formula to calculate the linear mass.
        Mlin.append(a)
    return Mlin

def Linear_mass_woundString (Density): # Calcul the linear mass of wound string
    H = float(DiaTorse.get())
    D = float(DiaCore.get())
    DensTorse = float(DensityTorse.get())
    MlinTorse = (pow(H/2,2)-pow(D/2,2))*m.pi*0.785*Density #Calcul the linear mass of the twisted part of the string.
    Mlinear = MlinTorse+pow(D/2,2)*m.pi*DensTorse #Calcul the linear mass of the string.
    return Mlinear

def MaxTension(pourcentage, R, Diameter, StringNumber): # Calcul the maximum tension the string can withstand for preset Kantel.
    T=[]
    for i in range (StringNumber):
        T.append((pow(Diameter[i]/2,2)*m.pi*R*pourcentage)/100)
        #round(T[i],2)
    return T

# Calcul of the length of strings.
def Length(StringNumber,Pitch,T, Diameter,Density): # Function to calculate the
    L = []                          #length of strings for preset Kantele.
    Mlin = linear_mass(StringNumber, Diameter, Density)
    for j in range (StringNumber):
        l = m.sqrt((T[j])/(Mlin[j]*4*pow(Pitch[j],2)))
        L.append(l)
    return L

def Tension_Calcul (L,Density,Pitch,Diameter):# Calcul of the tension of the string.
    if Wound.get()=="Yes":
        Mlin = Linear_mass_woundString(Density)
    else :
        Mlin = m.pi*(pow(Diameter/2,2))*Density # Calcul of the linear mass.
    if optionTensChar.get()=="Pourcentage of max tension":
        T=MaxTension_Calcul(Diameter)
    else :
        T = (Mlin*4*pow(L,2)*pow(Pitch,2)) # Calcul oh the tension.
    T = round(T,2)
    return T

def Diameter_Calcul (L,T,Pitch,Density): # Calcul of the diameterof the string.
    if Wound.get()=="Yes":
        Mlin = Linear_mass_woundString(Density)
    else :
        Mlin = T/(4*pow(L,2)*pow(Pitch,2)) # Calcul of the linear mass.
    Diameter = m.sqrt((4*Mlin)/(m.pi*Density)) # Calcul of the diameter.
    return round(Diameter,4)

def Length_Calcul (T,Density,Pitch,Diameter): # Calcul of the length of 1 string.
    if Wound.get()=="Yes":
        Mlin = Linear_mass_woundString(Density)
    else :
        Mlin = m.pi*(pow(Diameter/2,2))*Density # Calcul of the linear mass.
    L = m.sqrt((T)/(Mlin*4*pow(Pitch,2)))  # formula of the length calcul.
    return round(L,2)

def MaxTension_Calcul(Diameter): # Calcul of max tension for one string in the "Characteristic of the string" part.
    pourcentage = float(TensionEntry.get())  
    if MaterialPourcTens.get() == "Iron":
        R = 1750000000
    elif MaterialPourcTens.get() == "Brass":
        R= 770000000
    elif MaterialPourcTens.get() == "Nylon":
        R = 245000000
    elif MaterialPourcTens.get() == "Gut":
        R = 230000000
    else :
        R = 1000000000 # Not the good value
    T=(pow(Diameter/2,2)*m.pi*R*pourcentage)/100 #Formula for the maximal tension.
    round(T,2)
    return T

def ChoiceMaterial ():
    mat=MaterialChar.get()
    if mat == "Iron":
        Dens = 7800
        R = 1750000000
    elif mat == "Brass":
        Dens = 8600
        R= 770000000
    elif mat == "Nylon":
        Dens = 1000
        R = 245000000
    elif mat == "Gut":
        Dens = 1276
        R = 230000000
    else :
        Dens = 1791 
        R = 1000000000
    return Dens,R

def Note_TO_Freq (note, noteRef): #Function to convert note to frequency.
    ListeNotes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    if len(note)==3:
        octave = int(note[2])
        Keynumber = note[0:2]
        Keynumber = ListeNotes.index(Keynumber) #Get the octave and the note that the user put in the text box.
    else :
        octave=int(note[1])
        Keynumber = note[0:1]
        Keynumber = ListeNotes.index(Keynumber) #Get the octave and the note that the user put in the text box.
    if Keynumber < 3 :
        Keynumber = Keynumber + 12 + ((octave-1)*12)+1 #Calcul the number of cent between the actual note and the reference note.
    else :
        Keynumber = Keynumber + ((octave-1)*12)+1
    Frequency  =  noteRef * m.pow(2, (Keynumber - 49)/12) #Calcul the number of cent between the actual note and the reference note.
    print(Frequency)
    return round(Frequency,2)

def Choice_string_graph (R,Density,Diameter, L,Pitch): #Function wich display the second graph of "information about string"
    alpha=[]
    T=[]
    Zo=[]
    X=[]
    NbTens=20
    NbImp=4
    for i in range(1,51):                # x-axis of the graph.
        alpha.append(i*6)
    for iTens in range(NbTens):
        T.append([])
        for iCal in range(len(alpha)):                          # Create the tension lines to be displayed on the figure.
            T[iTens].append(m.sqrt(((iTens+1)*15)/(m.pow(alpha[iCal],2 )*Density*m.pi))*m.pow(10, 3))
    for iImp in range(NbImp):
        Zo.append([])
        for iCalcul in range(len(alpha)):                       # Create the impedance line to be displayed on the figure.
            Zo[iImp].append(m.sqrt((1*(0.8*(iImp+1)))/(m.pi*Density*alpha[iCalcul]))*m.pow(10, 3))
    BreakingPoint=m.sqrt((100*R)/(100*4*Density)) # Calcul of the breaking point of the string.
    AlmostBreakingPoint=m.sqrt((85*R)/(100*4*Density)) # Calcul of the point in 85% of the max tension.
    
    for iX in range(len(Pitch)):
        X.append(Pitch[iX]*L[iX])
    for iDia in range(len(Diameter)):
        Diameter[iDia]=Diameter[iDia]*m.pow(10,3)
    ax2.scatter(X,Diameter,zorder=4) # Display of the point corresponding to the characteristics of the string.
    
    for iT in range(len(T)):
        if 0.0658*(iT)>1:
            R=1
        else:
            R=0.0658*iT
        ax2.plot(alpha,T[iT],color=(R,0.0411*iT,0.0262*iT),zorder=1) # Display of the tension lines.
        
    for iZo in range(len(Zo)):
        ax2.plot(alpha,Zo[iZo],'--',color='magenta',zorder=2) # Display of the impedance lines.
        
    ax2.plot([BreakingPoint,BreakingPoint],[0,3],color='black',zorder=3) # Display of the breaking point.
    ax2.plot([AlmostBreakingPoint,AlmostBreakingPoint],[0,3],'--',color='black',zorder=4) # Display of 85% of the max tension.

    plt.ylim(0,3)
    plt.title("Kantele's strings")
    plt.ylabel('Diameter(mm)')
    plt.xlabel('Length (m) x frequencies (Hz)')
    
    canvas2.draw()
    canvas2.get_tk_widget().pack()

def Plot(StringNumber, Pitch, T, Diameter, Density,Note,R): #Function for display all result in the text box and the graph for preset Kantele.
    ax.cla() # Clean the plot.
    ax2.cla()
    L=Length(StringNumber, Pitch, T, Diameter, Density) #Get a table of alle the length of strings.
    PrintResult=""                                      #Create string variable tu put the result of the length calcul.
    PrintTensionInf=""                                  #Create string variable tu put the result of the tension calcul.
    PrintDiameterInf=""                                 #Create string variable tu put the result of the diameter calcul.
    PrintPitchInf=""                                    #Create string variable tu put the result of the pitch calcul.
    SpacingStrings = []                                 #Create a table for create the x axis of the plot.
    for k in range(StringNumber):                       # print all the result in the strings variable.
        SpacingStrings.append(k*1.9)
        PrintResult = PrintResult +"String"+ str(k+1)+" : "+str(round(L[k],2))+"m ; "
        PrintTensionInf = PrintTensionInf +"String"+ str(k+1)+" : "+str(round(T[k],2))+"N ; "
        PrintDiameterInf = PrintDiameterInf +"String"+ str(k+1)+" : "+str(Diameter[k])+"m ; "
        PrintPitchInf = PrintPitchInf +"String"+ str(k+1)+" : "+Note[k]+" ; "
    LengthInf.delete("0.0","end")                       # Clear text box.
    TensionInf.delete("0.0","end")                      #Clear text box.
    DiameterInf.delete("0.0","end")                     #Clear ext box.
    PitchInf.delete("0.0","end")                        #Clear text box.
    LengthInf.insert("0.0",str(PrintResult))            # Plot the lengths of the strings.
    TensionInf.insert("0.0",str(PrintTensionInf))       # Plot the tensions of the strings.
    DiameterInf.insert("0.0",str(PrintDiameterInf))     # Plot the diameter of the strings.
    PitchInf.insert("0.0",str(PrintPitchInf))           # Plot the Pitch of the strings.
    ax.bar(SpacingStrings,L)                            # plot of the graph.
    plt.Axes.plot
    plt.ylabel("Length of the strings (m)")
    canvas.draw()                                       # display of the graph in the window.
    canvas.get_tk_widget().pack() 
    Choice_string_graph (R,Density,Diameter, L,Pitch)

    
top_frame = ctk.CTkFrame(master=app, fg_color="black") # creation of the frame to seat all the widgets.
top_frame.pack(side="top",fill="both",expand=True)

bottom_frame = ctk.CTkFrame(master=app, fg_color="black")
bottom_frame.pack(side="top", fill="both", expand=True)

frame1 = ctk.CTkFrame(master=top_frame, fg_color="black")
frame1.pack(side="left", fill = "both", expand=True)

PresetLabel = ctk.CTkLabel(master=frame1, text="Preset Kantele", font=("Arial" ,20), text_color="#A987FF")
PresetLabel.pack() # Title of the preset Kantele

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

NbStrLabel = ctk.CTkLabel(master=frame1, text="Number of strings", text_color="#A987FF")
NbStrLabel.pack(pady=10)
NbStrings = ctk.CTkComboBox(master=frame1, values=["5 strings", "11 strings", "18 strings","26 strings"],command=combobox_callback)
NbStrings.pack(pady=3)

def Materials_callback(choice):
    print("combobox dropdown clicked:", choice)
    
MaterialLabel = ctk.CTkLabel(master=frame1, text="Choice of material", text_color="#A987FF")
MaterialLabel.pack(pady=3)
Material = ctk.CTkComboBox(master=frame1, values=["Iron","Brass","Nylon", "Gut", "Carbon"],command=Materials_callback)
Material.pack()

def optionTens_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    
EntryLabel = ctk.CTkLabel(master=frame1, text="Tensions of the strings", text_color="#A987FF")
EntryLabel.pack(pady=3)

optionTens = ctk.CTkOptionMenu(master = frame1, values=["Tension", "Percentage of max tension"], command=optionTens_callback, fg_color="#8454FF",button_color ="#723BFF",  button_hover_color="#723BFF")
optionTens.set("Tension")
optionTens.pack(pady=3)




entry = ctk.CTkEntry(master=frame1, placeholder_text="Tension")
entry.pack()



def Validate(): # Get the result of the combo-box of the nuöber et the materisl of the string and plot the result with the plot function.  
    print("button pressed")
    mat=Material.get()
    if mat == "Iron":
        Dens = 7800
        R = 1750000000
    elif mat == "Brass":
        Dens = 8600
        R= 770000000
    elif mat == "Nylon":
        Dens = 1000
        R = 245000000
    elif mat == "Gut":
        Dens = 1276
        R = 230000000
    else :
        Dens = 1791 
        R = 1000000000
    print(Dens)
    NbStr = NbStrings.get()
    if NbStr == "5 strings":
        Pitch = [293.665,329.628,369.994,391.995,440] # Pitch of string.
        Note = ["D4", "E4", "F#4", "G4", "A4"]
        Diameter = [0.0005,0.00045,0.0004,0.0004,0.00035] # Diameter of strings.
        StringNumber = 5;
    if NbStr == "11 strings":
        Pitch = [220,246.94,277.183,293.665,329.628,369.994,391.995,440,493.883,554.365,587.33] # Pitch of string.
        Note = ["A3","B3","C#4","D4", "E4", "F#4", "G4", "A4","B4","C#5","D5"]
        Diameter = [0.00055,0.0005,0.00045,0.00045,0.0004,0.0004,0.00035,0.00035,0.0003,0.0003,0.0003] # Diameter of strings.
        StringNumber = 11;
    if NbStr == "18 strings":
        Pitch = [196,220,246.94,261.53,293.665,329.628,349.23,391.995,440,493.883,523.25,587.33,659.25,698.46,783.99,880,987.77,1046.5] # Diameter of strings.
        Note = ["G3","A3","B3","C4","D4", "E4", "F4", "G4", "A4","B4","C5","D5","E5","F5","G5","A5","B5","C6"]
        Diameter = [0.00065,0.00055,0.0005,0.00045,0.00045,0.0004,0.0004,0.0004,0.00035,0.00035,0.00035,0.00035,0.0003,0.0003,0.00025,0.00025,0.00025,0.00025] # Diameter of strings
        StringNumber = 18
    if NbStr == "26 strings":
       Pitch = [130.81,146.83,164.81,174.61,196,220,246.94,261.63,293.665,329.628,349.23,391.995,440,493.883,523.33,587.33,659.25,698.46,783.99,880,987.77,1046.5,1174.66,1318.51,1396.91,1567.98] # Frenquencies of all strings
       Note = ["C3","D3","E3","F3","G3","A3","B3","C4","D4", "E4", "F4", "G4", "A4","B4","C5","D5","E5","F5","G5","A5","B5","C6","D6","E6","F6","G6"]
       Diameter = [0.0009,0.0009,0.00075,0.00075,0.00075,0.0007,0.0007,0.0007,0.00065,0.00065,0.00065,0.0006,0.0006,0.0006,0.00055,0.00055,0.00055,0.0005,0.0005,0.0005,0.00045,0.00045,0.00045,0.0004,0.0004,0.0004] # Diameter of each strings
       StringNumber = 26
    if optionTens.get()=="Percentage of max tension":
        pourcentage = float(entry.get())
        T = MaxTension(pourcentage, R, Diameter, StringNumber)
    else :
        T=[]
        for i in range(StringNumber):
            T.append(int(entry.get()))
    if check_var.get()=="Yes":
        WantDia = float(SameDia.get()) # Get the value of the desired diameter.
        Diameter = []
        for i in range(StringNumber):
            Diameter.append(WantDia)
    Plot(StringNumber, Pitch, T, Diameter, Dens, Note,R) #Plot the result.

Submit = ctk.CTkButton(master=frame1, text="Submit", command=Validate, fg_color="#8454FF", hover_color="#723BFF")
Submit.pack(pady=10)

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())
    if check_var.get()=="Yes":
        SameDia.pack(pady= 5)
    else:
        SameDia.pack_forget()
                
check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(master=frame1, text="Would you like to have strings of the same diameter ?", command=checkbox_event, variable=check_var, onvalue="Yes", offvalue="No")
checkbox.pack(pady = 5)

SameDia = ctk.CTkEntry(master=frame1, placeholder_text="Wanted diameter")


frame2 = ctk.CTkFrame(master=top_frame, fg_color="black")
frame2.pack(side="left", fill = "both", expand=True)

framechar = ctk.CTkFrame(master=frame2, fg_color="black") # Where the part "Characteristic of one string" is display.
framechar.pack(side="left", fill = "both", expand=True)

CharLabel = ctk.CTkLabel(master=framechar, text="Characteristic of one string", font=("Arial" ,20), text_color="#87A1FF")
CharLabel.pack()

LengthLabel = ctk.CTkLabel(master=framechar, text="Length (m)", text_color="#87A1FF")
LengthLabel.pack(pady=5, padx = 5)
LengthEntry = ctk.CTkEntry(master=framechar, placeholder_text="Length")
LengthEntry.pack( padx = 5)

DiameterLabel = ctk.CTkLabel(master=framechar, text="Diameter (m)", text_color="#87A1FF")
DiameterLabel.pack(pady=3,padx = 5)
DiameterEntry = ctk.CTkEntry(master=framechar, placeholder_text="Diameter")
DiameterEntry.pack(padx = 5)

TensionLabel = ctk.CTkLabel(master=framechar, text="Tension", text_color="#87A1FF")
TensionLabel.pack(pady=3, padx = 5)

optionTensChar = ctk.CTkOptionMenu(master = framechar, values=["Tension", "Percentage of max tension"], fg_color="#5479FF",button_color ="#3B65FF",  button_hover_color="#3B65FF")
optionTensChar.set("Tension")
optionTensChar.pack(pady=3)

TensionEntry = ctk.CTkEntry(master=framechar, placeholder_text="Tension")
TensionEntry.pack(padx = 5)

PitchLabel = ctk.CTkLabel(master=framechar, text="Note", text_color="#87A1FF")
PitchLabel.pack(pady=3, padx = 5)
NoteRefEntry = ctk.CTkEntry(master=framechar, placeholder_text="Reference note")
NoteRefEntry.pack(padx=5)
PitchEntry = ctk.CTkEntry(master=framechar, placeholder_text="Note")
PitchEntry.pack(padx = 5)


MaterialCharLabel = ctk.CTkLabel(master=framechar, text="Choice of material", text_color="#87A1FF")
MaterialCharLabel.pack(pady=3)
MaterialChar = ctk.CTkComboBox(master=framechar, values=["Iron","Brass","Nylon", "Gut", "Carbon"])
MaterialChar.pack()

def Clear(): # Supress all data of strings.
    global LS
    global n
    global f
    global Dia
    Dia=[]
    f=[]
    LS=[]
    n=0
    LengthInf.delete("0.0","end")
    TensionInf.delete("0.0","end")
    DiameterInf.delete("0.0","end")
    PitchInf.delete("0.0","end")
    ax.cla()
    ax2.cla()

Clear = ctk.CTkButton(master=framechar, text="Clear", command=Clear, fg_color="#5479FF", hover_color="#3B65FF", height=50, width=200)
Clear.pack(pady=10)

def Wound_box():   # Check if the wound string is selected or not.
    print("checkbox toggled, current value:", Wound.get())
    if Wound.get()=="Yes": #Display box to put the value of the diameter of the core and the torse of the string.
        DiaCore.pack(pady= 5)
        DensityTorse.pack(pady= 5)
        DiaTorse.pack(pady= 5)
    else:
        DiaCore.pack_forget()
        DensityTorse.pack_forget()
        DiaTorse.pack_forget()
                
Wound = ctk.StringVar(value="on")
WoundBox = ctk.CTkCheckBox(master=framechar, text="Is the string wound ?", command=Wound_box, variable=Wound, onvalue="Yes", offvalue="No")
WoundBox.pack(pady = 5)

DiaCore = ctk.CTkEntry(master=framechar, placeholder_text="Core Wanted diameter")
DensityTorse = ctk.CTkEntry(master=framechar, placeholder_text="Torse density")
DiaTorse = ctk.CTkEntry(master=framechar, placeholder_text="Torse Wanted diameter")

frameCal = ctk.CTkFrame(master=frame2, fg_color="black") #Where the part "Calculation of the unknowas parameters" is display.
frameCal.pack(side="left", fill = "both", expand=True)

CalLabel = ctk.CTkLabel(master=frameCal, text="Calculation of the unknows parameters", font=("Arial" ,20), text_color="#87A1FF")
CalLabel.pack()

TensionCalLabel = ctk.CTkLabel(master=frameCal, text="Tension", text_color="#87A1FF")
TensionCalLabel.pack(pady=5, padx = 10)
TensionCalEntry = ctk.CTkEntry(master=frameCal, placeholder_text="Tension")
TensionCalEntry.pack( padx = 10)

def Tenscal(): #get the entry of all text box from the part "unique Kantele" and calculate tension.
    L = float(LengthEntry.get())
    (D,R) = ChoiceMaterial()
    Frequency = PitchEntry.get()
    Refnote = int(NoteRefEntry.get())
    Pitch = Note_TO_Freq(Frequency, Refnote)
    if Wound.get()=="Yes":
        Diameter = float(DiaTorse.get())
    else :
        Diameter = float(DiameterEntry.get())
    T = Tension_Calcul(L, D, Pitch, Diameter)
    TensionCalEntry.delete("0","end")
    TensionCalEntry.insert("0",str(T))
   
TCal = ctk.CTkButton(master=frameCal, text="Calculate tension", command=Tenscal, fg_color="#5479FF", hover_color="#3B65FF")
TCal.pack()


DiameterCalLabel = ctk.CTkLabel(master=frameCal, text="Diameter (m)", text_color="#87A1FF")
DiameterCalLabel.pack(pady=3,padx = 5)
DiameterCalEntry = ctk.CTkEntry(master=frameCal, placeholder_text="Diameter")
DiameterCalEntry.pack(padx = 5)

def Diacal(): # Same as "Tenscal" but calculate the diameter.
   L = float(LengthEntry.get())
   (D,R) = ChoiceMaterial()
   Frequency = PitchEntry.get()
   Refnote = int(NoteRefEntry.get())
   Pitch = Note_TO_Freq(Frequency, Refnote)
   T = float(TensionEntry.get())
   Diameter = Diameter_Calcul(L, T, Pitch, D)
   DiameterCalEntry.delete("0","end")
   DiameterCalEntry.insert("0",str(Diameter))
    
DiaCal = ctk.CTkButton(master=frameCal, text="Calculate diameter", command=Diacal, fg_color="#5479FF", hover_color="#3B65FF")
DiaCal.pack()

LengthCalLabel = ctk.CTkLabel(master=frameCal, text="Length (m)", text_color="#87A1FF")
LengthCalLabel.pack(pady=3, padx = 5)
LengthCalEntry = ctk.CTkEntry(master=frameCal, placeholder_text="Length")
LengthCalEntry.pack( padx = 5)

def Lengthcal(): # Same as "Tenscal" but calculate the length.
    print("button pressed")
    (D,R) = ChoiceMaterial()
    Frequency = PitchEntry.get()
    Refnote = int(NoteRefEntry.get())
    Pitch = Note_TO_Freq(Frequency, Refnote)
    if Wound.get()=="Yes":
        Diameter = float(DiaTorse.get())
    else :
        Diameter = float(DiameterEntry.get())
    if optionTensChar.get()=="Pourcentage of max tension":
        T= MaxTension_Calcul(Diameter)
    else :
        T = float(TensionEntry.get())
    L = Length_Calcul(T, D, Pitch, Diameter) 
    LengthCalEntry.delete("0","end")
    LengthCalEntry.insert("0",str(L))
   
LengthCal = ctk.CTkButton(master=frameCal, text="Calculate length", command=Lengthcal, fg_color="#5479FF", hover_color="#3B65FF")
LengthCal.pack()

n=0
LS=[]
Dia = []
Tens = []
Freq = []
f=[]

def AddStringCal(): # Add all the parameter of a string in different table and display the characteristics.
    print("button pressed")
    plt.cla()
    global n 
    n=n+1
    Length=LengthEntry.get()
    Diameter = DiameterEntry.get()
    Tension = TensionEntry.get()
    Frequency = PitchEntry.get()
    if Length =="":
        Length = float(LengthCalEntry.get())
    else:
        Length = float(Length)
    LS.append(Length)
    if Wound.get()== "Yes":
        Diameter = float(DiaTorse.get())
    elif Diameter =="":
        Diameter = float(DiameterCalEntry.get())
    else:
        Diameter=float(Diameter)
    Dia.append(Diameter)
    if optionTensChar.get()=="Pourcentage of max tension":
        Tension = MaxTension_Calcul(Diameter)
    if Tension =="" and optionTensChar.get()=="Tension":
        Tension= float(TensionCalEntry.get())
    if TensionCalEntry.get()=="" and optionTensChar.get()=="Tension":
        Tension = float(Tension)
    Tens.append(Tension)
    Freq.append(Frequency)
    SpacingString = []
    for i in range (n):
        SpacingString.append(i*1.19)
    Result = ""
    for a in range(n):
        Result = Result+" "+"String"+str(a+1)+" : "+ str(LS[a])+"m"+" ; "
    ResultDia=""
    for a in range(n):
        ResultDia = ResultDia+" "+"String"+str(a+1)+" : "+ str(Dia[a])+"m"+" ; "
    ResultPitch=""
    for a in range(n):
        ResultPitch = ResultPitch+" "+"String"+str(a+1)+" : "+ str(Freq[a])+" ; "
    ResultTens=""
    for a in range(n):
        ResultTens = ResultTens+" "+"String"+str(a+1)+" : "+ str(Tens[a])+"N"+" ; "
    LengthInf.delete("0.0","end")
    TensionInf.delete("0.0","end")
    DiameterInf.delete("0.0","end")
    PitchInf.delete("0.0","end")
    LengthInf.insert("0.0",str(Result))
    TensionInf.insert("0.0",str(ResultTens))
    DiameterInf.insert("0.0",str(ResultDia))
    PitchInf.insert("0.0",str(ResultPitch))
    ax.bar(SpacingString,LS,color='blue')
    plt.Axes.plot
    canvas.draw()
    canvas.get_tk_widget().pack()
    Frequency = PitchEntry.get()
    Refnote = int(NoteRefEntry.get())
    f.append(Note_TO_Freq(Frequency, Refnote))
    (D,R) = ChoiceMaterial()
    Choice_string_graph(R, D, Dia, LS, f)
   
    
    
    
AddString = ctk.CTkButton(master=frameCal, text="Add String", command=AddStringCal, fg_color="#5479FF", hover_color="#3B65FF", height=50, width=200)
AddString.pack(pady = 10)
"""
def PourcTens():
    print("checkbox toggled, current value:", PourcTens_var.get())
    if PourcTens_var.get()=="Yes":
        PourcTensLabel.pack(pady=5)
        MaterialPourcTens.pack()
        PourcTensValue.pack(pady= 5)
    else:
        PourcTensLabel.pack_forget()
        MaterialPourcTens.pack_forget()
        PourcTensValue.pack_forget()
                
PourcTens_var = ctk.StringVar(value="on")
PourcTensbox = ctk.CTkCheckBox(master=frameCal, text="Would you like to enter the pourcentage of max tension ?", command=PourcTens, variable=PourcTens_var, onvalue="Yes", offvalue="No")
PourcTensbox.pack(pady = 5)
"""

def MaterialsPourcTens_callback(choice):
    print("combobox dropdown clicked:", choice)

PourcTensLabel = ctk.CTkLabel(master=frameCal, text="Material of the string", text_color="#87A1FF")
MaterialPourcTens = ctk.CTkComboBox(master=frameCal, values=["Iron","Brass","Nylon", "Gut", "Carbon"],command=MaterialsPourcTens_callback)

PourcTensValue = ctk.CTkEntry(master=frameCal, placeholder_text="Pourcentage of tension")

frame3 = ctk.CTkFrame(master=bottom_frame, fg_color="black")
frame3.pack(side="left", fill = "both", expand=True)

frameInf = ctk.CTkScrollableFrame(master=frame3, fg_color="black", scrollbar_button_color="#DA54FF", scrollbar_button_hover_color="#D43BFF")
frameInf.pack(side="left", fill = "both", expand=True) # Frame with all the table information.

TitleInf = ctk.CTkLabel(master=frameInf, text="Information about strings", font=("Arial" ,20), text_color="#E587FF")
TitleInf.pack()

LengthLabel = ctk.CTkLabel(master=frameInf, text="Length of strings", text_color="#E587FF")
LengthLabel.pack()
LengthInf = ctk.CTkTextbox(master=frameInf, height=60) #Print the result of length im a text box.
LengthInf.pack(fill="x", pady=10)

TensionInfLabel = ctk.CTkLabel(master=frameInf, text="Tension of the strings", text_color="#E587FF")
TensionInfLabel.pack()
TensionInf = ctk.CTkTextbox(master=frameInf, height=60) #Print the result of length im a text box.
TensionInf.pack(fill="x", pady=10)

DiameterInfLabel = ctk.CTkLabel(master=frameInf, text="Diameter of strings", text_color="#E587FF")
DiameterInfLabel.pack()
DiameterInf = ctk.CTkTextbox(master=frameInf, height=60) #Print the result of length im a text box.
DiameterInf.pack(fill="x", pady=10)

PitchInfLabel = ctk.CTkLabel(master=frameInf, text="Pitch of strings", text_color="#E587FF")
PitchInfLabel.pack()
PitchInf = ctk.CTkTextbox(master=frameInf, height=60) #Print the result of length im a text box.
PitchInf.pack(fill="x", pady=10)


framePlot = ctk.CTkScrollableFrame(master=frame3, fg_color="black", scrollbar_button_color="#DA54FF", scrollbar_button_hover_color="#D43BFF")
framePlot.pack(side="left", fill = "both", expand=True) #Frame with the graph

Titlegraph = ctk.CTkLabel(master=framePlot, text="Display of length of strings", font=("Arial" ,20), text_color="#E587FF")
Titlegraph.pack(pady=10)
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig,master=framePlot)
fig2, ax2 = plt.subplots()
canvas2 = FigureCanvasTkAgg(fig2,master=framePlot)



app.mainloop()  
