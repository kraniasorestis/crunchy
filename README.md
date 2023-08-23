# crunchy
A python script that takes a simple wordlist as input and produces a dictionary with thousands of possible passwords based on the input wordlist. 


For the script to work you have to provide a file named "input.txt" in the same directory where you'll run the script.

The "input.txt" should contain a list of names from whatever you think your target is interested in. For instance if the taret likes LotR you could ask something like ChatGPT to give you a list of characters and location names from the world of LotR which should follow a wordlist formating (one item per line):

Frodo Baggins
Gandalf
Aragorn
Legolas
Gimli
Samwise Gamgee
Gollum
Saruman 
Dáin Ironfoot
Frerin
Thorin Oakenshield
The Shire
Rivendell
Mirkwood
Lothlórien
Isengard
Minas Tirith
Helm's Deep
Rohan

Once you have that, just run the script and it will work on the provided file to generate a nice wordlist for a dictionary attack, which will be saved in the same folder.

The generated wordlist will contain:
 - the provided words in both lowercase format and with the first letter capitalized
 - conjoined words (ie instead of "Minas Tirith" > "minastirith" )
 - reversed lowercase words
 - appended chronologies both "normally" and in reverse with and without dashes at the back end of the lowercase stuff
 - it converts special vowels like "é" to "e"
 - leet stuff like: 
   "@" instead of "a",
   "1" instead of "i",
   "0" instead of "o"



The script is under GNU Public Licence v3, so do what you want with it. You just have to publish under the same licence.

Happy cracking
