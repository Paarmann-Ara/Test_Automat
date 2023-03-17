Conventions.
    A. Indentation
	    # Aligned with opening delimiter.
	    foo = long_function_name(var_one, var_two,
	                             var_three, var_four)

	B. Imports
		from subprocess import Popen, PIPE

	C. Whitespace in Expressions and Statements
		spam(ham[1], {eggs: 2})
		foo = (0,)
		ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
		spam(1)
		dct['key'] = lst[index]
		x = 1
		x = x*2 - 1
		def munge(sep: AnyStr = None) -> PosInt:
		def complex(real, imag=0.0):
		if foo == 'blah':
		    do_blah_thing()
		
	D. Naming Conventions
		* 	Non-public method begin with a single underscore
		** 	with words separated by underscores

		Packages
			lowercase

		Module
			lower case

		Class 
			UpperCaseCamelCase
		
		Functions 
			lowercase

		Variable
			lowercase

		Bool Variable
			is_ + lowercase

		Arguments
			lowercase

		Global
			should be all lowercase

		Constant
			fully capitalized

pip3 freeze > requirements.txt

Create repository
        python3 -m venv C:\OneDrive\TestCaseExec\.venv
        Create pth file in C:\OneDrive\TestCaseExec\.venv\Lib\site-packages\WAWi.pth contain(c:\\OneDrive\\TestCaseExec)
        cd C:\OneDrive\TestCaseExec\.venv\Scripts -> activate.bat

install Package
        selenium==3.141.0
        Appium-Python-Client==1.0.2
        win32gui
        comtypes==1.1.14
        pyodbc==4.0.35
        pywin32==305
        pywinauto==0.6.8
        PyYAML==6.0
        six==1.16.0

pip3 install -r requirements.txt