import tkinter #naimportuje kniznicu tkinter
canvas = tkinter.Canvas(width=1000,height=300) #vytvori premennu canvas platno 
canvas.pack()#privola canvas (platno)
subor = open('zastavba na ulici.txt', 'r',encoding='utf-8') #otvory subor zastavba...
i=[] #vytvory zoznam i
k=[] #vytvory zoznam k



x=[] #vytvory zoznam x
y=[] #vytvory zoznam y

def zastavba(): #vytvory podprogram zastavba
    for riadok in subor: #vytvory for cyklus ktory pojde od premmenej riadok po subor 
        global i # global i nepotrebna sice
       
        info = riadok.strip() #vymaze neviditelne znaky ako /n a podobne ... z riadku premennej a vlozi to do premennej info  
        k = info.split(' ') #vytvory premennu 'k' v ktorej premenna 'info' vytvory zoznamam
        y.append(k[0]) #prida cislo ktore sa nachadza pod nulou z txt suboru 
        x.append(k[1]) #prida cislo ktore sa nachadza pod prvou z txt suboru 
    print(x[1]) #printne do shelu x[1] premennu a hodnotu pod nou  
    
    canvas.create_rectangle(int(x[0])-40,int(y[0])+150,60,300,fill='gray') #vsetko toto je na budovy
    canvas.create_rectangle(int(x[1])+20,int(y[1])+150,60,300,fill='gray')
    canvas.create_rectangle(int(x[2])+60,int(y[2])+240,120,300,fill='gray')
    canvas.create_rectangle(int(x[3])+120,int(y[3])+299,150,300,fill='gray',outline='green',width=2)
    canvas.create_rectangle(int(x[4])+50,int(y[4])+80,200,300,fill='gray')
    canvas.create_rectangle(200,150,220,300,fill='gray')
    canvas.create_rectangle(220,290,260,300,fill='gray')
    canvas.create_rectangle(260,299,310,300,fill='gray',outline='green',width=2)
    canvas.create_rectangle(310,250,390,300,fill='gray')
    canvas.create_rectangle(390,150,420,300,fill='gray')
    canvas.create_rectangle(420,270,470,300,fill='gray')
    canvas.create_rectangle(470,220,520,300,fill='gray')
        


def cervena(): # vytvory podprogram cervena
    canvas.create_line(420,150,420,270,fill='red',width=2) #vytvory ciary na suradniciach... s farbou red
    canvas.create_line(390,150,390,250,fill='red',width=2)
    canvas.create_line(220,150,220,290,fill='red',width=2)
    







zastavba() #privola podprogram zastavbu
entry1 = tkinter.Entry() #vytvory uplne useless entry vstup ktvoli blbelmu zadaniu 
entry1.pack() #privola entry

button1 = tkinter.Button(text='vykresli',command=cervena) #vytvory tlacicu button na canvase
button1.pack() #privola button

subor.close() # zavre subor
