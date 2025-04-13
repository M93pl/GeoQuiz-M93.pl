from wejscie_wyjscie import *
from os import system
from tkinter import *
from random import *

# TWORZENIE OKNA I PODSTAWOWE FUNKCJE

def zagadka_mat(okno):

	okno.withdraw()
	okno_mat=Toplevel()
	okno_mat.focus_set()
	okno_mat.focus_force()
	okno_mat.geometry('500x360')
	okno_mat.resizable(False, False)
	okno_mat.title('Zagadka matematyczna')

	def cls_(nazwa_okna):
		for widgety in nazwa_okna.winfo_children():
			widgety.pack_forget()

	def cls_bez_zamknij(nazwa_okna, bez_zamknij):
		for widgety in nazwa_okna.winfo_children():
			if widgety is not bez_zamknij:
				widgety.pack_forget()






# FUNKCJE GUZIKÓW:

# ŁATWY:

	def easy():
		cls_bez_zamknij(okno_mat, zamknij)

		okno_info=Tk()
		okno_info.geometry('300x130')
		okno_info.title('Łatwizna')
		mat_e=Label(okno_info,text=f'{wyjscie_danych1()}, nie lubisz się przemęczać co?', font=("Arial",12))
		mat_e.pack(pady=15)
		def powrot_infoF():
			okno_info.quit()
			okno_info.destroy()
		powrot_info=Button(okno_info,text='Zaczynajmy!',command=powrot_infoF, font=("Arial",18))
		powrot_info.pack(pady=5, ipadx=15)
		okno_info.mainloop()

		def petla():
			cls_bez_zamknij(okno_mat, zamknij)
			l1=randrange(1,51)
			l2=randrange(1,51)
			mat_easy=Label(okno_mat,text=f'Ile wynosi suma liczb:\n{l1} i {l2}?', font=("Arial",12))
			mat_easy.pack(pady=11)
			odp_1=l1+l2
			odpowiedz_uzytkownika=Entry(okno_mat, width=25, font=('Arial', 16),justify="center")
			odpowiedz_uzytkownika.pack(pady=5)

			def odpowiedzUzytkownika():
				x=odpowiedz_uzytkownika.get()
				odpowiedz_button.config(state='disabled')
				tak=choice(['Prawidłowo!','Zgadza się!','Tak!','Brawo!','Dobrze!'])
				nie=choice(['Źle!','Odpowiedź nieprawidłowa!','Nie!'])

				if str(x)==str(odp_1):
					mat_eas=Label(okno_mat,text=f'{tak}\nPoprawna odpowiedź!',fg='green', font=("Arial",12)).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)

				else:
					mat_eas=Label(okno_mat,text=f'{nie}\nPoprawna odpowiedź to: {odp_1}!', fg='red', font=55).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)
			
			odpowiedz_button=Button(okno_mat,text='Sprawdź!',command=odpowiedzUzytkownika, font=("Arial",18))
			odpowiedz_button.pack(pady=5)

		petla()






# ŚREDNI

	def medium():
		cls_bez_zamknij(okno_mat, zamknij)

		okno_info=Tk()
		okno_info.geometry('350x130')
		okno_info.title('Średniak')
		mat_e=Label(okno_info,text=f'Wybrano poziom dla średniozaawansowanych.', font=("Arial",12))
		mat_e.pack(pady=15)
		def powrot_infoF():
			okno_info.quit()
			okno_info.destroy()
		powrot_info=Button(okno_info,text='Zaczynajmy!',command=powrot_infoF, font=("Arial",12))
		powrot_info.pack(pady=5, ipadx=15)
		okno_info.mainloop()

		def petla():
			cls_bez_zamknij(okno_mat, zamknij)
			lx=[0,1,2,3,4,5,10,100]
			l1=choice(lx)
			l2=randrange(2,4)
			mat_easy=Label(okno_mat,text=f'Ile wynosi\n{l1} podniesione do potęgi {l2}?', font=("Arial",12))
			mat_easy.pack(pady=11)
			odp_1=l1**l2
			odpowiedz_uzytkownika=Entry(okno_mat, width=25, font=('Arial', 16),justify="center")
			odpowiedz_uzytkownika.pack(pady=5)

			def odpowiedzUzytkownika():
				x=odpowiedz_uzytkownika.get()
				odpowiedz_button.config(state='disabled')
				tak=choice(['Prawidłowo!','Zgadza się!','Tak!','Brawo!','Dobrze!'])
				nie=choice(['Źle!','Odpowiedź nieprawidłowa!','Nie!'])

				if str(x)==str(odp_1):
					mat_eas=Label(okno_mat,text=f'{tak}\nPoprawna odpowiedź!',fg='green', font=("Arial",12)).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)

				else:
					mat_eas=Label(okno_mat,text=f'{nie}\nPoprawna odpowiedź to: {odp_1}!', fg='red', font=("Arial",12)).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)
			
			odpowiedz_button=Button(okno_mat,text='Sprawdź!',command=odpowiedzUzytkownika, font=("Arial",18))
			odpowiedz_button.pack(pady=5)

		petla()





