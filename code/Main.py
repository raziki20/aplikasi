from cProfile import label
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from matplotlib import pyplot as plt
from cv2 import Sobel, cv2
from Gray import gray
from Biner import biner
from RGB import rgb


root = Tk()
root.title("Halaman Utama")
root.geometry('400x350')
# root.eval('tk::PlaceWindow . center')
# root.frame = Tk.Frame(root, bg = "blue")
# root.frame.pack(fill=BOTH, expand=1)

# def about():
#     messagebox.showinfo( 'About','Ini Adalah Aplikasi Indentifikasi Tingkat Kematangan Buah Naga(Hylocereus SPP)')

# menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black') 
 
# file = Menu(menubar, tearoff=0)  
# file.add_command(label="New")  
# file.add_command(label="Open")  
# file.add_command(label="Save")  
# file.add_command(label="Save as")    
# file.add_separator()  
# file.add_command(label="Exit", command=root.quit)  
# menubar.add_cascade(label="File", menu=file)  

# edit = Menu(menubar, tearoff=0)  
# edit.add_command(label="Undo")  
# edit.add_separator()     
# edit.add_command(label="Cut")  
# edit.add_command(label="Copy")  
# edit.add_command(label="Paste")  
# menubar.add_cascade(label="Edit", menu=edit)  

# help = Menu(menubar, tearoff=0)  
# help.add_command(label="About", command=about)  
# menubar.add_cascade(label="Help", menu=help)  
    
# root.config(menu=menubar)


def buka():
    global photo
    root.namafile = filedialog.askopenfilename(initialdir="\Python38\aplikasi",title="membuka file baru",filetypes=(("jpg file","*.jpg"),("png file","*.png"),("jpeg file","*.jpeg")))
    # lbl = Label(root,text=(root.namafile)).grid()
    # frame = LabelFrame(root, text= "Gambar RGB").grid()
    # photo = ImageTk.PhotoImage(Image.open(root.namafile))
    # lbl = Label(frame, image=photo).grid()
    image = cv2.imread(root.namafile)
    image = cv2.resize(image,(300,300))
    # image = ImageTk.PhotoImage(image)
    # label = Label(text= "Gambar Asli")
    # label.place(x=25, y=25, width=50, height=50)
    # panel = Label(image=image)
    # panel.image = image
    cv2.imshow("Citra Asli", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # gray(root.namafile)
    # biner(root.namafile)
    # Sobel(root.namafile)
   
btn1 = Button(root, text="Buka Gambar", command=buka).grid(padx= 10, pady= 20)
person = Label(root,text="...")
person.place(x=100, y=275, width=200, height=20)

def segmentasi():
    global photo
    root.namafile = filedialog.askopenfilename(initialdir="\Python38\aplikasi",title="membuka file baru",filetypes=(("jpg file","*.jpg"),("png file","*.png"),("jpeg file","*.jpeg")))

    rgb(root.namafile)

btn2 = Button(root, text="Segmentasi RGB", command= segmentasi).grid(padx=20, pady=20)    

# def ekstraksi():
#     global photo
#     root.namafile = filedialog.askopenfilename(initialdir="\Python38\aplikasi",title="membuka file baru",filetypes=(("jpg file","*.jpg"),("png file","*.png"),("jpeg file","*.jpeg")))

#     glcm(root.namafile)

# btn3 = Button(root, text="Ekstraksi Ciri", command= ekstraksi).grid(padx=20, pady=20)    


root.mainloop()