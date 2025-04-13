from wejscie_wyjscie import *
from tkinter import *
from os import system
from wyniki import *
import openpyxl
from openpyxl import Workbook, load_workbook
from tkinter import messagebox



# TWORZENIE OKNA I PODSTAWOWE FUNKCJE


def menu_uzytkownika(okno):

	def cls_(nazwa_okna):
		for widgety in nazwa_okna.winfo_children():
			widgety.pack_forget()

	def cls_bez_zamknij(nazwa_okna, bez_zamknij):
		for widgety in nazwa_okna.winfo_children():
			if widgety is not bez_zamknij:
				widgety.pack_forget()



	okno.withdraw()
	okno_menu1=Toplevel()
	okno_menu1.focus_set()
	okno_menu1.geometry('500x360')
	okno_menu1.title('Menu użytkownika')






# GUZIK 1 FUNKCJA:


	def MenuGuzik1():
		okno_info=Toplevel()
		okno_info.geometry('280x130') 
		okno_info.title('Zmiana loginu')
		okno_info.focus_set()
		pytanie=Label(okno_info,text='Jak na imię ma nowy użytkownik?', font=('Arial',12))
		pytanie.pack()
		usuniecie_danych1()
		wpisz=Entry(okno_info, width=25, justify='center', font=('Arial',12))
		wpisz.pack()
		wpisz.focus_set()
		
		def powrot_infoF():
			if wpisz.get()=='' or wpisz.get()==None or wpisz.get().isspace():
				messagebox.showerror('Błąd!', 'Musisz coś wpisać!')
				wpisz.focus_set()
			else:
				x=wpisz.get()
				wprowadzenie_danych1(x)
				cls_(okno_info)
				powitanie=Label(okno_info,text=f'Witaj, {wyjscie_danych1()}!', font=('Arial',12))
				powitanie.pack()			
				def okey():
					okno_info.quit()
					okno_info.destroy()

				powrot_inf=Button(okno_info,text='OK',command=okey, font=('Arial',12))
				powrot_inf.pack(pady=15, ipadx=25)

		powrot_info=Button(okno_info,text='OK',command=powrot_infoF, font=('Arial',12))
		powrot_info.pack(pady=15, ipadx=25)
		okno_info.mainloop()







# GUZIK 2 FUNKCJA:


	def MenuGuzik2():
		baza_danych=load_workbook('baza.xlsx')
		arkusz=baza_danych.active
		okno_info=Tk()
		#okno_info.geometry('280x320')
		okno_info.title('Najlepsze wyniki')
		info_napis=Label(okno_info,padx=20,font=('Arial',12),\
text=f"Najlepsze wyniki gry 'A, B, czy C?':\n\
1. {arkusz['B19'].value}   {arkusz['A19'].value} pkt.\n\
2. {arkusz['B20'].value}   {arkusz['A20'].value} pkt.\n\
3. {arkusz['B21'].value}   {arkusz['A21'].value} pkt.\n\
4. {arkusz['B22'].value}   {arkusz['A22'].value} pkt.\n\
5. {arkusz['B23'].value}   {arkusz['A23'].value} pkt.\n\
\
\n\
Najlepsze wyniki gry 'Stolice':\n\
1. {arkusz['B11'].value}   {arkusz['A11'].value} pkt.\n\
2. {arkusz['B12'].value}   {arkusz['A12'].value} pkt.\n\
3. {arkusz['B13'].value}   {arkusz['A13'].value} pkt.\n\
4. {arkusz['B14'].value}   {arkusz['A14'].value} pkt.\n\
5. {arkusz['B15'].value}   {arkusz['A15'].value} pkt.\n\
\
\n\
Najlepsze wyniki gry 'Atlas':\n\
1. {arkusz['B29'].value}   {arkusz['A29'].value}%\n\
2. {arkusz['B30'].value}   {arkusz['A30'].value}%\n\
3. {arkusz['B31'].value}   {arkusz['A31'].value}%\n\
4. {arkusz['B32'].value}   {arkusz['A32'].value}%\n\
5. {arkusz['B33'].value}   {arkusz['A33'].value}%")

		info_napis.pack(pady=5)
		
		def powrot_infoF():
			okno_info.quit()
			okno_info.destroy()
		powrot_info=Button(okno_info,text='OK', font=('Arial',12),command=powrot_infoF)
		powrot_info.pack(pady=15, ipadx=25)
		okno_info.mainloop()






