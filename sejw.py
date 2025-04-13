import os
from tkinter import *
from wejscie_wyjscie import *
from menu_uzytkownik import *
from stolica import *
from zagadka import *
from slownik import *
from wyniki import *
from tkinter import messagebox
from mapy import mapa

okno_menu=Tk()
okno_menu.geometry('500x440')
okno_menu.title('M93.pl')
#okno_menu.call('tk','scaling', 1.0)               #   SKALOWANIE? ! ? !
okno_menu.resizable(False, False)

################################## M E N U #######################


def MenuGuzik1():
	stolice(okno_menu)

def MenuGuzik2():
	ABC(okno_menu)

def MenuGuzik3():
	zagadka_mat(okno_menu)
	
def MenuGuzik4():
	menu_uzytkownika(okno_menu)

def MenuGuzikM():
	mapa(okno_menu)

def dalej_menu():
	cls_bez_zamknij(okno_menu,zamknij)

	menu_guzik1=Button(okno_menu,command=MenuGuzik1,width=20, text="Gra w 'Stolice'",\
		font=("Arial",14))
	menu_guzik2=Button(okno_menu,command=MenuGuzik2,width=20, text="Pytania 'A, B, czy C?'",\
		font=("Arial",14))
	menu_guzik3=Button(okno_menu,command=MenuGuzik3,width=20, text='Zagadka matematyczna',\
		font=("Arial",14))
	manu_guzikM=Button(okno_menu,command=MenuGuzikM,width=20, text='Quiz "Atlas"',\
		font=("Arial",14))
	menu_guzik4=Button(okno_menu,command=MenuGuzik4,width=20, text='Menu użytkownika',\
		font=("Arial",14))


	menu_guzik1.pack(pady=15)
	menu_guzik2.pack(pady=15)
	menu_guzik3.pack(pady=15)
	manu_guzikM.pack(pady=15)
	menu_guzik4.pack(pady=15)







################################# L O G O W A N I E ###########

# CZYSZCZENIE EKRANU ZE ZBĘDNYCH WIDGETÓW


def cls(nazwa_okna):
    for widgety in nazwa_okna.winfo_children():
        widgety.pack_forget()

def cls_bez_zamknij(nazwa_okna, bez_zamknij):
    for widgety in nazwa_okna.winfo_children():
        if widgety is not bez_zamknij:
            widgety.pack_forget()




# WPROWADZANIE DANYCH UŻYTKOWNIKA


def yes_():
	cls_bez_zamknij(okno_menu,zamknij)
	pytanie=Label(okno_menu,text='Jak na imię ma nowy użytkownik?', font=("Arial",18))
	pytanie.pack()	

	wpisz=Entry(okno_menu, width=25, font=("Arial",18),justify="center")
	wpisz.pack()
	wpisz.focus_set()

	def potwierdz():
		if wpisz.get()=='' or wpisz.get()==None or wpisz.get().isspace():
			messagebox.showerror('Błąd!', 'Musisz coś wpisać!')
			wpisz.focus_set()
		else:
			x=wpisz.get()
			wprowadzenie_danych1(x)
			potwierdz.config(state=DISABLED)
			potwierzenie=Label(okno_menu, text=f'Zmieniono nazwę użytkownika na:\n{wyjscie_danych1()}!',\
				font=("Arial",18))
			potwierzenie.pack(pady=5)
			dalej=Button(okno_menu, text='Przejdź dalej',command=dalej_menu, font=("Arial",18))
			dalej.pack()
	potwierdz=Button(okno_menu, text='Potwierdź',command=potwierdz, font=("Arial",18))
	potwierdz.pack()

def no_():
	cls_bez_zamknij(okno_menu,zamknij)
	powitanie=Label(okno_menu,text=('Witaj, '+str(wyjscie_danych1())+'!'), font=("Arial",18))
	powitanie.pack(pady=30)
	dalej=Button(okno_menu, text='Przejdź dalej',command=dalej_menu, font=("Arial",18))
	dalej.pack(pady=30)


# SPRAWDZENIE CZY ISTNIEJE DANY UŻYTKOWNIK	


if wyjscie_danych1()!=None:
	ostatni=Label(okno_menu, text=(f'Ostatni użytkownik: {str(wyjscie_danych1())},\
\nczy chcesz zmienić użytkownika?'), font=("Arial",18))
	ostatni.pack()
	y_n=Frame(okno_menu)
	y_n.pack(ipady=50)
	yes=Button(y_n,text='Tak',fg='green',command=yes_, font=("Arial",18))
	no=Button(y_n,text='Nie',fg='red',command=no_, font=("Arial",18))
	yes.pack(side='left',ipadx=36,ipady=15, padx=21)
	no.pack(side='right',ipadx=36,ipady=15, padx=21)

elif wyjscie_danych1()==None:
	pytanie=Label(okno_menu,text=f'Brak danych użytkownika!\nJak na imię ma nowy użytkownik?',\
		font=("Arial",18))
	pytanie.pack(pady=10)	
	wpisz=Entry(okno_menu, width=25, font=("Arial",18), justify='center')
	wpisz.pack(pady=10)
	wpisz.focus_set()
	
	def potwierdz():
		if wpisz.get()=='' or wpisz.get()==None or wpisz.get().isspace():
			messagebox.showerror('Błąd!', 'Musisz coś wpisać!')
			wpisz.focus_set()
		else:
			potwierdz.config(state=DISABLED)
			x=wpisz.get()
			wprowadzenie_danych1(x)
			powitanie=Label(okno_menu,text=f'Miło Cię poznać, {wyjscie_danych1()}!', font=("Arial",18))
			powitanie.pack(pady=5)
			dalej=Button(okno_menu, text='Przejdź dalej',command=dalej_menu, font=("Arial",18))
			dalej.pack()
	potwierdz=Button(okno_menu, text='Potwierdź',command=potwierdz, font=("Arial",18))
	potwierdz.pack()



# PĘTLA GŁÓWNA I WYJŚCIE Z PROGRAMU


def exit():
	okno_menu.destroy()

zamknij=Button(okno_menu,text='Zamknij program',fg='red', borderwidth=4, command=exit,\
	font=("Arial",18))
zamknij.pack(padx=15,pady=15,side='bottom')

okno_menu.mainloop()



