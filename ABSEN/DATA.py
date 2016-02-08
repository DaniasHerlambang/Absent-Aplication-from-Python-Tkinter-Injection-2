"""
Name             : Aplication-Absent-from-Tkinter-II-Injection- version 2
Created By       : Rahmandani Herlambang (Danias)
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/DaniasHerlambang13/-II-Aplication-Absent-from-Tkinter-II-Injection-.git
Thanks to        : Python Tkinter - Mexico Tech - Newbie - Summon Agus 
"""

#****************************************** TK UNTUK DATA UTAMA ********************************************************************************
from Tkinter import*
from tkMessageBox  import*
import tkMessageBox as mb
import ttk
import time
import tkColorChooser
import csv

import os
##os.system("spd-say -l en -t female3 'welcome in fosti'")


##os.system("mpg321 suara/x.mp3")

##import subprocess
##subprocess.call(["mpg321","suara/BOM.wav"])

##from winsound import *  #untuk window

##from wave import open as waveOpen               #untuk ubuntu
##from ossaudiodev impohqwerty
##qqrt open as ossOpen         #untuk ubuntu
####s = open('./suara/tertawa.wav','w')



#****************************************** CLASS UNTUK KOMPONEN TAMPILAN AWAL PROGRAM******************************************************************

class Data(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("700x400")
        self.parent.resizable(False, False)
        self.teksJam = StringVar()
        self.initUI()
        self.awal()
        self.listboxData.bind('<ButtonRelease-1>', self.entry)
        self.listboxData.bind('<KeyRelease>', self.entry)
        self.entryc.bind('<KeyRelease>', self.cari)
     
    def initUI(self):
        self.update() #memenggil def update dan menjalankanya
        self.teksJam = StringVar()
        
        self.datJam_menu = time.strftime("FOSTI",
                                           time.localtime())
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar = 760
        tinggi = 415
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
 
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        
        mainFrame = Frame(self.parent,bg='#254117',cursor='spraycan',relief=RIDGE,bd=10 )
        mainFrame.pack(fill=BOTH, expand=YES)
        self.main = mainFrame
         
        self.parent.title(self.datJam_menu)

        self.menubar = Menu(self.parent)
        self.parent.config(menu = self.menubar)

        self.fr_inti = Frame(mainFrame,bg='#254117')
        self.fr_inti.pack(expand=YES)

        # ************************* penggunaan Cari 
                    
        fr_c=Frame(self.fr_inti ,bg='#254117')
        fr_c.pack(fill=X,pady=2)

        self.checkc=Menubutton(fr_c,text='Cari:',bg='black',fg='white',relief=RIDGE,bd=2)
        self.checkc.pack(side=LEFT)

        self.entryc=Entry(fr_c,relief=RIDGE,bd=2)
        self.entryc.pack(side=LEFT,fill=X,expand=YES)
        
        # ************************* penggunaan radiobutton hadir/ tidak

        self.fr_kanan= LabelFrame(self.fr_inti ,text='FITUR',fg='white',bg='#254117')
        self.fr_kanan.pack(side=RIGHT,fill=X,expand=YES,padx=5)

        fr_hdr=Frame(self.fr_kanan ,bg='#254117')
        fr_hdr.pack(side=BOTTOM,fill=X,expand=YES,pady=10)
        
        self.hadir = Radiobutton(fr_hdr,relief=GROOVE,bd=5 ,command=self.databaru,text=' H A D I R '
                                 ,bg='#800517',fg='white',width=15)#,height=5)
        self.hadir.pack(side=LEFT,pady=2)

        self.entryH=Entry(fr_hdr,relief=RIDGE,bd=5,width=5)
        self.entryH.pack(side=LEFT,fill=X)

        # ************************* button logo
        
        self.logo1 = PhotoImage(file='./gambar/F.gif')
        self.logo = Menubutton(self.fr_kanan,image=self.logo1)
        self.logo.pack()

        # ************************* penggunaan detail nomor dan nim 
                    
        fr_nn=Frame(self.fr_kanan ,bg='black')
        fr_nn.pack(fill=X,expand=YES,padx=5)

        self.entrynn3=Entry(fr_nn,relief=RIDGE,bd=4)
        self.entrynn3.pack(side=BOTTOM,fill=X,expand=YES,pady=3)

        self.entrynn2=Entry(fr_nn,relief=RIDGE,bd=4)
        self.entrynn2.pack(side=BOTTOM,fill=X,expand=YES,pady=3)

        self.entrynn1=Entry(fr_nn,relief=RIDGE,bd=4)
        self.entrynn1.pack(side=BOTTOM,fill=X,expand=YES,pady=3)

        
        # ************************* penggunaan listbox n scroll
        self.listboxData=Listbox(self.fr_inti, bg='black',fg='white',width=60 , height=15)
        self.listboxData.pack(fill=BOTH, side=RIGHT,expand=YES)
        s=ttk.Style()
        s.theme_use('classic')
        s.configure('TScrollbar', background='black')
        scrollbar = ttk.Scrollbar(self.fr_inti, orient=VERTICAL,
                                command=self.listboxData.yview,cursor='hand2')
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listboxData.config(yscrollcommand=scrollbar.set)
        
        
        # ************************* kumpulan menubar dan filemenu()
        
        self.digaris = PhotoImage(file='./gambar kecil/menu_divider.gif')
        
        self.gmbrimpor = PhotoImage(file='./gambar kecil/floppybuddy.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'IMPORT',menu = fileMenu)
        fileMenu.add_command( image=self.digaris)
        fileMenu.add_command( label = 'GO!',compound='right',command=self.impor,image=self.gmbrimpor)
        fileMenu.add_command( image=self.digaris)
##
##        fileMenu = Menu(self.menubar, tearoff=0)
##        self.menubar.add_cascade(state='disabled',label = ':-:'*50,compound='right',menu = fileMenu)
        
        self.ums = PhotoImage(file='./gambar/F.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'ABOUT',compound='right',menu = fileMenu)
        fileMenu.add_command( label = 'LINUX TEAM',image=self.ums,compound='top')

##        fileMenu = Menu(self.menubar, tearoff=0)
##        self.menubar.add_cascade(state='disabled',label = ':-:'*50,compound='right',menu = fileMenu)

        # ************************* button keluar berada di kiri bawah
        self.jpgout = PhotoImage(file='./gambar kecil/close.button.gif')
        self.fr_out = LabelFrame (mainFrame,bg='#254117')
        self.fr_out.pack(side=BOTTOM,fill=BOTH,expand=YES)
        self.tmbl_keluar = Button(self.fr_out,image=self.jpgout,command=self.keluar,bg='black')
        self.tmbl_keluar.pack(side=LEFT)
        self.jpgout2 = PhotoImage(file='./gambar kecil/thumbup.gif')

        # ************************* label untuk jam()
        self.j = Label(self.fr_out,bg='#254117',textvariable=self.teksJam
                                 ,compound='center',fg='white',font=('Century', 13))
        self.j.pack(side=RIGHT)
        
    def awal(self):
        self.listboxData.configure(state=DISABLED)
        self.entrynn3.configure(state=DISABLED)
        self.entrynn2.configure(state=DISABLED)
        self.entrynn1.configure(state=DISABLED)
        self.hadir.configure(state=DISABLED)
        self.listboxData.configure( bg='black',fg='white')


    # ************************* jika keluar maka akan muncul rosesbar seolah-olah seperti loading dan window menutup setelah sekian detik()    
    def keluar(self):
        self.parent.title('FOSTI - EXIT')
        self.SuaraSystemKeluar()
        s = ttk.Style()
        s.theme_use('classic')
        s.configure("red.Horizontal.TProgressbar", foreground='yellow', background='darkred')
        pb_hd = ttk.Progressbar(self.main,style="red.Horizontal.TProgressbar" ,orient='horizontal', mode='indeterminate')
        pb_hd.pack(expand=True, fill=BOTH, side=RIGHT)
        pb_hd.start(20)
        root.after(5000, root.destroy)  #menutup window setelah 3 detik
        self.tmbl_keluar.configure(image=self.jpgout2)
        
    def SuaraSystemKeluar(self,Event=None):
##        play =  PlaySound('./suara/Thank You.wav', SND_FILENAME)
        os.system("spd-say -l en -t male2 'GOOD BYE'")
        
    # ************************* jam update menurut waktu lokal pc()   
    def update(self):
        # strftime() berfungsi untuk merubah data waktu secara lokal
        # menjadi bentuk string yang kita inginkan.
        datJam = time.strftime("%H : %M : %S %p " ,
                               time.localtime())

        # mengubah teks jam sesuai dengan waktu saat ini
        self.teksJam.set(datJam)
        
        # perubahan teks jam dalam selang waktu 1 detik (1000 ms)
        self.timer = self.parent.after(1000, self.update)

    # ************************* sound about hello()   
    def aboutSistem(self,Event=None):
        play =  PlaySound('./suara/x.about-musik kelompok 8.wav', SND_FILENAME)
        play =  PlaySound('./suara/x.about-sapa hallo.wav', SND_FILENAME)
        play =  PlaySound('./suara/x.about-musik kelompok 8.wav', SND_FILENAME)
           
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#****************************************** FUNGSI IMPORT DATA ******************************************************************
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def impor(self):
        try:
            #******************************untuk**data**atas*********************************************************************************            
            self.listboxData.configure(state=NORMAL)
            self.entrynn3.configure(state=NORMAL)
            self.entrynn2.configure(state=NORMAL)
            self.entrynn1.configure(state=NORMAL)
            self.hadir.configure(state=NORMAL)
            
            import tkFileDialog as TD
            self.File = TD.askopenfilename()
            buka=open(self.File)
            buka.readline()
            r = csv.reader(buka)
            self.lis=[]
            

            hadir = 'HADIR'

            for item in r:
                if item[self._gantiColumn_perMinggu()] == hadir:
                    item
                else:
                    item1 = item[0]
                    item2 = item[1]
                    item3 = item[2]
                    self.lis.append(item)

                    self.listboxData.insert(END, item1)
                    self.listboxData.selection_set(0)

                    self.entryKosong()

                    self.entrynn1.insert(END, self.lis[0][0])
                    self.entrynn2.insert(END, self.lis[0][1])
                    self.entrynn3.insert(END, self.lis[0][2])

##        #****************************** jika impor berhasil *****************************************************                
            self.menubar.entryconfig(1,label= 'DATA FOSTI')
            self.parent.title('FOSTI - SUCCESS GAES !!!')
            self.SuaraImporSukses()

##            mb.showinfo("FOSTI - OPEN RECRUITMEN","SUCCESS GAES !!!")

    

##        #****************************** jika impor cancel ***************************************************** 
        except IOError :
            
            self.parent.title('HEY YOU !!!')

            self.SuaraImporCancel()

##            mb.showwarning("FOSTI - OPEN RECRUITMEN","HEY YOU !!!!")


##        #****************************** jika impor gagal ***************************************************** 
        except IndexError :
            
            self.parent.title('YOUR STUPID !!!')

            self.SuaraImporGagal()

##            mb.showerror("FOSTI - OPEN RECRUITMEN","YOUR STUPID :(")

            
    #****************************** kumpulan suara impor *****************************************************        
    def SuaraImporSukses(self,Event=None):
##        play =  PlaySound('./suara/tertawa', SND_FILENAME)
        os.system("spd-say -l en -t female2 'HA HA HA SUCCES'")
        
    def SuaraImporCancel(self,Event=None):
##        play =  PlaySound('./suara/ok sistem cancel.wav', SND_FILENAME)
        
        os.system("spd-say -l en -t female2 'your fucking fuck'")
        
    def SuaraImporGagal(self,Event=None):
##        play =  PlaySound('./suara/bom', SND_FILENAME)

        os.system("spd-say -l en -t female3 'your stupid fuck'")

    def entryKosong(self):
        self.entrynn1.delete(0, END)
        self.entrynn2.delete(0, END)
        self.entrynn3.delete(0, END)
        
        self.entryH.delete(0, END)

    def kosongan(self):
        for dat in range(len(self.lis)):
            self.listboxData.delete(0,END)
        self.listboxData.selection_set(0)
                    
        self.entrynn1.delete(0, END)
        self.entrynn2.delete(0, END)
        self.entrynn3.delete(0, END)


    def cari (self,Event=None):
        try:

        #**************************pencarian data atas**************************************************
            
            entry = self.entryc.get().lower() #Target Cari Adalah Masukan data dari entryc 
            dataCari = []
            for i in self.lis:
                if entry in i[0].lower()\
                    or entry in i[1].lower()\
                    or entry in i[2].lower():
                        dataCari.append(i)
                                
            self.kosongan()
            self.target = dataCari
            for dat in range(len(self.target )):
                    self.listboxData.insert(END, self.target [dat][0])               
            self.listboxData.selection_set(0)
            indeks = self.listboxData.curselection()
            kode = int(indeks[0])
##            self.isiData()
            self.entrynn1.insert(END, self.target[kode][0])
            self.entrynn2.insert(END, self.target[kode][1])
            self.entrynn3.insert(END, self.target[kode][2])
            self.listboxData.configure( bg='dark red',fg='white')
            
        except:
            pass
            os.system("spd-say -l id -t female2 'hayyooo salaaah'")
##            os.system("spd-say -l id -t female3 '%s ti dag di temukan'"%(self.entryc.get()))

    def entry (self,Event=None):
        indeks = self.listboxData.curselection()
        kode = int(indeks[0])
               
        # hapus data
        self.entryKosong()
               
        # isi data
        self.entrynn1.insert(END, self.lis[kode][0])
        self.entrynn2.insert(END, self.lis[kode][1])
        self.entrynn3.insert(END, self.lis[kode][2])
        self.listboxData.configure( bg='black',fg='white')
        self.parent.title('FORUM OPEN SOURCE TEKNIK INFORMATIKA')
        
    def _gantiColumn_perMinggu(self,event=None):
        from time import strftime
        bagi_bulan  = 4
        bulan_ini   = strftime('%m')
##        print bulan_ini
        bulan_ini_1 = str(bulan_ini)#[0].replace("0", "")
##        print bulan_ini_1
        minggu_ke   = int(bulan_ini_1)/bagi_bulan
        return minggu_ke+3 #agar ter inisialisai dimulai pada column 3 = item[3], Minggu1
        
            
    def databaru (self,event=None):
            tambahanNam = self.entrynn1.get()
            tambahannim = self.entrynn2.get()
            tambahanno = self.entrynn3.get()
                        
            v = open('FOSTI 2015 (ORIGINAL).csv')
            r = csv.reader(v)
            los=[]
                        
            hadir = 'HADIR'

            output = open('FOSTI 2015 (ORIGINAL).csv', 'rb+')
            writer = csv.writer(output)
            self.listboxData.bind('<ButtonRelease-1>', self.entry)
            self.listboxData.bind('<KeyRelease>', self.entry)

            try:
                self.parent.title('FINIC - UMS')
                mb.showinfo("FORUM OPEN SOURCE TEKNIK INFORMATIKA","ANDA SUDAH HADIR KAWANKU \n        TERIMAKASIH")
                os.system("spd-say -l en -t female2 'wel come in fosti familly'")
                            
                tambahanNam = self.entrynn1.get()
                            

                for item in r:
                    if item[1] == tambahannim:
                        los.append(item)
                        item[self._gantiColumn_perMinggu()] = hadir #yang di return cuman ini.
    ##                                print item
                        writer.writerow(item)
                    
                        
                    else:
                        tem1 = item[0:]
                        self.x()
                                                                   
                        writer.writerow(item)
                            
            except:
                pass
                    
    def x (self,event=None):
        v = open('FOSTI 2015 (ORIGINAL).csv')
        v.readline()
        r = csv.reader(v)
        self.las=[]
        self.loss=[]
                    
        hadir = 'HADIR'
        self.kosongan()
        for item in r:
            if item[self._gantiColumn_perMinggu()] == hadir:
##                item1 = item[0]
                self.loss.append(item)

            else:
                item1 = item[0]
                self.las.append(item)
                self.listboxData.insert(END, item[0])
                self.listboxData.selection_set(0)

                self.entryKosong()

                self.entrynn1.insert(END,self.las[0][0])
                self.entrynn2.insert(END,self.las[0][1])
                self.entrynn3.insert(END,self.las[0][2])
                self.listboxData.bind('<ButtonRelease-1>', self.entry_kondisi_2)
                self.listboxData.bind('<KeyRelease>', self.entry_kondisi_2)
                self.entryc.bind('<KeyRelease>', self.cari2)
                self.listboxData.configure( bg='black',fg='white')
                
        i= len(self.loss)        
        self.entryH.insert(END, i)              
                
    def entry_kondisi_2(self,event=None):
        indeks = self.listboxData.curselection()
        kode = int(indeks[0])

        self.entryKosong()

        
        self.entrynn1.insert(END, self.las[kode][0])
        self.entrynn2.insert(END, self.las[kode][1])
        self.entrynn3.insert(END, self.las[kode][2])
        
    def cari2 (self,Event=None):
        try:
        #**************************pencarian data atas**************************************************
            entry = self.entryc.get().lower() #Target Cari Adalah Masukan data dari entryc 
            dataCari = []
            for i in self.las:
                if entry in i[0].lower()\
                    or entry in i[1].lower()\
                    or entry in i[2].lower():
                        dataCari.append(i)
                                
            self.kosongan()
            self.target = dataCari
            for dat in range(len(self.target )):
                    self.listboxData.insert(END, self.target [dat][0])               
            self.listboxData.selection_set(0)
            indeks = self.listboxData.curselection()
            kode = int(indeks[0])
##            self.isiData()
            self.entrynn1.insert(END, self.target[kode][0])
            self.entrynn2.insert(END, self.target[kode][1])
            self.entrynn3.insert(END, self.target[kode][2])
            self.listboxData.configure( bg='dark red',fg='white')
        except:
            pass
            os.system("spd-say -l id -t female2 'haayyyooo salaaah'")
##            os.system("spd-say -l id -t female3 '%s ti dag di temukan'"%(self.entryc.get()))

#----------------------------------------------------------------------------------------------------------------#
if __name__ =='__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()
