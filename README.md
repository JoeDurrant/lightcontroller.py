# lightcontroller.py
A quick Flask app to control power Christmas lights using the Energenie PiMote.
Uses the ENER010 radio controlled 4 way extension lead, and Energenie's add on board for the Raspberry Pi to create a web
interface for turning on and off outdoor lights. 

The separate files for each function are used in a crontab, to turn them on and off automatically at specific times.
