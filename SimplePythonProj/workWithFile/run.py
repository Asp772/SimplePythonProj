import wfimp
import msvcrt as m
#from wfimp import FileWork
def testFunc():
    for i in 'hello world':
        if i == 'o':
            continue
        print(i * 2, end='')
    A = 't' if 'spam' else 'f'
    print("\n",A)

fl = wfimp.FileWork()
fl.setOpenType('w')
fl.writeFunc('somestr',3)
fl.readFunc()
fl.setOpenType('w')
fl.writeFunc('somestr',3)
fl.readFunc()

wfimp.readFile2()


print("Press any button...")
def wait():
    m.getch()
wait()
