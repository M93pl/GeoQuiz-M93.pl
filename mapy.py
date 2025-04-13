from os import system
from random import *
from wyniki import ustal_rank_atlas
from openpyxl import Workbook, load_workbook
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from wejscie_wyjscie import *

# napisy 	'#267c8d'
# tlo 		'#8ac4cf'
# ciemny	'#10424c'
# logo 		'768x512'
# zdj		'600(900-600)x400(wysokość maks 400)'

def mapa(oknox): #(okno_stare)
	# funkcja glowna quizu atlas
	oknox.withdraw()
	okno_atlas=Toplevel()
	okno_atlas.focus_force()
	okno_atlas.geometry('1000x700')
	okno_atlas.resizable(False, False)
	okno_atlas.title('Atlas')
	okno_atlas.config(bg='#8ac4cf')

	rama_tytul=Frame(okno_atlas,bg='#8ac4cf',borderwidth=0)
	rama_tytul.pack(padx=10,pady=5)

	class pytania:
	# klasa pytan
		def __init__(self, mapa, pytanie, odpowiedzi, prawidlowa, punkty, ciekawostka):
			self.mapa=mapa
			self.pytanie=pytanie
			self.odpowiedzi=odpowiedzi
			self.prawidlowa=prawidlowa
			self.punkty=punkty
			self.ciekawostka=ciekawostka



	# rodzaje pytan
	pyt1_flaga='Jakiego kraju to flaga?'
	pyt2_miasto='Jakie miasto przedstawia to zdjęcie?'
	pyt3_obiekt='Gdzie znajduje się to miejsce?'
	pyt4_mapa='Co znajduje się na tej mapie?'
	pyt5_satelita='Co to za miejsce?'

	# IMPORT OBRAZÓW 	#	 	#	 	# 		#
	



	obraz1=ImageTk.PhotoImage(Image.open('images/mapy/m1.png'))
	mapa1=pytania(obraz1,pyt4_mapa,['Czechy','Austria','Rumunia','Węgry'],'Węgry',2,\
		None)

	obraz2=ImageTk.PhotoImage(Image.open('images/mapy/m2.png'))
	mapa2=pytania(obraz2,pyt1_flaga,['Andory','Indonezji','Monako','Polski'],'Monako',2,\
		'Flagi Monako i Indonezji różnią się\njedynie odcieniem czerwieni oraz szerokością.')

	obraz3=ImageTk.PhotoImage(Image.open('images/mapy/m3.png'))
	mapa3=pytania(obraz3,pyt5_satelita,['Akropol','Plac Czerwony','Koloseum','Forum Romanum'],'Akropol',3,\
		'Znajdujący się na Ateńskim wzniesieniu Akropol,\nw swojej nazwie zawiera dwa słowa\n"akros" - czyli "najwyższy".')

	obraz4=ImageTk.PhotoImage(Image.open('images/mapy/m4.png'))
	mapa4=pytania(obraz4,pyt3_obiekt,['w Nowym Jorku','w Londynie','w Paryżu','w Tokio'],'w Londynie',2,\
		'Londyńskie "London Eye" otwarto\npo raz pierwszy\nw 1998 roku.')

	obraz5=ImageTk.PhotoImage(Image.open('images/mapy/m5.png'))
	mapa5=pytania(obraz5,pyt2_miasto,['Madryt','Nowy Jork','Toronto','Los Angeles'],'Los Angeles',2,\
		None)

	obraz6=ImageTk.PhotoImage(Image.open('images/mapy/m6.png'))
	mapa6=pytania(obraz6,pyt4_mapa,['Czechy','Austria','Rumunia','Słowacja'],'Czechy',1,\
		None)

	obraz7=ImageTk.PhotoImage(Image.open('images/mapy/m7.png'))
	mapa7=pytania(obraz7,pyt1_flaga,['Białorusi','Litwy','Estonii','Uzbekistanu'],'Białorusi',2,\
		'Wygląd flagi Białorusi został przyjęty\nw drodze referendum w 1995 roku.')

	obraz8=ImageTk.PhotoImage(Image.open('images/mapy/m8.png'))
	mapa8=pytania(obraz8,pyt2_miasto,['Łódź','Warszawę','Lublin','Poznań'],'Warszawę',1,\
		'Pomnik powstał w związku z budową\nw latach 1851–1855\npierwszego nowoczesnego wodociągu w Warszawie.')

	obraz9=ImageTk.PhotoImage(Image.open('images/mapy/m9.png'))
	mapa9=pytania(obraz9,pyt3_obiekt,['w Norwegii','na Węgrzech','w Szwecji','w Finlandii'],'w Szwecji',3,\
		'Zdjęcie przedstawia\nPałac Królewski w Sztokholmie.')

	obraz10=ImageTk.PhotoImage(Image.open('images/mapy/m10.png'))
	mapa10=pytania(obraz10,pyt4_mapa,['Arizona','Teksas','Floryda','Montana'],'Teksas',2,\
		None)
	obraz11=ImageTk.PhotoImage(Image.open('images/mapy/m11.png'))
	mapa11=pytania(obraz11,pyt5_satelita,['Europa','Afryka','Azja','Australia'],'Australia',1,\
		None)

	obraz12=ImageTk.PhotoImage(Image.open('images/mapy/m12.png'))
	mapa12=pytania(obraz12,pyt4_mapa,['Łódzkie','Mazowieckie','Opolskie','Świętokrzyskie'],'Łódzkie',2,\
		None)

	obraz13=ImageTk.PhotoImage(Image.open('images/mapy/m13.png'))
	mapa13=pytania(obraz13,pyt4_mapa,['Iran','Izrael','Afganistan','Irak'],'Irak',2,\
		'Stolicą Iraku jest\nBagdad')

	obraz14=ImageTk.PhotoImage(Image.open('images/mapy/m14.png'))
	mapa14=pytania(obraz14,pyt3_obiekt,['w Chinach','w Australii','w Nowej Zelandii','w Indiach'],'w Chinach',3,\
		'Są to Góry Południowochińskie.')

	obraz15=ImageTk.PhotoImage(Image.open('images/mapy/m15.png'))
	mapa15=pytania(obraz15,pyt3_obiekt,['Rzym','Ateny','Florencja','Bolonia'],'Rzym',2,\
		None)

	obraz16=ImageTk.PhotoImage(Image.open('images/mapy/m16.png'))
	mapa16=pytania(obraz16,pyt4_mapa,['Turcja','Grecja','Armenia','Syria'],'Turcja',2,\
		'Republika Turcji została proklamowana w 1923 roku,\npoprzedzającym ją państwem było Imperium Osmańskie.')

	obraz17=ImageTk.PhotoImage(Image.open('images/mapy/m17.png'))
	mapa17=pytania(obraz17,pyt4_mapa,['Szwajcaria','Luksemburg','Holandia','Belgia'],'Belgia',2,\
		None)

	obraz18=ImageTk.PhotoImage(Image.open('images/mapy/m18.png'))
	mapa18=pytania(obraz18,pyt4_mapa,['Czad','Egipt','Algieria','Libia'],'Libia',2,\
		None)

	obraz19=ImageTk.PhotoImage(Image.open('images/mapy/m19.png'))
	mapa19=pytania(obraz19,pyt4_mapa,['Katar','Irak','Iran','Pakistan'],'Pakistan',3,\
		None)

	obraz20=ImageTk.PhotoImage(Image.open('images/mapy/m20.png'))
	mapa20=pytania(obraz20,pyt4_mapa,['Gabon','RPA','Kenia','Angola'],'Angola',3,\
		None)
	
	obraz21=ImageTk.PhotoImage(Image.open('images/mapy/m21.png'))
	mapa21=pytania(obraz21,pyt5_satelita,['półwysep Apeniński','półwysep Indyjski','półwysep Tajmyr','półwysep Iberyjski'],'półwysep Iberyjski',1,\
		None)

	obraz22=ImageTk.PhotoImage(Image.open('images/mapy/m22.png'))
	mapa22=pytania(obraz22,pyt5_satelita,['Sardynię','Sycylię','Korsykę','Madagaskar'],'Madagaskar',2,\
		None)

	obraz23=ImageTk.PhotoImage(Image.open('images/mapy/m23.png'))
	mapa23=pytania(obraz23,pyt5_satelita,['półwysep Iberyjski','Australię','Afrykę','półwysep Arabski'],'półwysep Arabski',1,\
		None)
	
	obraz24=ImageTk.PhotoImage(Image.open('images/mapy/m24.png'))
	mapa24=pytania(obraz24,pyt5_satelita,['Mamry','Bajkał','Wigry','Śniardwy'],'Śniardwy',2,\
		'Śniardwy to największe z polskich jezior.')

	obraz25=ImageTk.PhotoImage(Image.open('images/mapy/m25.png'))
	mapa25=pytania(obraz25,pyt3_obiekt,['w Los Angeles','w Turynie','w Meksyku','w Rio de Janeiro'],'w Rio de Janeiro',3,\
		'Zdjęcie przedstawia słynną "Maracanę".')

	obraz26=ImageTk.PhotoImage(Image.open('images/mapy/m26.png'))
	mapa26=pytania(obraz26,pyt3_obiekt,['w Meksyku','na pustynii Gobi','na Saharze','w Arizonie'],'w Arizonie',3,\
		None)
	
	obraz27=ImageTk.PhotoImage(Image.open('images/mapy/m27.png'))
	mapa27=pytania(obraz27,pyt3_obiekt,['w Neapolu','we Florencji','w Wenecji','w Bolonii'],'w Bolonii',3,\
		None)

	obraz28=ImageTk.PhotoImage(Image.open('images/mapy/m28.png'))
	mapa28=pytania(obraz28,pyt1_flaga,['Indie','Australia','RPA','Argentyna'],'Argentyna',2,\
		None)

	obraz29=ImageTk.PhotoImage(Image.open('images/mapy/m29.png'))
	mapa29=pytania(obraz29,pyt1_flaga,['Mongolia','Tadżykistan','Kirgistan','Azerbejdżan'],'Azerbejdżan',3,\
		None)
	
	obraz30=ImageTk.PhotoImage(Image.open('images/mapy/m30.png'))
	mapa30=pytania(obraz30,pyt1_flaga,['Gwinea','Portoryko','Barbados','Belize'],'Belize',3,\
		None)
	
	obraz31=ImageTk.PhotoImage(Image.open('images/mapy/m31.png'))
	mapa31=pytania(obraz31,pyt1_flaga,['Boliwia','Argentyna','Teksas','Chile'],'Chile',3,\
		'Flaga stanu Teksas bardzo przypomina flagę Chile.')
	
	obraz32=ImageTk.PhotoImage(Image.open('images/mapy/m32.png'))
	mapa32=pytania(obraz32,pyt1_flaga,['Wiedeń','Lizbona','Wrocław','Monachium'],'Monachium',3,\
		None)
	
	obraz33=ImageTk.PhotoImage(Image.open('images/mapy/m33.png'))
	mapa33=pytania(obraz33,pyt1_flaga,['Kiribati','Kolumbia','Wenezuela','Ekwador'],'Ekwador',3,\
		None)
	
	obraz34=ImageTk.PhotoImage(Image.open('images/mapy/m34.png'))
	mapa34=pytania(obraz34,pyt1_flaga,['Dania','Norwegia','Szwecja','Finlanida'],'Finlanida',2,\
		None)
	
	obraz35=ImageTk.PhotoImage(Image.open('images/mapy/m35.png'))
	mapa35=pytania(obraz35,pyt1_flaga,['Syria','Cypr','Turcja','Grecja'],'Grecja',1,\
		None)
	
	obraz36=ImageTk.PhotoImage(Image.open('images/mapy/m36.png'))
	mapa36=pytania(obraz36,pyt1_flaga,['Austria','Szwajcaria','Francja','Włochy'],'Włochy',1,\
		None)
	
	obraz37=ImageTk.PhotoImage(Image.open('images/mapy/m37.png'))
	mapa37=pytania(obraz37,pyt1_flaga,['Andora','Macedonia','Holandia','Luksemburg'],'Luksemburg',2,\
		None)
	
	obraz38=ImageTk.PhotoImage(Image.open('images/mapy/m38.png'))
	mapa38=pytania(obraz38,pyt1_flaga,['Somalia','Erytea','Czad','Mali'],'Mali',3,\
		None)
	
	obraz39=ImageTk.PhotoImage(Image.open('images/mapy/m39.png'))
	mapa39=pytania(obraz39,pyt1_flaga,['Uzbekistan','Kirgistan','Tybet','Nepal'],'Nepal',2,\
		'To jedyna flaga na świecie która nie jest prostokątem.')
	
	obraz40=ImageTk.PhotoImage(Image.open('images/mapy/m40.png'))
	mapa40=pytania(obraz40,pyt1_flaga,['Hawaje','Tasmania','Seszele','Papua-Nowa Gwinea'],'Papua-Nowa Gwinea',3,\
		None)
	
	obraz41=ImageTk.PhotoImage(Image.open('images/mapy/m41.png'))
	mapa41=pytania(obraz41,pyt1_flaga,['ZEA','Jemen','Irak','Katar'],'Katar',3,\
		'Flaga Kataru ma inne proporcje niż większość flag świata.')
	
	obraz42=ImageTk.PhotoImage(Image.open('images/mapy/m42.png'))
	mapa42=pytania(obraz42,pyt1_flaga,['Mołdawia','Turcja','Bułgaria','Rumunia'],'Rumunia',2,\
		None)
	
	obraz43=ImageTk.PhotoImage(Image.open('images/mapy/m43.png'))
	mapa43=pytania(obraz43,pyt1_flaga,['Katar','Bahrain','Libia','Arabia Saudyjska'],'Arabia Saudyjska',3,\
		None)
	
	obraz44=ImageTk.PhotoImage(Image.open('images/mapy/m44.png'))
	mapa44=pytania(obraz44,pyt1_flaga,['Kosowo','Jugosławia','Chorwacja','Serbia'],'Serbia',2,\
		None)
	
	obraz45=ImageTk.PhotoImage(Image.open('images/mapy/m45.png'))
	mapa45=pytania(obraz45,pyt1_flaga,['Meksyk','Kostaryka','Portugalia','Hiszpania'],'Hiszpania',1,\
		None)
	
	obraz46=ImageTk.PhotoImage(Image.open('images/mapy/m46.png'))
	mapa46=pytania(obraz46,pyt1_flaga,['Oman','Iran','Irak','Sudan'],'Sudan',3,\
		None)
	
	obraz47=ImageTk.PhotoImage(Image.open('images/mapy/m47.png'))
	mapa47=pytania(obraz47,pyt1_flaga,['Islandia','Norwegia','Finlandia','Szwecja'],'Szwecja',2,\
		None)
	
	obraz48=ImageTk.PhotoImage(Image.open('images/mapy/m48.png'))
	mapa48=pytania(obraz48,pyt1_flaga,['Singapur','Egipt','Portugalia','Tajlandia'],'Tajlandia',3,\
		None)
	
	obraz49=ImageTk.PhotoImage(Image.open('images/mapy/m49.png'))
	mapa49=pytania(obraz49,pyt1_flaga,['Belize','Seszele','Kuba','Bahamy'],'Bahamy',3,\
		None)

	obraz50=ImageTk.PhotoImage(Image.open('images/mapy/m50.png'))
	mapa50=pytania(obraz50,pyt1_flaga,['Dania','Luksemburg','Belgia','Holandia'],'Holandia',1,\
		None)

	obraz51=ImageTk.PhotoImage(Image.open('images/mapy/m51.png'))
	mapa51=pytania(obraz51,pyt1_flaga,['Surinam','Wietnam','Rosja','Chiny'],'Chiny',2,\
		'Chiny to druge najludniejsze państwo świata,\nzaraz po Indiach.')

	obraz52=ImageTk.PhotoImage(Image.open('images/mapy/m52.png'))
	mapa52=pytania(obraz52,pyt1_flaga,['Tajlandia','Laos','Chiny','Tajwan'],'Tajwan',3,\
		'Inna nazwa Tajwanu to Republika Chińska.')

	obraz53=ImageTk.PhotoImage(Image.open('images/mapy/m53.png'))
	mapa53=pytania(obraz53,pyt1_flaga,['Macedonia','Mołdawia','Słowacja','Ukraina'],'Ukraina',1,\
		None)

	obraz54=ImageTk.PhotoImage(Image.open('images/mapy/m54.png'))
	mapa54=pytania(obraz54,pyt1_flaga,['Chiny','Kambodża','Laos','Wietnam'],'Wietnam',3,\
		None)

	obraz55=ImageTk.PhotoImage(Image.open('images/mapy/m55.png'))
	mapa55=pytania(obraz55,pyt1_flaga,['Izrael','Jemen','Oman','USA'],'Izrael',2,\
		None)

	obraz56=ImageTk.PhotoImage(Image.open('images/mapy/m56.png'))
	mapa56=pytania(obraz56,pyt2_miasto,['Sevilla','Lyon','Paryż','Madryt'],'Madryt',3,\
		'Jest to ratusz w Madrycie')

	obraz57=ImageTk.PhotoImage(Image.open('images/mapy/m57.png'))
	mapa57=pytania(obraz57,pyt2_miasto,['Pretoria','Budapeszt','Bukareszt','Bogota'],'Pretoria',3,\
		'Budynki Unii stanowią oficjalną siedzibę rządu RPA,\nmieszczą także biura Prezydenta.')

	obraz58=ImageTk.PhotoImage(Image.open('images/mapy/m58.png'))
	mapa58=pytania(obraz58,pyt3_obiekt,['na Ukrainie','we Francji','w Hiszpanii','w Nowej Zelandii'],'we Francji',3,\
		'Park Narodowy Pirenejów położony jest\nw południowej Francji')

	obraz59=ImageTk.PhotoImage(Image.open('images/mapy/m59.png'))
	mapa59=pytania(obraz59,pyt2_miasto,['Astanę','Moskwę','Pekin','Tokio'],'Astana',3,\
		'W 2019 roku kazachski parlament zmienił nazwę stolicy na Nur-Sułtan.\nPo przeszło 3 latach, przywrócono poprzednią nazwę – Astana.')

	obraz60=ImageTk.PhotoImage(Image.open('images/mapy/m60.png'))
	mapa60=pytania(obraz60,pyt4_mapa,['Urugwaj','Honduras','Argentyna','Brazylia'],'Brazylia',2,\
		None)


	'''
	PROBNIK:

	obraz=ImageTk.PhotoImage(Image.open('images/mapy/m.png'))
	mapa=pytania(obraz,pyt,['','','',''],'',,\
		None)
	'''

	lista_map=[mapa1,mapa2,mapa3,mapa4,mapa5,mapa6,mapa7,mapa8,mapa9,mapa10,\
	mapa11,mapa12,mapa13,mapa14,mapa15,mapa16,mapa17,mapa18,mapa19,mapa20,\
	mapa21,mapa22,mapa23,mapa24,mapa25,mapa26,mapa27,mapa28,mapa29,mapa30,\
	mapa31,mapa32,mapa33,mapa34,mapa35,mapa36,mapa37,mapa38,mapa39,mapa40,\
	mapa41,mapa42,mapa43,mapa44,mapa45,mapa46,mapa47,mapa48,mapa49,mapa50,\
	mapa51,mapa52,mapa53,mapa54,mapa55,mapa56,mapa57,mapa58,mapa59,mapa60]
	#	#		#		#		#		#		#


	# radiobuttony
	style=ttk.Style()
	style.configure("S1.Toolbutton",padding=(15,15), font=('Arial',14, 'bold'),foreground='#10424c',background='#8ac4cf')
	style.configure("S2.Toolbutton",padding=(15,15), font=('Arial',14, 'bold'),foreground='green',background='#8ac4cf')

	global count
	global pkt
	global pktMax
	count=0
	pkt=0
	pktMax=0
	def start(x):
		# petla quizu
		global count
		global pkt
		global pktMax
		count+=1

		if count<11:
			x.destroy()
			guz_start.destroy()
			# ramka pytan 	#	#
			rama_tytul=Frame(okno_atlas,bg='#8ac4cf')
			rama_tytul.pack(padx=10,pady=10)
			#	#	#	#	#	#


			pytanieLos=choice(lista_map)
			shuffle(pytanieLos.odpowiedzi)

			obraz_Pytanie=Label(rama_tytul,image=pytanieLos.mapa,bg='#8ac4cf')
			obraz_Pytanie.grid(row=2, column=1,columnspan=4,pady=(0,10))

			punktacja=Label(rama_tytul,text=f'Pytanie za {pytanieLos.punkty} pkt.',\
				font=('arial', 16),fg='white',bg='#8ac4cf')
			punktacja.grid(row=0, column=1,columnspan=4)

			pytanie=Label(rama_tytul,text=f'{pytanieLos.pytanie}',\
				font=('arial', 25,'bold'),fg='white',bg='#8ac4cf')
			pytanie.grid(row=1, column=1,columnspan=4)


			def activate():
				# aktywowanie guzika sprawdzenia
				sprawdz.config(state='active',fg='white',bg='#267c8d')

			# wartosc wybrana z radiobuttonow
			odp=StringVar()

			opcjaA=ttk.Radiobutton(rama_tytul,style='S1.Toolbutton',command=activate,\
				text=pytanieLos.odpowiedzi[0], variable=odp,value=pytanieLos.odpowiedzi[0])
			opcjaA.grid(row=3,column=1,padx=10)

			opcjaB=ttk.Radiobutton(rama_tytul,style='S1.Toolbutton',command=activate,\
				text=pytanieLos.odpowiedzi[1], variable=odp,value=pytanieLos.odpowiedzi[1])
			opcjaB.grid(row=3,column=2,padx=10)

			opcjaC=ttk.Radiobutton(rama_tytul,style='S1.Toolbutton',command=activate,\
				text=pytanieLos.odpowiedzi[2], variable=odp,value=pytanieLos.odpowiedzi[2])
			opcjaC.grid(row=3,column=3,padx=10)

			opcjaD=ttk.Radiobutton(rama_tytul,style='S1.Toolbutton',command=activate,\
				text=pytanieLos.odpowiedzi[3], variable=odp,value=pytanieLos.odpowiedzi[3])
			opcjaD.grid(row=3,column=4,padx=10)


			dobrze=choice(['Prawidłowo!','Zgadza się!','Tak!','Brawo!','Dobrze!',\
					'Świetnie!', 'Doskonale!', 'Rewelacyjnie!', 'Fantastycznie!', 'Super!',\
					'Bezapelacyjnie!', 'Oczywiście!', 'Jasne!', 'Absolutnie tak!',\
					'Bez wątpienia!', 'Okej!', 'Nieźle!'])
			zle=choice(['Źle!','Odpowiedź nieprawidłowa!','Nie!',\
					'Niestety nie.', 'Błąd :/', 'Pudło...', 'Niestety, to nie to :(', 'Nie tym razem.'])


			def sprawdzam():
			# sprawdzenie warunkowosci
				global pkt
				global pktMax
				# zmiana guzika na koncu gry
				if count<10:
					sprawdz.config(state='active',text='Następne pytanie',\
					command=lambda:start(rama_tytul))
				elif count==10:
					sprawdz.config(state='active',text='Zakończ grę!',\
					command=lambda:start(rama_tytul))					
				lista_map.remove(pytanieLos)

				# poprawna odpowiedz na zielono
				if pytanieLos.odpowiedzi[0]==pytanieLos.prawidlowa:
					opcjaA.config(style='S2.Toolbutton')
				elif pytanieLos.odpowiedzi[1]==pytanieLos.prawidlowa:
					opcjaB.config(style='S2.Toolbutton')
				elif pytanieLos.odpowiedzi[2]==pytanieLos.prawidlowa:
					opcjaC.config(style='S2.Toolbutton')
				elif pytanieLos.odpowiedzi[3]==pytanieLos.prawidlowa:
					opcjaD.config(style='S2.Toolbutton')


				if odp.get()==pytanieLos.prawidlowa:
					pytanie.config(text=f'{dobrze}',fg='green')
					obraz_Pytanie.config(bg='green')
					pkt+=pytanieLos.punkty
					ciekawostka_napis=Label(rama_tytul,text=f'{pytanieLos.ciekawostka}',\
					font=('arial', 28,'bold'),fg='white',bg='green')
					punktacja.config(fg='green')
					pktMax+=pytanieLos.punkty

				elif odp.get()!=pytanieLos.prawidlowa:
					pytanie.config(text=f'{zle}',fg='red')
					obraz_Pytanie.config(bg='red')
					ciekawostka_napis=Label(rama_tytul,text=f'{pytanieLos.ciekawostka}',\
					font=('arial', 28,'bold'),fg='white',bg='red')
					punktacja.config(fg='red')
					pktMax+=pytanieLos.punkty

				if pytanieLos.ciekawostka != None:
					ciekawostka_napis.grid(row=2, column=1,columnspan=4,pady=(0,10))


			sprawdz=Button(rama_tytul,text='Sprawdź!', state='disabled',activebackground='#267c8d',activeforeground='white',\
				borderwidth=4,command=sprawdzam, font=("Arial",18),fg='white',bg='#8ac4cf')
			sprawdz.grid(row=4, column=1, columnspan=4,pady=10)

		elif count==11:
			x.destroy()
			rama_tytul=Frame(okno_atlas,bg='#8ac4cf')
			rama_tytul.pack(padx=10,pady=10)

			# wyswietlanie wynikow gry
			if pkt>=5 or pkt==0:
				wynik=Label(okno_atlas, text=f'Zdobywasz {pkt} punktów\nna {pktMax} możliwych!',\
					bg='#8ac4cf', fg='white',font=('arial', 36))
			elif 1<pkt<5:
					wynik=Label(okno_atlas, text=f'Zdobywasz {pkt} punkty\nna {pktMax} możliwych!',\
					bg='#8ac4cf', fg='white',font=('arial', 36))
			elif pkt==1:
					wynik=Label(okno_atlas, text=f'Zdobywasz {pkt} punkt\nna {pktMax} możliwych!',\
					bg='#8ac4cf', fg='white',font=('arial', 36))
			wynik.pack()

			#obliczenia i wyswietlanie rezultatu w procentach
			procentowy=(pkt/pktMax)*100
			proc=round(procentowy,2)
			podsumowanie=Label(okno_atlas, text=f'Osiągasz {proc}% poprawnych odpowiedzi!',\
				bg='#8ac4cf', fg='green',font=('arial', 34, 'bold'))
			podsumowanie.pack(pady=22)

			# wyswietlanie najlepszych wynikow
			ustal_rank_atlas(proc)
			baza_danych=load_workbook('baza.xlsx')
			arkusz=baza_danych.active
			podsumowanie2=Label(okno_atlas,text=f"Najlepsze wyniki gry 'Atlas':\n\n\
1. {arkusz['B29'].value}   {arkusz['A29'].value}%\n\
2. {arkusz['B30'].value}   {arkusz['A30'].value}%\n\
3. {arkusz['B31'].value}   {arkusz['A31'].value}%\n\
4. {arkusz['B32'].value}   {arkusz['A32'].value}%\n\
5. {arkusz['B33'].value}   {arkusz['A33'].value}%",\
			bg='#8ac4cf', fg='white',font=('arial', 24))
			podsumowanie2.pack(pady=(35,0))


	# logotyp
	obraz_tytulowy=ImageTk.PhotoImage(Image.open('images/atlaslogo.jpg'))
	obraz_tytul=Label(rama_tytul,image=obraz_tytulowy,bg='#8ac4cf')
	obraz_tytul.grid(row=2, column=1,padx=116)
	# tytul
	napis_tytul=Label(rama_tytul,text='ATLAS',font=('arial', 55,'bold'),fg='white',bg='#8ac4cf')
	napis_tytul.grid(row=1, column=1)

	guz_start=Button(okno_atlas,text='Zaczynamy',width=30,command=lambda:start(rama_tytul),\
		borderwidth=4, font=("Arial",18),fg='white',bg='#267c8d')
	guz_start.place(x=300, y=550)



	def back():
		# powrot do menu
		oknox.deiconify()
		okno_atlas.destroy()
	guz_back=Button(okno_atlas,text='Powrót do menu', borderwidth=4, command=back, font=("Arial",18))
	guz_back.pack(side='bottom',pady=12)

	def close():
		# zamkniecie programu
		okno_atlas.destroy()
		oknox.destroy()
	okno_atlas.protocol("WM_DELETE_WINDOW", close)

	okno_atlas.mainloop()
























