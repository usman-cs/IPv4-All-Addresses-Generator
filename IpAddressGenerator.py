import os
import Ui_ipAddress
from threading import Thread
import multiprocessing
import sys
import os
import glob
import psutil
from PySide6.QtCore import QRunnable, Slot, QThreadPool
ui = Ui_ipAddress.Ui_mainWindow()
shared = None
result = None
threadpool=QThreadPool()
class Worker(QRunnable):
    def __init__(self,fn,*args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
    @Slot()
    def run(self):
        self.fn(*self.args,**self.kwargs)

def ipAddressA(shared):
    if os.path.exists('Class A IpAddress'):
        list_of_files = glob.glob('Class A IpAddress/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        start=''
        for i in latest_file:
            try:
                int(i)
                start+=i
            except:
                pass
        os.remove(latest_file)
        for i in range(int(start),256):
            path = f'Class A IpAddress/ClassA_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class A Ip Address Generated Sucessfully')
        shared.put('Class A Ip Address Generated Sucessfully')
    else:
        os.mkdir('Class A IpAddress')
        for i in range(1,128):
            path = f'Class A IpAddress/ClassA_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        shared.put('Class A Ip Address Generated Sucessfully')
def ipAddressB(shared):
    if os.path.exists('Class B IpAddress'):
        list_of_files = glob.glob('Class B IpAddress/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        start=''
        for i in latest_file:
            try:
                int(i)
                start+=i
            except:
                pass
        os.remove(latest_file)
        for i in range(int(start),256):
            path = f'Class B IpAddress/ClassB_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class B Ip Address Generated Sucessfully')
        shared.put('Class B Ip Address Generated Sucessfully')
    else:
        os.mkdir('Class B IpAddress')
        for i in range(128,192):
            path = f'Class B IpAddress/ClassB_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class B Ip Address Generated Sucessfully')
        shared.put('Class B Ip Address Generated Sucessfully')
def ipAddressC(shared):
    if os.path.exists('Class C IpAddress'):
        list_of_files = glob.glob('Class C IpAddress/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        start=''
        for i in latest_file:
            try:
                int(i)
                start+=i
            except:
                pass
        os.remove(latest_file)
        for i in range(int(start),256):
            path = f'Class C IpAddress/ClassC_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class C Ip Address Generated Sucessfully')
        shared.put('Class C Ip Address Generated Sucessfully')
    else:
        os.mkdir('Class C IpAddress')
        for i in range(192,224):
            path = f'Class C IpAddress/ClassC_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class C Ip Address Generated Sucessfully')
        shared.put('Class C Ip Address Generated Sucessfully')
def ipAddressD(shared):
    if os.path.exists('Class D IpAddress'):
        list_of_files = glob.glob('Class D IpAddress/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        start=''
        for i in latest_file:
            try:
                int(i)
                start+=i
            except:
                pass
        os.remove(latest_file)
        for i in range(int(start),240):
            path = f'Class D IpAddress/ClassD_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class D Ip Address Generated Sucessfully')
        shared.put('Class D Ip Address Generated Sucessfully')
    else:
        os.mkdir('Class D IpAddress')
        for i in range(224,240):
            path = f'Class D IpAddress/ClassD_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class D Ip Address Generated Sucessfully')
        shared.put('Class D Ip Address Generated Sucessfully')
def ipAddressE(shared):
    if os.path.exists('Class E IpAddress'):
        list_of_files = glob.glob('Class E IpAddress/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        start=''
        for i in latest_file:
            try:
                int(i)
                start+=i
            except:
                pass
        os.remove(latest_file)
        for i in range(int(start),256):
            path = f'Class E IpAddress/ClassE_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class E Ip Address Generated Sucessfully')
        shared.put('Class E Ip Address Generated Sucessfully')
    else:
        os.mkdir('Class E IpAddress')
        for i in range(254,256):
            path = f'Class E IpAddress/ClassE_{i}.txt'
            f = open(path,'w')
            for j in range(0,256):
                for v in range(0,256):
                    for l in range(0,256):
                        f.write('.'.join((str(i),str(j),str(v),str(l))))
                        f.write('\n')
            f.close()
        # print('All Class E Ip Address Generated Sucessfully')
        shared.put('Class E Ip Address Generated Sucessfully')
def printing(shared):
    while True:
        while not shared.empty():
            data=shared.get()
            ui.results.addItem(data)
            if ui.results.count()==6:
                ui.results.addItem('All Task Finished')
                ui.cancelProcess.hide()
                ui.startProcessBtn.show()
                return
def run():
    global shared
    ui.startProcessBtn.hide()
    ui.cancelProcess.show()
    ui.results.addItem('Generating IpV4 Addresses For You Please Wait...')
    shared = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=ipAddressA, args=(shared,),daemon=True)
    p2 = multiprocessing.Process(target=ipAddressB, args=(shared,),daemon=True)
    p3 = multiprocessing.Process(target=ipAddressC, args=(shared,),daemon=True)
    p4 = multiprocessing.Process(target=ipAddressD, args=(shared,),daemon=True)
    p5 = multiprocessing.Process(target=ipAddressE, args=(shared,),daemon=True)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    t1=Thread(target=printing,daemon=True,args=(shared,))
    t1.start()
def killtree():
    try:
        pid=os.getpid()
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            print( "child", child)
            child.kill()
        ui.results.clear()
        ui.cancelProcess.hide()
        ui.startProcessBtn.show()
        ui.results.clear()
    except:
        pass
if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = Ui_ipAddress.QApplication(sys.argv)
    MainWindow = Ui_ipAddress.QWidget()
    ui.setupUi(MainWindow)
    ui.cancelProcess.hide()
    ui.startProcessBtn.clicked.connect(run)
    ui.cancelProcess.clicked.connect(killtree)
    MainWindow.setFixedSize(441, 348)
    MainWindow.show()
    sys.exit(app.exec())