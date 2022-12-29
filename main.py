from tkinter import *
import os
pencere1 = Tk()
class DataURL:

    dataFile = "dataURL.txt"

def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

def ekleme():
    pencere3 = Toplevel()
    siteURL = Label(pencere3, text="Url eklemek için, site adresini ön eki ile birlikte giriniz: ", font=" Arial 11 bold")
    siteURL.pack()
    ent1 = Entry(pencere3, width=25, borderwidth=5)
    ent1.pack()
    buton8 = Button(pencere3, text="Ekle", bg="black", fg="white", font="Arial 20 bold")
    buton8.pack()
    if (ent1.get() == str("http://")) or (ent1.get() == str("https://")):
        Label3 = Label(pencere3, text="Giriş Başarılı...")
    else:
        Label3 = Label("Hatalı Giriş !")
    Label3.pack()
def dataRead(self):
      pencere5= Toplevel()
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Henüz kaydedilmiş adres yok!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()

class GetURL:

    dataFile = "dataURL.txt"
    getFile = "getURL.txt"

def __init__(self):
    fileTest = open(self.getFile, 'a')
    fileTest.close()

def getWeb(self):

    print("Örümcek çalışıyor...")

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

    print("Çalışma tamamlandı!")

def getList(self):
    getOpen = open(self.getFile, 'r')
    if os.stat(self.getFile).st_size == 0:
        print("Henüz ziyaret edilmiş adres yok!")
    else:
        for dataShow in getOpen:
            print(dataShow)
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

buton1 = Button(text="Menü", command=yenipencere)
buton3 = Button(text="Çıkış", fg="white", bg="red", command=pencere1.quit)
buton1.pack()
buton3.pack()

pencere1.mainloop()
pencere2.mainloop()
pencere3.mainloop()
pencere4.mainloop()