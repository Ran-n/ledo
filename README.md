# Ledo
Ledo is a encrytion algorithm that uses both substitution and transposition of the characters. Also, the key is automatically made the same length as the text is.  
This program can be used both as a command line utility and a interactive program (with no gui).

-------

## Donations

| Coin 			| Address 										|
| ------------ 	| ------------ 									|
| Bitcoin 		| bc1q4gj3t0f4aulrn7z3dtgfxrxsv5c323x5yzvz7r 	|

## Install
git clone --recursive https://github.com/Ran-n/ledo

## Configuration
In the configuration file (.config on the root folder) you have many elements you can tinker with that come well explained in both gallician and english.  
A important change might be to the language (its set to gallician by default), only if you opt for the interactive option since the command line execution type does not prompt messages that would have to be translated. Supported languages are gallician, english and spanish.

## Execution
You can execute the following 'python3 main.py -h' or 'python3 main.py -?' to get the description of the elements for the command form of the program. If you opt for the interactive form the messages will be self explanatory.  
### For the command version
python3 main.py -c/-d -p password {-e entry text} {-i}  
They may be in any order and, if spaced, must be surrounded by '' or "" (as is usual in this cases)  
-c -> calls the code operation  
-d -> calls the decode operation  
>> These are mutually exclusive, if used -c do not use -d and viceversa.  
-e entry_text -> if configured not take text input by file you must put this option, if you put it and the configuration is set to take input from file it will be ignored  
-i -> same as -e but the input will be taken from standard input. This is useful to chain it with unix commands like echo, sed, etc  
>> These are mutually exclusive, if used -e the -i option will be ignored.  

### For the interactive version
python3 main.py  
From there messages will point you the direction, beware to change the language as is set to gallician by default.
