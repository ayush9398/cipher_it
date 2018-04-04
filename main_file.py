import argparse
from Morse_code.morse import morse
import Tap_code.tap as tap

def main():
    parser=argparse.ArgumentParser(description="Cipher your text to the available cipher codes. Currently, available codes are:"
                                               +" morse, tap"
                                   )
    parser.add_argument('-t',"--text", help="text you want to enter", type=str)
    parser.add_argument("cipher", help="enter the cipher to encode to")
    parser.add_argument("-f","--file", help="enter file to encode, .txt only")
    parser.add_argument("-s","--save", help="Save to file")
    args=parser.parse_args()
    if (args.file):
        with open(args.file,'r') as filem:
            if(args.cipher=='morse'):
                crypt=morse(filem.read())
                print(crypt)
            elif(args.cipher=='tap'):
                crypt=tap(filem.read())
                print(crypt)

    else:
        if (args.cipher == 'morse'):
            crypt = morse(args.text)
            print(crypt)
        elif (args.cipher == 'tap'):
            crypt = tap.tap(args.text)
            print(crypt)
    if(args.save):
        with open(args.save,'a') as ofile:
            ofile.write('\n'+crypt)
            print("Saved to file "+ args.save)

if __name__== "__main__":
    main()