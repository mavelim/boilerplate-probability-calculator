import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **kargs):
		self.contents=[]
		for key in kargs:
			for i in range(kargs[key]):
				self.contents.append(key)
	def draw(self,number):
		
		balls=[]
		if number > len(self.contents):
			balls=self.contents
		else:
			for i in range(number):
				a_sacar=random.choice(self.contents)
				self.contents.remove(a_sacar)
				balls.append(a_sacar)
				
		return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	
	prob=0
	M=0

	for i in range(num_experiments):
		hat_full=copy.deepcopy(hat)
		#formamos un dict con las balls drawn
		actual_balls_list=hat_full.draw(num_balls_drawn)
		actual_balls={}
		for i in actual_balls_list:
			actual_balls[i]=actual_balls.get(i,0)+1
		#comparamos los dict
		aux=0
		for balls in expected_balls:
			if expected_balls[balls] <= actual_balls.get(balls,0):
				aux += 1

		if aux==len(expected_balls):
			M += 1
			
	prob=M/num_experiments

	return prob
