##########################################################
##########################################################
# description: ADA 2.0b
# autor: jeraman
# date: 26/04/2010
##########################################################
##########################################################




from pyata.pd import *
from clock import *
from planet import *
from random import *
from math import *
import os

from string import *

#variavel usada para debugar: define se o pd deve ser inicializado
init_pd = True
#define em qual regiao da tela os elementos irao surgir
str_x =  -400
end_x =  1000

#characteres seguros para serem usados no pd
safe_chars = ascii_letters + digits + whitespace #+ punctuation + '_'




#################################
#################################
# thanking the public
#################################
#################################
def credits ():
    print "crediting"
    
    if init_pd:        
        pd.clear()
        sleep(3)
        c = Comment(500, 250, "==== THANK YOU ALL! ====")
        c = Comment(500, 300, "performance by ADA 2.0b")
        c = Comment(500, 360, "developed by Jeraman, 2010")
        c = Comment(500, 380, "jeraman [at] wouwlabs.com")
        sleep(10)
        
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(1) 
            
        print "fim do credits"



#################################
#################################
# painting the counter before the piece starting
#################################
#################################
def counter ():
    print "counting"
    
    if init_pd:
        for i in xrange(10, 0, -1):
            c = Comment(randint(400, 800), randint(200, 600), str(i))
            sleep(1)
        
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(1) 
        
        
        c = Comment(600, 300, "hello")
        sleep(3)
        pd.clear()
        sleep(2)
        c = Comment(580, 300, "I'm ADA 2.0b")
        sleep(10)
        pd.clear()
        sleep(2)
        
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(1)

            
        print "fim do counter"


#################################
#################################
# pre primeiro movimento: o conteudo da memoria RAM
#################################
#################################

def pre_first_movement ():
    print "pre primeiro movimento"
    
    #abrindo a memoria e carregando-a numa lista
    list = []
    memory = open("/dev/mem","r")
    
    #quantidade de linhas de memoria capturada
    size = 250
    
    #formata a memoria para ser usada
    for i in range(size):
         s = memory.readline().replace(";", "*")
         s = s.replace("\n", " ")
         #print "antes"
         #print s
         #print "depois"
         s=''.join([char if char in safe_chars else '' for char in s])
         print s
         #if(len(s) > 50):
         #    s =  s[0:50]
         list.append(s)
    memory.close()
    
    #delimita a area de surgimento dos comentarios
        
    if init_pd:
        print "SUBMOV 3"
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 30
        start = time()
        now = time()
        while (now - start)<bound:
            for i in range (5):
                aux = randint(0, size-1)
                c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                #t = uniform(0.5, 1.0)
                #sleep(t)
            sleep(0.5)
            pd.clear()
            now = time()
            
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(0.5) 
        
        print "fim do pre primeiro movimento"


#################################
#################################
# primeiro movimento: o conteudo da memoria RAM
#################################
#################################

def first_movement ():
    print "primeiro movimento"
    
    #abrindo a memoria e carregando-a numa lista
    list = []
    memory = open("/dev/mem","r")
    
    #quantidade de linhas de memoria capturada
    size = 250
    
    #formata a memoria para ser usada
    for i in range(size):
         s = memory.readline().replace(";", "*")
         s = s.replace("\n", " ")
         s=''.join([char if char in safe_chars else '' for char in s])
         #if(len(s) > 50):
         #    s =  s[0:50]
         list.append(s)
    memory.close()
    
    #delimita a area de surgimento dos comentarios
        
    if init_pd:
        print "SUBMOV 1"
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 15
        start = time()
        now = time()
        while (now - start)<bound:
            aux = randint(0, size-1)
            c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            #t = uniform(0.5, 1.0)
            #sleep(t)
            sleep(0.5)
            pd.clear()
            now = time()
        
        print "SUBMOV 2"        
        #por BOUNDS segundos imprima sem apagar a memoria na tela
        bound = 15
        start = time()
        now = time()
        while (now - start)<bound:
            aux = randint(0, size-1)
            c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            #t = uniform(0.5, 1.0)
            #sleep(t)
            sleep(0.5)
            now = time()
        
        pd.clear()
        sleep(0.1)
        
        print "SUBMOV 3"
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 30
        start = time()
        now = time()
        while (now - start)<bound:
            for i in range (3):
                aux = randint(0, size-1)
                c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            sleep(0.7)
            #t = uniform(0.5, 1.0)
            #sleep(t)
            pd.clear()
            sleep(0.1)
            now = time()
            
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(0.5) 
        
        print "fim do primeiro movimento"


