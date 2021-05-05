# The Jython system (originally known as JPython) is an alternative implementation of the Python language, targeted for integration with the Java programming language


# Stackless: Python for concurrency
# Stackless adds smicrothreads to Python. These are an efficient and lightweight alternative to Python's standard multi tasking tools such as threads and processes, and promise better program strucrtue, more readable code, and increased programmer productivity.

#PyPy: Python for speed.
# The PyPy system is another standard CPython reimplementation, fcoused on performance. 


#  What is the Python interpreter? 
# What runs your code
# A program that runs the Python programs you write

# 2. What is source code?
#  The code you write
# The statements you write for your programs after Python compiles it. Python automatically stores byte code in files with a .pyc extension.

# 3. What is byte code?
# What your code gets translated into in preperation to be read by the computer

# 4. What is the PVM?
# Python Virtual Machine. Reads your code line by line. Whats next?
# The runtime engine of Python that interprets your compiled byte code.

# 5. Name two or more variations on Python’s standard execution
#  model. 
# Psyco, Shed Skin, and frozen binaries are all varations on the escution model. In addition, the alternative implementations of Python named in the next two answers modify the model in some fashion as well by replacing byte code and VMs, or by adding tools and JITs.

# 
# 6. How are CPython, Jython, and IronPython different?
# CPython is the original and most stable. Jython is for Java, IronPython is for .NET

# # 7. What are Stackless and PyPy?
# For speadig up your code.
# Stackless is an enhanced version of Python aimed at concurrency, and PyPy is a reimplementation of Python targeted at speed. PyPy is also the successor to Psyco, and incorporates the JIT concepts that Psyco pioneered.