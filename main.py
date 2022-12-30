from tkinter import *
from tkinter import messagebox
import os
import urllib.request
from bs4 import BeautifulSoup


pencere1 = Tk()
pencere1.geometry("200x200")
class DataURL:

    dataFile = "dataURL.txt"
   
def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

def ekleme(self):
    pencere3 = Toplevel()
    siteURL = Label(pencere3, text="Url eklemek için, site adresini ön eki ile birlikte giriniz: ", font=" Arial 11 bold")
    siteURL.pack()
    ent1 = Entry(pencere3, width=25, borderwidth=5)
    ent1.pack()
    buton8 = Button(pencere3, text="Ekle", bg="black", fg="white", font="Arial 20 bold")
    buton8.pack()
    dataOpen = open(self.dataFile, 'a')
    if (ent1.get() == str("http://")) or (ent1.get() == str("https://")):
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        label3= Label(pencere3, text= "Url kaydedildi.")
        label3.pack()
    else:
        hata = messagebox.showinfo("Hata", "Lütfen url'yi ön ekiyle birlikte giriniz.")
        hata.pack()
def dataRead(self):
      pencere5= Toplevel()
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
        label9= Label(pencere5, text="Henüz kaydedilmiş adres yok!")
        label9.pack()
      else:
            for dataShow in dataOpen:
                label10= Label(pencere5, dataShow)
                label10.pack()
      dataOpen.close()

class GetURL:

    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

def __init__(self, fileTest):
    fileTest = open(self.getFile, 'a')
    fileTest.close()

def getWeb(self):
    pencere6 = Toplevel()

    pencere6.title("Örümcek gönderiliyor...")

    dataOpen = open(self.dataFile, 'r')
    getOpen = open(self.getFile, 'w')

    for dataGet in dataOpen:
        webSite = urllib.request.urlopen(dataGet)
        getBytes = webSite.read()
        webPage = getBytes.decode("utf8")
        webSite.close()
        soup = BeautifulSoup(webPage, 'html.parser')
        getOpen.write(dataGet.strip() + " - " + soup.title.contents[0] + "\n" + soup.find("p").text)
        dataOpen.close()
        getOpen.close()

    label11= (pencere6, "Çalışma tamamlandı!")
    label11.pack()
    buton11= Button(pencere6, text= "Menü", command= yenipencere)
    buton11.pack()
def getList(self):
    pencere7 = Toplevel()
    getOpen = open(self.getFile, 'r')
    if os.stat(self.getFile).st_size == 0:
        label12= Label(pencere7, text= "Henüz ziyaret edilmiş adres yok! Örümceği çalıştırmak için lütfen aşağıdaki butona tıklayın.")
        label12.pack()
        buton14= Button(pencere7, text="Örümcek gönder", fg="red", bg="white", width=20, height=5, command=getWeb)
        buton14.pack()
    else:
        for dataShow in getOpen:
            label13= Label(pencere7, text= dataShow)
            label13.pack()
    getOpen.close()
def yenipencere():
    pencere2 = Toplevel()
    buton2 = Button(pencere2, text="Url Ekle", width=20, height=5, fg="red", bg="green",command=ekleme)
    buton4 = Button(pencere2, text="Url Listele", fg="black", bg="green", width=20, height=5,command=dataRead)
    buton5 = Button(pencere2, text="Örümcek Gönder", fg="red", bg="green", width=20, height=5, command=getWeb)
    buton6 = Button(pencere2, text="Sonuçları Listele", fg="black", bg="green",width=20, height=5, command= getList)
    buton7 = Button(pencere2, text="Çıkış", fg="white", bg="red", command=pencere2.quit, width=20, height=5)
    buton2.pack()
    buton4.pack()
    buton5.pack()
    buton6.pack()
    buton7.pack()

buton1 = Button(text="Menü", command=yenipencere, width=10, height=5)
buton3 = Button(text="Çıkış", fg="white", bg="red", width=10, height=5, command=pencere1.quit)
buton1.pack()
buton3.pack()

pencere1.mainloop()
pencere2.mainloop()
pencere3.mainloop()
pencere4.mainloop()
pencere5.mainloop()
pencere6.mainloop()
pencere7.mainloop()