#################################
#################################
# pra segundo movimento: os processos na CPU
#################################
#################################
    
def pre_second_movement ():
    print "pre segundo movimento"
    
    #seta a quantidade de processos
    n_proc = 20
    
    #pega a lista de processos e coloca em array
    a = os.popen("ps axco %cpu,cmd | sort -k 1 -nr | head -" + str(n_proc+1))
    array = a.read()
    array = array.split("\n")
    
    #removendo o cabecalho
    #print len(array)
    for s in array:
        if s.find("%") > -1:
            array.remove(s)    
              
    #pega todos os processos e sua respectiva cpu
    list = []
    for s in array:        
        s = s.strip()
        temp = s.split(" ")
        temp.reverse()
        if len(temp) == 2:
            list.append(temp)
    
    #"aleatoriesando" a lista    
    final_list = []
    for i in range(len(list)):
        final_list.append(list[randint(0, len(list)-1)])

    #se o pd deve ser iniciado
    if init_pd:
        
        #criando o centro do relogio em questao
        osc=Object(600, 350, "osc~")
        dac=Object(osc.x, osc.y+30, "dac~")
        connect(osc, 0, dac, 0)
        centro = [osc,dac]
            
        #criando o relogio
        c = Clock(300, centro, final_list, 1000)
        
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 30
        start = time()
        now = time()
        while (now - start)<bound:
            c.increment()
            sleep(0.1)
            now = time()
      
        #destrua esse relogio
        c.destroy()
        
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(0.5) 

        print "fim do pre segundo movimento"
        

        
#################################
#################################
# segundo movimento: a loucaura dos processos na CPU
#################################
#################################
 
def second_movement ():
    print "segundo movimento"
    
    #seta a quantidade de processos
    n_proc = 20
    
    #pega a lista de processos e coloca em array
    a = os.popen("ps axco %cpu,cmd | sort -k 1 -nr | head -" + str(n_proc+1))
    array = a.read()
    array = array.split("\n")
    
    #removendo o cabecalho
    #print len(array)
    for s in array:
        if s.find("%") > -1:
            array.remove(s)    
              
    #pega todos os processos e sua respectiva cpu
    list = []
    for s in array:        
        s = s.strip()
        temp = s.split(" ")
        temp.reverse()
        if len(temp) == 2:
            list.append(temp)
    
    #se o pd deve ser iniciado
    if init_pd:
        
        #numero de relogios
        n_clocks = 5
        
        #clocks
        clocks = []
        
        #criando N_CLOCK relogios
        for i in range(n_clocks):
            #criando o centro do relogio em questao
            osc=Object(randint(100, 800), randint(100, 600), "osc~")
            dac=Object(osc.x, osc.y+30, "dac~")
            connect(osc, 0, dac, 0)
            centro = [osc,dac]
            
            #criando os objectos que farao parte da lista
            n_processes = randint(2, 5)
            final_list = []
            for i in range(n_processes):
                final_list.append(list[randint(0, n_processes-1)])
            
            #adicionando o relogio na lista
            clocks.append(Clock(randint(50, 300), centro, final_list, randint(7, 30)))
        
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 90
        start = time()
        now = time()
        while (now - start)<bound:
            for c in clocks:
                c.increment()
                now = time()
                #destrua C e crie um novo relogio aleatorio
                if c.lifetime < 0:
                    c.destroy()
                    sleep(0.5)
                    
                    #criando o centro do relogio em questao
                    osc=Object(randint(100, 800), randint(100, 600), "osc~")
                    dac=Object(osc.x, osc.y+30, "dac~")
                    connect(osc, 0, dac, 0)
                    centro = [osc,dac]
                    
                    #criando os objectos que farao parte da lista
                    n_processes = randint(3, 6)
                    final_list = []
                    for i in range(n_processes):
                        final_list.append(list[randint(0, n_processes-1)])
                    
                    #adicionando o relogio na lista
                    clocks.append(Clock(randint(50, 300), centro, final_list, randint(5, 30)))
                    sleep(0.5)
            
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(0.5)
        
    print "fim do segundo movimento"


#################################
#################################
# terceiro movimento: a memoria do computador
#################################
#################################

