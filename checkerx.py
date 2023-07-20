from tkinter import *
import os
import subprocess


def install_requirements():
    try:
        # requirements.txt dosyasındaki bağımlılıkları kur
        subprocess.run(["pip", "install", "-r", "FIXED-NETFLIXER/requirements.txt"])
    except Exception as e:
        print("Hata oluştu:", e)

def toggle_checker(checker):
    if checker == "Netflix":
        if netflix_var.get() == 1:
            print("Netflix Checker çalıştırılıyor!")
            try:
                # FIXED-NETFLIXER adlı GitHub uygulamasını indir
                subprocess.run(["git", "clone", "https://github.com/yunus-EmreX/FIXED-NETFLIXER.git"])

                # GitHub uygulamasının klasörüne gir
                os.chdir("FIXED-NETFLIXER")

                # requirements.txt dosyasındaki bağımlılıkları kur
                install_requirements()

                # main.py dosyasını başka bir terminal penceresinde çalıştır
                command = "python main.py"  # Ya da kendi Python sürümünüzü belirtin, örneğin: "python3 main.py"
                subprocess.Popen(command, shell=True)
            except Exception as e:
                print("Hata oluştu:", e)

        else:
            print("Netflix Checker durduruldu!")
    elif checker == "Valorant":
        if valorant_var.get() == 1:
            print("Valorant Checker çalıştırılıyor!")
            # Valorant Checker ile ilgili kod buraya gelecek
        else:
            print("Valorant Checker durduruldu!")
    elif checker == "Roblox":
        if roblox_var.get() == 1:
            print("Roblox Checker çalıştırılıyor!")
            # Roblox Checker ile ilgili kod buraya gelecek
        else:
            print("Roblox Checker durduruldu!")
    elif checker == "Disney+":
        if disney_var.get() == 1:
            print("Disney+ Checker çalıştırılıyor!") 
            # Disney+ Checker ile ilgili kod buraya gelecek
        else:
            print("Disney+ Checker durduruldu!")

# Ana kod
pencere = Tk()
pencere.title('Checker Arayüzü')
pencere.geometry('500x300')

sol_cerceve = Frame(pencere, bg='lightblue')
sol_cerceve.pack(side='left', fill='both', expand=True)

baslik_etiketi = Label(sol_cerceve, text="Checker Listesi", font=('Arial', 16), padx=10, pady=10)
baslik_etiketi.pack()

checkerler = ["Netflix", "Valorant", "Roblox", "Disney+"]

netflix_var = IntVar()
valorant_var = IntVar()
roblox_var = IntVar()
disney_var = IntVar()

for i in range(len(checkerler)):
    checkbutton = Checkbutton(sol_cerceve, text=checkerler[i], font=('Arial', 12), padx=10, pady=5,
                              variable=[netflix_var, valorant_var, roblox_var, disney_var][i],
                              command=lambda c=checkerler[i]: toggle_checker(c))
    checkbutton.pack(fill=X)

pencere.mainloop()
