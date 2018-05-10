class FileWork:
    def __init__(self,url = 'out.txt',openType = 'r'): #default values
        self.url = url
        self.openType = openType

    def readFunc(self):
        with open(self.url) as f:
            while True:
                buf = f.read()
                if not buf:
                    break        
                print('%s'%(buf))
        f.close()
        return

    def writeFunc(self,str,amount):
        f = open(self.url,self.openType)
        for x in range(0,amount):
            print(str,end='\n',file=f)
        f.close()
        return
    
    def setOpenType(self,openType):
        self.openType = openType
        
#В Python деструктор используется редко,
#       так как интерпретатор и без него хорошо убирает "мусор".

#class ended
        
#readFunc
def readFile():
    with open('out.txt') as f:
        while True:
            buf = f.read()
            if not buf: break        
            print(buf)
    f.close()
    return

#readFunc
def readFile2():
    with open('out.txt') as f:
        for line in f:
            if not line:
                break        
            print("line: %s|line ended" %(line))
    f.close()
    return

#writeFunc
def writeFile( str, amount ):
    f = open('out.txt', 'w')
    for x in range(0, amount):
        print(str,file=f)
#    f.write(str+'\n')
    f.close()
    return
