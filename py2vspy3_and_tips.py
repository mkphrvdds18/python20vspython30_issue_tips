

# add this below to each file at the beginning

from __future__ import absolute_import, division, print_function

#note-1 
# in case you like to check the code execution status , place this below:
exit()

#note -2
#when interacting with the OS sytem or other application , error message, failure must be handled
# to continue running program to the end.
#manual run program before automation, and catch the exception , create exception tuples with common exceptions



#note - 3
#if you are running python script in Linux, it does not care what is xtension 'py' , it will open the file and run as Linux commands
# so must add , as 1st line of script "#!/usr/bin/env python " - must start with '#'

#!/usr/bin/env python
