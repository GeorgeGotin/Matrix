def NOD(a,b):
	r = a % b
	while r != 0:
		a = b
		b = r
		r = a % b
	return b
	
def power(a,n):
	m = []
	while n > 0:
		m.append(n%2)
		n = n // 2
	s = 1
	q = len(m)
	for i in range(q):
		if m[q - i - 1] == 0:
			s = s*s
		else:
			s=s*s*a
	return s
	
class frac:
	def __init__(self,up,down=1):
		if down == 0:
			print('blue screen of  death(we can\'t div 0)')
			return None
		c = NOD(int(up),int(down))
		self.up = up // c
		self.down = down // c
			
	def __str__(self):
		if self.down == 1:
			return '{}'.format(self.up)
		else:
			return ('{}/{}'.format(self.up,self.down))
						
	def __add__(self,other):
		if type(other) == frac:
			return frac(self.up*other.down+self.down*other.up,self.down*other.down)
		elif type(other) == int:
			return frac(self.up+other*self.down,self.down)
		else:
			print('oops')
	def __radd__(self,other):
		if type(other) == int:
			return self + other
		else:
			print('oops')
				
	def __sub__(self,other):
		if type(other) == frac:
			return self + frac(-1*other.up,other.down)
		elif type(other) == int:
			return self + (-1*other)
		else:
			print('oops')
	def __rsub__(self,other):
		if type(other) == int:
			return -self + other		
			
	def __mul__(self,other):
		if type(other) == frac:
			return frac(self.up*other.up,self.down*other.down)
		elif type(other) == int:
			return frac(self.up*other,self.down)
		else:
			print('oops')
	def __rmul__(self,other):
		return self * other
			
	def __neg__(self):
		return frac(-self.up,self.down)
		
	def __truediv__(self,other):  #should answer after '/', but print error
		if type(other) == frac:
			return frac(self.up*other.down,self.down*other.up)
		elif type(other) == int:
			return frac(self.up,self.down*other)
		else:
			print('oops')
	def __rtruediv__(self,other):
		if type(other) == int:
			return frac(other*self.down,self.up)
		else:
			print('oops')
			
	def __pow__(self,p):
		return frac(power(self.up,p),power(self.down,p))
	
	def __eq__(self,other):
		if type(other) == frac:
			if self.up == other.up and self.down == other.down:
				return True
			else:
				return False
		elif type(other) == int:
			return self == frac(other)
		else:
			print('oops')
	def __ne__(self,other):
		return not(self == other)
	def __lt__(self,other):
		if type(other) == frac:
			if (self - other).up < 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self<frac(other)
		else:
			print('oops')
	def __gt__(self,other):
		if type(other) == frac:
			if (self - other).up > 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self>frac(other)
		else:
			print('oops')
	def __le__(self,other):
		if type(other) == frac:
			if (self - other).up <= 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self<=frac(other)
		else:
			print('oops')
	def __ge__(self,other):
		if type(other) == frac:
			if (self - other).up >= 0:
				return True
			else:
				return False
		elif type(other) == int:
			return self>=frac(other)
		else:
			print('oops')
			
	def __float__(self):
		return self.up/self.down

		

