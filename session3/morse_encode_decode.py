decode = {".-": "A","-...": "B","-.-.": "C","-..": "D",".": "E","..-.": "F","--.": "G","....": "H","..": "I",".---": "J","-.-": "K",".-..": "L","--": "M","-.": "N","---": "O",".--.": "P","--.-": "Q",".-.": "R","...": "S","-": "T","..-": "U","...-": "V",".--": "W","-..-": "X","-.--": "Y","--..": "Z","-----": "0",".----": "1","..---": "2","...--": "3","....-": "4",".....": "5","-....": "6","--...": "7","---..": "8","----.": "9","/":" "}
encode = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.-- ","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"," ":"/"}
check = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"," "]
usah = input("Input text(no caps)/morse:")
aws = ""
if usah[0:1] == "-" or usah[0:1] == ".":
    des = ""
    for i in usah:
     if i != " ":
            des += i
     else:
            aws += decode.get(des)
            des = ""
    aws += decode.get(des)
if usah[0:1] in check:
    x = "false"
    for i in usah:
       if x == "true":
          aws += " "
       aws += encode.get(i)
       x = "true"
print (aws)
