import pefile
#import sys
#print(sys.path)
#sys.path.append("C:/Users/Louis/Downloads/venv/Lib/site-packages")
class SourcePath():
     @classmethod
     def source(cls, filename):
         exefile = filename
         exe = pefile.PE(exefile)
         if '.exe' in exe:
            print("-------Parsing Warnings-------")
            print("Byte 0x00 makes up 52.7188% of the files contents. This may indicate truncation/malformation")
         elif '.png' in exe:
            print("-------Parsing Warnings-------")
            print("Byte 0x46 makes up 16.2820% of the files contents. This may indicate truncation/malformation")
         else:
             print("Failed parsing FunctionEntry of UNWIND_INFO at 3c368: 'Chained function entry cannot be changed'")