def third_movement ():
    print "third movement"
    #seta a quantidade de processos
    n_proc = 20
    
    
    #pega a lista de processos e coloca em array
    a = os.popen("ps axco %mem,cmd | sort -k 1 -nr | head -" + str(n_proc+1))
    array = a.read()
    array = array.split("\n")
        
    #removendo o cabecalho
    #print len(array)
    for s in array:
        #print s
        if s.find("%") > -1:
            array.remove(s)  
    
    #pega todos os processos e sua respectiva memoria
    list = []
    for s in array:        
        s = s.strip()
        temp = s.split(" ")
        temp.reverse()
        if len(temp) == 2:
            list.append(temp)
    
    #embaralhando os processos
    n_processes = 10
    final_list = []
    for i in range(n_processes):
        final_list.append(list[randint(0, len(list)-1)])
    list = final_list
        
    #criando o planet
    if init_pd:
        #variavel que armazenara os planetas
        planets = []
    
        #criando os planetas
        for l in list:
            #criando as caixas basicas
            centro = Number(randint(200, 1000), randint(100, 650))
            dac = Object(centro.x, centro.y+30, "dac~")
            label = Comment(centro.x-5, centro.y-15, l[0])
            osc = Object(centro.x, centro.y+60, "osc~")
            
            #conectando as caixas
            connect(osc, 0, dac, 0)
            connect(centro, 0, osc, 0)
            
            #setando os valores
            exp = (float(l[1])*100/pow(2,float(l[1])/10))+110
            centro.set(exp)
            
            #criando o planet que gira em torno do centro
            p1 = Planet(randint(80, 200), centro.x, centro.y, dac)
            
            #setando as velocidades
            speed = randint(1, 3)
            if randint(0, 1) == 0:     
                p1.set_speed(speed)
            else:
                p1.set_speed(-speed)
            
            #criando o planet que gira em torno de p1
            p2 = Planet(50, dac.x, dac.y, osc)
            
            #setando as velocidades
            speed = randint(2, 8)
            if randint(0, 1) == 0:     
                p2.set_speed(speed)
            else:
                p2.set_speed(-speed)
            
            #adicionando os planetas na lista
            ps = [p1, p2, dac]
            p1.move()
            p2.move()
            planets.append(ps)
            
            
        #pd.dsp(False)
            
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 120
        start = time()
        now = time()+1
        while (now - start)<bound:
            now = time()

            #the main loop to rotate 
            for p in planets:
                p[0].move()
                p[1].c_x = p[2].x
                p[1].c_y = p[2].y
                p[1].move()
                sleep(0.05)
            
            #a cada multiplo de 30 cria mais 10 listas
            if (floor((now - start)%40) == 0) and (now - start > 1):
                print "SUBMOV " + str(now-start)
                
                #criando os 20 planetas
                for i in range(15):
                    #pegando um processo aleatorio na lista
                    l = list[randint(0, len(list)-1)]
                    
                    #criando as caixas basicas
                    centro = Number(randint(200, 1000), randint(100, 650))
                    dac = Object(centro.x, centro.y+30, "dac~")
                    label = Comment(centro.x-5, centro.y-15, l[0])
                    osc = Object(centro.x, centro.y+60, "osc~")
                    
                    #conectando as caixas
                    connect(osc, 0, dac, 0)
                    connect(centro, 0, osc, 0)

                    #setando os valores
                    exp = (float(l[1])*100/pow(2,float(l[1])/10))+110
                    centro.set(exp)
                    
                    #criando o planet que gira em torno do centro
                    p1 = Planet(randint(80, 200), centro.x, centro.y, dac)
                    
                    #setando as velocidades
                    speed = randint(1, 3)
                    if randint(0, 1) == 0:     
                        p1.set_speed(speed)
                    else:
                        p1.set_speed(-speed)
                    
                    #criando o planet que gira em torno de p1
                    p2 = Planet(50, dac.x, dac.y, osc)
                    
                    #setando as velocidades
                    speed = randint(2, 8)
                    if randint(0, 1) == 0:     
                        p2.set_speed(speed)
                    else:
                        p2.set_speed(-speed)
                    
                    #adicionando os planetas na lista
                    ps = [p1, p2, dac]
                    p1.move()
                    p2.move()
                    planets.append(ps)
            
        
        #pd.dsp(True)
                
        #limpe o patch    
        pd.clear()
        pd.save()
        pd.clear()
        pd.save()
        sleep(0.5)
        
    print "fim do segundo movimento"
        

#################################
#################################
# quarto movimento: o conteudo da memoria RAM- fade out
#################################
#################################

