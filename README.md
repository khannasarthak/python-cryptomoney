# python-cryptomoney
A ticker that shows my cryptocurreny portfolio as a desktop notification after a set interval of time


**Usage:**
* One time use:

	Download the script ```myportfolio.py``` and execute it from the correct directory. 

	```
	python3 myportfolio.py
	```

* Running at regular intervals using crontab:

	1. 
	


* To change your region, edit the marked areas in the script ```myportfolio.py```.

	```python
	### CHANGE THESE IF NEEDED ###

	myeth = <your ethereum amount>
	mybtc = <your bitcoin amount>

	##############################
``

**Requirements:**

* Python 3
* The libnotify library, download instructions given [here](http://www.devdungeon.com/content/desktop-notifications-python-libnotify)
* Tested for Ubuntu 16.04 but should work with 14.04 as well.

**Errors/Troubleshooting:**

