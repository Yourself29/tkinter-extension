from tkinter import *

class PlainTable(Frame) :
    
    def get_val( self, type = 'c', column = 0, row = 0, n = 0) :
        if type == 'h' :
            if n < 0 : raise ValueError(f"error : n = {n}, it should be >= 0")
            if n >= len(self.heading) : raise ValueError(f"error : n >= {n}, it should be < {len(self.heading)}")
            
            exec(f"val = self.h{n}[\'text\']")
            return val
        #need to do it for type == "c"

    def set_val( self,value, row = 0, column = 0, n = 0, type = "c") :
        if type == "h" :
            if n >= len(self.heading) : raise ValueError(f"error : n >= {n}, it should be < {len(self.heading)}")#n = len(self.heading)-1
            if n < 0 : n = 0
            exec("self.h"+str(n)+"[\'text\'] = "+ '\'' +str(value)+'\'')
        else :
            if column >= self.columns : raise ValueError(f"error : columnumn = {column}, it should be < {self.columns}")#column = self.columns-1
            if row > self.rows : raise ValueError(f"error : row = {row}, should be <= {self.rows} ")#row = self.rows
            if row < 1 : raise ValueError(f"error : row = {row}, should be >= {1} ")#row = 1
            if column < 0 : raise ValueError(f"error : column = {column}, should be >= {0} ")#column = 0

            exec("self.c_"+str(column)+'_'+str(row)+"[\'text\'] = "+'\''+ str(value)+'\'')
    
    def __init__(self, parent, border = 2, common_text = "", columns = 1, rows = 1, heading = list(), font = ("Courier", '15'), h_font = ("Courier", '20'), *args, **kwargs) :
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.heading = heading
        self.rows = rows
        self.border = border
        self.columns = columns
        self.common_text = common_text
        self.font = font
        self.h_font = h_font

        if self.rows == 0 : self.rows = 1
        if self.columns == 0 : self.columns = 1 

        if len(self.heading) != 0 : 
            i = 0
            for text in self.heading :
                exec("self.h"+str(i)+'='+"Label(self, text = text, bd = self.border, font = self.h_font, relief = RAISED)")
                exec("self.h"+str(i)+'.grid(column = '+str(i)+", row = 0, sticky = \"nsew\")")
                i+=1

        for c in range(self.columns) :
           
            for ro in range(self.rows) :
                r = ro+1
                exec("self.c_"+str(c)+'_'+str(r)+" = Label(self, bd = self.border, relief = RAISED, font = self.font, text = self.common_text)")
                exec("self.c_"+str(c)+'_'+str(r)+".grid(column = "+str(c)+', row = '+str(r)+", sticky = \'nsew\')")
