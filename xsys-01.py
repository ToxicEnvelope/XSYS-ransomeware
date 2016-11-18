#!/usr/bin/python

import os, sys, platform, random, pkg_resources
import base64
from Crypto.Hash import SHA256
from Crypto.Cipher import AES




# pause program
def pause():
    Pause = raw_input(" Press on <ENTER> key to continue...\n " )
    return Pause

# clear console
def clear_console():

    p = platform.platform() # indentiy OS paltform - Windows, Linux, Darwin
    win = []
    linux = []
    drw = []
    if p.startswith('Win') or p.startswith('win'):   # check if namespace starts with Win || win
       win = lambda: os.system('cls')                #return prompt command  to clear the console screen 
       return win()
    elif p.startswith('Lin') or p.startswith('lin'): # Lin || lin
       linux = lambda: os.system('clear')
       return linux()
    else:
       drw = lambda: os.system('clean')              # Mac || IBM
       return drw()



# encrypt files
# Parmas:
# key <= password
# filename <= filename
def encrypt(key, filename):
    chunkSize = 65 * 1024       # size of data char encrypted 65,792 bytes
    outFile = os.path.join(os.path.dirname(filename), ".(encrypted)"+os.path.basename(filename)) # add marker to filename
    fileSize = str(os.path.getsize(filename)).zfill(16) # get the size of filename and fill with 16 bytes binary of zeros
    IV = ''  # initialize vector - randomize cipher modes
    for i in range(16):
        IV += chr(random.randint(0, 0xFF))        # random ASCII 0-255 chars into IV

    encryptor = AES.new(key, AES.MODE_CBC, IV)    # append (password, encryption in char.cipher.blocks ,randomize IV
    encoder = base64

    with open(filename, 'rb') as infile:          # as we opend filename > readbinary code
         with open(oudFile, 'wb') as outfile:     # stream binary code of filename and randIV into outfile 
              outfile.write(filename)
              outfile.write(IV)
              while True:
                    chunk = infile.read(chunkSize)      # append 65,792 byte encryption stream file into chunk
                    if len(chunk) == 0:                      # exit in chunk bytes equal to 0
                        break
                    elif len(chunk) % 16 != 0:               # if length of stream file size is 4bit and not equal to 0
                         chunk += ' ' * (16 - (len(chunk) % 16)) # fake size of encrypted file stream

                    encChunk = encryptor.encrypt(chunk)
                    enChunk = encoder.b64encode(encChunk)
                    outfile.write(enChunk)  # write encrypted data into outfile




# decrypt files  <FBI's Part>
# paramas:
# key <= password
# filename <= filename
def decrypt(key, filename):
    outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[12:])) # stream filename to outFile 
    chunkSize = 64 * 1028                         # size of data char encrypted 65,792 bytes
    with open(filename, 'rb') as infile:          # as we opend filename > readbinary code
         fileSize = infile.read(16)               # read 16 encypted chars and append to fileSize
         IV = infile.read(16)                     # stream 16 char randomized IV into IV

    decryptor = AES.new(key, AES.MODE_CBC, IV)    # append password into IV  and decipher its using char.cipher.blocks
    decoder = base64

    with open(outFile, 'wb') as outfile:
         while True:
               chunk = infile.read(chunkSize)
               if len(chunk) == 0:
                  break

               deChunk = decoder.b64decode(chunk)
               decChunk = decryptor.decrypt(deChunk)
               outfile.write(decChunk)   # decrypt the encrypted file

         outfile.truncate(int(fileSize))  # stream and sort the ASCII numeric value of chars decrypted chars


""" 
# allfiles <scan for files in current directory>
 def allfiles():
      allFiles = []                                        # init allFiles as array
      for path, dirs, files in os.walk(os.path.getcwd()):   # scan for the current working directory of the process
          for dir in path:                              # run through all the filenames
              allFiles.append(os.path.join(path, dir))   # add filenames full path in to allFiles Array

      return allFiles()                            # return the files list from allFiles Array
""" 


# allfiles <get all dirs and files from specific path>
# parmas:
# initpath <= path to scan
def allfiles(initpath):
    allFiles = []
    for path, dirs, files in os.walk(os.path.abspath(initpath)):
        if len(dirs) == 0:
            break
        else:
            allFiles.append(path, dirs)
            pass
        if len(files) == 0:
            break
        else:
            allFiles.append(path, files)

        return allFiles


clear_console()                                      # clear the console screen

# print the programs menu
print "\n\t\t################################"
print "\t\t## ~~~~~~~~ XSYS 1.0 ~~~~~~~~ ##"
print "\t\t##   Encrypt   ||   Decrypt   ##"
print "\t\t## ~~~~~~~~~~~~~~~~~~~~~~~~~~ ##"
print "\t\t## .....M.a.d.e....B.y....... ##"
print "\t\t##    Yahav   N   Hoffmann    ##"
print "\t\t##            A.K.A.          ##"
print "\t\t##     M  a  ~  F  a  r  $    ##"
print "\t\t################################"
print ""    
print ""    
print " ATTENTION !!! "
print ""    
print " This program may cause harm to your computer files system, machine functionality,"
print " personal data and private information."
print ""    
print " XSYS is a tool that build an Hierarchical Tree diagram of"
print " all files from your root folder and its descendants until its (E)ncrypt || (D)ecrypt any leaf"
print " in the system tree diagram.\n"
print " if you wish to EXIT this program,\n press Ctrl+C now.\n"
pause()

initpath = raw_input(" Enter a root path for scan: ")
choice = raw_input(" Do you want to (E)ncrypt or (D)ecrypt? ")
# password = raw_input(" Enter encryption key: ")  <-  move into the condition blocks

encFiles = allfiles(initpath)                                 # run main function recursively

if choice == "E":                                              # if choose "E"
   password = raw_input(" Enter encryption key: ")             # get keyinput from user
   for Tfiles in encFiles:                                     # run through all target files in encrypted file list
       if os.path.basename(Tfiles).startswith(".(encrypted)"): # check if add marker to filename exist
           print " %s is already encrypted" %str(Tfiles)        # print to user
           pass        # move in
       elif Tfiles == os.path.join(os.path.abspath(initpath), sys.argv[0]):
      # elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):  # check if target files equal to current runing process folders input
           pass        # move on
       else:
           encrypt(SHA256.new(password).digest(), str(Tfiles))  # digest the keyinput from target files and encrypt it using SHA256 key
           print " Done encrypting %s" %str(Tfiles)      # print the encrypted files results
           os.remove(Tfiles)                                   # remove the original files

elif choice == "D":                                            # if choose "D"
     filename = raw_input(" Enter the filename to decrypt: ")  # get filname from user
     password = raw_input(" Enter decryption key: ")            # get keyinput from user
     if not os.path.exists(filename):                          # check if filenames path exists
         print " The file does not exist"               # print message to user
         sys.exit(0)   # exit the program
     elif not filename.startswith(".(encrypted)"):             # check if add marker to filename exist
         print " %s is already not encrypted" %filename # print message to user
         sys.exit()    # exit the program
     elif not password:
         print " wrong decryption key!"
         sys.exit()
     else:
         decrypt(SHA256.new(password).digest(), filename)      # digest the keyinput from target files and decrypt it using SHA256 key
         print " Done decrypting %s " %filename         # print message to user
         os.remove(filename)                            # remove the encrypted file

else:
     print " Please choose a valid choice."             # print message to user
     sys.exit()        # exit the program

