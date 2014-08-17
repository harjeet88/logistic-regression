import pylab as pl
def plotDB(X,Y,theta) :
	posX1 = X[Y==1,1]
	negX1 = X[Y==0,1]

	posX2 = X[Y==1,2]
	negX2 = X[Y==0,2]
	
	pl.scatter(posX1,posX2, marker ='o' , c= 'b')
	
	pl.scatter(negX1,negX2, marker ='+' , c= 'r')
	
	pl.xlabel('Exam 1 score')
	pl.ylabel('Exam 2 score')
	pl.legend(['Not Admitted', 'Admitted'])
	
	pl.show()
