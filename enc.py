#!/usr/bin/env python
import time,sys,os,subprocess,getpass
start = time.time()

def exit():	#exit
	print 'exiting...';print
	sys.exit()

def valid_name(file):	#ensure file to encrypt exists
	if ( (os.path.exists(file)  ) or file == 'q'):
		return True
	print 'Filename or file path invalid; try again'
	return False

def main():
	print;print;print '###### simple encrypt ######'
	print ' _Encrypt or Decrypt your files_';print
	task = ''; edq = ['e','d','q']; edq_alert = ['encrypt','decrypt']
	chars = ''.join([chr(x) for x in range(128)])
	while task not in edq: 
		task = raw_input('__Select option__ \n   e: encrypt \n   d: decrypt \n   q: quit \n Enter command: ')
	if task == 'q': exit()#exit
	else:
		print '\t\t-->',edq_alert[edq.index(task)];print
		print 'Files in this folder:';print
		os.system('ls');print
		file = ''
		#file = raw_input('Enter filename, path, or q: ')
		while file == '' or not valid_name(file):
			file = raw_input('Enter filename, path, or q: ')
		if file == 'q': exit()#exit
		with open(file,'r') as f:
			file1 = f.read()
		pw = ''
		while pw == '' or not all([False if x not in chars else x for x in pw]):
			pw = getpass.getpass('Enter password for file '+edq_alert[edq.index(task)]+'ion (A-z,0-9,symbols):')
		file2 = ''; j = 0		
		for i in range(len(file1)):
			file2+=(chr(ord(file1[i]) ^ ord(pw[i%len(pw)])))	#create encoding sequentially
		print '\tThe file "'+file+'" was encrypted.'
		print 'New file:'
		print file2
		
		write_file = ''
		while write_file not in list('ynq'):
			write_file = raw_input('Write new file to disk? Type y, n, or q: ')
		if write_file in list('qn'):
			exit()#exit
		else:	#write file
			filename = ''
			while filename == '':
				filename = raw_input('Enter filename to write: ')
			with open(filename,'w') as f:
				f.write(file2)
			print '\tNew file saved as:',filename
			showfile = 'ls -al $(find '+str(filename)+')'
			proc = subprocess.Popen([showfile],stdout=subprocess.PIPE,shell=True)
			print '\tFile size:',proc.communicate()[0].split()[4],'bytes'
			#print 'current directory: '
			#os.system('pwd')
			exit()
	



if __name__ == '__main__':
	main()
print 'process completed in',time.time()-start,' s'