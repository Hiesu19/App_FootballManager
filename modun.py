import random

def chiatien(sotien , ti_le ,winer , loser):
	try:
	
		if ti_le =="7:3":

			d = -winer*3*loser - loser*7*winer	
			dx = -sotien*3*loser
			dy = 0-7*winer*sotien
			if d ==0:
				x = -1
				y = -1
				return -1,-1,-1
			if d == 0 and dx == 0 and dy == 0:	
				x = -1
				y = -1
				return -1,-1,-1
			else:	
				x = dx/d
				y = dy/d
			
		elif ti_le =="5:5":
			if winer+loser ==0:
				x = -1
				y = -1
				return -1,-1,-1
			else:	
				x = sotien/(winer+loser)
				y = sotien/(winer+loser)

			

		elif ti_le=="10:0":
			if loser ==0:
				x = -1
				y = -1
				return -1,-1,-1
			else:	
				x = 0
				y = sotien/loser
			
		if x%5 == 0 and y%5 ==0:
			q = y*loser +x*winer - sotien
			return x ,y ,q

		if x %5 ==0 and y%5!=0:
			h = ((y//5)+1) *5
			q = h*loser +x*winer - sotien
			return x  ,h ,q	
		if x %5 !=0 and y%5==0:
			h = ((x//5)+1) *5
			q = y*loser +h*winer - sotien
			return h ,y ,q	
		else:
			if ti_le =="7:3": 	
				du_win = ((x//5) +1) *5 - x	
				du_los = y - (y//5)*5
				k_thu = du_win*winer - du_los*loser
				if k_thu >= 0:
					h = ((x//5) +1) *5
					k = (y//5)*5
					q = k*loser +h*winer - sotien
					return h,k,q
				else:	
					h = ((x//5) +1 ) *5
					k = ((y//5) +1 ) *5
					q = k*loser +h*winer - sotien
					return h,k,q
			if ti_le =="5:5":
				h = ((x//5)+1)*5
				k = ((y//5)+1)*5
				q = k*loser +h*winer - sotien
				return h,k,q
			if ti_le =="10:0":
				h = 0
				k = k = ((y//5)+1)*5
				q = k*loser +h*winer - sotien
				return h,k,q

	except Exception as e:
		return -1,-1,-1	


def chonnguoi(nguoi):
	try:
	
		a = []

		so_nguoi = len(nguoi)
		chia = so_nguoi// 2
		for i in range (1, chia+1):

			h = random.choice(nguoi)
			a.append(h)
			nguoi.remove(h)
		return nguoi , a	

	except Exception as e:
		return ["-1"] , ["-1"]		

def chiadeu(a , b):
	try:
		c = []
		for x in range (0 , abs(len(a) - len(b))):
			if len(a) >len (b):
				b.append(' ')
			elif len (a) < len(b):
				a.append(" ")

		for i in range(0 , len(a)):
			if random.choice([True , False]) == True:
				c.append(a[i])
				a[i] = b[i]
				b[i] = c[0]
				c.clear()
		return a,b
	except Exception as e:
		b.append["ERROR"]
		return a ,b	


def list_to_12 (a):
	for x in range(0 , 12 - len(a)):
		a.append("?")
	return a

def dem_true_false(a):
	c_true = 0
	c_false = 0
	for i in a:
		if i:
			c_true +=1
		else:
			c_false +=1	
	d = c_true -c_false
	return d					
		
if __name__ == '__main__':
	pass