from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json
from patrocinioypoder import patrocinioYPoder
from demandaDMA import divorcioMutuoAcuerdo
from renunciapatrociniofin import patrocinioYPoderFin
from ddaUnilateralCese import divorcioUnilateralCese
from acuerdoCySSimple import acuerdoCompletoSimple
from acuerdoCySEscPub import acuerdoCompletoEscPub
from demandaAlimMenores import alimentosMenores

class MyApp(Tk):
    '''Crea la ventana principal desde la cual las vistas son desplegadas'''
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        self.frames = {}
        for F in (Inicio, Patrocinado, Contraparte, Matrimonio, Adicionales, Acuerdo, HijosEntrePartes, HijosPatrocinado, HijosContraparte, Configuracion):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = NSEW)
        self.show_frame(Inicio)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    def get_page(self, classname):
        '''Returns an instance of a page given its class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None

class Inicio(ttk.Frame):
    '''Primera vista, desde la cual se puede acceder al resto'''
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Inicio').grid()
        button0 = ttk.Button(self, text='Datos del Patrocinado y su Abogado',
                                  command=lambda: controller.show_frame(Patrocinado))
        button1 = ttk.Button(self, text='Datos de la Contraparte y su Abogado',
                                  command=lambda: controller.show_frame(Contraparte))
        button2 = ttk.Button(self, text='Información relación entre las partes',
                                  command=lambda: controller.show_frame(Matrimonio))
        button3 = ttk.Button(self, text='Datos de la Causa',
                                  command=lambda: controller.show_frame(Adicionales))
        button4 = ttk.Button(self, text='Acuerdo Completo y Suficiente',
                                  command=lambda: controller.show_frame(Acuerdo))                                  
        button5 = ttk.Button(self, text='Hijos Entre las Partes',
                                  command=lambda: controller.show_frame(HijosEntrePartes))
        button6 = ttk.Button(self, text='Hijos del Patrocinado',
                                  command=lambda: controller.show_frame(HijosPatrocinado))
        button7 = ttk.Button(self, text='Hijos de la Contraparte',
                                  command=lambda: controller.show_frame(HijosContraparte))
        button8 = ttk.Button(self, text='Configuración',
                                  command=lambda: controller.show_frame(Configuracion))
        button0.grid()
        button1.grid()
        button2.grid()
        button3.grid()
        button4.grid()
        button5.grid()
        button6.grid()
        button7.grid()
        button8.grid()

class Patrocinado(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Patrocinado').grid()
        self.titulo=Label(self, text ="Datos del patrocinado y su abogado")
        self.nombPat=Label(self, text ="Nombre Patrocinado")
        self.nombPatTXT=Entry(self)        
        self.apePatPat=Label(self, text ="Apellido Paterno")
        self.apePatPatTXT=Entry(self)
        self.apeMatPat=Label(self, text ="Apellido Materno")
        self.apeMatPatTXT=Entry(self)
        self.sexoPat=Label(self, text ="Sexo")
        self.var1 = StringVar()
        self.sexoPatDrop= OptionMenu(self,self.var1,'Masculino','Femenino')
        self.sexoPatCheck=self.var1.get()
        self.nacPat=Label(self, text ="Nacionalidad")
        self.nacPatTXT=Entry(self)
        self.estCivilPat=Label(self, text ="Estado Civil")
        self.var2 = StringVar()
        self.estCivilPatDrop= OptionMenu(self,self.var2,'Casado','Soltero','Viudo','Divorciado')
        self.estCivilPatCheck=self.var2.get()
        self.rutPat=Label(self, text ="Cédula de Identidad")
        self.rutPatTXT=Entry(self)
        self.profPat=Label(self, text ="Profesión")
        self.profPatTXT=Entry(self)
        self.domicPat=Label(self, text ="Dirección")
        self.domicPatTXT=Entry(self)
        self.numDomicPat=Label(self, text ="Número")
        self.numDomicPatTXT=Entry(self)        
        self.comunaPat=Label(self, text ="Comuna")
        self.comunaPatTXT=Entry(self)
        self.ciudPat=Label(self, text="Ciudad")
        self.ciudPatTXT=Entry(self)
        self.regPat=Label(self,text="Región")
        self.regPatVar=StringVar()
        self.regPatDrop=OptionMenu(self, self.regPatVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')
        self.sitProcPat=Label(self, text ="Sit. Procesal Patrocinado")        
        self.var16 = StringVar()
        self.sitProcPatDrop= OptionMenu(self,self.var16,'Demandante','Demandado')        
        self.sitProcPatCheck=self.var16.get()        

        self.nombAboPat=Label(self, text ="Nombre Abogado Patrocinado")
        self.nombAboPatTXT=Entry(self)
        self.apePatAboPat=Label(self, text ="Apellido Paterno")
        self.apePatAboPatTXT=Entry(self)
        self.apeMatAboPat=Label(self, text ="Apellido Materno")
        self.apeMatAboPatTXT=Entry(self)
        self.sexoAboPat=Label(self, text ="Sexo")
        self.var3 = StringVar()
        self.sexoAboPatDrop= OptionMenu(self,self.var3,'Masculino','Femenino')
        self.sexoAboPatCheck=self.var3.get()
        self.nacAboPat=Label(self, text ="Nacionalidad")
        self.nacAboPatTXT=Entry(self)
        self.estCivilAboPat=Label(self, text ="Estado Civil")
        self.var4 = StringVar()
        self.estCivilAboPatDrop= OptionMenu(self,self.var4,'Casado','Soltero','Viudo','Divorciado')
        self.facAboPat=Label(self, text ="Facultades amplias")
        self.facAboPatVar = StringVar()
        self.facAboPatDrop= OptionMenu(self,self.facAboPatVar,'Sí','No')        
        self.rutAboPat=Label(self, text ="Cedula de Identidad")
        self.rutAboPatTXT=Entry(self)
        self.emailAboPat=Label(self, text ="Email")
        self.emailAboPatTXT=Entry(self)
        self.domicAboPat=Label(self, text ="Direccion")
        self.domicAboPatTXT=Entry(self)
        self.numDomicAboPat=Label(self, text ="Número")
        self.numDomicAboPatTXT=Entry(self)        
        self.comunaAboPat=Label(self, text ="Comuna")
        self.comunaAboPatTXT=Entry(self)        
        self.ciudAboPat=Label(self, text="Ciudad")
        self.ciudAboPatTXT=Entry(self)
        self.regAboPat=Label(self,text="Región")
        self.regAboPatVar=StringVar()
        self.regAboPatDrop=OptionMenu(self, self.regAboPatVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')
        
        self.nombApoPat=Label(self, text ="Nombre Apoderado")
        self.nombApoPatTXT=Entry(self)
        self.apePatApoPat=Label(self, text ="Apellido Paterno")
        self.apePatApoPatTXT=Entry(self)
        self.apeMatApoPat=Label(self, text ="Apellido Materno")
        self.apeMatApoPatTXT=Entry(self)
        self.sexoApoPat=Label(self, text ="Sexo")
        self.var33 = StringVar()
        self.sexoApoPatDrop= OptionMenu(self,self.var33,'Masculino','Femenino')
        self.sexoApoPatCheck=self.var33.get()
        self.nacApoPat=Label(self, text ="Nacionalidad")
        self.nacApoPatTXT=Entry(self)
        self.estCivilApoPat=Label(self, text ="Estado Civil")
        self.facApoPat=Label(self, text ="Facultades amplias")
        self.facApoPatVar = StringVar()
        self.facApoPatDrop= OptionMenu(self,self.facAboPatVar,'Sí','No')        
        self.var34 = StringVar()
        self.estCivilApoPatDrop= OptionMenu(self,self.var34,'Casado','Soltero','Viudo','Divorciado')
        self.rutApoPat=Label(self, text ="Cedula de Identidad")
        self.rutApoPatTXT=Entry(self)
        self.emailApoPat=Label(self, text ="Email")
        self.emailApoPatTXT=Entry(self)
        self.domicApoPat=Label(self, text ="Direccion")
        self.domicApoPatTXT=Entry(self)
        self.numDomicApoPat=Label(self, text ="Número")
        self.numDomicApoPatTXT=Entry(self)        
        self.comunaApoPat=Label(self, text ="Comuna")
        self.comunaApoPatTXT=Entry(self)   
        self.ciudApoPat=Label(self, text="Ciudad")
        self.ciudApoPatTXT=Entry(self)
        self.regApoPat=Label(self,text="Región")
        self.regApoPatVar=StringVar()
        self.regApoPatDrop=OptionMenu(self, self.regApoPatVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')        
        
        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Datos de la contraparte y su abogado',
                                  command=lambda: controller.show_frame(Contraparte))


        self.titulo.grid(row=0,column=0)
        self.nombPat.grid(row= 1 ,column=0)
        self.nombPatTXT.grid(row= 2 ,column=0)
        self.apePatPat.grid(row= 3 ,column=0)
        self.apePatPatTXT.grid(row= 4 ,column=0)
        self.apeMatPat.grid(row= 5 ,column=0)
        self.apeMatPatTXT.grid(row= 6 ,column=0)
        self.sexoPat.grid(row= 7 ,column=0)
        self.sexoPatDrop.grid(row= 8 ,column=0)
        self.nacPat.grid(row= 9 , column=0)
        self.nacPatTXT.grid(row= 10 , column=0)
        self.estCivilPat.grid(row= 11 , column=0)
        self.estCivilPatDrop.grid(row= 12 , column=0)
        self.rutPat.grid(row= 13 , column=0)
        self.rutPatTXT.grid(row= 14 , column=0)
        self.profPat.grid(row= 15 , column=0)
        self.profPatTXT.grid(row= 16 , column=0)
        self.domicPat.grid(row= 17 , column=0)
        self.domicPatTXT.grid(row= 18 , column=0)
        self.numDomicPat.grid(column=0)
        self.numDomicPatTXT.grid(column=0)      
        
        self.comunaPat.grid(column=0)
        self.comunaPatTXT.grid(column=0)
        self.ciudPat.grid(column=0)
        self.ciudPatTXT.grid(column=0)
        self.regPat.grid(column=0)
        self.regPatDrop.grid(column=0)        
        self.sitProcPat.grid(column=0)
        self.sitProcPatDrop.grid(column=0)
        
        self.nombAboPat.grid(row= 1 , column=1)
        self.nombAboPatTXT.grid(row= 2 , column=1)
        self.apePatAboPat.grid(row= 3 , column=1)
        self.apePatAboPatTXT.grid(row= 4 , column=1)
        self.apeMatAboPat.grid(row= 5 , column=1)
        self.apeMatAboPatTXT.grid(row= 6 , column=1)
        self.sexoAboPat.grid(row= 7 , column=1)
        self.sexoAboPatDrop.grid(row= 8 , column=1)
        self.nacAboPat.grid(row= 9 , column=1)
        self.nacAboPatTXT.grid(row= 10 , column=1)
        self.estCivilAboPat.grid(row= 11 , column=1)
        self.estCivilAboPatDrop.grid(row= 12 , column=1)
        self.facAboPat.grid(row=13,column=1)
        self.facAboPatDrop.grid(row=14,column=1)
        self.rutAboPat.grid(row= 15 , column=1)
        self.rutAboPatTXT.grid(row= 16 , column=1)
        self.emailAboPat.grid(row= 17 , column=1)
        self.emailAboPatTXT.grid(row= 18 , column=1)
        self.domicAboPat.grid(row= 19 , column=1)
        self.domicAboPatTXT.grid(row= 20 , column=1)
        self.numDomicAboPat.grid(row= 21, column=1)
        self.numDomicAboPatTXT.grid(row= 22, column=1)        
        self.comunaAboPat.grid(row= 23, column=1)
        self.comunaAboPatTXT.grid(row= 24, column=1)
        self.ciudAboPat.grid(row=25,column=1)
        self.ciudAboPatTXT.grid(row=26,column=1)
        self.regAboPat.grid(row=27,column=1)
        self.regAboPatDrop.grid(row=28,column=1)        

        self.nombApoPat.grid(row= 1 , column=2)
        self.nombApoPatTXT.grid(row= 2 , column=2)
        self.apePatApoPat.grid(row= 3 , column=2)
        self.apePatApoPatTXT.grid(row= 4 , column=2)
        self.apeMatApoPat.grid(row= 5 , column=2)
        self.apeMatApoPatTXT.grid(row= 6 , column=2)
        self.sexoApoPat.grid(row= 7 , column=2)
        self.sexoApoPatDrop.grid(row= 8 , column=2)
        self.nacApoPat.grid(row= 9 , column=2)
        self.nacApoPatTXT.grid(row= 10 , column=2)
        self.estCivilApoPat.grid(row= 11 , column=2)
        self.estCivilApoPatDrop.grid(row= 12 , column=2)
        self.facApoPat.grid(row=13,column=2)
        self.facApoPatDrop.grid(row=14,column=2)        
        self.rutApoPat.grid(row= 15 , column=2)
        self.rutApoPatTXT.grid(row= 16 , column=2)
        self.emailApoPat.grid(row= 17 , column=2)
        self.emailApoPatTXT.grid(row= 18 , column=2)
        self.domicApoPat.grid(row= 19 , column=2)
        self.domicApoPatTXT.grid(row= 20 , column=2)
        self.numDomicApoPat.grid(row= 21, column=2)
        self.numDomicApoPatTXT.grid(row= 22, column=2)        
        self.comunaApoPat.grid(row= 23, column=2)
        self.comunaApoPatTXT.grid(row= 24, column=2)
        self.ciudApoPat.grid(row=25,column=2)
        self.ciudApoPatTXT.grid(row=26,column=2)
        self.regApoPat.grid(row=27,column=2)
        self.regApoPatDrop.grid(row=28,column=2)
        
        button1.grid(column=0)
        button2.grid(row= 29, column=2)

class Contraparte(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Contraparte').grid()
        self.titulo=Label(self, text ="Datos de la contraparte y su abogado")
        self.nombContrap=Label(self, text ="Nombre Contraparte")
        self.nombContrapTXT=Entry(self)
        self.apePatContrap=Label(self, text ="Apellido Paterno")
        self.apePatContrapTXT=Entry(self)
        self.apeMatContrap=Label(self, text ="Apellido Materno")
        self.apeMatContrapTXT=Entry(self)
        self.sexoContrap=Label(self, text ="Sexo")
        self.var5 = StringVar()
        self.sexoContrapDrop= OptionMenu(self,self.var5,'Masculino','Femenino')
        self.nacContrap=Label(self, text ="Nacionalidad")
        self.nacContrapTXT=Entry(self)
        self.estCivilContrap=Label(self, text ="Estado Civil")
        self.var6 = StringVar()
        self.estCivilContrapDrop= OptionMenu(self,self.var6,'Casado','Soltero','Viudo','Divorciado')
        self.rutContrap=Label(self, text ="Cedula de Identidad")
        self.rutContrapTXT=Entry(self)
        self.profContrap=Label(self, text ="Profesion")
        self.profContrapTXT=Entry(self)
        self.domicContrap=Label(self, text ="Direccion")
        self.domicContrapTXT=Entry(self)
        self.numDomicContrap=Label(self, text ="Número")
        self.numDomicContrapTXT=Entry(self)        
        self.comunaContrap=Label(self, text ="Comuna")
        self.comunaContrapTXT=Entry(self)
        self.ciudContrap=Label(self, text="Ciudad")
        self.ciudContrapTXT=Entry(self)
        self.regContrap=Label(self,text="Región")
        self.regContrapVar=StringVar()
        self.regContrapDrop=OptionMenu(self, self.regContrapVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')        

        self.nombAboContrap=Label(self, text ="Nombre Abogado Contraparte")
        self.nombAboContrapTXT=Entry(self)
        self.apePatAboContrap=Label(self, text ="Apellido Paterno")
        self.apePatAboContrapTXT=Entry(self)
        self.apeMatAboContrap=Label(self, text ="Apellido Materno")
        self.apeMatAboContrapTXT=Entry(self)
        self.sexoAboContrap=Label(self, text ="Sexo")
        self.var7 = StringVar()
        self.sexoAboContrapDrop= OptionMenu(self,self.var7,'Masculino','Femenino')
        self.nacAboContrap=Label(self, text ="Nacionalidad")
        self.nacAboContrapTXT=Entry(self)
        self.estCivilAboContrap=Label(self, text ="Estado Civil")
        self.var8 = StringVar()
        self.estCivilAboContrapDrop= OptionMenu(self,self.var8,'Casado','Soltero','Viudo','Divorciado')
        self.facAboContrap=Label(self, text ="Facultades amplias")
        self.facAboContrapVar = StringVar()
        self.facAboContrapDrop= OptionMenu(self,self.facAboContrapVar,'Sí','No')         
        self.rutAboContrap=Label(self, text ="Cedula de Identidad")
        self.rutAboContrapTXT=Entry(self)
        self.emailAboContrap=Label(self, text ="Email")
        self.emailAboContrapTXT=Entry(self)
        self.domicAboContrap=Label(self, text ="Direccion")
        self.domicAboContrapTXT=Entry(self)
        self.numDomicAboContrap=Label(self, text ="Número")
        self.numDomicAboContrapTXT=Entry(self)        
        self.comunaAboContrap=Label(self, text ="Comuna")
        self.comunaAboContrapTXT=Entry(self)
        self.ciudAboContrap=Label(self, text="Ciudad")
        self.ciudAboContrapTXT=Entry(self)
        self.regAboContrap=Label(self,text="Región")
        self.regAboContrapVar=StringVar()
        self.regAboContrapDrop=OptionMenu(self, self.regAboContrapVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')        

        self.nombApoContrap=Label(self, text ="Nombre Apoderado")
        self.nombApoContrapTXT=Entry(self)
        self.apePatApoContrap=Label(self, text ="Apellido Paterno")
        self.apePatApoContrapTXT=Entry(self)
        self.apeMatApoContrap=Label(self, text ="Apellido Materno")
        self.apeMatApoContrapTXT=Entry(self)
        self.sexoApoContrap=Label(self, text ="Sexo")
        self.var35 = StringVar()
        self.sexoApoContrapDrop= OptionMenu(self,self.var35,'Masculino','Femenino')
        self.nacApoContrap=Label(self, text ="Nacionalidad")
        self.nacApoContrapTXT=Entry(self)
        self.estCivilApoContrap=Label(self, text ="Estado Civil")
        self.facApoContrap=Label(self, text ="Facultades amplias")
        self.facApoContrapVar = StringVar()
        self.facApoContrapDrop= OptionMenu(self,self.facApoContrapVar,'Sí','No')         
        self.var36 = StringVar()
        self.estCivilApoContrapDrop= OptionMenu(self,self.var36,'Casado','Soltero','Viudo','Divorciado')
        self.rutApoContrap=Label(self, text ="Cedula de Identidad")
        self.rutApoContrapTXT=Entry(self)
        self.emailApoContrap=Label(self, text ="Email")
        self.emailApoContrapTXT=Entry(self)
        self.domicApoContrap=Label(self, text ="Direccion")
        self.domicApoContrapTXT=Entry(self)
        self.numDomicApoContrap=Label(self, text ="Número")
        self.numDomicApoContrapTXT=Entry(self)        
        self.comunaApoContrap=Label(self, text ="Comuna")
        self.comunaApoContrapTXT=Entry(self)
        self.ciudApoContrap=Label(self, text="Ciudad")
        self.ciudApoContrapTXT=Entry(self)
        self.regApoContrap=Label(self,text="Región")
        self.regApoContrapVar=StringVar()
        self.regApoContrapDrop=OptionMenu(self, self.regApoContrapVar, 'RM','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIV','XV')
        
        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Datos sobre el Matrimonio',
                                  command=lambda: controller.show_frame(Matrimonio))

        self.titulo.grid(row=0,column=0)
        self.nombContrap.grid(row= 1 ,column=0)
        self.nombContrapTXT.grid(row= 2 ,column=0)
        self.apePatContrap.grid(row= 3 ,column=0)
        self.apePatContrapTXT.grid(row= 4 ,column=0)
        self.apeMatContrap.grid(row= 5 ,column=0)
        self.apeMatContrapTXT.grid(row= 6 ,column=0)
        self.sexoContrap.grid(row= 7 ,column=0)
        self.sexoContrapDrop.grid(row= 8 ,column=0)
        self.nacContrap.grid(row= 9 , column=0)
        self.nacContrapTXT.grid(row= 10 , column=0)
        self.estCivilContrap.grid(row= 11 , column=0)
        self.estCivilContrapDrop.grid(row= 12 , column=0)
        self.rutContrap.grid(row= 13 , column=0)
        self.rutContrapTXT.grid(row= 14 , column=0)
        self.profContrap.grid(row= 15 , column=0)
        self.profContrapTXT.grid(row= 16 , column=0)
        self.domicContrap.grid(row= 17 , column=0)
        self.domicContrapTXT.grid(row= 18 , column=0)
        self.numDomicContrap.grid(row=19, column=0)
        self.numDomicContrapTXT.grid(row=20, column=0)        
        self.comunaContrap.grid(row= 21, column=0)
        self.comunaContrapTXT.grid(row= 22, column=0)
        self.ciudContrap.grid(row=25,column=0)
        self.ciudContrapTXT.grid(row=26,column=0)
        self.regContrap.grid(row=27,column=0)
        self.regContrapDrop.grid(row=28,column=0)        

        self.nombAboContrap.grid(row= 1 , column=1)
        self.nombAboContrapTXT.grid(row= 2 , column=1)
        self.apePatAboContrap.grid(row= 3 , column=1)
        self.apePatAboContrapTXT.grid(row= 4 , column=1)
        self.apeMatAboContrap.grid(row= 5 , column=1)
        self.apeMatAboContrapTXT.grid(row= 6 , column=1)
        self.sexoAboContrap.grid(row= 7 , column=1)
        self.sexoAboContrapDrop.grid(row= 8 , column=1)
        self.nacAboContrap.grid(row= 9 , column=1)
        self.nacAboContrapTXT.grid(row= 10 , column=1)
        self.estCivilAboContrap.grid(row= 11 , column=1)
        self.estCivilAboContrapDrop.grid(row= 12 , column=1)
        self.facAboContrap.grid(row=13,column=1)
        self.facAboContrapDrop.grid(row=14,column=1)        
        self.rutAboContrap.grid(row= 15 , column=1)
        self.rutAboContrapTXT.grid(row= 16 , column=1)
        self.emailAboContrap.grid(row= 17 , column=1)
        self.emailAboContrapTXT.grid(row= 18 , column=1)
        self.domicAboContrap.grid(row= 19 , column=1)
        self.domicAboContrapTXT.grid(row= 20 , column=1)
        self.numDomicAboContrap.grid(row=21, column=1)
        self.numDomicAboContrapTXT.grid(row=22, column=1)
        self.comunaAboContrap.grid(row= 23, column=1)
        self.comunaAboContrapTXT.grid(row= 24, column=1)
        self.ciudAboContrap.grid(row=25,column=1)
        self.ciudAboContrapTXT.grid(row=26,column=1)
        self.regAboContrap.grid(row=27,column=1)
        self.regAboContrapDrop.grid(row=28,column=1)        

        self.nombApoContrap.grid(row= 1 , column=2)
        self.nombApoContrapTXT.grid(row= 2 , column=2)
        self.apePatApoContrap.grid(row= 3 , column=2)
        self.apePatApoContrapTXT.grid(row= 4 , column=2)
        self.apeMatApoContrap.grid(row= 5 , column=2)
        self.apeMatApoContrapTXT.grid(row= 6 , column=2)
        self.sexoApoContrap.grid(row= 7 , column=2)
        self.sexoApoContrapDrop.grid(row= 8 , column=2)
        self.nacApoContrap.grid(row= 9 , column=2)
        self.nacApoContrapTXT.grid(row= 10 , column=2)
        self.estCivilApoContrap.grid(row= 11 , column=2)
        self.estCivilApoContrapDrop.grid(row= 12 , column=2)
        self.facApoContrap.grid(row=13,column=2)
        self.facApoContrapDrop.grid(row=14,column=2)        
        self.rutApoContrap.grid(row= 15 , column=2)
        self.rutApoContrapTXT.grid(row= 16 , column=2)
        self.emailApoContrap.grid(row= 17 , column=2)
        self.emailApoContrapTXT.grid(row= 18 , column=2)
        self.domicApoContrap.grid(row= 19 , column=2)
        self.domicApoContrapTXT.grid(row= 20 , column=2)
        self.numDomicApoContrap.grid(row=21, column=2)
        self.numDomicApoContrapTXT.grid(row=22, column=2)
        self.comunaApoContrap.grid(row= 23, column=2)
        self.comunaApoContrapTXT.grid(row= 24, column=2)
        self.ciudApoContrap.grid(row=25,column=2)
        self.ciudApoContrapTXT.grid(row=26,column=2)
        self.regApoContrap.grid(row=27,column=2)
        self.regApoContrapDrop.grid(row=28,column=2)        
        button1.grid()
        button2.grid(row=29,column=2)

class Matrimonio(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Matrimonio').grid()
        self.titulo=Label(self, text ="Relación entre las partes")
        self.fechaMatrimonio=Label(self, text =" Fecha Matrimonio")
        self.var9=StringVar()
        self.diaMatrimonio=Label(self, text ="Dia")
        self.diaMatrimonioDrop= OptionMenu(self,self.var9,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','')

        self.mesMatrimonio=Label(self, text ="Mes")
        self.var10=StringVar()
        self.mesMatrimonioDrop= OptionMenu(self,self.var10,'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','')
        self.añoMatrimonio=Label(self, text ="Año")
        self.añoMatrimonioTXT= Entry(self)
        self.comunaMatrimonio=Label(self, text ="Comuna celebracion")
        self.comunaMatrimonioTXT=Entry(self)
        self.numeroInscripcion=Label(self, text ="Numero Inscripcion")
        self.numeroInscripcionTXT=Entry(self)
        self.var11=StringVar()
        self.regimenMatrimonio=Label(self, text ="Regimen Matrimonial")
        self.regimenMatrimonioDrop= OptionMenu(self,self.var11,'Sociedad Conyugal','Participación en los gananciales','Separación total de bienes')
        self.existeBienVar=StringVar()
        self.existeBienLabel=Label(self, text= 'Existen bienes que liquidar')
        self.existeBienDrop = OptionMenu(self,self.existeBienVar,'Sí','No')

        self.fechaCeseConvivencia=Label(self, text =" Fecha Cese de convivencia")
        self.var12=StringVar()
        self.diaCeseConvivencia=Label(self, text ="Dia")
        self.diaCeseConvivenciaDrop= OptionMenu(self,self.var12,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','')
        self.var13=StringVar()
        self.mesCeseConvivencia=Label(self, text ="Mes")
        self.mesCeseConvivenciaDrop= OptionMenu(self,self.var13,'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','')
        self.añoCeseConvivencia=Label(self, text ="Año")
        self.añoCeseConvivenciaTXT= Entry(self)
        
        
        self.duracionRelacion=Label(self, text =" Duración relación entre las partes")
        self.añosDuracionRelacion=Label(self, text ="Años")
        self.añosDuracionRelacionTXT= Entry(self)     
        self.mesesDuracionRelacion=Label(self, text ="Meses")
        self.mesesDuracionRelacionTXT= Entry(self)  
         
        self.fechaCeseRelacion=Label(self, text =" Fecha término de relación")
        self.diaCeseRelacionVar=StringVar()
        self.diaCeseRelacion=Label(self, text ="Día")
        self.diaCeseRelacionDrop= OptionMenu(self,self.diaCeseRelacionVar,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','')
        self.mesCeseRelacionVar=StringVar()
        self.mesCeseRelacion=Label(self, text ="Mes")
        self.mesCeseRelacionDrop= OptionMenu(self,self.mesCeseRelacionVar,'Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','')
        self.añoCeseRelacion=Label(self, text ="Año")
        self.añoCeseRelacionTXT= Entry(self)        

        self.titulo.grid(row= 0 ,column=0)
        self.fechaMatrimonio.grid(row= 1 ,column=0)
        self.diaMatrimonio.grid(row= 2 ,column=0)
        self.diaMatrimonioDrop.grid(row= 3 ,column=0)
        self.mesMatrimonio.grid(row= 4 ,column=0)
        self.mesMatrimonioDrop.grid(row= 5 ,column=0)
        self.añoMatrimonio.grid(row= 6 ,column=0)
        self.añoMatrimonioTXT.grid(row= 7 ,column=0)
        self.comunaMatrimonio.grid(row= 8 ,column=0)
        self.comunaMatrimonioTXT.grid(row= 9 ,column=0)
        self.numeroInscripcion.grid(row= 10 ,column=0)
        self.numeroInscripcionTXT.grid(row= 11 ,column=0)
        self.regimenMatrimonio.grid(row= 12 ,column=0)
        self.regimenMatrimonioDrop.grid(row= 13 ,column=0)
        self.existeBienLabel.grid(row=14, column=0)
        self.existeBienDrop.grid(row=15, column=0)
        
        
        self.fechaCeseConvivencia.grid(row= 1,column=1)
        self.diaCeseConvivencia.grid(row= 2 ,column=1)
        self.diaCeseConvivenciaDrop.grid(row= 3 ,column=1)
        self.mesCeseConvivencia.grid(row= 4 ,column=1)
        self.mesCeseConvivenciaDrop.grid(row= 5,column=1)
        self.añoCeseConvivencia.grid(row= 6 ,column=1)
        self.añoCeseConvivenciaTXT.grid(row= 7 ,column=1)

        self.duracionRelacion.grid(row=0,column=2)
        self.añosDuracionRelacion.grid(row=1,column=2)
        self.añosDuracionRelacionTXT.grid(row=2,column=2)
        self.mesesDuracionRelacion.grid(row=3,column=2)
        self.mesesDuracionRelacionTXT.grid(row=4,column=2)

        self.fechaCeseRelacion.grid(row=5,column=2)
        self.diaCeseRelacion.grid(row=6,column=2)
        self.diaCeseRelacionDrop.grid(row=7,column=2)
        self.mesCeseRelacion.grid(row=8,column=2)
        self.mesCeseRelacionDrop.grid(row=9,column=2)
        self.añoCeseRelacion.grid(row=10,column=2)
        self.añoCeseRelacionTXT.grid(row=11,column=2)        

        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Datos de la Causa',
                                  command=lambda: controller.show_frame(Adicionales))
        button1.grid()
        button2.grid(row=21,column=1)

class Adicionales(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        self.titulo=Label(self, text ="Datos Adicionales")
        self.ritCausa=Label(self, text ="RIT Causa")
        self.ritCausaTXT= Entry(self)
        self.juzgadoCausa=Label(self, text ="Juzgado")
        self.var15=StringVar()
        self.juzgadoCausaDrop = OptionMenu(self,self.var15,'1°','2°','3°','4°')
        self.varMateria = StringVar()
        self.materia = Label(self, text ="Materia:")
        self.materiaDrop = OptionMenu(self, self.varMateria,'Div. Unilateral','Div. Mutuo Acuerdo','Cump. Alimentos','Cump. R. dir. y R.','Aumento de Alimentos','Rebaja de Alimentos')
        self.caratula = Label(self, text ="Carátula:")
        self.caratulaTXT = Entry(self)
        self.var14 = StringVar()
        self.pideComp = Label(self, text ="Pide Compensación Económica")
        self.pideCompDrop = OptionMenu(self,self.var14,'Patrocinado','Contraparte','No se pide')
        self.varAbandona = StringVar()
        self.abandHogar = Label(self, text ="Abandona hogar Comun")
        self.abandHogarDrop=OptionMenu(self,self.varAbandona,'Patrocinado','Contraparte')
        self.nuevaRelPat = StringVar()
        self.relPat = Label(self, text= 'Nueva Relación Patrocinado')
        self.relPatDrop = OptionMenu(self,self.nuevaRelPat,'Si','No')
        self.añosRelacionPatrocinado=Label(self, text ="Años Relación Patrocinado")
        self.añosRelacionPatrocinadoTXT= Entry(self)
        self.nuevaRelCont = StringVar()
        self.relCont = Label(self, text= 'Nueva Relación Contraparte')
        self.relContDrop = OptionMenu(self,self.nuevaRelCont,'Si','No')
        self.añosRelacionContraparte = Label(self, text ="Años Relación Contraparte:")
        self.añosRelacionContraparteTXT = Entry(self)
        
        self.huboMedVar = StringVar()
        self.huboMed=Label(self, text= 'Hubo mediación:')
        self.huboMedDrop=OptionMenu(self,self.huboMedVar,'Si','No') 
        self.ritMed = Label(self, text ="RIT mediación: ")
        self.ritMedTXT = Entry(self)        
        
        self.pagoCompVar = StringVar()
        self.pagoComp = Label(self, text ="Modo de pago Compensación Económica")
        self.pagoCompDrop = OptionMenu(self,self.pagoCompVar,'Bien Inmueble', 'Derechos sobre un inmueble','Derechos sobre inmueble sociedad conyugal', 'Dinero', 'Otro')  
        self.valorComp=Label(self, text= 'Valor compensación económica')
        self.valorCompTXT=Entry(self)
        self.datosInmComp=Label(self,text="Datos de inmueble con que se paga")
        self.dirInmComp=Label(self,text='Dirección:')
        self.dirInmCompTXT=Entry(self)
        self.numInmComp=Label(self,text='Número')
        self.numInmCompTXT=Entry(self)        
        self.comunaInmComp=Label(self, text= "Comuna")
        self.comunaInmCompTXT=Entry(self)
        
        self.pagoAlimContrapVar = StringVar()
        self.pagoAlimContrap = Label (self, text = "Alimentos prestados por la contraparte")
        self.pagoAlimContrapDrop = OptionMenu(self, self.pagoAlimContrapVar, 'No adeuda','Menos de lo fijado','Ayuda ocasional o errática','Nada')
        
        self.titulo.grid(row= 1 ,column=0)
        self.ritCausa.grid(row= 2 ,column=0)
        self.ritCausaTXT.grid(row= 3 ,column=0)
        self.juzgadoCausa.grid(row= 4 ,column=0)
        self.juzgadoCausaDrop.grid(row= 5 ,column=0)
        self.materia.grid(row= 6 ,column=0)
        self.materiaDrop.grid(row= 7 ,column=0)
        self.caratula.grid(row= 8 ,column=0)
        self.caratulaTXT.grid(row= 9 ,column=0)
        self.pideComp.grid(row= 10 ,column=0)
        self.pideCompDrop.grid(row= 11 ,column=0)
        self.abandHogar.grid(row= 12 , column=0)
        self.abandHogarDrop.grid(row= 13 , column=0)
        self.relPat.grid(row= 14 , column=0)
        self.relPatDrop.grid(row= 15 , column=0)
        self.añosRelacionPatrocinado.grid(row= 16 ,column=0)
        self.añosRelacionPatrocinadoTXT.grid(row= 17 ,column=0)
        self.relCont.grid(row= 18 , column=0)
        self.relContDrop.grid(row= 19 , column=0)
        self.añosRelacionContraparte.grid(row= 20 ,column=0)
        self.añosRelacionContraparteTXT.grid(row= 21 ,column=0)
        
        self.huboMed.grid(row = 2,column = 1)
        self.huboMedDrop.grid(row = 3,column = 1)
        self.ritMed.grid(row = 4,column = 1)
        self.ritMedTXT.grid(row = 5,column = 1)
        
        self.pagoComp.grid(row=6,column = 1)
        self.pagoCompDrop.grid(row = 7, column = 1)
        self.valorComp.grid(row = 8, column= 1)
        self.valorCompTXT.grid(row = 9, column= 1)
        self.datosInmComp.grid(row=10,column=1)
        self.dirInmComp.grid(row=11,column=1)       
        self.dirInmCompTXT.grid(row=12,column=1) 
        self.numInmComp.grid(row=13,column=1)       
        self.numInmCompTXT.grid(row=14,column=1)         
        self.comunaInmComp.grid(row=15,column=1)         
        self.comunaInmCompTXT.grid(row=16,column=1)         
        
        self.pagoAlimContrap.grid (row = 2, column = 2)
        self.pagoAlimContrapDrop.grid(row = 3, column = 2)

        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Acuerdo Completo y Suficiente',
                                  command=lambda: controller.show_frame(Acuerdo))


        button1.grid()
        button2.grid(row=22,column=1)

class Acuerdo(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        self.titulo=Label(self, text ="Datos Adicionales")        

                                  
        self.pagaAlimMenores=Label(self, text ='Se pagan alimentos menores')
        self.pagaAlimMenoresVar=StringVar()
        self.pagaAlimMenoresDrop=OptionMenu(self, self.pagaAlimMenoresVar, 'Patrocinado', 'Contraparte', 'No hay')
        self.alimMenores=Label(self, text = 'Cuantía alimentos menores')
        self.alimMenoresTXT=Entry(self)
        self.cuantIMR=Label(self, text = 'Valor IMR')
        self.cuantIMRTXT=Entry(self)        
        
        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Hijos Entre las Partes',
                                  command=lambda: controller.show_frame(HijosEntrePartes))         
        
        self.pagaAlimMenores.grid()
        self.pagaAlimMenoresDrop.grid()
        self.alimMenores.grid()
        self.alimMenoresTXT.grid()
        self.cuantIMR.grid()
        self.cuantIMRTXT.grid()
       
        button1.grid()
        button2.grid(row=22,column=1)
        
class HijosEntrePartes(ttk.Frame):

    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        self.titulo=Label(self, text ="Hijos entre las partes")

        self.nombreHijoEntreParte1=Label(self, text ="Nombre 1")
        self.nombreHijoEntreParte1TXT=Entry(self)
        self.sexoHijoEntreParte1=Label(self, text ="Sexo")
        self.var37 = StringVar()
        self.sexoHijoEntreParte1Drop= OptionMenu(self,self.var37,'Masculino','Femenino')
        self.RUTHijoEntreParte1=Label(self, text ="RUT 1")
        self.RUTHijoEntreParte1TXT=Entry(self)
        self.edadHijoEntreParte1=Label(self, text ="Edad 1")
        self.edadHijoEntreParte1TXT=Entry(self)
        self.cuidadoHijo1=Label(self, text ="Cuidado personal 1")
        self.cuidadoHijo1Var = StringVar()
        self.cuidadoHijo1VarDrop= OptionMenu(self,self.cuidadoHijo1Var,'Ninguno','Patrocinado','Contraparte')
        self.cuidadoHijo1Var.set('Ninguno')
        self.patriapHijo1=Label(self, text ="Patria potestad 1")
        self.patriapHijo1Var = StringVar()
        self.patriapHijo1VarDrop= OptionMenu(self,self.patriapHijo1Var,'Ninguno','Patrocinado','Contraparte') 
        self.patriapHijo1Var.set('Ninguno')
        
        self.nombreHijoEntreParte2=Label(self, text ="Nombre 2")
        self.nombreHijoEntreParte2TXT=Entry(self)
        self.sexoHijoEntreParte2=Label(self, text ="Sexo")
        self.var38 = StringVar()
        self.sexoHijoEntreParte2Drop= OptionMenu(self,self.var38,'Masculino','Femenino')
        self.RUTHijoEntreParte2=Label(self, text ="RUT 2")
        self.RUTHijoEntreParte2TXT=Entry(self)
        self.edadHijoEntreParte2=Label(self, text ="Edad 2")
        self.edadHijoEntreParte2TXT=Entry(self)
        self.cuidadoHijo2=Label(self, text ="Cuidado personal 2")
        self.cuidadoHijo2Var = StringVar()
        self.cuidadoHijo2VarDrop= OptionMenu(self,self.cuidadoHijo2Var,'Ninguno','Patrocinado','Contraparte')
        self.cuidadoHijo2Var.set('Ninguno')
        self.patriapHijo2=Label(self, text ="Patria potestad 2")
        self.patriapHijo2Var = StringVar()
        self.patriapHijo2VarDrop= OptionMenu(self,self.patriapHijo2Var,'Ninguno','Patrocinado','Contraparte')
        self.patriapHijo2Var.set('Ninguno')
        
        self.nombreHijoEntreParte3=Label(self, text ="Nombre 3")
        self.nombreHijoEntreParte3TXT=Entry(self)
        self.sexoHijoEntreParte3=Label(self, text ="Sexo")
        self.var39 = StringVar()
        self.sexoHijoEntreParte3Drop= OptionMenu(self,self.var39,'Masculino','Femenino')
        self.RUTHijoEntreParte3=Label(self, text ="RUT 3")
        self.RUTHijoEntreParte3TXT=Entry(self)
        self.edadHijoEntreParte3=Label(self, text ="Edad 3")
        self.edadHijoEntreParte3TXT=Entry(self)
        self.cuidadoHijo3=Label(self, text ="Cuidado personal 3")
        self.cuidadoHijo3Var = StringVar()
        self.cuidadoHijo3VarDrop= OptionMenu(self,self.cuidadoHijo3Var,'Ninguno','Patrocinado','Contraparte')
        self.cuidadoHijo3Var.set('Ninguno')
        self.patriapHijo3=Label(self, text ="Patria potestad 3")
        self.patriapHijo3Var = StringVar()
        self.patriapHijo3VarDrop= OptionMenu(self,self.patriapHijo3Var,'Ninguno','Patrocinado','Contraparte')
        self.patriapHijo3Var.set('Ninguno')
        
        self.nombreHijoEntreParte4=Label(self, text ="Nombre 4")
        self.nombreHijoEntreParte4TXT=Entry(self)
        self.sexoHijoEntreParte4=Label(self, text ="Sexo")
        self.var40 = StringVar()
        self.sexoHijoEntreParte4Drop= OptionMenu(self,self.var40,'Masculino','Femenino')
        self.RUTHijoEntreParte4=Label(self, text ="RUT 4")
        self.RUTHijoEntreParte4TXT=Entry(self)
        self.edadHijoEntreParte4=Label(self, text ="Edad 4")
        self.edadHijoEntreParte4TXT=Entry(self)
        self.cuidadoHijo4=Label(self, text ="Cuidado personal 4")
        self.cuidadoHijo4Var = StringVar()
        self.cuidadoHijo4VarDrop= OptionMenu(self,self.cuidadoHijo4Var,'Ninguno','Patrocinado','Contraparte')
        self.cuidadoHijo4Var.set('Ninguno')
        self.patriapHijo4=Label(self, text ="Patria potestad 4")
        self.patriapHijo4Var = StringVar()
        self.patriapHijo4VarDrop= OptionMenu(self,self.patriapHijo4Var,'Ninguno','Patrocinado','Contraparte')
        self.patriapHijo4Var.set('Ninguno')
        
        self.nombreHijoEntreParte5=Label(self, text ="Nombre 5")
        self.nombreHijoEntreParte5TXT=Entry(self)
        self.sexoHijoEntreParte5=Label(self, text ="Sexo")
        self.var41 = StringVar()
        self.sexoHijoEntreParte5Drop= OptionMenu(self,self.var41,'Masculino','Femenino')
        self.RUTHijoEntreParte5=Label(self, text ="RUT 5")
        self.RUTHijoEntreParte5TXT=Entry(self)
        self.edadHijoEntreParte5=Label(self, text ="Edad 5")
        self.edadHijoEntreParte5TXT=Entry(self)
        self.cuidadoHijo5=Label(self, text ="Cuidado personal 5")
        self.cuidadoHijo5Var = StringVar()
        self.cuidadoHijo5VarDrop= OptionMenu(self,self.cuidadoHijo5Var,'Ninguno','Patrocinado','Contraparte')
        self.cuidadoHijo5Var.set('Ninguno')
        self.patriapHijo5=Label(self, text ="Patria potestad 5")
        self.patriapHijo5Var = StringVar()
        self.patriapHijo5VarDrop= OptionMenu(self,self.patriapHijo5Var,'Ninguno','Patrocinado','Contraparte')
        self.patriapHijo5Var.set('Ninguno')        

        self.titulo.grid(row=0,column=0)
        self.nombreHijoEntreParte1.grid(row=1,column=0)
        self.nombreHijoEntreParte1TXT.grid(row=2,column=0)
        self.sexoHijoEntreParte1.grid(row=3,column=0)
        self.sexoHijoEntreParte1Drop.grid(row=4,column=0)
        self.RUTHijoEntreParte1.grid(row=5,column=0)
        self.RUTHijoEntreParte1TXT.grid(row=6,column=0)
        self.edadHijoEntreParte1.grid(row=7,column=0)
        self.edadHijoEntreParte1TXT.grid(row=8,column=0)
        self.cuidadoHijo1.grid(row=9,column=0)
        self.cuidadoHijo1VarDrop.grid(row=10,column=0)   
        self.patriapHijo1.grid(row=11,column=0)
        self.patriapHijo1VarDrop.grid(row=12,column=0)        

        self.nombreHijoEntreParte2.grid(row=1,column=1)
        self.nombreHijoEntreParte2TXT.grid(row=2,column=1)
        self.sexoHijoEntreParte2.grid(row=3,column=1)
        self.sexoHijoEntreParte2Drop.grid(row=4,column=1)
        self.RUTHijoEntreParte2.grid(row=5,column=1)
        self.RUTHijoEntreParte2TXT.grid(row=6,column=1)
        self.edadHijoEntreParte2.grid(row=7,column=1)
        self.edadHijoEntreParte2TXT.grid(row=8,column=1)
        self.cuidadoHijo2.grid(row=9,column=1)
        self.cuidadoHijo2VarDrop.grid(row=10,column=1)   
        self.patriapHijo2.grid(row=11,column=1)
        self.patriapHijo2VarDrop.grid(row=12,column=1)        

        self.nombreHijoEntreParte3.grid(row=1,column=2)
        self.nombreHijoEntreParte3TXT.grid(row=2,column=2)
        self.sexoHijoEntreParte3.grid(row=3,column=2)
        self.sexoHijoEntreParte3Drop.grid(row=4,column=2)
        self.RUTHijoEntreParte3.grid(row=5,column=2)
        self.RUTHijoEntreParte3TXT.grid(row=6,column=2)
        self.edadHijoEntreParte3.grid(row=7,column=2)
        self.edadHijoEntreParte3TXT.grid(row=8,column=2)
        self.cuidadoHijo3.grid(row=9,column=2)
        self.cuidadoHijo3VarDrop.grid(row=10,column=2) 
        self.patriapHijo3.grid(row=11,column=2)
        self.patriapHijo3VarDrop.grid(row=12,column=2)        

        self.nombreHijoEntreParte4.grid(row= 13 ,column=0)
        self.nombreHijoEntreParte4TXT.grid(row= 14 ,column=0)
        self.sexoHijoEntreParte4.grid(row= 15 ,column=0)
        self.sexoHijoEntreParte4Drop.grid(row= 16 ,column=0)
        self.RUTHijoEntreParte4.grid(row= 17 ,column=0)
        self.RUTHijoEntreParte4TXT.grid(row= 18 ,column=0)
        self.edadHijoEntreParte4.grid(row= 19 ,column=0)
        self.edadHijoEntreParte4TXT.grid(row= 20 ,column=0)
        self.cuidadoHijo4.grid(row=21,column=0)
        self.cuidadoHijo4VarDrop.grid(row=22,column=0)     
        self.patriapHijo4.grid(row=23,column=0)
        self.patriapHijo4VarDrop.grid(row=24,column=0)        

        self.nombreHijoEntreParte5.grid(row= 13 ,column=1)
        self.nombreHijoEntreParte5TXT.grid(row= 14 ,column=1)
        self.sexoHijoEntreParte5.grid(row= 15 ,column=1)
        self.sexoHijoEntreParte5Drop.grid(row= 16 ,column=1)
        self.RUTHijoEntreParte5.grid(row= 17 ,column=1)
        self.RUTHijoEntreParte5TXT.grid(row= 18 ,column=1)
        self.edadHijoEntreParte5.grid(row= 19 ,column=1)
        self.edadHijoEntreParte5TXT.grid(row= 20 ,column=1)
        self.cuidadoHijo5.grid(row=21,column=1)
        self.cuidadoHijo5VarDrop.grid(row=22,column=1)  
        self.patriapHijo5.grid(row=23,column=1)
        self.patriapHijo5VarDrop.grid(row=24,column=1)        

        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Hijos del Patrocinado',
                                  command=lambda: controller.show_frame(HijosPatrocinado))

        button1.grid()
        button2.grid(row=17,column=2)

class HijosPatrocinado(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Hijos del Patrocinado').grid()
        self.titulo=Label(self, text ="Hijos del Patrocinado")
        self.nombreHijoPatrocinado1=Label(self, text ="Nombre 1")
        self.nombreHijoPatrocinado1TXT=Entry(self)
        self.sexoHijoPatrocinado1=Label(self, text ="Sexo")
        self.var42 = StringVar()
        self.sexoHijoPatrocinado1Drop= OptionMenu(self,self.var42,'Masculino','Femenino')
        self.RUTHijoPatrocinado1=Label(self, text ="RUT 1")
        self.RUTHijoPatrocinado1TXT=Entry(self)
        self.edadHijoPatrocinado1=Label(self, text ="Edad 1")
        self.edadHijoPatrocinado1TXT=Entry(self)
        self.nombreHijoPatrocinado2=Label(self, text ="Nombre 2")
        self.nombreHijoPatrocinado2TXT=Entry(self)
        self.sexoHijoPatrocinado2=Label(self, text ="Sexo")
        self.var43 = StringVar()
        self.sexoHijoPatrocinado2Drop= OptionMenu(self,self.var43,'Masculino','Femenino')
        self.RUTHijoPatrocinado2=Label(self, text ="RUT 2")
        self.RUTHijoPatrocinado2TXT=Entry(self)
        self.edadHijoPatrocinado2=Label(self, text ="Edad 2")
        self.edadHijoPatrocinado2TXT=Entry(self)
        self.nombreHijoPatrocinado3=Label(self, text ="Nombre 3")
        self.nombreHijoPatrocinado3TXT=Entry(self)
        self.sexoHijoPatrocinado3=Label(self, text ="Sexo")
        self.var44 = StringVar()
        self.sexoHijoPatrocinado3Drop= OptionMenu(self,self.var44,'Masculino','Femenino')
        self.RUTHijoPatrocinado3=Label(self, text ="RUT 3")
        self.RUTHijoPatrocinado3TXT=Entry(self)
        self.edadHijoPatrocinado3=Label(self, text ="Edad 3")
        self.edadHijoPatrocinado3TXT=Entry(self)
        self.nombreHijoPatrocinado4=Label(self, text ="Nombre 4")
        self.nombreHijoPatrocinado4TXT=Entry(self)
        self.sexoHijoPatrocinado4=Label(self, text ="Sexo")
        self.var45 = StringVar()
        self.sexoHijoPatrocinado4Drop= OptionMenu(self,self.var45,'Masculino','Femenino')
        self.RUTHijoPatrocinado4=Label(self, text ="RUT 4")
        self.RUTHijoPatrocinado4TXT=Entry(self)
        self.edadHijoPatrocinado4=Label(self, text ="Edad 4")
        self.edadHijoPatrocinado4TXT=Entry(self)
        self.nombreHijoPatrocinado5=Label(self, text ="Nombre 5")
        self.nombreHijoPatrocinado5TXT=Entry(self)
        self.sexoHijoPatrocinado5=Label(self, text ="Sexo")
        self.var46 = StringVar()
        self.sexoHijoPatrocinado5Drop= OptionMenu(self,self.var46,'Masculino','Femenino')
        self.RUTHijoPatrocinado5=Label(self, text ="RUT 5")
        self.RUTHijoPatrocinado5TXT=Entry(self)
        self.edadHijoPatrocinado5=Label(self, text ="Edad 5")
        self.edadHijoPatrocinado5TXT=Entry(self)

        self.titulo.grid(row=0,column=0)
        self.nombreHijoPatrocinado1.grid(row=1,column=0)
        self.nombreHijoPatrocinado1TXT.grid(row=2,column=0)
        self.sexoHijoPatrocinado1.grid(row=3,column=0)
        self.sexoHijoPatrocinado1Drop.grid(row=4,column=0)
        self.RUTHijoPatrocinado1.grid(row=5,column=0)
        self.RUTHijoPatrocinado1TXT.grid(row=6,column=0)
        self.edadHijoPatrocinado1.grid(row=7,column=0)
        self.edadHijoPatrocinado1TXT.grid(row=8,column=0)

        self.nombreHijoPatrocinado2.grid(row=1,column=1)
        self.nombreHijoPatrocinado2TXT.grid(row=2,column=1)
        self.sexoHijoPatrocinado2.grid(row=3,column=1)
        self.sexoHijoPatrocinado2Drop.grid(row=4,column=1)
        self.RUTHijoPatrocinado2.grid(row=5,column=1)
        self.RUTHijoPatrocinado2TXT.grid(row=6,column=1)
        self.edadHijoPatrocinado2.grid(row=7,column=1)
        self.edadHijoPatrocinado2TXT.grid(row=8,column=1)

        self.nombreHijoPatrocinado3.grid(row=1,column=2)
        self.nombreHijoPatrocinado3TXT.grid(row=2,column=2)
        self.sexoHijoPatrocinado3.grid(row=3,column=2)
        self.sexoHijoPatrocinado3Drop.grid(row=4,column=2)
        self.RUTHijoPatrocinado3.grid(row=5,column=2)
        self.RUTHijoPatrocinado3TXT.grid(row=6,column=2)
        self.edadHijoPatrocinado3.grid(row=7,column=2)
        self.edadHijoPatrocinado3TXT.grid(row=8,column=2)

        self.nombreHijoPatrocinado4.grid(row= 9 ,column=0)
        self.nombreHijoPatrocinado4TXT.grid(row= 10 ,column=0)
        self.sexoHijoPatrocinado4.grid(row= 11 ,column=0)
        self.sexoHijoPatrocinado4Drop.grid(row= 12 ,column=0)
        self.RUTHijoPatrocinado4.grid(row= 13 ,column=0)
        self.RUTHijoPatrocinado4TXT.grid(row= 14 ,column=0)
        self.edadHijoPatrocinado4.grid(row= 15 ,column=0)
        self.edadHijoPatrocinado4TXT.grid(row= 16 ,column=0)

        self.nombreHijoPatrocinado5.grid(row= 9 ,column=1)
        self.nombreHijoPatrocinado5TXT.grid(row= 10 ,column=1)
        self.sexoHijoPatrocinado5.grid(row= 11 ,column=1)
        self.sexoHijoPatrocinado5Drop.grid(row= 12 ,column=1)
        self.RUTHijoPatrocinado5.grid(row= 13 ,column=1)
        self.RUTHijoPatrocinado5TXT.grid(row= 14 ,column=1)
        self.edadHijoPatrocinado5.grid(row= 15 ,column=1)
        self.edadHijoPatrocinado5TXT.grid(row= 16 ,column=1)
        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))
        button2 = ttk.Button(self, text='Hijos de la Contraparte',
                                  command=lambda: controller.show_frame(HijosContraparte))

        button1.grid()
        button2.grid(row=17,column=2)

class HijosContraparte(ttk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        self.titulo=Label(self, text ="Hijos de la Contraparte")
        self.nombreHijoContraparte1=Label(self, text ="Nombre 1")
        self.nombreHijoContraparte1TXT=Entry(self)
        self.sexoHijoContraparte1=Label(self, text ="Sexo")
        self.var47 = StringVar()
        self.sexoHijoContraparte1Drop= OptionMenu(self,self.var47,'Masculino','Femenino')
        self.RUTHijoContraparte1=Label(self, text ="RUT 1")
        self.RUTHijoContraparte1TXT=Entry(self)
        self.edadHijoContraparte1=Label(self, text ="Edad 1")
        self.edadHijoContraparte1TXT=Entry(self)
        self.nombreHijoContraparte2=Label(self, text ="Nombre 2")
        self.nombreHijoContraparte2TXT=Entry(self)
        self.sexoHijoContraparte2=Label(self, text ="Sexo")
        self.var48 = StringVar()
        self.sexoHijoContraparte2Drop= OptionMenu(self,self.var48,'Masculino','Femenino')
        self.RUTHijoContraparte2=Label(self, text ="RUT 2")
        self.RUTHijoContraparte2TXT=Entry(self)
        self.edadHijoContraparte2=Label(self, text ="Edad 2")
        self.edadHijoContraparte2TXT=Entry(self)
        self.nombreHijoContraparte3=Label(self, text ="Nombre 3")
        self.nombreHijoContraparte3TXT=Entry(self)
        self.sexoHijoContraparte3=Label(self, text ="Sexo")
        self.var49 = StringVar()
        self.sexoHijoContraparte3Drop= OptionMenu(self,self.var49,'Masculino','Femenino')
        self.RUTHijoContraparte3=Label(self, text ="RUT 3")
        self.RUTHijoContraparte3TXT=Entry(self)
        self.edadHijoContraparte3=Label(self, text ="Edad 3")
        self.edadHijoContraparte3TXT=Entry(self)
        self.nombreHijoContraparte4=Label(self, text ="Nombre 4")
        self.nombreHijoContraparte4TXT=Entry(self)
        self.sexoHijoContraparte4=Label(self, text ="Sexo")
        self.var50 = StringVar()
        self.sexoHijoContraparte4Drop= OptionMenu(self,self.var50,'Masculino','Femenino')
        self.RUTHijoContraparte4=Label(self, text ="RUT 4")
        self.RUTHijoContraparte4TXT=Entry(self)
        self.edadHijoContraparte4=Label(self, text ="Edad 4")
        self.edadHijoContraparte4TXT=Entry(self)
        self.nombreHijoContraparte5=Label(self, text ="Nombre 5")
        self.nombreHijoContraparte5TXT=Entry(self)
        self.sexoHijoContraparte5=Label(self, text ="Sexo")
        self.var51 = StringVar()
        self.sexoHijoContraparte5Drop= OptionMenu(self,self.var51,'Masculino','Femenino')
        self.RUTHijoContraparte5=Label(self, text ="RUT 5")
        self.RUTHijoContraparte5TXT=Entry(self)
        self.edadHijoContraparte5=Label(self, text ="Edad 5")
        self.edadHijoContraparte5TXT=Entry(self)

        button1 = ttk.Button(self, text='Inicio',
                                  command=lambda: controller.show_frame(Inicio))

        self.titulo.grid(row=0,column=0)
        self.nombreHijoContraparte1.grid(row=1,column=0)
        self.nombreHijoContraparte1TXT.grid(row=2,column=0)
        self.sexoHijoContraparte1.grid(row=3,column=0)
        self.sexoHijoContraparte1Drop.grid(row=4,column=0)
        self.RUTHijoContraparte1.grid(row=5,column=0)
        self.RUTHijoContraparte1TXT.grid(row=6,column=0)
        self.edadHijoContraparte1.grid(row=7,column=0)
        self.edadHijoContraparte1TXT.grid(row=8,column=0)

        self.nombreHijoContraparte2.grid(row=1,column=1)
        self.nombreHijoContraparte2TXT.grid(row=2,column=1)
        self.sexoHijoContraparte2.grid(row=3,column=1)
        self.sexoHijoContraparte2Drop.grid(row=4,column=1)
        self.RUTHijoContraparte2.grid(row=5,column=1)
        self.RUTHijoContraparte2TXT.grid(row=6,column=1)
        self.edadHijoContraparte2.grid(row=7,column=1)
        self.edadHijoContraparte2TXT.grid(row=8,column=1)

        self.nombreHijoContraparte3.grid(row=1,column=2)
        self.nombreHijoContraparte3TXT.grid(row=2,column=2)
        self.sexoHijoContraparte3.grid(row=3,column=2)
        self.sexoHijoContraparte3Drop.grid(row=4,column=2)
        self.RUTHijoContraparte3.grid(row=5,column=2)
        self.RUTHijoContraparte3TXT.grid(row=6,column=2)
        self.edadHijoContraparte3.grid(row=7,column=2)
        self.edadHijoContraparte3TXT.grid(row=8,column=2)

        self.nombreHijoContraparte4.grid(row= 9 ,column=0)
        self.nombreHijoContraparte4TXT.grid(row= 10 ,column=0)
        self.sexoHijoContraparte4.grid(row= 11 ,column=0)
        self.sexoHijoContraparte4Drop.grid(row= 12 ,column=0)
        self.RUTHijoContraparte4.grid(row= 13 ,column=0)
        self.RUTHijoContraparte4TXT.grid(row= 14 ,column=0)
        self.edadHijoContraparte4.grid(row= 15 ,column=0)
        self.edadHijoContraparte4TXT.grid(row= 16 ,column=0)

        self.nombreHijoContraparte5.grid(row= 9 ,column=1)
        self.nombreHijoContraparte5TXT.grid(row= 10 ,column=1)
        self.sexoHijoContraparte5.grid(row= 11 ,column=1)
        self.sexoHijoContraparte5Drop.grid(row= 12 ,column=1)
        self.RUTHijoContraparte5.grid(row= 13 ,column=1)
        self.RUTHijoContraparte5TXT.grid(row= 14 ,column=1)
        self.edadHijoContraparte5.grid(row= 15 ,column=1)
        self.edadHijoContraparte5TXT.grid(row= 16 ,column=1)

        button2 = ttk.Button(self, text='Configuración',
                                  command=lambda: controller.show_frame(Configuracion))

        button1.grid()
        button2.grid(row=17,column=2)
data={}
class Configuracion(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Configuracion').grid()

        button1 = ttk.Button(self, text='Guardar', command=self.guardar)
        button2 = ttk.Button(self, text='Cargar', command=self.cargar)
        button3 = ttk.Button(self, text='Inicio',
                             command=lambda: controller.show_frame(Inicio))

        patrocinioBTN=ttk.Button(self,text='Otorga Patrocinio y Poder',command=patrocinioYPoder)
        dmaBTN=ttk.Button(self,text='Demanda Divorcio de Mutuo Acuerdo',command=divorcioMutuoAcuerdo)
        renPatrocFinBTN=ttk.Button(self,text='Renuncia Patrocinio y Poder por fin de la gestión', command=patrocinioYPoderFin)
        dceseBTN=ttk.Button(self,text='Divorcio Unilateral por Cese de Convivencia',command=divorcioUnilateralCese)
        aCYSBTN=ttk.Button(self,text='Acuerdo Completo y Suficiente Simple', command = acuerdoCompletoSimple)
        aCYSEPBTN=ttk.Button(self, text='Acuerdo C. y S. en Escritura Pública', command = acuerdoCompletoEscPub)
        aM=ttk.Button(self, text= 'Demanda Alimentos Menores', command = alimentosMenores)

        patrocinioBTN.grid(row=1,column=0)
        dmaBTN.grid(row=2,column=0)
        aCYSBTN.grid(row=3,column=0)
        aM.grid(row=4, column=0)
        aCYSEPBTN.grid(column=0)
        dceseBTN.grid(column=0)
        renPatrocFinBTN.grid(column=0)
        button1.grid()
        button2.grid()
        button3.grid()


    def guardar(self):
        
        get_pat = self.controller.get_page("Patrocinado")
        get_contrap = self.controller.get_page("Contraparte")
        get_matri = self.controller.get_page("Matrimonio")
        get_adic = self.controller.get_page("Adicionales")
        get_acu = self.controller.get_page("Acuerdo")
        get_hijopart=self.controller.get_page("HijosEntrePartes")
        get_hijopatro=self.controller.get_page("HijosPatrocinado")
        get_hijocontrap=self.controller.get_page("HijosContraparte")

        data['nombrePatrocinado']=get_pat.nombPatTXT.get()
        data['apellidoPaternoPatrocinado']=get_pat.apePatPatTXT.get()
        data['apellidoMaternoPatrocinado']=get_pat.apeMatPatTXT.get()
        data['sexoPatrocinado']=get_pat.var1.get()
        data['nacionalidadPatrocinado']=get_pat.nacPatTXT.get()
        data['estadoCivilPatrocinado']=get_pat.var2.get()
        data['rutPatrocinado']=get_pat.rutPatTXT.get()
        data['profesionPatrocinado']=get_pat.profPatTXT.get()
        data['domicilioPatrocinado']=get_pat.domicPatTXT.get()
        data['numeroDomicilioPatrocinado']=get_pat.numDomicPatTXT.get()
        data['comunaPatrocinado']=get_pat.comunaPatTXT.get()
        data['ciudadPatrocinado']=get_pat.ciudPatTXT.get()
        data['regionPatrocinado']=get_pat.regPatVar.get()        
        data['situacionProcesalPatrocinado']=get_pat.var16.get()

        data['nombreAbogadoPatrocinado']=get_pat.nombAboPatTXT.get()
        data['apellidoPaternoAbogadoPatrocinado']=get_pat.apePatAboPatTXT.get()
        data['apellidoMaternoAbogadoPatrocinado']=get_pat.apeMatAboPatTXT.get()
        data['sexoAbogadoPatrocinado']=get_pat.var3.get()
        data['nacionalidadAbogadoPatrocinado']=get_pat.nacAboPatTXT.get()
        data['estadoCivilAbogadoPatrocinado']=get_pat.var4.get()
        data['rutAbogadoPatrocinado']=get_pat.rutAboPatTXT.get()
        data['emailAbogadoPatrocinado']=get_pat.emailAboPatTXT.get()
        data['domicilioAbogadoPatrocinado']=get_pat.domicAboPatTXT.get()
        data['facultadesAbogadoPatrocinado']=get_pat.facAboPatVar.get()
        data['numeroDomicilioAbogadoPatrocinado']=get_pat.numDomicAboPatTXT.get()
        data['comunaAbogadoPatrocinado']=get_pat.comunaAboPatTXT.get()
        data['ciudadAbogadoPatrocinado']=get_pat.ciudAboPatTXT.get()
        data['regionAbogadoPatrocinado']=get_pat.regAboPatVar.get()        

        data['nombreApoderadoPatrocinado']=get_pat.nombApoPatTXT.get()
        data['apellidoPaternoApoderadoPatrocinado']=get_pat.apePatApoPatTXT.get()
        data['apellidoMaternoApoderadoPatrocinado']=get_pat.apeMatApoPatTXT.get()
        data['sexoApoderadoPatrocinado']=get_pat.var33.get()
        data['nacionalidadApoderadoPatrocinado']=get_pat.nacApoPatTXT.get()
        data['estadoCivilApoderadoPatrocinado']=get_pat.var34.get()
        data['facultadesApoderadoPatrocinado']=get_pat.facApoPatVar.get()        
        data['rutApoderadoPatrocinado']=get_pat.rutApoPatTXT.get()
        data['emailApoderadoPatrocinado']=get_pat.emailApoPatTXT.get()
        data['domicilioApoderadoPatrocinado']=get_pat.domicApoPatTXT.get()
        data['numeroDomicilioApoderadoPatrocinado']=get_pat.numDomicApoPatTXT.get()
        data['comunaApoderadoPatrocinado']=get_pat.comunaApoPatTXT.get()
        data['ciudadApoderadoPatrocinado']=get_pat.ciudApoPatTXT.get()
        data['regionApoderadoPatrocinado']=get_pat.regApoPatVar.get()        

        data['nombreContraparte']=get_contrap.nombContrapTXT.get()
        data['apellidoPaternoContraparte']=get_contrap.apePatContrapTXT.get()
        data['apellidoMaternoContraparte']=get_contrap.apeMatContrapTXT.get()
        data['sexoContraparte']=get_contrap.var5.get()
        data['nacionalidadContraparte']=get_contrap.nacContrapTXT.get()
        data['estadoCivilContraparte']=get_contrap.var6.get()
        data['rutContraparte']=get_contrap.rutContrapTXT.get()
        data['profesionContraparte']=get_contrap.profContrapTXT.get()
        data['domicilioContraparte']=get_contrap.domicContrapTXT.get()
        data['numeroDomicilioContraparte']=get_contrap.numDomicContrapTXT.get()
        data['comunaContraparte']=get_contrap.comunaContrapTXT.get()
        data['ciudadContraparte']=get_contrap.ciudContrapTXT.get()
        data['regionContraparte']=get_contrap.regContrapVar.get()        

        data['nombreAbogadoContraparte']=get_contrap.nombAboContrapTXT.get()
        data['apellidoPaternoAbogadoContraparte']=get_contrap.apePatAboContrapTXT.get()
        data['apellidoMaternoAbogadoContraparte']=get_contrap.apeMatAboContrapTXT.get()
        data['sexoAbogadoContraparte']=get_contrap.var7.get()
        data['nacionalidadAbogadoContraparte']=get_contrap.nacAboContrapTXT.get()
        data['estadoCivilAbogadoContraparte']=get_contrap.var8.get()
        data['facultadesAbogadoContraparte']=get_contrap.facAboContrapVar.get()
        data['rutAbogadoContraparte']=get_contrap.rutAboContrapTXT.get()
        data['emailAbogadoContraparte']=get_contrap.emailAboContrapTXT.get()
        data['domicilioAbogadoContraparte']=get_contrap.domicAboContrapTXT.get()
        data['numeroDomicilioAbogadoContraparte']=get_contrap.numDomicAboContrapTXT.get()
        data['comunaAbogadoContraparte']=get_contrap.comunaAboContrapTXT.get()
        data['ciudadAbogadoContraparte']=get_contrap.ciudAboContrapTXT.get()
        data['regionAbogadoContraparte']=get_contrap.regAboContrapVar.get()        

        data['nombreApoderadoContraparte']=get_contrap.nombApoContrapTXT.get()
        data['apellidoPaternoApoderadoContraparte']=get_contrap.apePatApoContrapTXT.get()
        data['apellidoMaternoApoderadoContraparte']=get_contrap.apeMatApoContrapTXT.get()
        data['sexoApoderadoContraparte']=get_contrap.var35.get()
        data['nacionalidadApoderadoContraparte']=get_contrap.nacApoContrapTXT.get()
        data['estadoCivilApoderadoContraparte']=get_contrap.var36.get()
        data['facultadesApoderadoContraparte']=get_contrap.facApoContrapVar.get()        
        data['rutApoderadoContraparte']=get_contrap.rutApoContrapTXT.get()
        data['emailApoderadoContraparte']=get_contrap.emailApoContrapTXT.get()
        data['domicilioApoderadoContraparte']=get_contrap.domicApoContrapTXT.get()
        data['numeroDomicilioApoderadoContraparte']=get_contrap.numDomicApoContrapTXT.get()
        data['comunaApoderadoContraparte']=get_contrap.comunaApoContrapTXT.get()
        data['ciudadApoderadoContraparte']=get_contrap.ciudApoContrapTXT.get()
        data['regionApoderadoContraparte']=get_contrap.regApoContrapVar.get()        

        data['diaDeMatrimonio']=get_matri.var9.get()
        data['mesDeMatrimonio']=get_matri.var10.get()
        data['añoDeMatrimonio']=get_matri.añoMatrimonioTXT.get()
        data['comunaDeMatrimonio']=get_matri.comunaMatrimonioTXT.get()
        data['numeroInscripcionMatrimonio']=get_matri.numeroInscripcionTXT.get()
        data['regimenMatrimonial']=get_matri.var11.get()
        data['existeBienQueLiquidar']=get_matri.existeBienVar.get()
        data['diaDeCeseConvivencia']=get_matri.var12.get()
        data['mesDeCeseConvivencia']=get_matri.var13.get()
        data['añoDeCeseConvivencia']=get_matri.añoCeseConvivenciaTXT.get()
        
        data['añosDuracionRelacion']=get_matri.añosDuracionRelacionTXT.get()
        data['mesesDuracionRelacion']=get_matri.mesesDuracionRelacionTXT.get()
        data['diaCeseRelacion']=get_matri.diaCeseRelacionVar.get()
        data['mesCeseRelacion']=get_matri.mesCeseRelacionVar.get()
        data['añoCeseRelacion']=get_matri.añoCeseRelacionTXT.get()
        

        data['ritDeCausa']=get_adic.ritCausaTXT.get()
        data['juzgado']=get_adic.var15.get()
        data['materiaCausa']=get_adic.varMateria.get()
        data['caratulaCausa']=get_adic.caratulaTXT.get()
        data['pideCompensacionEconomica']=get_adic.var14.get()
        data['abandonaHogarComun']=get_adic.varAbandona.get()
        data['nuevaRelacionPatrocinado']=get_adic.nuevaRelPat.get()
        data['añosRelacionPatrocinado']=get_adic.añosRelacionPatrocinadoTXT.get()
        data['nuevaRelacionContraparte']=get_adic.nuevaRelCont.get()
        data['añosRelacionContraparte']=get_adic.añosRelacionContraparteTXT.get()
        data['huboMediacion'] = get_adic.huboMedVar.get()
        data['ritMediacion'] = get_adic.ritMedTXT.get()
        data['modoPagoCompensacion']=get_adic.pagoCompVar.get()
        data['valorCompensacion']=get_adic.valorCompTXT.get()
        data['direccionInmueblePagoCompensacion']=get_adic.dirInmCompTXT.get()
        data['numeroInmueblePagoCompensacion'] = get_adic.numInmCompTXT.get()        
        data['comunaInmueblePagoCompensacion'] = get_adic.comunaInmCompTXT.get() 
        data['pagoAlimentosContraparte'] = get_adic.pagoAlimContrapVar.get()
        
       


        

        data['pagaAlimentosMenores']=get_acu.pagaAlimMenoresVar.get()
        data['cuantiaAlimentosMenores']=get_acu.alimMenoresTXT.get()
        data['cuantiaIMR']=get_acu.cuantIMRTXT.get()

        data['nombreDeHijoEntreParte1']=get_hijopart.nombreHijoEntreParte1TXT.get()
        data['sexoDeHijoEntreParte1']=get_hijopart.var37.get()
        data['rutDeHijoEntreParte1']=get_hijopart.RUTHijoEntreParte1TXT.get()
        data['edadDeHijoEntreParte1']=get_hijopart.edadHijoEntreParte1TXT.get()
        data['cuidadoPersonalHijo1']=get_hijopart.cuidadoHijo1Var.get()
        data['patriaPotestadHijo1']=get_hijopart.patriapHijo1Var.get()        
        data['nombreDeHijoEntreParte2']=get_hijopart.nombreHijoEntreParte2TXT.get()
        data['sexoDeHijoEntreParte2']=get_hijopart.var38.get()
        data['rutDeHijoEntreParte2']=get_hijopart.RUTHijoEntreParte2TXT.get()
        data['edadDeHijoEntreParte2']=get_hijopart.edadHijoEntreParte2TXT.get()
        data['cuidadoPersonalHijo2']=get_hijopart.cuidadoHijo2Var.get()
        data['patriaPotestadHijo2']=get_hijopart.patriapHijo2Var.get()        
        data['nombreDeHijoEntreParte3']=get_hijopart.nombreHijoEntreParte3TXT.get()
        data['sexoDeHijoEntreParte3']=get_hijopart.var39.get()
        data['rutDeHijoEntreParte3']=get_hijopart.RUTHijoEntreParte3TXT.get()
        data['edadDeHijoEntreParte3']=get_hijopart.edadHijoEntreParte3TXT.get()
        data['cuidadoPersonalHijo3']=get_hijopart.cuidadoHijo3Var.get()
        data['patriaPotestadHijo3']=get_hijopart.patriapHijo3Var.get()        
        data['nombreDeHijoEntreParte4']=get_hijopart.nombreHijoEntreParte4TXT.get()
        data['sexoDeHijoEntreParte4']=get_hijopart.var40.get()
        data['rutDeHijoEntreParte4']=get_hijopart.RUTHijoEntreParte4TXT.get()
        data['edadDeHijoEntreParte4']=get_hijopart.edadHijoEntreParte4TXT.get()
        data['cuidadoPersonalHijo4']=get_hijopart.cuidadoHijo4Var.get()
        data['patriaPotestadHijo4']=get_hijopart.patriapHijo4Var.get()        
        data['nombreDeHijoEntreParte5']=get_hijopart.nombreHijoEntreParte5TXT.get()
        data['sexoDeHijoEntreParte5']=get_hijopart.var41.get()
        data['rutDeHijoEntreParte5']=get_hijopart.RUTHijoEntreParte5TXT.get()
        data['edadDeHijoEntreParte5']=get_hijopart.edadHijoEntreParte5TXT.get()
        data['cuidadoPersonalHijo5']=get_hijopart.cuidadoHijo5Var.get()
        data['patriaPotestadHijo5']=get_hijopart.patriapHijo5Var.get()
        
        data['nombreDeHijoPatrocinado1']=get_hijopatro.nombreHijoPatrocinado1TXT.get()
        data['sexoDeHijoPatrocinado1']=get_hijopatro.var42.get()
        data['rutDeHijoPatrocinado1']=get_hijopatro.RUTHijoPatrocinado1TXT.get()
        data['edadDeHijoPatrocinado1']=get_hijopatro.edadHijoPatrocinado1TXT.get()
        data['nombreDeHijoPatrocinado2']=get_hijopatro.nombreHijoPatrocinado2TXT.get()
        data['sexoDeHijoPatrocinado2']=get_hijopatro.var43.get()
        data['rutDeHijoPatrocinado2']=get_hijopatro.RUTHijoPatrocinado2TXT.get()
        data['edadDeHijoPatrocinado2']=get_hijopatro.edadHijoPatrocinado2TXT.get()
        data['nombreDeHijoPatrocinado3']=get_hijopatro.nombreHijoPatrocinado3TXT.get()
        data['sexoDeHijoPatrocinado3']=get_hijopatro.var44.get()
        data['rutDeHijoPatrocinado3']=get_hijopatro.RUTHijoPatrocinado3TXT.get()
        data['edadDeHijoPatrocinado3']=get_hijopatro.edadHijoPatrocinado3TXT.get()
        data['nombreDeHijoPatrocinado4']=get_hijopatro.nombreHijoPatrocinado4TXT.get()
        data['sexoDeHijoPatrocinado4']=get_hijopatro.var45.get()
        data['rutDeHijoPatrocinado4']=get_hijopatro.RUTHijoPatrocinado4TXT.get()
        data['edadDeHijoPatrocinado4']=get_hijopatro.edadHijoPatrocinado4TXT.get()
        data['nombreDeHijoPatrocinado5']=get_hijopatro.nombreHijoPatrocinado5TXT.get()
        data['sexoDeHijoPatrocinado5']=get_hijopatro.var46.get()
        data['rutDeHijoPatrocinado5']=get_hijopatro.RUTHijoPatrocinado5TXT.get()
        data['edadDeHijoPatrocinado5']=get_hijopatro.edadHijoPatrocinado5TXT.get()

        data['nombreDeHijoContraparte1']=get_hijocontrap.nombreHijoContraparte1TXT.get()
        data['sexoDeHijoContraparte1']=get_hijocontrap.var47.get()
        data['rutDeHijoContraparte1']=get_hijocontrap.RUTHijoContraparte1TXT.get()
        data['edadDeHijoContraparte1']=get_hijocontrap.edadHijoContraparte1TXT.get()
        data['nombreDeHijoContraparte2']=get_hijocontrap.nombreHijoContraparte2TXT.get()
        data['sexoDeHijoContraparte2']=get_hijocontrap.var48.get()
        data['rutDeHijoContraparte2']=get_hijocontrap.RUTHijoContraparte2TXT.get()
        data['edadDeHijoContraparte2']=get_hijocontrap.edadHijoContraparte2TXT.get()
        data['nombreDeHijoContraparte3']=get_hijocontrap.nombreHijoContraparte3TXT.get()
        data['sexoDeHijoContraparte3']=get_hijocontrap.var49.get()
        data['rutDeHijoContraparte3']=get_hijocontrap.RUTHijoContraparte3TXT.get()
        data['edadDeHijoContraparte3']=get_hijocontrap.edadHijoContraparte3TXT.get()
        data['nombreDeHijoContraparte4']=get_hijocontrap.nombreHijoContraparte4TXT.get()
        data['sexoDeHijoContraparte4']=get_hijocontrap.var50.get()
        data['rutDeHijoContraparte4']=get_hijocontrap.RUTHijoContraparte4TXT.get()
        data['edadDeHijoContraparte4']=get_hijocontrap.edadHijoContraparte4TXT.get()
        data['nombreDeHijoContraparte5']=get_hijocontrap.nombreHijoContraparte5TXT.get()
        data['sexoDeHijoContraparte5']=get_hijocontrap.var51.get()
        data['rutDeHijoContraparte5']=get_hijocontrap.RUTHijoContraparte5TXT.get()
        data['edadDeHijoContraparte5']=get_hijocontrap.edadHijoContraparte5TXT.get()
        
        if len(get_matri.añoCeseConvivenciaTXT.get())==4 and len(get_matri.añoMatrimonioTXT.get())==4:
            data['duracionMatrimonio']=int(get_matri.añoCeseConvivenciaTXT.get())-int(get_matri.añoMatrimonioTXT.get())
        elif len(get_matri.añoMatrimonioTXT.get())!=4:
            data['duracionMatrimonio']='ERROR: AÑO DE MATRIMONIO DEBE SER UNA CIFRA DE 4 DÍGITOS'
        elif len(get_matri.añoCeseConvivenciaTXT.get()):
            data['duracionMatrimonio']='ERROR: AÑO DE CESE DE CONVIVENCIA DEBE SER UNA CIFRA DE 4 DÍGITOS'


        if 'F' in get_pat.var3.get():
            data['profesionAbogadoPatrocinado']="abogada"
            data['conectorAbogadoPatrocinado']='la'
            data['conector2AbogadoPatrocinado']='a la'
            data['generoAbogadoPatrocinado']='a'
            data['honorificoAbogadoPatrocinado']='doña'
        elif 'M' in get_pat.var3.get():
            data['profesionAbogadoPatrocinado']="abogado"
            data['conectorAbogadoPatrocinado']='el'
            data['conector2AbogadoPatrocinado']='al'
            data['generoAbogadoPatrocinado']='o'
            data['honorificoAbogadoPatrocinado']='don'

        if 'F' in get_pat.var33.get():
            data['profesionApoderadoPatrocinado']="abogada"
            data['conectorApoderadoPatrocinado']='la'
            data['conector2ApoderadoPatrocinado']='a la'
            data['generoApoderadoPatrocinado']='a'
            data['honorificoApoderadoPatrocinado']='doña'
        elif 'M' in get_pat.var33.get():
            data['profesionApoderadoPatrocinado']="abogado"
            data['conectorApoderadoPatrocinado']='el'
            data['conector2ApoderadoPatrocinado']='al'
            data['generoApoderadoPatrocinado']='o'
            data['honorificoApoderadoPatrocinado']='don'               

        if 'F' in get_contrap.var7.get():
            data['profesionAbogadoContraparte']="abogada"
            data['conectorAbogadoContraparte']='la'
            data['conector2AbogadoContraparte']='a la'
            data['generoAbogadoContraparte']='a'
            data['honorificoAbogadoContraparte']='doña'
        elif 'M' in get_contrap.var7.get():
            data['profesionAbogadoContraparte']="abogado"
            data['conectorAbogadoContraparte']='el'
            data['conector2AbogadoContraparte']='al'
            data['generoAbogadoContraparte']='o'
            data['honorificoAbogadoContraparte']='don'            

        if 'F' in get_contrap.var35.get():
            data['profesionApoderadoContraparte']="abogada"
            data['conectorApoderadoContraparte']='la'
            data['conector2ApoderadoContraparte']='a la'
            data['generoApoderadoContraparte']='a'
            data['honorificoApoderadoContraparte']='doña'
        elif 'M' in get_contrap.var35.get():
            data['profesionApoderadoContraparte']="abogado"
            data['conectorApoderadoContraparte']='el'
            data['conector2ApoderadoContraparte']='al'
            data['generoApoderadoContraparte']='o'
            data['honorificoApoderadoContraparte']='don' 


        if 'F' in get_pat.var1.get():
            if 'Casado' in get_pat.var2.get():
                estadoCivilPatrocinado='casada'
            elif 'Divorciado' in get_pat.var2.get():
                estadoCivilPatrocinado='divorciada'
            elif 'Viudo' in get_pat.var2.get():
                estadoCivilPatrocinado='viuda'
            elif 'Soltero' in get_pat.var2.get():
                estadoCivilPatrocinado='soltera'
            elif 'Separado' in get_pat.var2.get():
                estadoCivilPatrocinado='separada'

        elif 'M' in get_pat.var1.get():
            if 'Casado' in get_pat.var2.get():
                estadoCivilPatrocinado='casado'
            elif 'Divorciado' in get_pat.var2.get():
                estadoCivilPatrocinado='divorciado'
            elif 'Viudo' in get_pat.var2.get():
                estadoCivilPatrocinado='viudo'
            elif 'Soltero' in get_pat.var2.get():
                estadoCivilPatrocinado='soltero'
            elif 'Separado' in get_pat.var2.get():
                estadoCivilPatrocinado='separado' 

        if 'F' in get_contrap.var5.get():
            if 'Casado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='casada'
            elif 'Divorciado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='divorciada'
            elif 'Viudo' in get_contrap.var6.get():
                data['estadoCivilContraparte']='viuda'
            elif 'Soltero' in get_contrap.var6.get():
                data['estadoCivilContraparte']='soltera'
            elif 'Separado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='separada'

        elif 'M' in get_contrap.var5.get():
            if 'Casado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='casado'
            elif 'Divorciado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='divorciado'
            elif 'Viudo' in get_contrap.var6.get():
                data['estadoCivilContraparte']='viudo'
            elif 'Soltero' in get_contrap.var6.get():
                data['estadoCivilContraparte']='soltero'
            elif 'Separado' in get_contrap.var6.get():
                data['estadoCivilContraparte']='separado'                

        if 'F' in get_pat.var1.get():
            data['conectorPatrocinado']='la'
            data['generoPatrocinado']='a'
            data['honorificoPatrocinado']='doña'        
        elif 'M' in get_pat.var1.get():
            data['conectorPatrocinado']='el'
            data['generoPatrocinado']='o'
            data['honorificoPatrocinado']='don'        

        if 'F' in get_contrap.var5.get():
            data['conectorContraparte']='la'
            data['generoContraparte']='a'
            data['honorificoContraparte']='doña'        
        elif 'M' in get_contrap.var5.get():
            data['conectorContraparte']='el'
            data['generoContraparte']='o'
            data['honorificoContraparte']='don'
            
        if 'ante' in get_pat.var16.get():
            data['situacionProcesalPatrocinado']='demandante'
        elif 'ado' in get_pat.var16.get():
            data['situacionProcesalPatrocinado']='demandada'

        data['hijosEntrePartes']=0
        if 'a' in get_hijopart.nombreHijoEntreParte1TXT.get() or 'e' in get_hijopart.nombreHijoEntreParte1TXT.get() or 'i' in get_hijopart.nombreHijoEntreParte1TXT.get() or 'o' in get_hijopart.nombreHijoEntreParte1TXT.get() or 'u' in get_hijopart.nombreHijoEntreParte1TXT.get():
            data['hijosEntrePartes']+=1
        if 'a' in get_hijopart.nombreHijoEntreParte2TXT.get() or 'e' in get_hijopart.nombreHijoEntreParte2TXT.get() or 'i' in get_hijopart.nombreHijoEntreParte2TXT.get() or 'o' in get_hijopart.nombreHijoEntreParte2TXT.get() or 'u' in get_hijopart.nombreHijoEntreParte2TXT.get():
            data['hijosEntrePartes']+=1    
        if 'a' in get_hijopart.nombreHijoEntreParte3TXT.get() or 'e' in get_hijopart.nombreHijoEntreParte3TXT.get() or 'i' in get_hijopart.nombreHijoEntreParte3TXT.get() or 'o' in get_hijopart.nombreHijoEntreParte3TXT.get() or 'u' in get_hijopart.nombreHijoEntreParte3TXT.get():
            data['hijosEntrePartes']+=1
        if 'a' in get_hijopart.nombreHijoEntreParte4TXT.get() or 'e' in get_hijopart.nombreHijoEntreParte4TXT.get() or 'i' in get_hijopart.nombreHijoEntreParte4TXT.get() or 'o' in get_hijopart.nombreHijoEntreParte4TXT.get() or 'u' in get_hijopart.nombreHijoEntreParte4TXT.get():
            data['hijosEntrePartes']+=1
        if 'a' in get_hijopart.nombreHijoEntreParte5TXT.get() or 'e' in get_hijopart.nombreHijoEntreParte5TXT.get() or 'i' in get_hijopart.nombreHijoEntreParte5TXT.get() or 'o' in get_hijopart.nombreHijoEntreParte5TXT.get() or 'u' in get_hijopart.nombreHijoEntreParte5TXT.get():
            data['hijosEntrePartes']+=1        

        data['hijosPatrocinado']=0
        if 'a' in get_hijopatro.nombreHijoPatrocinado1TXT.get() or 'e' in get_hijopatro.nombreHijoPatrocinado1TXT.get() or 'i' in get_hijopatro.nombreHijoPatrocinado1TXT.get() or 'o' in get_hijopatro.nombreHijoPatrocinado1TXT.get() or 'u' in get_hijopatro.nombreHijoPatrocinado1TXT.get():
            data['hijosPatrocinado']+=1
        if 'a' in get_hijopatro.nombreHijoPatrocinado2TXT.get() or 'e' in get_hijopatro.nombreHijoPatrocinado2TXT.get() or 'i' in get_hijopatro.nombreHijoPatrocinado2TXT.get() or 'o' in get_hijopatro.nombreHijoPatrocinado2TXT.get() or 'u' in get_hijopatro.nombreHijoPatrocinado2TXT.get():
            data['hijosPatrocinado']+=1    
        if 'a' in get_hijopatro.nombreHijoPatrocinado3TXT.get() or 'e' in get_hijopatro.nombreHijoPatrocinado3TXT.get() or 'i' in get_hijopatro.nombreHijoPatrocinado3TXT.get() or 'o' in get_hijopatro.nombreHijoPatrocinado3TXT.get() or 'u' in get_hijopatro.nombreHijoPatrocinado3TXT.get():
            data['hijosPatrocinado']+=1
        if 'a' in get_hijopatro.nombreHijoPatrocinado4TXT.get() or 'e' in get_hijopatro.nombreHijoPatrocinado4TXT.get() or 'i' in get_hijopatro.nombreHijoPatrocinado4TXT.get() or 'o' in get_hijopatro.nombreHijoPatrocinado4TXT.get() or 'u' in get_hijopatro.nombreHijoPatrocinado4TXT.get():
            data['hijosPatrocinado']+=1
        if 'a' in get_hijopatro.nombreHijoPatrocinado5TXT.get() or 'e' in get_hijopatro.nombreHijoPatrocinado5TXT.get() or 'i' in get_hijopatro.nombreHijoPatrocinado5TXT.get() or 'o' in get_hijopatro.nombreHijoPatrocinado5TXT.get() or 'u' in get_hijopatro.nombreHijoPatrocinado5TXT.get():
            data['hijosPatrocinado']+=1        

        data['hijosContraparte']=0
        if 'a' in get_hijocontrap.nombreHijoContraparte1TXT.get() or 'e' in get_hijocontrap.nombreHijoContraparte1TXT.get() or 'i' in get_hijocontrap.nombreHijoContraparte1TXT.get() or 'o' in get_hijocontrap.nombreHijoContraparte1TXT.get() or 'u' in get_hijocontrap.nombreHijoContraparte1TXT.get():
            data['hijosContraparte']+=1
        if 'a' in get_hijocontrap.nombreHijoContraparte2TXT.get() or 'e' in get_hijocontrap.nombreHijoContraparte2TXT.get() or 'i' in get_hijocontrap.nombreHijoContraparte2TXT.get() or 'o' in get_hijocontrap.nombreHijoContraparte2TXT.get() or 'u' in get_hijocontrap.nombreHijoContraparte2TXT.get():
            data['hijosContraparte']+=1    
        if 'a' in get_hijocontrap.nombreHijoContraparte3TXT.get() or 'e' in get_hijocontrap.nombreHijoContraparte3TXT.get() or 'i' in get_hijocontrap.nombreHijoContraparte3TXT.get() or 'o' in get_hijocontrap.nombreHijoContraparte3TXT.get() or 'u' in get_hijocontrap.nombreHijoContraparte3TXT.get():
            data['hijosContraparte']+=1
        if 'a' in get_hijocontrap.nombreHijoContraparte4TXT.get() or 'e' in get_hijocontrap.nombreHijoContraparte4TXT.get() or 'i' in get_hijocontrap.nombreHijoContraparte4TXT.get() or 'o' in get_hijocontrap.nombreHijoContraparte4TXT.get() or 'u' in get_hijocontrap.nombreHijoContraparte4TXT.get():
            data['hijosContraparte']+=1
        if 'a' in get_hijocontrap.nombreHijoContraparte5TXT.get() or 'e' in get_hijocontrap.nombreHijoContraparte5TXT.get() or 'i' in get_hijocontrap.nombreHijoContraparte5TXT.get() or 'o' in get_hijocontrap.nombreHijoContraparte5TXT.get() or 'u' in get_hijocontrap.nombreHijoContraparte5TXT.get():
            data['hijosContraparte']+=1   

        if get_adic.varMateria.get()=='Div. Unilateral':
            data['materiaCausa']='Divorcio Unilateral'
        if get_adic.varMateria.get()=='Div. Mutuo Acuerdo':
            data['materiaCausa']='Divorcio de Mutuo Acuerdo'
        if get_adic.varMateria.get()=='Cump. Alimentos':
            data['materiaCausa']='Cumplimiento de Alimentos'
        if get_adic.varMateria.get()=='Cump. R. dir. y R.':
            data['materiaCausa']='Cumplimiento de relacion directa y regular'                
                    
        if get_pat.regPatVar.get()== 'RM':
            data['regionPatrocinado'] = " Metropolitana"
        elif get_pat.regPatVar.get()== 'I':
            data['regionPatrocinado'] = " de Tarapacá"
        elif get_pat.regPatVar.get()== 'II':
            data['regionPatrocinado'] = " de Antofagasta"
        elif get_pat.regPatVar.get()== 'III':
            data['regionPatrocinado'] = " de Atacama"
        elif get_pat.regPatVar.get()== 'IV':
            data['regionPatrocinado'] = " de Coquimbo"
        elif get_pat.regPatVar.get()== 'V':
            data['regionPatrocinado'] = " de Valparaíso"
        elif get_pat.regPatVar.get()== 'VI':
            data['regionPatrocinado'] = " de O'Higgins"
        elif get_pat.regPatVar.get()== 'VII':
            data['regionPatrocinado'] = " del Maule"
        elif get_pat.regPatVar.get()== 'VIII':
            data['regionPatrocinado'] = " del Biobío"
        elif get_pat.regPatVar.get()== 'IX':
            data['regionPatrocinado'] = " de La Araucanía"
        elif get_pat.regPatVar.get()== 'X':
            data['regionPatrocinado'] = " de Los Lagos"
        elif get_pat.regPatVar.get()== 'XI':
            data['regionPatrocinado'] = " de Aysén"
        elif get_pat.regPatVar.get()== 'XII':
            data['regionPatrocinado'] = " de Magallanes"
        elif get_pat.regPatVar.get()== 'XIV':
            data['regionPatrocinado'] = " Los Ríos"
        elif get_pat.regPatVar.get()== 'XV':
            data['regionPatrocinado'] = " de Arica y Parinacota"

        if get_pat.regAboPatVar.get()== 'RM':
            data['regionAbogadoPatrocinado'] = " Metropolitana"
        elif get_pat.regAboPatVar.get()== 'I':
            data['regionAbogadoPatrocinado'] = " de Tarapacá"
        elif get_pat.regAboPatVar.get()== 'II':
            data['regionAbogadoPatrocinado'] = " de Antofagasta"
        elif get_pat.regAboPatVar.get()== 'III':
            data['regionAbogadoPatrocinado'] = " de Atacama"
        elif get_pat.regAboPatVar.get()== 'IV':
            data['regionAbogadoPatrocinado'] = " de Coquimbo"
        elif get_pat.regAboPatVar.get()== 'V':
            data['regionAbogadoPatrocinado'] = " de Valparaíso"
        elif get_pat.regAboPatVar.get()== 'VI':
            data['regionAbogadoPatrocinado'] = " de O'Higgins"
        elif get_pat.regAboPatVar.get()== 'VII':
            data['regionAbogadoPatrocinado'] = " del Maule"
        elif get_pat.regAboPatVar.get()== 'VIII':
            data['regionAbogadoPatrocinado'] = " del Biobío"
        elif get_pat.regAboPatVar.get()== 'IX':
            data['regionAbogadoPatrocinado'] = " de La Araucanía"
        elif get_pat.regAboPatVar.get()== 'X':
            data['regionAbogadoPatrocinado'] = " de Los Lagos"
        elif get_pat.regAboPatVar.get()== 'XI':
            data['regionAbogadoPatrocinado'] = " de Aysén"
        elif get_pat.regAboPatVar.get()== 'XII':
            data['regionAbogadoPatrocinado'] = " de Magallanes"
        elif get_pat.regAboPatVar.get()== 'XIV':
            data['regionAbogadoPatrocinado'] = " Los Ríos"
        elif get_pat.regAboPatVar.get()== 'XV':
            data['regionAbogadoPatrocinado'] = " de Arica y Parinacota"        

            
        if get_pat.regApoPatVar.get()== 'RM':
            data['regionApoderadoPatrocinado'] = " Metropolitana"
        elif get_pat.regApoPatVar.get()== 'I':
            data['regionApoderadoPatrocinado'] = " de Tarapacá"
        elif get_pat.regApoPatVar.get()== 'II':
            data['regionApoderadoPatrocinado'] = " de Antofagasta"
        elif get_pat.regApoPatVar.get()== 'III':
            data['regionApoderadoPatrocinado'] = " de Atacama"
        elif get_pat.regApoPatVar.get()== 'IV':
            data['regionApoderadoPatrocinado'] = " de Coquimbo"
        elif get_pat.regApoPatVar.get()== 'V':
            data['regionApoderadoPatrocinado'] = " de Valparaíso"
        elif get_pat.regApoPatVar.get()== 'VI':
            data['regionApoderadoPatrocinado'] = " de O'Higgins"
        elif get_pat.regApoPatVar.get()== 'VII':
            data['regionApoderadoPatrocinado'] = " del Maule"
        elif get_pat.regApoPatVar.get()== 'VIII':
            data['regionApoderadoPatrocinado'] = " del Biobío"
        elif get_pat.regApoPatVar.get()== 'IX':
            data['regionApoderadoPatrocinado'] = " de La Araucanía"
        elif get_pat.regApoPatVar.get()== 'X':
            data['regionApoderadoPatrocinado'] = " de Los Lagos"
        elif get_pat.regApoPatVar.get()== 'XI':
            data['regionApoderadoPatrocinado'] = " de Aysén"
        elif get_pat.regApoPatVar.get()== 'XII':
            data['regionApoderadoPatrocinado'] = " de Magallanes"
        elif get_pat.regApoPatVar.get()== 'XIV':
            data['regionApoderadoPatrocinado'] = " Los Ríos"
        elif get_pat.regApoPatVar.get()== 'XV':
            data['regionApoderadoPatrocinado'] = " de Arica y Parinacota"

        if get_contrap.regContrapVar.get()== 'RM':
            data['regionContraparte'] = " Metropolitana"
        elif get_contrap.regContrapVar.get()== 'I':
            data['regionContraparte'] = " de Tarapacá"
        elif get_contrap.regContrapVar.get()== 'II':
            data['regionContraparte'] = " de Antofagasta"
        elif get_contrap.regContrapVar.get()== 'III':
            data['regionContraparte'] = " de Atacama"
        elif get_contrap.regContrapVar.get()== 'IV':
            data['regionContraparte'] = " de Coquimbo"
        elif get_contrap.regContrapVar.get()== 'V':
            data['regionContraparte'] = " de Valparaíso"
        elif get_contrap.regContrapVar.get()== 'VI':
            data['regionContraparte'] = " de O'Higgins"
        elif get_contrap.regContrapVar.get()== 'VII':
            data['regionContraparte'] = " del Maule"
        elif get_contrap.regContrapVar.get()== 'VIII':
            data['regionContraparte'] = " del Biobío"
        elif get_contrap.regContrapVar.get()== 'IX':
            data['regionContraparte'] = " de La Araucanía"
        elif get_contrap.regContrapVar.get()== 'X':
            data['regionContraparte'] = " de Los Lagos"
        elif get_contrap.regContrapVar.get()== 'XI':
            data['regionContraparte'] = " de Aysén"
        elif get_contrap.regContrapVar.get()== 'XII':
            data['regionContraparte'] = " de Magallanes"
        elif get_contrap.regContrapVar.get()== 'XIV':
            data['regionContraparte'] = " Los Ríos"
        elif get_contrap.regContrapVar.get()== 'XV':
            data['regionContraparte'] = " de Arica y Parinacota"

        if get_contrap.regAboContrapVar.get()== 'RM':
            data['regionAbogadoContraparte'] = " Metropolitana"
        elif get_contrap.regAboContrapVar.get()== 'I':
            data['regionAbogadoContraparte'] = " de Tarapacá"
        elif get_contrap.regAboContrapVar.get()== 'II':
            data['regionAbogadoContraparte'] = " de Antofagasta"
        elif get_contrap.regAboContrapVar.get()== 'III':
            data['regionAbogadoContraparte'] = " de Atacama"
        elif get_contrap.regAboContrapVar.get()== 'IV':
            data['regionAbogadoContraparte'] = " de Coquimbo"
        elif get_contrap.regAboContrapVar.get()== 'V':
            data['regionAbogadoContraparte'] = " de Valparaíso"
        elif get_contrap.regAboContrapVar.get()== 'VI':
            data['regionAbogadoContraparte'] = " de O'Higgins"
        elif get_contrap.regAboContrapVar.get()== 'VII':
            data['regionAbogadoContraparte'] = " del Maule"
        elif get_contrap.regAboContrapVar.get()== 'VIII':
            data['regionAbogadoContraparte'] = " del Biobío"
        elif get_contrap.regAboContrapVar.get()== 'IX':
            data['regionAbogadoContraparte'] = " de La Araucanía"
        elif get_contrap.regAboContrapVar.get()== 'X':
            data['regionAbogadoContraparte'] = " de Los Lagos"
        elif get_contrap.regAboContrapVar.get()== 'XI':
            data['regionAbogadoContraparte'] = " de Aysén"
        elif get_contrap.regAboContrapVar.get()== 'XII':
            data['regionAbogadoContraparte'] = " de Magallanes"
        elif get_contrap.regAboContrapVar.get()== 'XIV':
            data['regionAbogadoContraparte'] = " Los Ríos"
        elif get_contrap.regAboContrapVar.get()== 'XV':
            data['regionAbogadoContraparte'] = " de Arica y Parinacota"


        if get_contrap.regApoContrapVar.get()== 'RM':
            data['regionApoderadoContraparte'] = " Metropolitana"
        elif get_contrap.regApoContrapVar.get()== 'I':
            data['regionApoderadoContraparte'] = " de Tarapacá"
        elif get_contrap.regApoContrapVar.get()== 'II':
            data['regionApoderadoContraparte'] = " de Antofagasta"
        elif get_contrap.regApoContrapVar.get()== 'III':
            data['regionApoderadoContraparte'] = " de Atacama"
        elif get_contrap.regApoContrapVar.get()== 'IV':
            data['regionApoderadoContraparte'] = " de Coquimbo"
        elif get_contrap.regApoContrapVar.get()== 'V':
            data['regionApoderadoContraparte'] = " de Valparaíso"
        elif get_contrap.regApoContrapVar.get()== 'VI':
            data['regionApoderadoContraparte'] = " de O'Higgins"
        elif get_contrap.regApoContrapVar.get()== 'VII':
            data['regionApoderadoContraparte'] = " del Maule"
        elif get_contrap.regApoContrapVar.get()== 'VIII':
            data['regionApoderadoContraparte'] = " del Biobío"
        elif get_contrap.regApoContrapVar.get()== 'IX':
            data['regionApoderadoContraparte'] = " de La Araucanía"
        elif get_contrap.regApoContrapVar.get()== 'X':
            data['regionApoderadoContraparte'] = " de Los Lagos"
        elif get_contrap.regApoContrapVar.get()== 'XI':
            data['regionApoderadoContraparte'] = " de Aysén"
        elif get_contrap.regApoContrapVar.get()== 'XII':
            data['regionApoderadoContraparte'] = " de Magallanes"
        elif get_contrap.regApoContrapVar.get()== 'XIV':
            data['regionApoderadoContraparte'] = " Los Ríos"
        elif get_contrap.regApoContrapVar.get()== 'XV':
            data['regionApoderadoContraparte'] = " de Arica y Parinacota"                
        
        data['hijosMenoresDeEdad']=0
        data['listaHijosMenoresDeEdad']=[]
        
        
        if data['hijosEntrePartes']>=1:
            if int(get_hijopart.edadHijoEntreParte1TXT.get())<18:
                data['hijosMenoresDeEdad']+=1
                data['listaHijosMenoresDeEdad'].append(get_hijopart.nombreHijoEntreParte1TXT.get())
            
        if data['hijosEntrePartes']>=2:    
            if int(get_hijopart.edadHijoEntreParte2TXT.get())<18:
                data['hijosMenoresDeEdad']+=1
                data['listaHijosMenoresDeEdad'].append(get_hijopart.nombreHijoEntreParte2TXT.get())
        if data['hijosEntrePartes']>=3:
            if int(get_hijopart.edadHijoEntreParte3TXT.get())<18:
                data['hijosMenoresDeEdad']+=1
                data['listaHijosMenoresDeEdad'].append(get_hijopart.nombreHijoEntreParte3TXT.get())
        if data['hijosEntrePartes']>=4:
            if int(get_hijopart.edadHijoEntreParte4TXT.get())<18:
                data['hijosMenoresDeEdad']+=1
                data['listaHijosMenoresDeEdad'].append(get_hijopart.nombreHijoEntreParte4TXT.get())
        if data['hijosEntrePartes']==5:
            if int(get_hijopart.edadHijoEntreParte5TXT.get())<18:
                data['hijosMenoresDeEdad']+=1
                data['listaHijosMenoresDeEdad'].append(get_hijopart.nombreHijoEntreParte5TXT.get())            
                
        data['listaCuidadoPersonal']=[]
       # 'Patrocinado','Contraparte'
        if get_hijopart.cuidadoHijo1Var.get() =='Patrocinado':
            data['listaCuidadoPersonal'].append("1"+get_hijopart.nombreHijoEntreParte1TXT.get())
        if get_hijopart.cuidadoHijo1Var.get() =='Contraparte':
            data['listaCuidadoPersonal'].append("2"+get_hijopart.nombreHijoEntreParte1TXT.get())            
        if get_hijopart.cuidadoHijo2Var.get() =='Patrocinado':
            data['listaCuidadoPersonal'].append("1"+get_hijopart.nombreHijoEntreParte2TXT.get())
        if get_hijopart.cuidadoHijo2Var.get() =='Contraparte':
            data['listaCuidadoPersonal'].append("2"+get_hijopart.nombreHijoEntreParte2TXT.get())            
        if get_hijopart.cuidadoHijo3Var.get() =='Patrocinado':
            data['listaCuidadoPersonal'].append("1"+get_hijopart.nombreHijoEntreParte3TXT.get())
        if get_hijopart.cuidadoHijo3Var.get() =='Contraparte':
            data['listaCuidadoPersonal'].append("2"+get_hijopart.nombreHijoEntreParte3TXT.get())            
        if get_hijopart.cuidadoHijo4Var.get() =='Patrocinado':
            data['listaCuidadoPersonal'].append("1"+get_hijopart.nombreHijoEntreParte4TXT.get()) 
        if get_hijopart.cuidadoHijo4Var.get() =='Contraparteo':
            data['listaCuidadoPersonal'].append("2"+get_hijopart.nombreHijoEntreParte4TXT.get())             
        if get_hijopart.cuidadoHijo5Var.get() =='Patrocinado':
            data['listaCuidadoPersonal'].append("1"+get_hijopart.nombreHijoEntreParte5TXT.get())  
        if get_hijopart.cuidadoHijo5Var.get() =='Contraparte':
            data['listaCuidadoPersonal'].append("2"+get_hijopart.nombreHijoEntreParte5TXT.get())            

        data['listaPatriaPotestad']=[]
        
        if get_hijopart.patriapHijo1Var.get() =='Patrocinado':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("11"+get_hijopart.nombreHijoEntreParte1TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("12"+get_hijopart.nombreHijoEntreParte1TXT.get())
        if get_hijopart.patriapHijo1Var.get() =='Contraparte':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("21"+get_hijopart.nombreHijoEntreParte1TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("22"+get_hijopart.nombreHijoEntreParte1TXT.get())            
        if get_hijopart.patriapHijo2Var.get() =='Patrocinado':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("11"+get_hijopart.nombreHijoEntreParte2TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("12"+get_hijopart.nombreHijoEntreParte2TXT.get())
        if get_hijopart.patriapHijo2Var.get() =='Contraparte':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("21"+get_hijopart.nombreHijoEntreParte2TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("22"+get_hijopart.nombreHijoEntreParte2TXT.get())           
        if get_hijopart.patriapHijo3Var.get() =='Patrocinado':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("11"+get_hijopart.nombreHijoEntreParte3TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("12"+get_hijopart.nombreHijoEntreParte3TXT.get())
        if get_hijopart.patriapHijo3Var.get() =='Contraparte':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("21"+get_hijopart.nombreHijoEntreParte3TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("22"+get_hijopart.nombreHijoEntreParte3TXT.get())           
        if get_hijopart.patriapHijo4Var.get() =='Patrocinado':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("11"+get_hijopart.nombreHijoEntreParte4TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("12"+get_hijopart.nombreHijoEntreParte4TXT.get())
        if get_hijopart.patriapHijo4Var.get() =='Contraparte':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("21"+get_hijopart.nombreHijoEntreParte4TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("22"+get_hijopart.nombreHijoEntreParte4TXT.get())            
        if get_hijopart.patriapHijo5Var.get() =='Patrocinado':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("11"+get_hijopart.nombreHijoEntreParte5TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("12"+get_hijopart.nombreHijoEntreParte5TXT.get())
        if get_hijopart.patriapHijo5Var.get() =='Contraparte':
            if get_hijopart.var37.get()=='Masculino':
                data['listaPatriaPotestad'].append("21"+get_hijopart.nombreHijoEntreParte5TXT.get())
            elif get_hijopart.var37.get()=='Femenino':
                data['listaPatriaPotestad'].append("22"+get_hijopart.nombreHijoEntreParte5TXT.get())  
            
                
        with open(filedialog.asksaveasfilename(defaultextension='.json'), 'w') as fp:
            json.dump(data, fp,sort_keys = True, indent = 4,ensure_ascii=False)



    def cargar(self):

        with open(filedialog.askopenfilename()) as fp:
            data_load=json.load(fp)
        get_pat = self.controller.get_page("Patrocinado")
        get_contrap = self.controller.get_page("Contraparte")
        get_matri = self.controller.get_page("Matrimonio")
        get_adic = self.controller.get_page("Adicionales")
        get_acu = self.controller.get_page("Acuerdo")
        get_hijopart=self.controller.get_page("HijosEntrePartes")
        get_hijopatro=self.controller.get_page("HijosPatrocinado")
        get_hijocontrap=self.controller.get_page("HijosContraparte")

        get_pat.nombPatTXT.delete(0,END)
        get_pat.nombPatTXT.insert(0,data_load['nombrePatrocinado'])
        get_pat.apePatPatTXT.delete(0,END)
        get_pat.apePatPatTXT.insert(0,data_load['apellidoPaternoPatrocinado'])
        get_pat.apeMatPatTXT.delete(0,END)
        get_pat.apeMatPatTXT.insert(0,data_load['apellidoMaternoPatrocinado'])
        get_pat.var1.set(data_load['sexoPatrocinado'])
        get_pat.nacPatTXT.delete(0,END)
        get_pat.nacPatTXT.insert(0,data_load['nacionalidadPatrocinado'])
        get_pat.var2.set(data_load['estadoCivilPatrocinado'])
        get_pat.rutPatTXT.delete(0,END)
        get_pat.rutPatTXT.insert(0,data_load['rutPatrocinado'])
        get_pat.profPatTXT.delete(0,END)
        get_pat.profPatTXT.insert(0,data_load['profesionPatrocinado'])
        get_pat.domicPatTXT.delete(0,END)
        get_pat.domicPatTXT.insert(0,data_load['domicilioPatrocinado'])
        get_pat.comunaPatTXT.delete(0,END)
        get_pat.comunaPatTXT.insert(0,data_load['comunaPatrocinado'])
        get_pat.var16.set(data_load['situacionProcesalPatrocinado'])

        get_pat.nombAboPatTXT.delete(0,END)
        get_pat.nombAboPatTXT.insert(0,data_load['nombreAbogadoPatrocinado'])
        get_pat.apePatAboPatTXT.delete(0,END)
        get_pat.apePatAboPatTXT.insert(0,data_load['apellidoPaternoAbogadoPatrocinado'])
        get_pat.apeMatAboPatTXT.delete(0,END)
        get_pat.apeMatAboPatTXT.insert(0,data_load['apellidoMaternoAbogadoPatrocinado'])
        get_pat.var3.set(data_load['sexoAbogadoPatrocinado'])
        get_pat.nacAboPatTXT.delete(0,END)
        get_pat.nacAboPatTXT.insert(0,data_load['nacionalidadAbogadoPatrocinado'])
        get_pat.var4.set(data_load['estadoCivilAbogadoPatrocinado'])
        get_pat.rutAboPatTXT.delete(0,END)
        get_pat.rutAboPatTXT.insert(0,data_load['rutAbogadoPatrocinado'])
        get_pat.emailAboPatTXT.delete(0,END)
        get_pat.emailAboPatTXT.insert(0,data_load['emailAbogadoPatrocinado'])
        get_pat.domicAboPatTXT.delete(0,END)
        get_pat.domicAboPatTXT.insert(0,data_load['domicilioAbogadoPatrocinado'])
        get_pat.comunaAboPatTXT.delete(0,END)
        get_pat.comunaAboPatTXT.insert(0,data_load['comunaAbogadoPatrocinado'])

        get_pat.nombApoPatTXT.delete(0,END)
        get_pat.nombApoPatTXT.insert(0,data_load['nombreApoderadoPatrocinado'])
        get_pat.apePatApoPatTXT.delete(0,END)
        get_pat.apePatApoPatTXT.insert(0,data_load['apellidoPaternoApoderadoPatrocinado'])
        get_pat.apeMatApoPatTXT.delete(0,END)
        get_pat.apeMatApoPatTXT.insert(0,data_load['apellidoMaternoApoderadoPatrocinado'])
        get_pat.var33.set(data_load['sexoApoderadoPatrocinado'])
        get_pat.nacApoPatTXT.delete(0,END)
        get_pat.nacApoPatTXT.insert(0,data_load['nacionalidadApoderadoPatrocinado'])
        get_pat.var34.set(data_load['estadoCivilApoderadoPatrocinado'])
        get_pat.rutApoPatTXT.delete(0,END)
        get_pat.rutApoPatTXT.insert(0,data_load['rutApoderadoPatrocinado'])
        get_pat.emailApoPatTXT.delete(0,END)
        get_pat.emailApoPatTXT.insert(0,data_load['emailApoderadoPatrocinado'])
        get_pat.domicApoPatTXT.delete(0,END)
        get_pat.domicApoPatTXT.insert(0,data_load['domicilioApoderadoPatrocinado'])
        get_pat.comunaApoPatTXT.delete(0,END)
        get_pat.comunaApoPatTXT.insert(0,data_load['comunaApoderadoPatrocinado'])

        get_contrap.nombContrapTXT.delete(0,END)
        get_contrap.nombContrapTXT.insert(0,data_load['nombreContraparte'])
        get_contrap.apePatContrapTXT.delete(0,END)
        get_contrap.apePatContrapTXT.insert(0,data_load['apellidoPaternoContraparte'])
        get_contrap.apeMatContrapTXT.delete(0,END)
        get_contrap.apeMatContrapTXT.insert(0,data_load['apellidoMaternoContraparte'])
        get_contrap.var5.set(data_load['sexoContraparte'])
        get_contrap.nacContrapTXT.delete(0,END)
        get_contrap.nacContrapTXT.insert(0,data_load['nacionalidadContraparte'])
        get_contrap.var6.set(data_load['estadoCivilContraparte'])
        get_contrap.rutContrapTXT.delete(0,END)
        get_contrap.rutContrapTXT.insert(0,data_load['rutContraparte'])
        get_contrap.profContrapTXT.delete(0,END)
        get_contrap.profContrapTXT.insert(0,data_load['profesionContraparte'])
        get_contrap.domicContrapTXT.delete(0,END)
        get_contrap.domicContrapTXT.insert(0,data_load['domicilioContraparte'])
        get_contrap.comunaContrapTXT.delete(0,END)
        get_contrap.comunaContrapTXT.insert(0,data_load['comunaContraparte'])


        get_contrap.nombAboContrapTXT.delete(0,END)
        get_contrap.nombAboContrapTXT.insert(0,data_load['nombreAbogadoContraparte'])
        get_contrap.apePatAboContrapTXT.delete(0,END)
        get_contrap.apePatAboContrapTXT.insert(0,data_load['apellidoPaternoAbogadoContraparte'])
        get_contrap.apeMatAboContrapTXT.delete(0,END)
        get_contrap.apeMatAboContrapTXT.insert(0,data_load['apellidoMaternoAbogadoContraparte'])
        get_contrap.var7.set(data_load['sexoAbogadoContraparte'])
        get_contrap.nacAboContrapTXT.delete(0,END)
        get_contrap.nacAboContrapTXT.insert(0,data_load['nacionalidadAbogadoContraparte'])
        get_contrap.var8.set(data_load['estadoCivilAbogadoContraparte'])
        get_contrap.rutAboContrapTXT.delete(0,END)
        get_contrap.rutAboContrapTXT.insert(0,data_load['rutAbogadoContraparte'])
        get_contrap.emailAboContrapTXT.delete(0,END)
        get_contrap.emailAboContrapTXT.insert(0,data_load['emailAbogadoContraparte'])
        get_contrap.domicAboContrapTXT.delete(0,END)
        get_contrap.domicAboContrapTXT.insert(0,data_load['domicilioAbogadoContraparte'])
        get_contrap.comunaAboContrapTXT.delete(0,END)
        get_contrap.comunaAboContrapTXT.insert(0,data_load['comunaAbogadoContraparte'])

        get_contrap.nombApoContrapTXT.delete(0,END)
        get_contrap.nombApoContrapTXT.insert(0,data_load['nombreApoderadoContraparte'])
        get_contrap.apePatApoContrapTXT.delete(0,END)
        get_contrap.apePatApoContrapTXT.insert(0,data_load['apellidoPaternoApoderadoContraparte'])
        get_contrap.apeMatApoContrapTXT.delete(0,END)
        get_contrap.apeMatApoContrapTXT.insert(0,data_load['apellidoMaternoApoderadoContraparte'])
        get_contrap.var35.set(data_load['sexoApoderadoContraparte'])
        get_contrap.nacApoContrapTXT.delete(0,END)
        get_contrap.nacApoContrapTXT.insert(0,data_load['nacionalidadApoderadoContraparte'])
        get_contrap.var36.set(data_load['estadoCivilApoderadoContraparte'])
        get_contrap.rutApoContrapTXT.delete(0,END)
        get_contrap.rutApoContrapTXT.insert(0,data_load['rutApoderadoContraparte'])
        get_contrap.emailApoContrapTXT.delete(0,END)
        get_contrap.emailApoContrapTXT.insert(0,data_load['emailApoderadoContraparte'])
        get_contrap.domicApoContrapTXT.delete(0,END)
        get_contrap.domicApoContrapTXT.insert(0,data_load['domicilioApoderadoContraparte'])
        get_contrap.comunaApoContrapTXT.delete(0,END)
        get_contrap.comunaApoContrapTXT.insert(0,data_load['comunaApoderadoContraparte'])

        get_matri.var9.set(data_load['diaDeMatrimonio'])
        get_matri.var10.set(data_load['mesDeMatrimonio'])
        get_matri.añoMatrimonioTXT.delete(0,END)
        get_matri.añoMatrimonioTXT.insert(0,data_load['añoDeMatrimonio'])
        get_matri.comunaMatrimonioTXT.delete(0,END)
        get_matri.comunaMatrimonioTXT.insert(0,data_load['comunaDeMatrimonio'])
        get_matri.numeroInscripcionTXT.delete(0,END)
        get_matri.numeroInscripcionTXT.insert(0,data_load['numeroInscripcionMatrimonio'])
        get_matri.var11.set(data_load['regimenMatrimonial'])

        get_matri.var12.set(data_load['diaDeCeseConvivencia'])
        get_matri.var13.set(data_load['mesDeCeseConvivencia'])
        get_matri.añoCeseConvivenciaTXT.delete(0,END)
        get_matri.añoCeseConvivenciaTXT.insert(0,data_load['añoDeCeseConvivencia'])

        get_adic.ritCausaTXT.delete(0,END)
        get_adic.ritCausaTXT.insert(0,data_load['ritDeCausa'])
        get_adic.var15.set(data_load['juzgado'])
        get_adic.varMateria.set(data_load['materiaCausa'])
        get_adic.caratulaTXT.delete(0,END)
        get_adic.caratulaTXT.insert(0,data_load['caratulaCausa'])
        get_adic.var14.set(data_load['pideCompensacionEconomica'])
        get_adic.varAbandona.set(data_load['abandonaHogarComun'])
        get_adic.nuevaRelPat.set(data_load['nuevaRelacionPatrocinado'])
        get_adic.añosRelacionPatrocinadoTXT.delete(0,END)
        get_adic.añosRelacionPatrocinadoTXT.insert(0,data_load['añosRelacionPatrocinado'])
        get_adic.nuevaRelCont.set(data_load['nuevaRelacionContraparte'])
        get_adic.añosRelacionContraparteTXT.delete(0,END)
        get_adic.añosRelacionContraparteTXT.insert(0,data_load['añosRelacionContraparte'])
        get_adic.huboMedVar.set(data_load['huboMediacion'])
        get_adic.ritMedTXT.delete(0,END)
        get_adic.ritMedTXT.insert(0,data_load['ritMediacion'])        

        get_hijopart.nombreHijoEntreParte1TXT.delete(0,END)
        get_hijopart.nombreHijoEntreParte1TXT.insert(0,data_load['nombreDeHijoEntreParte1'])
        get_hijopart.var37.set(data_load['sexoDeHijoEntreParte1'])
        get_hijopart.RUTHijoEntreParte1TXT.delete(0,END)
        get_hijopart.RUTHijoEntreParte1TXT.insert(0,data_load['rutDeHijoEntreParte1'])
        get_hijopart.edadHijoEntreParte1TXT.delete(0,END)
        get_hijopart.edadHijoEntreParte1TXT.insert(0,data_load['edadDeHijoEntreParte1'])

        
        get_hijopart.nombreHijoEntreParte2TXT.delete(0,END)
        get_hijopart.nombreHijoEntreParte2TXT.insert(0,data_load['nombreDeHijoEntreParte2'])
        get_hijopart.var38.set(data_load['sexoDeHijoEntreParte2'])
        get_hijopart.RUTHijoEntreParte2TXT.delete(0,END)
        get_hijopart.RUTHijoEntreParte2TXT.insert(0,data_load['rutDeHijoEntreParte2'])
        get_hijopart.edadHijoEntreParte2TXT.delete(0,END)
        get_hijopart.edadHijoEntreParte2TXT.insert(0,data_load['edadDeHijoEntreParte2'])

        
        get_hijopart.nombreHijoEntreParte3TXT.delete(0,END)
        get_hijopart.nombreHijoEntreParte3TXT.insert(0,data_load['nombreDeHijoEntreParte3'])
        get_hijopart.var39.set(data_load['sexoDeHijoEntreParte3'])
        get_hijopart.RUTHijoEntreParte3TXT.delete(0,END)
        get_hijopart.RUTHijoEntreParte3TXT.insert(0,data_load['rutDeHijoEntreParte3'])
        get_hijopart.edadHijoEntreParte3TXT.delete(0,END)
        get_hijopart.edadHijoEntreParte3TXT.insert(0,data_load['edadDeHijoEntreParte3'])

        
        get_hijopart.nombreHijoEntreParte4TXT.delete(0,END)
        get_hijopart.nombreHijoEntreParte4TXT.insert(0,data_load['nombreDeHijoEntreParte4'])
        get_hijopart.var40.set(data_load['sexoDeHijoEntreParte4'])
        get_hijopart.RUTHijoEntreParte4TXT.delete(0,END)
        get_hijopart.RUTHijoEntreParte4TXT.insert(0,data_load['rutDeHijoEntreParte4'])
        get_hijopart.edadHijoEntreParte4TXT.delete(0,END)
        get_hijopart.edadHijoEntreParte4TXT.insert(0,data_load['edadDeHijoEntreParte4'])

        
        get_hijopart.nombreHijoEntreParte5TXT.delete(0,END)
        get_hijopart.nombreHijoEntreParte5TXT.insert(0,data_load['nombreDeHijoEntreParte5'])
        get_hijopart.var41.set(data_load['sexoDeHijoEntreParte5'])
        get_hijopart.RUTHijoEntreParte5TXT.delete(0,END)
        get_hijopart.RUTHijoEntreParte5TXT.insert(0,data_load['rutDeHijoEntreParte5'])
        get_hijopart.edadHijoEntreParte5TXT.delete(0,END)
        get_hijopart.edadHijoEntreParte5TXT.insert(0,data_load['edadDeHijoEntreParte5'])
       

        get_hijopatro.nombreHijoPatrocinado1TXT.delete(0,END)
        get_hijopatro.nombreHijoPatrocinado1TXT.insert(0,data_load['nombreDeHijoPatrocinado1'])
        get_hijopatro.var42.set(data_load['sexoDeHijoPatrocinado1'])
        get_hijopatro.RUTHijoPatrocinado1TXT.delete(0,END)
        get_hijopatro.RUTHijoPatrocinado1TXT.insert(0,data_load['rutDeHijoPatrocinado1'])
        get_hijopatro.edadHijoPatrocinado1TXT.delete(0,END)
        get_hijopatro.edadHijoPatrocinado1TXT.insert(0,data_load['edadDeHijoPatrocinado1'])
        get_hijopatro.nombreHijoPatrocinado2TXT.delete(0,END)
        get_hijopatro.nombreHijoPatrocinado2TXT.insert(0,data_load['nombreDeHijoPatrocinado2'])
        get_hijopatro.var43.set(data_load['sexoDeHijoPatrocinado2'])
        get_hijopatro.RUTHijoPatrocinado2TXT.delete(0,END)
        get_hijopatro.RUTHijoPatrocinado2TXT.insert(0,data_load['rutDeHijoPatrocinado2'])
        get_hijopatro.edadHijoPatrocinado2TXT.delete(0,END)
        get_hijopatro.edadHijoPatrocinado2TXT.insert(0,data_load['edadDeHijoPatrocinado2'])
        get_hijopatro.nombreHijoPatrocinado3TXT.delete(0,END)
        get_hijopatro.nombreHijoPatrocinado3TXT.insert(0,data_load['nombreDeHijoPatrocinado3'])
        get_hijopatro.var44.set(data_load['sexoDeHijoPatrocinado3'])
        get_hijopatro.RUTHijoPatrocinado3TXT.delete(0,END)
        get_hijopatro.RUTHijoPatrocinado3TXT.insert(0,data_load['rutDeHijoPatrocinado3'])
        get_hijopatro.edadHijoPatrocinado3TXT.delete(0,END)
        get_hijopatro.edadHijoPatrocinado3TXT.insert(0,data_load['edadDeHijoPatrocinado3'])
        get_hijopatro.nombreHijoPatrocinado4TXT.delete(0,END)
        get_hijopatro.nombreHijoPatrocinado4TXT.insert(0,data_load['nombreDeHijoPatrocinado4'])
        get_hijopatro.var45.set(data_load['sexoDeHijoPatrocinado4'])
        get_hijopatro.RUTHijoPatrocinado4TXT.delete(0,END)
        get_hijopatro.RUTHijoPatrocinado4TXT.insert(0,data_load['rutDeHijoPatrocinado4'])
        get_hijopatro.edadHijoPatrocinado4TXT.delete(0,END)
        get_hijopatro.edadHijoPatrocinado4TXT.insert(0,data_load['edadDeHijoPatrocinado4'])
        get_hijopatro.nombreHijoPatrocinado5TXT.delete(0,END)
        get_hijopatro.nombreHijoPatrocinado5TXT.insert(0,data_load['nombreDeHijoPatrocinado5'])
        get_hijopatro.var46.set(data_load['sexoDeHijoPatrocinado5'])
        get_hijopatro.RUTHijoPatrocinado5TXT.delete(0,END)
        get_hijopatro.RUTHijoPatrocinado5TXT.insert(0,data_load['rutDeHijoPatrocinado5'])
        get_hijopatro.edadHijoPatrocinado5TXT.delete(0,END)
        get_hijopatro.edadHijoPatrocinado5TXT.insert(0,data_load['edadDeHijoPatrocinado5'])

        get_hijocontrap.nombreHijoContraparte1TXT.delete(0,END)
        get_hijocontrap.nombreHijoContraparte1TXT.insert(0,data_load['nombreDeHijoContraparte1'])
        get_hijocontrap.var47.set(data_load['sexoDeHijoContraparte1'])
        get_hijocontrap.RUTHijoContraparte1TXT.delete(0,END)
        get_hijocontrap.RUTHijoContraparte1TXT.insert(0,data_load['rutDeHijoContraparte1'])
        get_hijocontrap.edadHijoContraparte1TXT.delete(0,END)
        get_hijocontrap.edadHijoContraparte1TXT.insert(0,data_load['edadDeHijoContraparte1'])
        get_hijocontrap.nombreHijoContraparte2TXT.delete(0,END)
        get_hijocontrap.nombreHijoContraparte2TXT.insert(0,data_load['nombreDeHijoContraparte2'])
        get_hijocontrap.var48.set(data_load['sexoDeHijoContraparte2'])
        get_hijocontrap.RUTHijoContraparte2TXT.delete(0,END)
        get_hijocontrap.RUTHijoContraparte2TXT.insert(0,data_load['rutDeHijoContraparte2'])
        get_hijocontrap.edadHijoContraparte2TXT.delete(0,END)
        get_hijocontrap.edadHijoContraparte2TXT.insert(0,data_load['edadDeHijoContraparte2'])
        get_hijocontrap.nombreHijoContraparte3TXT.delete(0,END)
        get_hijocontrap.nombreHijoContraparte3TXT.insert(0,data_load['nombreDeHijoContraparte3'])
        get_hijocontrap.var49.set(data_load['sexoDeHijoContraparte3'])
        get_hijocontrap.RUTHijoContraparte3TXT.delete(0,END)
        get_hijocontrap.RUTHijoContraparte3TXT.insert(0,data_load['rutDeHijoContraparte3'])
        get_hijocontrap.edadHijoContraparte3TXT.delete(0,END)
        get_hijocontrap.edadHijoContraparte3TXT.insert(0,data_load['edadDeHijoContraparte3'])
        get_hijocontrap.nombreHijoContraparte4TXT.delete(0,END)
        get_hijocontrap.nombreHijoContraparte4TXT.insert(0,data_load['nombreDeHijoContraparte4'])
        get_hijocontrap.var50.set(data_load['sexoDeHijoContraparte4'])
        get_hijocontrap.RUTHijoContraparte4TXT.delete(0,END)
        get_hijocontrap.RUTHijoContraparte4TXT.insert(0,data_load['rutDeHijoContraparte4'])
        get_hijocontrap.edadHijoContraparte4TXT.delete(0,END)
        get_hijocontrap.edadHijoContraparte4TXT.insert(0,data_load['edadDeHijoContraparte4'])
        get_hijocontrap.nombreHijoContraparte5TXT.delete(0,END)
        get_hijocontrap.nombreHijoContraparte5TXT.insert(0,data_load['nombreDeHijoContraparte5'])
        get_hijocontrap.var51.set(data_load['sexoDeHijoContraparte5'])
        get_hijocontrap.RUTHijoContraparte5TXT.delete(0,END)
        get_hijocontrap.RUTHijoContraparte5TXT.insert(0,data_load['rutDeHijoContraparte5'])
        get_hijocontrap.edadHijoContraparte5TXT.delete(0,END)
        get_hijocontrap.edadHijoContraparte5TXT.insert(0,data_load['edadDeHijoContraparte5'])
        
        #versión 2.0
        get_hijopart.cuidadoHijo1Var.set(data_load['cuidadoPersonalHijo1'])
        get_hijopart.patriapHijo1Var.set(data_load['patriaPotestadHijo1'])
        get_hijopart.cuidadoHijo2Var.set(data_load['cuidadoPersonalHijo2'])
        get_hijopart.patriapHijo2Var.set(data_load['patriaPotestadHijo2'])
        get_hijopart.cuidadoHijo3Var.set(data_load['cuidadoPersonalHijo3'])
        get_hijopart.patriapHijo3Var.set(data_load['patriaPotestadHijo3'])
        get_hijopart.cuidadoHijo4Var.set(data_load['cuidadoPersonalHijo4'])
        get_hijopart.patriapHijo4Var.set(data_load['patriaPotestadHijo4'])        
        get_hijopart.cuidadoHijo5Var.set(data_load['cuidadoPersonalHijo5'])
        get_hijopart.patriapHijo5Var.set(data_load['patriaPotestadHijo5']) 
        get_matri.existeBienVar.set(data_load['existeBienQueLiquidar']) 
        get_adic.pagoCompVar.set(data_load['modoPagoCompensacion'])
        get_adic.valorCompTXT.delete(0,END)
        get_adic.valorCompTXT.insert(0,data_load['valorCompensacion'])
        get_adic.dirInmCompTXT.delete(0,END)
        get_adic.dirInmCompTXT.insert(0,data_load['direccionInmueblePagoCompensacion'])
        get_adic.comunaInmCompTXT.delete(0,END)
        get_adic.comunaInmCompTXT.insert(0,data_load['comunaInmueblePagoCompensacion'])
        
        get_pat.numDomicPatTXT.delete(0,END)
        get_pat.numDomicPatTXT.insert(0,data_load['numeroDomicilioPatrocinado'])
        get_pat.numDomicAboPatTXT.delete(0,END)
        get_pat.numDomicAboPatTXT.insert(0,data_load['numeroDomicilioAbogadoPatrocinado'])
        get_pat.numDomicApoPatTXT.delete(0,END)
        get_pat.numDomicApoPatTXT.insert(0,data_load['numeroDomicilioApoderadoPatrocinado'])
       
        get_contrap.numDomicContrapTXT.delete(0,END)
        get_contrap.numDomicContrapTXT.insert(0,data_load['numeroDomicilioContraparte'])
        get_contrap.numDomicAboContrapTXT.delete(0,END)
        get_contrap.numDomicAboContrapTXT.insert(0,data_load['numeroDomicilioAbogadoContraparte'])
        get_contrap.numDomicApoContrapTXT.delete(0,END)
        get_contrap.numDomicApoContrapTXT.insert(0,data_load['numeroDomicilioApoderadoContraparte'])
        get_adic.numInmCompTXT.delete(0, END)
        get_adic.numInmCompTXT.insert(0,data_load['numeroInmueblePagoCompensacion'])

        get_acu.pagaAlimMenoresVar.set(data_load['pagaAlimentosMenores'])
        get_acu.alimMenoresTXT.delete(0,END)
        get_acu.alimMenoresTXT.insert(0,data_load['cuantiaAlimentosMenores'])
        get_acu.cuantIMRTXT.delete(0,END)
        get_acu.cuantIMRTXT.insert(0, data_load['cuantiaIMR'])

        get_pat.facAboPatVar.set(data_load['facultadesAbogadoPatrocinado'])
        get_contrap.facAboContrapVar.set(data_load['facultadesAbogadoContraparte'])
        get_pat.facApoPatVar.set(data_load['facultadesApoderadoPatrocinado'])   
        get_contrap.facApoContrapVar.set(data_load['facultadesApoderadoContraparte'])   
        
        get_pat.ciudPatTXT.delete(0,END)
        get_pat.ciudPatTXT.insert(0,data_load['ciudadPatrocinado'])
        get_pat.regPatVar.set(data_load['regionPatrocinado'])
        get_pat.ciudAboPatTXT.delete(0,END)
        get_pat.ciudAboPatTXT.insert(0,data_load['ciudadAbogadoPatrocinado'])
        get_pat.regAboPatVar.set(data_load['regionAbogadoPatrocinado'])
        get_pat.ciudApoPatTXT.delete(0,END)
        get_pat.ciudApoPatTXT.insert(0,data_load['ciudadApoderadoPatrocinado'])
        get_pat.regApoPatVar.set(data_load['regionApoderadoPatrocinado']) 

        get_contrap.ciudContrapTXT.delete(0,END)
        get_contrap.ciudContrapTXT.insert(0,data_load['ciudadContraparte'])
        get_contrap.regContrapVar.set(data_load['regionContraparte'])
        get_contrap.ciudAboContrapTXT.delete(0,END)
        get_contrap.ciudAboContrapTXT.insert(0,data_load['ciudadAbogadoContraparte'])
        get_contrap.regAboContrapVar.set(data_load['regionAbogadoContraparte'])
        get_contrap.ciudApoContrapTXT.delete(0,END)
        get_contrap.ciudApoContrapTXT.insert(0,data_load['ciudadApoderadoContraparte'])
        get_contrap.regApoContrapVar.set(data_load['regionApoderadoContraparte'])        
        get_adic.pagoAlimContrapVar.set(data_load['pagoAlimentosContraparte'])
        
        
    
app = MyApp()
app.title('Generador Documentos Derecho de Familia')
app.mainloop()
