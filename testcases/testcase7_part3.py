#Collections
sub =["python","java","Ruby","java"]  #list - ordered, indexed, changeable, allow duplicates, Uses[]
print(sub)
print(sub[1])
sub[1]="Javascript"
print(sub)

sub =("python","java","Ruby","java")  #tuple - ordered, indexed, unchangeable, allow duplicates, Uses()
print(sub)
print(sub[1])
# sub[1]="Javascript"  #Tuple does not support change in elements

sub ={"python","java","Ruby","java"}  #set - unordered, unindexed, unchangeable, No duplicates allowed, Uses{}
print(sub)

dic1={"name":"Toby",
      "job":"software engineer",
      "id":20}   #dictionary - unordered, changeable, No duplicates allowed, Uses{key:value}
print(dic1)
print(dic1["job"])