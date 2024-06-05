# Simply pure pain doing these equations
import tkinter as tk
import math

#Fixed pi variable
PI = math.pi

def choice():
    def calccylinder():
        x = PI * float(cylinderentry.get())**2 * float(cylinderentry1.get())
        y = PI * float(cylinderentry.get())**2 * 2 + 2 * float(cylinderentry.get()) * PI * float(cylinderentry1.get())
        cylinderanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calcsphere():
        x = PI * 4/3 * float(sphereentry.get())**3
        y = 4 * PI * float(sphereentry.get())**2
        sphereanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calcprism():
        # Calculating the height of triangles (Pythagorean Theorem)
        z = math.sqrt(float(prismentry.get()) ** 2 + (float(prismentry.get())/2) ** 2)
        x = (float(prismentry.get())*z)/2 * float(prismentry1.get())
        y = float(prismentry.get())*z + float(prismentry.get()) *3 * float(prismentry1.get())
        prismanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calcquader():
        x = float(quaderentry3.get()) * float(quaderentry2.get()) * float(quaderentry1.get())
        y = 2 * (float(quaderentry3.get()) * float(quaderentry2.get()) + float(quaderentry2.get()) * float(quaderentry1.get()) + float(quaderentry3.get()) * float(quaderentry1.get()))
        quaderanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calcpyramid():
        x = float(pyramidentry1.get()) ** 2 * float(pyramidentry2.get()) / 3
        # Calculating the height of triangles (Pythagorean Theorem)
        z = math.sqrt(float(pyramidentry2.get()) ** 2 - (float(pyramidentry1.get())/2) ** 2)
        y = float(pyramidentry1.get())*z*2 + float(pyramidentry1.get())**2
        pyramidanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calccone():
        x = float(coneentry1.get()) ** 2 * PI * float(coneentry2.get()) / 3
        # Calculating the side (Pythagorean Theorem)
        z = math.sqrt(float(coneentry2.get())**2 + float(coneentry1.get())**2)
        y = PI * float(coneentry1.get()) * z + PI * float(coneentry1.get())**2
        coneanswer.config(text="Volume: " + str(x) + " cm³\nOberflächeninhalt: " + str(y) + " cm²")
    def calccube():
        x = float(cubeentry.get()) ** 3
        y = float(cubeentry.get()) ** 2 * 6
        cubeanswer.config(text= "Volume: " + str(x) + " cm³ \nOberflächeninhalt: " + str(y) + " cm2")

    if (x.get()==0): #Window for cube
        cubemain = tk.Toplevel()
        cubemain.geometry("500x100")
        cubemain.title("Würfel berechnen")

        cubelabel = tk.Label(cubemain, text='Gib die Seite a an')
        cubelabel.pack()

        cubeentry = tk.Entry(cubemain)
        cubeentry.pack()

        cubebutton = tk.Button(cubemain, text='Submit', command= calccube)
        cubebutton.pack()

        cubeanswer = tk.Label(cubemain)
        cubeanswer.pack()

        cubemain.mainloop()
    elif (x.get()==1): #Window for cone
        conemain = tk.Toplevel()
        conemain.geometry("500x140")
        conemain.title("Kegel berechnen")

        conelabel1 = tk.Label(conemain, text='Gib den Radius an')
        conelabel1.pack()

        coneentry1 = tk.Entry(conemain)
        coneentry1.pack()

        conelabel2 = tk.Label(conemain, text='Gib die Höhe an')
        conelabel2.pack()

        coneentry2 = tk.Entry(conemain)
        coneentry2.pack()

        conebutton = tk.Button(conemain, text='Submit', command=calccone)
        conebutton.pack()

        coneanswer = tk.Label(conemain)
        coneanswer.pack()

        conemain.mainloop()
    elif (x.get() == 2): #Window for pyramide
        pyramidmain = tk.Toplevel()
        pyramidmain.geometry("500x140")
        pyramidmain.title("Pyramide berechnen")

        pyramidlabel1 = tk.Label(pyramidmain, text='Gib die Seite a an')
        pyramidlabel1.pack()

        pyramidentry1 = tk.Entry(pyramidmain)
        pyramidentry1.pack()

        pyramidlabel2 = tk.Label(pyramidmain, text='Gib die Höhe an')
        pyramidlabel2.pack()

        pyramidentry2 = tk.Entry(pyramidmain)
        pyramidentry2.pack()

        pyramidbutton = tk.Button(pyramidmain, text='Submit', command=calcpyramid)
        pyramidbutton.pack()

        pyramidanswer = tk.Label(pyramidmain)
        pyramidanswer.pack()
        pyramidmain.mainloop()
    elif (x.get() == 3): #Window for Quader
        quadermain = tk.Toplevel()
        quadermain.geometry("500x180")
        quadermain.title("Quader berechnen")

        quaderlabel1 = tk.Label(quadermain, text='Gib die Seite a an')
        quaderlabel1.pack()

        quaderentry1 = tk.Entry(quadermain)
        quaderentry1.pack()

        quaderlabel2 = tk.Label(quadermain, text='Gib die Seite b an')
        quaderlabel2.pack()

        quaderentry2 = tk.Entry(quadermain)
        quaderentry2.pack()

        quaderlabel3 = tk.Label(quadermain, text='Gib die Seite c an')
        quaderlabel3.pack()

        quaderentry3 = tk.Entry(quadermain)
        quaderentry3.pack()

        quaderbutton = tk.Button(quadermain, text='Submit', command=calcquader)
        quaderbutton.pack()

        quaderanswer = tk.Label(quadermain)
        quaderanswer.pack()
        quadermain.mainloop()
    elif (x.get() == 4): #Window for prism
        prismmain = tk.Toplevel()
        prismmain.geometry("500x160")
        prismmain.title("Prisma berechnen")

        prismnote = tk.Label(prismmain, text="Alle Seiten der Grundflächen müssen gleich sein!!!")
        prismnote.pack()

        prismlabel = tk.Label(prismmain, text='Gib die Seite a an')
        prismlabel.pack()

        prismentry = tk.Entry(prismmain)
        prismentry.pack()

        prismlabel1 = tk.Label(prismmain, text='Gib die Höhe an')
        prismlabel1.pack()

        prismentry1 = tk.Entry(prismmain)
        prismentry1.pack()

        prismbutton = tk.Button(prismmain, text='Submit', command=calcprism)
        prismbutton.pack()

        prismanswer = tk.Label(prismmain)
        prismanswer.pack()
        prismmain.mainloop()
    elif(x.get()==5): #window for sphere
        spheremain = tk.Toplevel()
        spheremain.geometry("500x100")
        spheremain.title("Kugel berechnen")

        spherelabel = tk.Label(spheremain, text='Gib den Radius an')
        spherelabel.pack()

        sphereentry = tk.Entry(spheremain)
        sphereentry.pack()

        spherebutton = tk.Button(spheremain, text='Submit', command=calcsphere)
        spherebutton.pack()

        sphereanswer = tk.Label(spheremain)
        sphereanswer.pack()
        spheremain.mainloop()
    else:
        cylindermain = tk.Toplevel()
        cylindermain.geometry("500x140")
        cylindermain.title("Zylinder berechnen")

        cylinderlabel = tk.Label(cylindermain, text='Gib den Radius an')
        cylinderlabel.pack()

        cylinderentry = tk.Entry(cylindermain)
        cylinderentry.pack()

        cylinderlabel1 = tk.Label(cylindermain, text='Gib die Höhe an')
        cylinderlabel1.pack()

        cylinderentry1 = tk.Entry(cylindermain)
        cylinderentry1.pack()

        cylinderbutton = tk.Button(cylindermain, text='Submit', command=calccylinder)
        cylinderbutton.pack()

        cylinderanswer = tk.Label(cylindermain)
        cylinderanswer.pack()
        cylindermain.mainloop()

window = tk.Tk()
window.geometry("600x600")
window.title("Körper Berechnen")
window.configure(background="lightgrey")

shapes = ["Würfel", "Kegel", "Pyramide", "Quader", "Prisma", "Kugel", "Zylinder"] # list of buttons


#Main title
startlabel = tk.Label(window,
                      text= "Wähle einen Körper aus",
                      font=('Arial', 22, 'bold'),
                      background="lightgrey")
startlabel.pack()

#Buttons for different shapes
x = tk.IntVar()
for index in range(len(shapes)):
    options = tk.Radiobutton(window,
                             text= shapes[index],
                             variable= x,
                             value= index,
                             padx=10,
                             font=("Arial", 35),
                             indicatoron= 0,
                             width= 15,
                             command= choice
                             )
    options.pack()

window.mainloop()
