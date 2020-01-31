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
						if (type(self.body[i][l]) != int and type(self.body[i][l]) != float and type(self.body[i][l]) != complex) or (type(other.body[l][j]) != int and type(other.body[l][j]) != float and type(other.body[l][j]) != complex):
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

	def reprow(self,i,j,inplace=False):
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
	def repcol(self,i,j,inplace=False):
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
    
    
	def trc(self):
		if self.nrow() != self.ncol():
			return None
		else:
			res = 0
			for i in range(self.nrow()):
				res += self.body[i][i]
			return res
					
	
	def trans(self):
		res=[]
		for i in range(self.ncol()):
			res.append([])
			for j in range(self.nrow()):
				res[i].append(self.body[j][i])
		res = matrix(res)
		return res
        
a=matrix([[1,2,3],[4,5,6],[7,8,9]])
print(a,a.nrow(),a.ncol(),'\n')
b = a.trans()
print(a,b,sep='')
            
