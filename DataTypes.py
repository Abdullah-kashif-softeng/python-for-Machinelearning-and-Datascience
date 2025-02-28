name="Abdullah"
age=21
cgpa=3.15
married=False
list=[1,2,3,4]
tupple=("Hello",45,"World",66)
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
list[1]=55
print(list)#[1,55,3,4]
#lists are dynamic, we can add new elements
list.append(5)
print(list)#[1,55,3,4,5]
#Tuples are faster than lists because of immutability
#tuples are made to protect data
#Tuples have fixed size

#Typecasting datatypes

