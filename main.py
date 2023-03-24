from read import read_nfc
from write import write_nfc

while(True):
    opt = input("R/W: ")
    if(opt == "R"):
        read_nfc()
    elif(opt == "W"):
        write_nfc()
    elif(opt == "X"):
        break
    else:
        print("Invalid!")
        break