# Jack Schefer, began 7/30/16
#
from subprocess import call
from sys        import argv
#
def main():
   #
   # 1. call the printer to write the js resource file
   args = ['python3', 'printer.py'] + argv[1:] # Use for Linux command line
   #args = ['Python', 'printer.py'] + argv[1:] # Use for Mac command line
   call(args)
   #
   # 2. call the map. TODO change this for your browser of choice
   args = ['firefox', 'map.html'] # Use for Linux command line
   #args = ['open', 'map.html'] # Use for Mac command line
   call(args)
   #
#
################################################################
#
if __name__ == '__main__':
   #
   main()
   #
#
# End of file
