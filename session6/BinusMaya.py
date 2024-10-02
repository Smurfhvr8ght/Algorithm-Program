class BinusMaya:
    def __init__(self,Lecturers,Classes,):
        self.lec = []
        self.clas = []
        self.sched = []
        self.lec = Lecturers
        self.clas = Classes

    def addlec(self,name,subject,id):   #add lecturer
        for i in self.lec:
            if i["lecturer"] != name:   #check for duplicate name
                x = 1   #counter to make sure the second part of dict is read
                for j in i:
                    flag = False
                    if j != subject and x == 2:    #check for duplicate subject
                         flag = True
                    if i[j] != id and flag==True:  #check for duplicate id
                            self.lec.append({"lecturer":name,subject:id})
                            break
                    x += 1

    def remlec(self,id):    #remove lecturer
         flag = False
         for i in range(len(self.lec)):
              for j in self.lec[i]:
                   if self.lec[i][j] == id:
                        self.lec.pop(i)
                        flag = True
                        break
              if flag == True:
                break
                   
    def addclass(self,code):    #add class
         if code not in self.clas:
              self.clas.append(code)

    def remclass(self,code):    #remove class
         for i in range(len(self.clas)):
              if self.clas[i] == code:
                   self.clas.pop(i)
                   break
    
    def schedule(self,cls,time,subject):    #add schedule
         for i in self.lec:
              x=1
              for j in i:
                   if x==2:
                        if j == subject:
                             name = i["lecturer"]
                             self.sched.append((time,cls,subject,name))
                   x+=1

#testing below
test = BinusMaya([{"lecturer":"Ben","AlgPro":"A007"}],[1])
test.addlec("Bob","Math","A008")
print (test.lec)
test.remlec("A007")
print (test.lec)
test.addclass(2)
print (test.clas)
test.remclass(2)
print (test.clas)
test.schedule(1,"1:00","Math")
print (test.sched)