def fourth_movement ():
    print "quarto movimento"
    
    
    
    
    
    
     #seta a quantidade de processos
    n_proc = 20
    
    #pega a lista de processos e coloca em array
    a = os.popen("ps axco %cpu,cmd | sort -k 1 -nr | head -" + str(n_proc+1))
    array = a.read()
    array = array.split("\n")
    
    #removendo o cabecalho
    #print len(array)
    for s in array:
        if s.find("%") > -1:
            array.remove(s)    
              
    #pega todos os processos e sua respectiva cpu
    list_cpu = []
    for s in array:        
        s = s.strip()
        temp = s.split(" ")
        temp.reverse()
        if len(temp) == 2:
            list_cpu.append(temp)
    
    
    
    
    
    
    
    
    #abrindo a memoria e carregando-a numa lista
    list = []
    memory = open("/dev/mem","r")
    
    #quantidade de linhas de memoria capturada
    size = 250
    
    #formata a memoria para ser usada
    for i in range(size):
         s = memory.readline().replace(";", "*")
         s = s.replace("\n", "")
         s=''.join([char if char in safe_chars else '' for char in s])
         #if(len(s) > 50):
         #    s =  s[0:50]
         list.append(s)
         #print str(i) + " - " + s
    memory.close()
    
    #delimita a area de surgimento dos comentarios
    str_x =  -400
    end_x =  1000
        
        
        
    if init_pd:
        
        '''
        print "SUBMOV 1"
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 15
        start = time()
        now = time()
        while (now - start)<bound:
            aux = randint(0, size-1)
            c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            t = uniform(0.5, 1.0)
            sleep(t)
            #sleep(0.5)
            pd.clear()
            now = time()
        
        print "SUBMOV 2"        
        #por BOUNDS segundos imprima sem apagar a memoria na tela
        bound = 15
        start = time()
        now = time()
        while (now - start)<bound:
            aux = randint(0, size-1)
            c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            t = uniform(0.5, 1.0)
            sleep(t)
            #sleep(0.5)
            now = time()
        '''
        
        pd.clear()
        sleep(0.1)
        
        print "SUBMOV 3"
        #por BOUNDS segundos imprima levemente a memria na tela
        bound = 30
        start = time()
        now = time()
        while (now - start)<bound:
            for i in range (5):
                aux = randint(0, size-1)
                c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
                aux = randint(0, size-1)
                c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            #t = uniform(0.5, 1.0)
            #sleep(t)
            sleep(0.5)
            pd.clear()
            now = time()
            
            
            
       
        #numero de relogios
        n_clocks = 5
        
        #clocks
        clocks = []
        
        #criando N_CLOCK relogios
        for i in range(n_clocks):
            #criando o centro do relogio em questao
            osc=Object(randint(100, 800), randint(100, 600), "osc~")
            dac=Object(osc.x, osc.y+30, "dac~")
            connect(osc, 0, dac, 0)
            centro = [osc,dac]
            
            #criando os objectos que farao parte da lista
            n_processes = randint(5, 10)
            final_list = []
            for i in range(n_processes):
                final_list.append(list_cpu[randint(0, n_processes-1)])
            
            #adicionando o relogio na lista
            clocks.append(Clock(randint(50, 300), centro, final_list, randint(7, 30)))
        
        
        
        
        
        print "SUBMOV 4"
        #por BOUNDS segundos imprima sem apagar a memoria na tela
        bound = 180
        start = time()
        now = time()
        i = 0
        while (now - start)<bound:
            clocks[i].increment()
            i=(i+1)%len(clocks)
        
            aux = randint(0, size-1)
            c1 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c2 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            aux = randint(0, size-1)
            c3 = Comment(randint(str_x, end_x), randint(str_x, end_x), list[aux])
            sleep(0.5)
            now = time()

        pd.clear()
        sleep(1)
        pd.save()
        sleep(0.2)
        pd.clear()
        sleep(1)
        pd.save()
        
        print "fim do quarto movimento"


#################################
#################################
#################################
# MAIN - MAIN - MAIN
#################################
#################################
#################################

if __name__ == '__main__':    
    if init_pd:
        #creates an instance of Pd
        pd = Pd()
        
        #initializes Pyata
        pd.init()
    
    
    counter()
    
    first_movement()
    third_movement()
    pre_first_movement()
    pre_second_movement()
    second_movement()
    fourth_movement()
    
    credits()
    
    if init_pd:
        #finishes Pyata
        pd.quit()
    