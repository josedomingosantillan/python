from tkinter import *
class App:
    _res= "Resultado"
    def __init__(self,master):
        ventana= Frame(master)
        ventana.pack()
        self.suma= Button(ventana,text="Sumar",command=self.sumar)
        self.caja1= Text(ventana, width=10,height=1)
        self.caja2= Text(ventana, width=10,height=1)
        self.label1= Label(ventana,text=self._res)
        self.caja1.pack(side=LEFT)
        self.caja2.pack(side=LEFT)
        self.suma.pack(side=LEFT)
        self.label1.pack(side=LEFT)
    
    def sumar(self):
        self.a= int(self.caja1.get("1.0"))
        self.b= int(self.caja2.get("1.0"))
        print("Suma: ", int(self.a+self.b))
        self._res= "Resultado: ",int(self.a+self.b), 
        self.label1.config(text= self._res)

root= Tk()
app=App(root)
root.mainloop()