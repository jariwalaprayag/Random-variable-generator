import sys
import random
import math
seed=int(input("Seed value:")) #Enter seed value here
def bernoulli(p):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		if(rn<p):
			l1.append(1)
		else:
			l1.append(0)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",p)
	print("Population variance",p*(1-p))
def binomial(p,n1):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		x=0
		for i in range(0,n1):
			rn=random.random()
			if(rn<p):
				x=x+1 
		l1.append(x)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",n1*p)
	print("Population variance",n1*p*(1-p))
def geometric(p):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		x=1
		while(random.random()>p):
			x=x+1
		l1.append(x)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",1/p)
	print("Population variance :",(1-p)/(p*p))
def negbinomial(k,p):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	
	for i in range(0,n):
		nk=0
		trial=0
		while(nk!=k):
			rn=random.random()
			if(rn<p): 
				nk=nk+1
			trial=trial+1 
		l1.append(trial)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",k/p)
	print("Population variance :",(k*(1-p))/(p*p))
def poisson(lam):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		i=0
		e=2.71828
		cdf=e**(-lam)
		while(rn>cdf):
			cdf=cdf+(e*(-lam))(lam**i)/math.gamma(i+1)
			i=i+1
		l1.append(i)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",lam)
	print("Population variance :",lam)
def arbdiscrete(p):
	n1=len(p)
	exp=0
	var=0
	for i in range(0,n1):
		exp=exp+i*p[i]
	for i in range(0,n1):
		var=var+((i-exp)**2)*p[i]
	rangep=[]
	rangep.append(0)
	
	for i in range(0,n1):
		if i==0:
			rangep.append(p[0])
		else:
			rangep.append(rangep[len(rangep)-1]+p[i]) 
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		i=0
		while(rn>rangep[i+1]):
			rn=random.random()
			i=i+1
		l1.append(i) 
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",exp)
	print("Population variance :",var)
def uniform(a,b):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=a+(b-a)*random.random()
		l1.append(rn)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",(a+b)/2)
	print("Population variance :",(b-a)*(b-a)/12)
def exponential(lam):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=(-1/lam)*math.log(random.random())
		l1.append(rn)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm) 
	print("sample variance :",sv) 
	print("Population mean : ",1/lam) 
	print("Population variance :",1/(lam*lam))
def gamma(alp,lam):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=0
		for j in range(0,alp):
			rn=rn+(-1/lam)*math.log(random.random())
		l1.append(rn)
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",alp/lam)
	print("Population variance :",alp/(lam*lam))
def normal(mue,sig):
	l1=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	if (n%2==0):
		x=int(n/2)
		for i in range(0,x):
			u1=random.random()
			u2=random.random()
			z1=((-2) * math.log(u1))*0.5
			z1=z1*math.cos(2*math.pi*u2)
			z2=((-2) * math.log(u1))*0.5
			z2=z2*math.cos(2*math.pi*u2)
			x=mue+sig*z1
			y=mue+sig*z2
			l1.append(x)
			l1.append(y) 
	else:
		x1=int(n/2)+1  
		for i in range(0,x1):
			u1=random.random()
			u2=random.random()
			z1=((-2)*math.log(u1))*0.5
			z1=z1*math.cos(2*math.pi*u2)
			z2=((-2)*math.log(u1))*0.5
			z2=z2*math.cos(2*math.pi*u2)
			x=mue+sig*z1
			y=mue+sig*z2
			if(i!=x1-1): 
				l1.append(x)
				l1.append(y)
			else:
				l1.append(x) 
	sm=sum(l1)/n
	data=list(map(lambda x: (x-sm)**2 ,l1))  
	sv=sum(data)/(n-1)
	print("sample :", l1)
	print("sample mean : ",sm)
	print("sample variance :",sv)
	print("Population mean : ",mue)
	print("Population variance :",sig**2) 

if (sys.argv[2]=="bernoulli"):
	p=float(sys.argv[3])
	bernoulli(p)
elif(sys.argv[2]=="binomial"): 
	n=int(sys.argv[3])
	p=float(sys.argv[4])
	binomial(p,n)
elif(sys.argv[2]=="geometric"): 
	p=float(sys.argv[3])
	geometric(p)
elif(sys.argv[2]=="neg-binomial"): 
	k=int(sys.argv[3])
	p=float(sys.argv[4])
	negbinomial(k,p)
elif(sys.argv[2]=="poisson"):
	print("poisson")
	lam=float(sys.argv[3])
	poisson(lam)
elif(sys.argv[2]=="arb-discrete"):
	p=[]
	for i in range(3,len(sys.argv)):
		p.append(float(sys.argv[i]))
	arbdiscrete(p) 
elif(sys.argv[2]=="uniform"):
	print("uniform")
	a=float(sys.argv[3])
	b=float(sys.argv[4])
	uniform(a,b)
elif(sys.argv[2]=="exponential"):
	print("exponential")
	lam=float(sys.argv[3])
	exponential(lam)
elif(sys.argv[2]=="gamma"):
	print("gamma")
	alp=int(sys.argv[3])
	lam=float(sys.argv[4])
	gamma(alp,lam)
elif(sys.argv[2]=="normal"): 
	mue=float(sys.argv[3])
	sig=float(sys.argv[4])
	normal(mue,sig)
else:
	print("enter proper name of distribution")