class matrix:
	def __init__(self,body=[[1]]):
		if type(body) != type([1]):
			print('1st Siniy ecran smerti')
			exit(1)
		for i in body:
			if (type(i) != type([1])):
				print('2nd Siniy ecran smerti')
				exit(2)
		norm = len(body[0])
		for i in body:
			if len(i) != norm:
				print('3rd Siniy ecran smerti')
				exit(3)
		self.body = body
	
	def frac(self):
		for i in range(self.nrow()):
			for j in range(self.ncol()):
				self.body[i][j]=frac(self.body[i][j])
		return self
	
	def copy(self):
		res = []
		for i in range(self.nrow()):
			res.append([])
			for j in range(self.ncol()):
				res[i].append(self.body[i][j])
		return matrix(res)

	def nrow(self):
		return len(self.body)
	def ncol(self):
		return len(self.body[0])
			
	def __str__(self):
		ms = []                                                            #nachalo podgonki po probelam
		for i in range(self.ncol()):
			ms.append(0)
			for j in range(self.nrow()):
				if len(str(self.body[j][i])) > ms[i]:
					ms[i] = len(str(self.body[j][i]))
		res=''
		for i in range(self.nrow()):
			for j in range(self.ncol()):
				res+='{}'.format(' '*(ms[j]-len(str(self.body[i][j]))+1))  #konec podgonki po probelam
				res+=str(self.body[i][j])
			res+='\n'
		return res
			
	def __add__(self,other):
		if type(other) != matrix:
			print('Wrong type')
			return self
		if (self.nrow() != other.nrow()) or (self.ncol() != other.ncol()):
			print('Different sizes of matrixes')
			return None
		res = []
		for i in range(self.nrow()):
			res.append([])
			for j in range(self.ncol()):
				res[i].append(self.body[i][j]+other.body[i][j])
		return matrix(res)

	def __mul__(self,other):
		if type(other) == int or type(other) == float or type(other) == complex:
			res = []
			for i in range(self.nrow()):
				res.append([])
				for j in range(self.ncol()):
					res[i].append(self.body[i][j]*other)
			return matrix(res)
		elif type(other) == matrix:
			if self.ncol() != other.nrow():
				print('Different sizes of matrixes')
				return None
			res = []
			for i in range(self.nrow()):
				res.append([])
				for j in range(other.ncol()):
					c = 0
					for l in range(self.ncol()):
						if (type(self.body[i][l]) != int and type(self.body[i][l]) != float and type(self.body[i][l]) != complex and type(self.body[l][j]) != frac) or (type(other.body[l][j]) != int and type(other.body[l][j]) != float and type(other.body[l][j]) != complex and type(other.body[l][j]) != frac):
							print('Impossible to mull! ({0},{1}),({1},{2})'.format(i,l,j))
							return None
						c+=self.body[i][l]*other.body[l][j]
					res[i].append(c)
			return matrix(res)
		else:
			print('Wrong type')
			return self
	def __rmul__(self,other):
		return self * other

	def __eq__(self,other):
		if type(other) != matrix:
			return False
		elif self.ncol() != other.ncol() or self.nrow() != other.nrow():
			return False
		else:
			for i in range(self.nrow()):
				if self.body[i] != other.body[i]:
					return False
			return True

	def chgrow(self,i,j,inplace=False):
		if inplace == True:
			a = self.body[i]
			self.body[i] = self.body[j]
			self.body[j] = a
			return self
		else:
			res = []
			for k in range(self.nrow()):
				if k == i:
					res.append(self.body[j])
				elif k == j:
					res.append(self.body[i])
				else:
					res.append(self.body[k])
			return matrix(res)
	def chgcol(self,i,j,inplace=False):
		if inplace == True:
			for k in range(self.nrow()):
				a = self.body[k][i]
				self.body[k][i] = self.body[k][j]
				self.body[k][j] = a
			return self
		else:
			res = []
			for k in range(self.nrow()):
				res.append([])
				for l in range(self.ncol()):
					if l ==i:
						res[k].append(self.body[k][j])
					elif l == j:
						res[k].append(self.body[k][i])
					else:
						res[k].append(self.body[k][l])
			return matrix(res)

	def mulrow(self,i,n,inplace=False):
		if inplace == True:
			for k in range(self.ncol()):
				self.body[i][k] *=n
			return self
		else:
			res=[]
			for l in range(self.nrow()):
				if l == i:
					res.append([])
					for k in self.body[i]:
						res[l].append(k*n)
				else:
					res.append(self.body[l])
			return matrix(res)
	def mulcol(self,i,n,inplace=False):
		if inplace == True:
			for k in range(self.nrow()):
				self.body[k][i] *= n
			return self
		else:
			res = []
			for l in range(self.nrow()):
				res.append([])
				for k in range(self.ncol()):
					if k == i:
						res[l].append(self.body[l][i]*n)
					else:
						res[l].append(self.body[l][k])
			return matrix(res)
	
	
	def sumrow(self,frm1,frm2,to,n=1,inplace=False):
		if inplace == True:
			for i in range(self.ncol()):
				self.body[to][i]= self.body[frm1][i]+self.body[frm2][i]
				self.body[to][i] *= n
			return self
		else:
			res = a.copy()
			for i in range(res.ncol()):
				res.body[to][i]= res.body[frm1][i]+res.body[frm2][i]
				res.body[to][i] *= n
			return res	
	def sumcol(self,frm1,frm2,to,n=1,inplace=False):
		if inplace == True:
			for i in range(self.nrow()):
				self.body[i][to] = self.body[i][frm1] + self.body[i][frm2]
				self.body[i][to]*=n
			return self
		else:
			res = self.copy()
			for i in range(res.nrow()):
				res.body[i][to] = res.body[i][frm1] + res.body[i][frm2]
				res.body[i][to]*=n
			return res			
    
	def delrow(self,n):
		res=[]
		for i in range(self.nrow()):
			if i == n:
				continue
			else:
				res.append(self.body[i])
		return matrix(res)
	def delcol(self,n):
		res=[]
		for i in range(self.nrow()):
			res.append([])
			for j in range(self.ncol()):
				if j == n:
					continue
				else:
					res[i].append(self.body[i][j])
		return matrix(res)
    
	def trc(self):
		if not(self.sqr()):
			return None
		else:
			res = 0
			for i in range(self.nrow()):
				res += self.body[i][i]
			return res
	
	def det(self,k):
		if not(self.sqr()):
			return None
		else:
			res = 1
			for i in range(self.nrow()):
				res *= self.body[i][i]
			return res * power(-1,k)
	
	def trans(self):
		res=[]
		for i in range(self.ncol()):
			res.append([])
			for j in range(self.nrow()):
				res[i].append(self.body[j][i])
		res = matrix(res)
		return res
		
	def sqr(self):
		if self.nrow() == self.ncol():
			return True
		else:
			return False

	def Gause(self,ans):
		if not(self.sqr()) or (type(ans) != list and type(ans) != matrix):
			return None
		if type(ans)==list:
			hlp=[]
			hlp.append(ans)
			ans = matrix(hlp)
			ans = ans.trans()
		if ans.nrow() != self.nrow():
			return None
		k = 0
		resu=self.copy()
		for l in range(resu.nrow()-1):
			if resu.body[l][l] == 0:
				for i in range(l,resu.nrow()):
					if resu.body[i][l] != 0:
						resu.chgrow(l,i,True)
						ans.chgrow(l,i,True)
						k += 1
						break
			for i in range(l+1,resu.nrow()):	
				ans=ans.mulrow(l,1/resu.body[l][l],True)
				resu=resu.mulrow(l,1/resu.body[l][l],True)
				ans=ans.mulrow(l,-resu.body[i][l],True)
				resu=resu.mulrow(l,-resu.body[i][l],True)
				ans=ans.sumrow(i,l,i,1,True)
				resu=resu.sumrow(i,l,i,1,True)
			ans=ans.mulrow(l,1/resu.body[l][l],True)
			resu=resu.mulrow(l,1/resu.body[l][l],True)
		if resu.det(k) == 0:
			return None
		for l in range(resu.nrow()-1,-1,-1):
			for i in range(l-1,-1,-1):	
				ans=ans.mulrow(l,1/resu.body[l][l],True)
				resu=resu.mulrow(l,1/resu.body[l][l],True)
				ans=ans.mulrow(l,-resu.body[i][l],True)
				resu=resu.mulrow(l,-resu.body[i][l],True)
				ans=ans.sumrow(i,l,i,1,True)
				resu=resu.sumrow(i,l,i,1,True)
			ans=ans.mulrow(l,1/resu.body[l][l],True)
			resu=resu.mulrow(l,1/resu.body[l][l],True)
		return ans
					
		
			
        

a=frac(1,2)
print(a,'\n')
print(2/a,sep='')
            
