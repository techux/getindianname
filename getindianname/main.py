import random
space =" "
msufix=["Abhinav","Devu","Dev","Dipendra","Deva","Pratyush","Roshan","Rudra","Roshan","Aman","Unnat","Adarsh","Abhishek","Abhi","Abhimanyu","Raju","Akshath","Rudra","Sanoj","Mahendra","Puneeth","Shankar","Aarav", "Kshitij", "Shantanu", "Onkar", "Aniket", "Atharva", "Prajwal", "Yash", "Abhijeet", "Ganesh", "Sachin", "Prathamesh", "Vaibhav", "Ninad", "Mihir", "Tejas", "Suyash", "Sanket", "Devang", "Darshan", "Soham", "Rohit", "Manish", "Aadesh", "Siddhesh",
"Aakash", "Anmol", "Chaitanya", "Dharmesh", "Gagan", "Gaurav", "Gopal", "Ishan", "Mehul", "Om", "Rahul", "Sandesh", "Tanmay", "Tushar", "Utkarsh",
"Vedang", "Varun", "Vinay", "Vivek", "Yogesh","Saritha","Vijay","Shila","Arjun","Gauri","Rohit","Senthil","Bavya","Abhijeet","Udaya","Ankit","Krishna","Hayat","Murat","Ravindra","Nagaraju","Ranjit","Rupesh","Sarthak","Gagan", "Hari", "Bala", "Maan", "Naveen", "Sukhan", "Guru", "Karam", "Karan", "Diljeet", "Dharam", "Param", "Devesh", "Jaspreet","Ankit","Devansh","Pranjal","Gagan", "Har", "Bal", "Man", "Nav", "Sukh", "Kush", "Gur", "Karam", "Karan", "Dil", "Dharam", "Param", "Dal", "Jas", "Par", "Dul"]

fsufix = ["Gayatri","Roshni","Priyanka","Priyanshee","Priyanshi","Priya","Pragya","Paridhi","Pallawi","Shivani","Siwangi","Sweta","Silam","Nilam","Annu","Anushka","Riya","Radha","Shyama","Nikita","Janhavi","Rakhi","Kamini","Anshika","Nitya","Ridhima","Namita","Namrata","Yashi","Kirti","Ambika","Anamika","Manisha","Damini","Ananya","Shradha","Aishwarya","Anjali","Jooli","Deepa","Savita","Sita","Sherya","Pinky","Monika","Khushi","Jyoti","Anupriya","Kajal","Tripti","Priti","Pradhi","Komal","Vandana","Khushi","Gouri","Nivedita","Parul","Sanjana","Shruti","Simran","Puspha","Nitya","Ruhi","Aaroohi","Pragati","Rahul","Ronak"]

mprefix=["Singh","Yadav","Rajput","Pandey","Mishra","Seth","Srivastav","Vishwakarma","Maurrya","Pratap","Thakur","Tiwari","Divedi","Sonkar","Rai","Rao","Gupta","Kumar","Pandit"]

fprefix=["Devi","Singh","Yadav","Rajput","Pandey","Mishra","Seth","Srivastav","Vishwakarma","Maurya","Thakur","Tiwari","Divedi","Sonkar","Rai","Rao","Gupta","Kumari"]

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
