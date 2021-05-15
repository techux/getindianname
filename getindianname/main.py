import random, requests

space =" "

with open("malename") as mn:
    msufix = mn.read().splitlines()

with open("femalename") as fn:
    fsufix = fn.read().splitlines()

with open("maletitle") as mt:
    mprefix = mt.read().splitlines()

with open("femaletitle") as fmt:
    fprefix = fmt.read().splitlines()

allname=fsufix+msufix
alltitle=mprefix+fprefix

def randname():
	name = random.choice(allname)+space+random.choice(alltitle)
	return name
	
def female():
	name = random.choice(fsufix)+space+random.choice(fprefix)
	return name
	
def male():
	name = random.choice(msufix)+space+random.choice(mprefix)
	return name

def chkupdate():
	oldv=open("nameversion","r")
	old = oldv.read()
	newv = open("https://raw.githubusercontent.com/devesh7272/getindianname/main/getindianname/nameversion","r")
	new=newv.read()
	if old==new:
		pass
	else:
		update()

def pypicheck():
	oldpv=open("pyversion","r")
	oldp = oldpv.read()
	newpv = open("https://raw.githubusercontent.com/devesh7272/getindianname/main/getindianname/pypiversion","r")
	newp=newpv.read()
	if oldp==newp:
		pass
	else:
		print("Update Available on Pypi\n\n Updating...")
		pypiupdate()
		
def pypiupdate():
	try:
		print("Updating from Pypi")
		os.system("pip install getindianname")
		os.system("clear")
	except:
		print("Check Your Internet Connection")
		
def update():
	mdata = requests.get("https://raw.githubusercontent.com/devesh7272/getindianname/main/assets/male_name").text
	mfile = open("malename","w")
	mfile.write(mdata)
	mfile.close()
	
	fdata = requests.get("https://raw.githubusercontent.com/devesh7272/getindianname/main/assets/female_name").text
	fmfile = open("femalename","w")
	fmfile.write(fdata)
	fmfile.close()
	
	mtdata = requests.get("https://raw.githubusercontent.com/devesh7272/getindianname/main/assets/male_title").text
	mtfile = open("maletitle","w")
	mtfile.write(mtdata)
	mtfile.close()
	
	ftdata = requests.get("https://raw.githubusercontent.com/devesh7272/getindianname/main/assets/female_title").text
	fmtfile = open("fmaletitle","w")
	fmtfile.write(ftdata)
	fmtfile.close()

chkupdate()
pypicheck()
