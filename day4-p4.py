Create a function showStudent() in such a way that it should accept student id, name, and it’s college name  and if the id and college name is missing in function call it should show it as by default id is 1 and college name  is VITA.



def student(name,clgname="Vita",id=1):
    print(name,"studying in",clgname,", your id is",id)
    
student("shrutika","vita",7)
student("adi")
student("apurva","vita")
