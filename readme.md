The simple_encrypt program enc.py was written in python 2.7 using standard imported python modules. 

The simple interface implements XOR encryption on any file type to generate an encrypted file. 

Note that simple, one-pass XOR encryption with short passwords is not inherently secure. 
This program is only intended to encrypt data from casual observers. 

The output of the encrypted file is printed to the terminal so that you can assess the level of obscurity introduced by your password. Note that longer passwords provide enhanced obscurity, but large numbers of repeated characters in the unencrypted file can make your password vulnerable even to visual inspection (e.g., repeated spaces are common). An added layer of security is recommended, by implementing two passwords of dissimilar length, the longer the better. Do this by generating an encrypted file once, then encrypting that file with a second password. 
The output of each encryption/decryption operation is automatically printed to the terminal window. 

Run the program with the command "python enc.py". 
You will be prompted to select a task and then prompted for a file name. 
You can supply a file path to another directory, but it is most straightforward to put the program enc.py in the same folder as the file to be encrypted. The new file will be saved to the folder where enc.py is located.  

Your password is not stored anywhere and acts on the document data directly. Do not lose or forget your password or you will be unable to recover your file (if you choose to delete the original). 

Text documents, pictures, videos, or programs are all encrypted with equal ease using this python script. 
