name="Abdullah"
age=21
cgpa=3.15
married=False
list=[1,2,3,4]
tupple=("Hello",45,"World",66)
complex_a=1+6j#Real and imaginary part
dictionary={"name":"Abdullah","age":21,"Degree":"Software Engineering"}
set={1,2,2,3,4,5}
print(type(name)) #str
print(type(age)) #int
print(type(cgpa)) #float
print(type(married)) #bool
print(type(list))# list
print(type(tupple))#tuple
print(type(dictionary))#dictionary
print(type(set))#set

#List are mutable, means we can add,insertm change, delete or replace new element
#list[1]=55
print(list)#[1,55,3,4]
#lists are dynamic, we can add new elements
#list.append(5)
print(list)#[1,55,3,4,5]
#Tuples are faster than lists because of immutability
#tuples are made to protect data
#Tuples have fixed size

#Typecasting datatypes

name="Abdullah" #Cannot convert to int
age2=21
cgpa=3.15
married=False
listy=[1,2,3,4]
tupple=("Hello",45,"World",66)
dictionary={"name":"Abdullah","age":21,"Degree":"Software Engineering"}
sett={1,2,2,3,4,5}

print(type(str(age2)))#"21"
print(float(age2))# 21.0
print(bool(age2))#True, Because not 0
print(list(tupple))#Tupple converted to list
print(tuple(listy))#List converted to Tupple
print(tuple(sett))#set converted to tupple
print(set(listy))#List converted to set

#Cannot add int with string which includes letters
inta=21
intb="33"
#print(inta+intb)#Wrong
print(inta+int(intb))#Correct

#print(listy+sett)#Wrong
print(listy+list(sett))#Correct


