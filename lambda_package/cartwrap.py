import subprocess
import io
from threading import Thread
from queue import Queue
import re
import math

def reader(pipe, pipe_name, queue):
    try:
        with pipe:
            for line in iter(pipe.readline, b''):
                queue.put((pipe_name, line))
    finally:
        queue.put(None)

# This function invokes the C code to calculate a cartogram for a given gen and area input.
# It returns a generator that yields its output on stdout and stderr in the format:
#
#   source, line
# 
# where source is a string (either 'stdout' or 'stderr'), and line is a string.
#
# It takes as input:
#
# area_data:            A string containing appropriately formated area data
# gen_file:             A string containing the path to the appropriate .gen file
# cartogram_executable: A string containg the path to the C code executable
def generate_cartogram(area_data, gen_file, cartogram_executable, world=False):

    flag = '-s'
    if world == True:
        flag = '-sw'
        
    cartogram_process = subprocess.Popen([
        cartogram_executable,
        '-g',
        gen_file,
        flag
    ],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=1)

    q = Queue()

    Thread(target=reader,args=[cartogram_process.stdout, "stdout", q]).start()
    Thread(target=reader,args=[cartogram_process.stderr, "stderr", q]).start()

    cartogram_process.stdin.write(str.encode(area_data))
    cartogram_process.stdin.close()

    for _ in range(2):
        for source, line in iter(q.get, None):
            yield source,line
    
    #output, errors = cartogram_process.communicate(bytes(area_data, 'UTF-8'))

    #return io.StringIO(output.decode())



        
        

                    