# TRUDNY

	def hard():
		cls_bez_zamknij(okno_mat, zamknij)

		okno_info=Tk()
		okno_info.geometry('300x130')
		okno_info.title('Dla wymagających')
		mat_e=Label(okno_info,text=f'Dobrze Cię tu widzieć {wyjscie_danych1()},\nwybrano najtrudniejsze z zadań!', font=("Arial",12))
		mat_e.pack(pady=15)
		def powrot_infoF():
			okno_info.quit()
			okno_info.destroy()
		powrot_info=Button(okno_info,text='Zaczynajmy!',command=powrot_infoF, font=("Arial",12))
		powrot_info.pack(pady=5, ipadx=15)
		okno_info.mainloop()

		def petla():
			cls_bez_zamknij(okno_mat, zamknij)
			hx=randrange(1,6)
			hy=randrange(1,6)
			hz=randrange(2,4)
			hv=randrange(1,10)
			hp=randrange(1,4)

			if hp==2:
				mat_easy=Label(okno_mat,text=f'Jaki jest wynik poniższego działania:\
({str(hx)} + {str(hy)}) * {str(hz)} - {str(hv)}\npodniesiony do potęgi drugiej?', font=("Arial",12))
				mat_easy.pack(pady=11)

			elif hp==1:
				mat_easy=Label(okno_mat,text=f'Jaki jest wynik poniższego działania:\
({str(hx)} + {str(hy)}) * {str(hz)} - {str(hv)}\npodniesiony do potęgi pierwszej?', font=("Arial",12))
				mat_easy.pack(pady=11)

			else:
				mat_easy=Label(okno_mat,text=f'Jaki jest wynik poniższego działania:\
({str(hx)} + {str(hy)}) * {str(hz)} - {str(hv)}\npodniesiony do potęgi trzeciej?\n', font=("Arial",12))
				mat_easy.pack(pady=7)

			odp_1=((hx+hy)*hz-hv)**hp
			odpowiedz_uzytkownika=Entry(okno_mat, width=25, font=('Arial', 16),justify="center")
			odpowiedz_uzytkownika.pack(pady=5)

			def odpowiedzUzytkownika():
				x=odpowiedz_uzytkownika.get()
				odpowiedz_button.config(state='disabled')
				tak=choice(['Prawidłowo!','Zgadza się!','Tak!','Brawo!','Dobrze!'])
				nie=choice(['Źle!','Odpowiedź nieprawidłowa!','Nie!'])

				if str(x)==str(odp_1):
					mat_eas=Label(okno_mat,text=f'{tak}\nPoprawna odpowiedź!',fg='green', font=("Arial",12)).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)

				else:
					mat_eas=Label(okno_mat,text=f'{nie}\nPoprawna odpowiedź to: {odp_1}!', fg='red', font=("Arial",12)).pack(pady=10)
					mat_easnext=Button(okno_mat,text=f'Jeszcze raz', font=("Arial",12), command=petla).pack(pady=5)
			
			odpowiedz_button=Button(okno_mat,text='Sprawdź!',command=odpowiedzUzytkownika,font=("Arial",16))
			odpowiedz_button.pack(pady=5)

		petla()





# WIZUALIZACJA GUZIKÓW W MENU:



	mat_powitanie=Label(okno_mat,text=f'Wybierz poziom trudności zadania:', font=("Arial",18))
	mat_powitanie.pack(pady=15)

	mat_easy=Button(okno_mat,text='Łatwizna',width=10,command=easy,bg='light green',font=('Arial Black',18)).pack(pady=5)

	mat_medium=Button(okno_mat,text='Średniak',width=10,command=medium,bg='light yellow',font=('Arial Black',18)).pack(pady=5)

	mat_hard=Button(okno_mat,text='Trudne',width=10,command=hard,bg='pink',font=('Arial Black',18)).pack(pady=5)





# PĘTLA OKNA I WYJŚCIE Z OKNA


	def powrot():
		okno_mat.destroy()
		okno.deiconify()

	zamknij=Button(okno_mat,text='Powrót do menu', borderwidth=4, command=powrot, font=("Arial",18))
	zamknij.pack(padx=15,pady=15,side='bottom')
	okno_mat.mainloop()


