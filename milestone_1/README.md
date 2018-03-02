Milestone 1
===========

Folders
-------

Each milestone folder should include the following

* All code you wrote/used
* A README file

They should not include

* Datasets
	(we are including the csvs because they're small and they're our own custom aggregated data, if this is a bad idea, we can remove them)
* Large packages

README
------

The README file should include

* Description of what your team did
	We used python's scipy machine learning library to implement logistic linear classification with tenfold cross validation.
* Methods used to accomplish each part
	As a small group, our only task was milestone 1. We constructed a dataset using downloaded midi files and python. We used the built in scipy methods to perform the machine learning task.
* Potential difficulties faced
	Our biggest issue was finding a dataset of midi files that had the necessary information about the musical key of each piece. Because we could not find such a dataset, we manually appended the key information of a variety of pieces taken from a repository of midi transcriptions of J.S. Bach pieces.
* Resources used
	SciPy
	http://jsbach.net/midi/
	https://en.wikipedia.org/wiki/List_of_compositions_by_Johann_Sebastian_Bach
	
* Description of how to run the code in the folder
	Simply run the linModel10CV python file. In the code, it should be pointed at two .csv files: one should have bag-of-notes data from G Major pieces, the other from D Major pieces.
