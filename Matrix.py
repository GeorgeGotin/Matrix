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
						
			
		
		
a=matrix([[1,1,1],[1,1,1]])
print(a,a.nrow(),a.ncol(),'\n')
b=matrix([[1,1],[1,1],[1,1]])
print(b,b.nrow(),b.ncol(),'\n')
c = a*b
print(c)
			
