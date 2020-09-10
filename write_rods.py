import numpy as np
# number of rods
N = 200
# mean number of units per rod
mean = 30
poly = 0.2


L = 50.
xlo=ylo=zlo=0.
xhi=yhi=zhi=L

a=0.5

class Rod(object):
	def __init__(self,spacing):
		self.length=int(np.random.normal(mean,poly*mean))
		for i in range(self.length):
			self.x=np.linspace(0,self.length*spacing,self.length)
			self.y=np.zeros(self.length)
			self.z=np.zeros(self.length)
# create rods
rods = [Rod(a) for i in range(N)]
# total numer of atoms
nAtoms = 0
for rod in rods:
	nAtoms+=rod.length

with open("data.rigid.rods2",'w') as fout:
	fout.write("""LAMMPS	 data file
		%d atoms
		1 atom types

		"""%nAtoms)
	fout.write("""%g	%g	xlo xhi
	%g	%g	ylo yhi
	%g	%g	zlo zhi

Masses

1 1.000

Atoms

"""%(xlo,xhi,ylo,yhi,zlo,zhi))
	atom=1
	for c,rod in enumerate(rods):
		# random translation
		tr = np.random.uniform(0,L,3)
		for i in range(rod.length):
			x=rod.x[i]+tr[0]
			y=rod.y[i]+tr[1]
			z=rod.z[i]+tr[2]
			fout.write("%d %d 1 %g %g %g\n"%(atom, c+1,x,y,z))
			atom+=1
