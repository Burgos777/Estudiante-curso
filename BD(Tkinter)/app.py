from tkinter import *
from tkinter import ttk
from database import *
from tkinter import messagebox



class App:
    def __init__(self, master):
        self.ventana = master
        self.DibujarLabel()
        self.DibujarEntry()
        self.DibujarBoton()
        self.Dibujar_lista("")



    def DibujarLabel(self):
        self.lbl_documento=Label(self.ventana, foreground="white", background="#314252", text="Documento", font=8).place(x=60,y=110)
        self.lbl_nombre=Label(self.ventana, foreground="white", background="#314252", text="Nombre", font=8).place(x=60,y=160)
        self.lbl_creditos=Label(self.ventana, foreground="white", background="#314252", text="Creditos", font= 8).place(x=60,y=210)


    def DibujarEntry(self):
        self.documento =StringVar()
        self.nombre =StringVar()
        self.creditos =StringVar()
        self.buscar_=StringVar()
        self.txt_documento = Entry(self.ventana, font=('Aarial',12), textvariable=self.documento).place(x=160, y=110)
        self.txt_documento = Entry(self.ventana, font=('Aarial',12), textvariable=self.nombre).place(x=160, y=160)
        self.txt_documento = Entry(self.ventana, font=('Aarial',12), textvariable=self.creditos).place(x=160, y=210)

        #Agregar Buscar
        self.txt_buscar = Entry(self.ventana, font=('Aarial',12), textvariable = self.buscar_).place(x=160, y=352)

    def DibujarBoton(self):
        self.btn_guardar =Button(self.ventana, text="Guardar", relief="flat", background="#0051C8", cursor="hand1", foreground="white", command= lambda: self.guardar()).place(x=750, y=350, width=90)
        self.btn_cancelar =Button(self.ventana, text="Cancelar", relief="flat", background="red", cursor="hand1", foreground="white", command= lambda: self.Limpiarlista ()).place(x=850, y=350, width=90)

        #Agregar Buscar
        self.btn_buscar =Button(self.ventana, text="Filtrar", relief="flat", background="Green", cursor="hand1", foreground="white", command = lambda: self.buscar(self.buscar_.get())).place(x=350, y=350, width=90)
    
    def buscar(self,ref):
        self.Limpiarlista()
        self.Dibujar_lista(ref)


        


    def guardar(self):
        arr =[self.documento.get(), self.nombre.get(), self.creditos.get()]
        d = Data()
        d.InsertItems(arr)
        self.documento.set("")
        self.nombre.set("")
        self.creditos.set("")
        self.Limpiarlista()
        self.Dibujar_lista("")


    def Limpiarlista(self):
        self.lista.delete(*self.lista.get_children())




    def Dibujar_lista(self,ref):
        self.lista = ttk.Treeview(self.ventana, columns=(1,2,3),show="headings", height="8")
        #stylo
        estilo= ttk.Style()
        estilo.theme_use("clam")

        estilo.configure("Treeview.Heading", background="#0051C8", relief="flat", foreground="white")
        self.lista.heading(1,text="Documento")
        self.lista.heading(2,text="Nombre")
        self.lista.heading(3,text="Creditos")
        self.lista.column(2, anchor=CENTER)

        #Evento
        self.lista.bind("<Double 1>", self.obtenerFila)

        if ref =="":
            #fill list
            d = Data()
            elements = d.returnAllElements()
            for i in elements:
                self.lista.insert('', 'end', values=i)
        else:
            #fill list
            d = Data()
            elements = d.ReturnForCarreer(ref)
            for i in elements:
                self.lista.insert('', 'end', values=i)
        self.lista.place(x=350,y=90)

    def obtenerFila(self, event):
        do= StringVar()
        na= StringVar()
        cr= StringVar()
        DocumentoFila= self.lista.identify_row(event.y)
        elemento= self.lista.item(self.lista.focus())
        d = elemento['values'][0]#Accedemos al documento
        n = elemento['values'][1]#Accedemos al nombre
        c = elemento['values'][2]#Accedemos a los creditos
        do.set(d)
        na.set(n)
        cr.set(c)

        pop =Toplevel(self.ventana)
        pop.geometry("400x200")
        text_d =Entry(pop, textvariable=do).place(x=40, y=40)
        text_n =Entry(pop, textvariable=na).place(x=40, y=80)
        text_c =Entry(pop, textvariable=cr).place(x=40, y=120)
        #botones
        btn_cambiar = Button(pop, text="Actualizar", relief="flat", background="#00CE54", foreground="white", command=lambda:self.editar(d, do.get(), na.get(),cr.get())).place(x=180,y=160,  width=90)
        btn_eliminar = Button(pop, text="Eliminar", relief="flat", background="red", foreground="white", command=lambda:self.eliminar(do.get())).place(x=280,y=160,  width=90)
        

    def editar(self, d, do, n, c):
        d = Data()
        arr = [do, n, c]
        d.UpdateItenm(arr, do)
        messagebox.showinfo(title="Actualizacion", message="Se ha actualidazo la base de datos")
        self.Limpiarlista()
        self.Dibujar_lista("")

    def eliminar(self,do):
        d= Data()
        d.Delete(do)
        messagebox.showinfo(title="Actualizacion", message="Se ha actualizado la base de datos")
        self.Limpiarlista()
        self.Dibujar_lista("")


        


root = Tk()
root.title("Base Datos")
root.geometry("1000x400")
root.config(background="#314252")
aplication = App(root)
root.mainloop() 
