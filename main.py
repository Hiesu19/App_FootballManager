import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivy.lang import Builder


from modun import *






class DemoApp(MDApp):
	top_ping = ""

	tien_sanbong = 0
	tien_thang = 0
	tien_thua = 0
	tien_quy = 0

	txt_thang = ""
	txt_thua = ""
	txt_quy = ""
	txt_tien_sanbong = ""

	left_c = []
	right_c = []

	money_left = 0
	money_right = 0

	tien_thu_duoc_left = 0
	tien_thu_duoc_right = 0

	tien_thu_duoc_all = 0


	def checkbox_click(self , instance , value , topping):
		DemoApp.top_ping = topping
		if value ==False:
			DemoApp.top_ping = "Not"

	def build(self):
		self.theme_cls.primary_palette = 'Blue'
		return Builder.load_file('demo.kv')

	def  press_tinhtien(self):
		try:

			tiensan = self.root.ids.tiensan.text
			winer = self.root.ids.winer.text
			loser = self.root.ids.loser.text

			a,b,c = chiatien(int(tiensan) , DemoApp.top_ping , int(winer) , int(loser))
			DemoApp.tien_sanbong = tiensan
			DemoApp.tien_thang = a
			DemoApp.tien_thua = b
			DemoApp.tien_quy = c
			self.root.ids.kq_thang.text = str(int(a)) +"k"
			self.root.ids.kq_thua.text = str(int(b)) +"k"
			self.root.ids.kq_quy.text = str(int(c)) +"k"
		except Exception as e:
			self.root.ids.kq_thang.text = "-1k"
			self.root.ids.kq_thua.text = "-1k"
			self.root.ids.kq_quy.text = "-1k"
			DemoApp.tien_thang = -1
			DemoApp.tien_thua = -1
			DemoApp.tien_quy = -1

	def press_chianguoi(self):
		try:
			txt1 = self.root.ids.text_in_1.text	
			txt2 = self.root.ids.text_in_2.text	
			h1 = list(set(txt1.split("\n")))
			h2 = list(set(txt2.split("\n")))
			h_c = h1+h2

			h=list(set(h_c))
			for i in h:
				if i == "":
					h.remove(i)

			a_1 , a_2 = chonnguoi(h)
			a_1_text = "\n".join(a_1)
			a_2_text = "\n".join(a_2)
			self.root.ids.text_in_1.text = a_1_text
			self.root.ids.text_in_2.text = a_2_text
		except Exception as e:
			self.ids.text_in_2.text = "ERROR"

	def press_chiadeu(self):
		try:
			txt1 = self.root.ids.text_in_1.text	
			txt2 = self.root.ids.text_in_2.text
			h1 = txt1.split("\n")
			h2 = txt2.split("\n")
			for i in h1:
				if i == "":
					h1.remove(i)
			for j in h2:
				if j == "":
					h2.remove(j)

			a_1 , a_2 = chiadeu(h1 , h2)
			a_1_text = "\n".join(a_1)
			a_2_text = "\n".join(a_2)
			self.root.ids.text_in_1.text = a_1_text
			self.root.ids.text_in_2.text = a_2_text	
		except Exception as e:
			self.ids.text_in_2.text = "ERROR"

	def slider_it(self , *args):
		if int(args[1]) >60:
			DemoApp.money_left = DemoApp.tien_thua
			DemoApp.money_right = DemoApp.txt_thang
			self.root.ids.sld_right.text = "Thắng  " + str(DemoApp.txt_thang) +"k"
			self.root.ids.sld_left.text = "Thua  " + str(DemoApp.txt_thua)+"k"
		elif int(args[1]) <40:
			DemoApp.money_left = DemoApp.tien_thang
			DemoApp.money_right = DemoApp.txt_thua
			self.root.ids.sld_right.text = "Thua  " + str(DemoApp.txt_thua)+"k"
			self.root.ids.sld_left.text = "Thắng  " + str(DemoApp.txt_thang )+"k"					
		else:
			DemoApp.money_left = -1
			DemoApp.money_right = -1
			self.root.ids.sld_right.text = ""
			self.root.ids.sld_left.text = ""

	def import_team(self):
		txt1 = self.root.ids.text_in_1.text	
		txt2 = self.root.ids.text_in_2.text
		h1 = txt1.split("\n")
		h2 = txt2.split("\n")
		for i in h1:
			if i == "":
				h1.remove(i)
		for j in h2:
			if j == "":
				h2.remove(j)

		left_team_import =  list_to_12(h1)
		right_team_import = list_to_12(h2)

		self.root.ids.a1.text = str(left_team_import[0])
		self.root.ids.a2.text = str(left_team_import[1])
		self.root.ids.a3.text = str(left_team_import[2])
		self.root.ids.a4.text = str(left_team_import[3])
		self.root.ids.a5.text = str(left_team_import[4])
		self.root.ids.a6.text = str(left_team_import[5])
		self.root.ids.a7.text = str(left_team_import[6])
		self.root.ids.a8.text = str(left_team_import[7])
		self.root.ids.a9.text = str(left_team_import[8])
		self.root.ids.a10.text = str(left_team_import[9])
		self.root.ids.a11.text = str(left_team_import[10])
		self.root.ids.a12.text = str(left_team_import[11])	

		self.root.ids.b1.text = str(right_team_import[0])
		self.root.ids.b2.text = str(right_team_import[1])
		self.root.ids.b3.text = str(right_team_import[2])
		self.root.ids.b4.text = str(right_team_import[3])
		self.root.ids.b5.text = str(right_team_import[4])
		self.root.ids.b6.text = str(right_team_import[5])
		self.root.ids.b7.text = str(right_team_import[6])
		self.root.ids.b8.text = str(right_team_import[7])
		self.root.ids.b9.text = str(right_team_import[8])
		self.root.ids.b10.text = str(right_team_import[9])
		self.root.ids.b11.text = str(right_team_import[10])
		self.root.ids.b12.text = str(right_team_import[11])

	def import_tien(self):
		DemoApp.txt_tien_sanbong = int(DemoApp.tien_sanbong)
		DemoApp.txt_thang = int(DemoApp.tien_thang)
		DemoApp.txt_thua = int(DemoApp.tien_thua)
		DemoApp.txt_quy = int(DemoApp.tien_quy)

		self.root.ids.txt_ketqua.text ="0/" + str(DemoApp.txt_tien_sanbong) + "k"


	def checkbox_left( self , instance , value ):
		try:
			if value:
				DemoApp.left_c.append(value)
				DemoApp.tien_thu_duoc_left = int(DemoApp.money_left)*dem_true_false(DemoApp.left_c)
				DemoApp.tien_thu_duoc_right = int(DemoApp.money_right)*dem_true_false(DemoApp.right_c)
				DemoApp.tien_thu_duoc_all = DemoApp.tien_thu_duoc_left + DemoApp.tien_thu_duoc_right
				self.root.ids.txt_ketqua.text =str(DemoApp.tien_thu_duoc_all) + "/" +str(DemoApp.txt_tien_sanbong) + "k"
			else:
				DemoApp.left_c.append(value)
				DemoApp.tien_thu_duoc_left = int(DemoApp.money_left)*dem_true_false(DemoApp.left_c)
				DemoApp.tien_thu_duoc_right = int(DemoApp.money_right)*dem_true_false(DemoApp.right_c)
				DemoApp.tien_thu_duoc_all = DemoApp.tien_thu_duoc_left + DemoApp.tien_thu_duoc_right
				self.root.ids.txt_ketqua.text =str(DemoApp.tien_thu_duoc_all) + "/" +str(DemoApp.txt_tien_sanbong) + "k"

			if DemoApp.tien_thu_duoc_all >= DemoApp.txt_tien_sanbong:
				a = DemoApp.tien_thu_duoc_all - DemoApp.txt_tien_sanbong
				self.root.ids.txt_ketquaquy.text = "Quỹ: "+	str(a) +"k"
				self.root.ids.txt_ketquaquy.text_color = (0,1,0,1)
				self.root.ids.txt_ketqua.text_color = (0,1,0,1)
			if DemoApp.tien_thu_duoc_all < DemoApp.txt_tien_sanbong:
				self.root.ids.txt_ketquaquy.text = "Quỹ: 0k"
				self.root.ids.txt_ketquaquy.text_color = (1,0,0,1)
				self.root.ids.txt_ketqua.text_color = (1,0,0,1)
		except Exception as e:
			self.root.ids.txt_ketqua.text= "ERROR"		

	def checkbox_right( self , instance , value ):
		try:
			if value:
				DemoApp.right_c.append(value)
				DemoApp.tien_thu_duoc_right = int(DemoApp.money_right)*dem_true_false(DemoApp.right_c)
				DemoApp.tien_thu_duoc_left = int(DemoApp.money_left)*dem_true_false(DemoApp.left_c)
				DemoApp.tien_thu_duoc_all = DemoApp.tien_thu_duoc_left + DemoApp.tien_thu_duoc_right
				self.root.ids.txt_ketqua.text =str(DemoApp.tien_thu_duoc_all) + "/" +str(DemoApp.txt_tien_sanbong) + "k"
			else:
				DemoApp.right_c.append(value)
				DemoApp.tien_thu_duoc_right = int(DemoApp.money_right)*dem_true_false(DemoApp.right_c)
				DemoApp.tien_thu_duoc_left = int(DemoApp.money_left)*dem_true_false(DemoApp.left_c)
				DemoApp.tien_thu_duoc_all = DemoApp.tien_thu_duoc_left + DemoApp.tien_thu_duoc_right
				self.root.ids.txt_ketqua.text =str(DemoApp.tien_thu_duoc_all) + "/" +str(DemoApp.txt_tien_sanbong) + "k"

			
			if DemoApp.tien_thu_duoc_all >= DemoApp.txt_tien_sanbong:
				a = DemoApp.tien_thu_duoc_all - DemoApp.txt_tien_sanbong
				self.root.ids.txt_ketquaquy.text = "Quỹ: "+	str(a) +"k"
				self.root.ids.txt_ketquaquy.text_color = (0,1,0,1)
				self.root.ids.txt_ketqua.text_color = (0,1,0,1)
			if DemoApp.tien_thu_duoc_all < DemoApp.txt_tien_sanbong:
				self.root.ids.txt_ketquaquy.text = "Quỹ: 0k"
				self.root.ids.txt_ketquaquy.text_color = (1,0,0,1)
				self.root.ids.txt_ketqua.text_color = (1,0,0,1)	
		except Exception as e:
			self.root.ids.txt_ketqua.text= "ERROR"	


			

if __name__ == '__main__':
	DemoApp().run()		