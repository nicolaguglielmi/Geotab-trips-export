# Geotab trips export
In past I needed to export from the Geotab system some tracking device records of specific trip to something usable in another system, like .csv or .kml for further analysis.
I wrote several small utility scripts to get different data in different formats

config.py
---------
Set your authentication data and script variables

trip_to_kml.py
--------------
This is a little utiliy to export trips of a single vehicle of a specific day in kml format.

get_fleet_speed.py
------------------
This exports the whole fleet visible by the user you use to authenticate, positions and speed, for a range of date
that you have to set in config.py
A single file for each date, for each vehicles will be create in the data/ folder
If the fleet is big and the data range wide, you could encounter some limits of the filesystem for the hight number of files you create in a folder. In this case I suggest to use an higher value of data_range in config.py to accregate the data, link for week or for month

These scripts require the my-geotab python lib, please install as first step:
https://github.com/Geotab/mygeotab-python