# GUZIK 3 FUNKCJA:


	def MenuGuzik3():
		okno_info=Tk()
		okno_info.geometry('500x130')
		okno_info.title('Reset punktacji')

		info_napis=Label(okno_info,padx=20, text="Czy jesteś pewien że chcesz usunąć\
\nzapisaną punktację najlepszych wyników?", font=('Arial',12))
		info_napis.pack()
		ramka=Frame(okno_info)
		ramka.pack()
		def powrotN():
			okno_info.quit()
			okno_info.destroy()

		def powrot_infoF():
			usuniecie_danych2()
			usuniecie_danych4()
			usuniecie_danych3()
			usuniecie_danych5()
			usun_rank()
			usun_rank_abc()
			usun_rank_atlas()
			info_napis.config(text="Usunięto punktację gier:\n\n'A, B, czy C?', 'Stolice' oraz 'Atlas'!")

			def powrotI():
				okno_info.quit()
				okno_info.destroy()

			ramka.destroy()
			powrot_info3=Button(okno_info,text='Zamknij',command=powrotI, font=('Arial',12))
			powrot_info3.pack(pady=15, ipadx=25)

		powrot_info1=Button(ramka,width=15,text='Tak, usuń dane!',command=powrot_infoF,\
font=('Arial black',10),bg='red',fg='white')
		powrot_info1.pack(side='left',padx=15, ipadx=15)

		powrot_info2=Button(ramka,width=15,text='Nie, powróć do menu',command=powrotN,\
font=('Arial black',10),bg='light green',fg='white')
		powrot_info2.pack(side='right',padx=15, ipadx=15)



		okno_info.mainloop()





# GUZIK 4 FUNKCJA:


	def MenuGuzik4():
		okno_info=Tk()
		okno_info.geometry('280x180')
		okno_info.title('M93.pl')
		info_napis=Label(okno_info,padx=20, text='Programik stworzony przez:\n\nM93.pl\
\n\nw języku Python\n(c) 2024', font=('Arial',12))
		info_napis.pack()


		def powrot_infoF():
			okno_info.quit()
			okno_info.destroy()
		powrot_info=Button(okno_info,text='OK',command=powrot_infoF, font=('Arial',12))
		powrot_info.pack(pady=15, ipadx=25)
		okno_info.mainloop()






# WIZUALIZACJA GUZIKÓW W MENU:


	menu_guzik1=Button(okno_menu1,command=MenuGuzik1,width=20, text="Zmiana nazwy użytkownika",\
		font=("Arial",14))
	menu_guzik2=Button(okno_menu1,command=MenuGuzik2,width=20, text="Najlepsze wyniki",\
		font=("Arial",14))
	menu_guzik3=Button(okno_menu1,command=MenuGuzik3,width=20, text='Reset punktacji',\
		font=("Arial",14))
	menu_guzik4=Button(okno_menu1,command=MenuGuzik4,width=20, text='Informacje o programie',\
		font=("Arial",14))


	menu_guzik1.pack(pady=15)
	menu_guzik2.pack(pady=15)
	menu_guzik3.pack(pady=15)
	menu_guzik4.pack(pady=15)





		




# PĘTLA OKNA I WYJŚCIE Z OKNA

	def powrot():
		okno_menu1.destroy()
		okno.deiconify()

	zamknij=Button(okno_menu1,text='Powrót do menu', borderwidth=4, command=powrot,\
		font=("Arial",18))
	zamknij.pack(padx=15,pady=15,side='bottom')
	okno_menu1.mainloop()








