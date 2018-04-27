Milestone 2
===========

README
------

* We used python's SciPy machine learning laboratory to implement Gaussian Process Regression.
  * We used the RBF kernel function and the Matern kernel funciton smoothing parameters.
  * Our dataset was constructed using manually downloaded MIDI files as described in the data section
* Our biggest difficulty again was ensuring that our dataset was large enough to support tenfold cross validation while still doing meaningful learning. This time, we were able to triple the size of our dataset by spending more time collecting files. We also tried to balance the dataset, ending up closer to a 50/50 split of D key and G key pieces.
* Resources used:
  * SciPy
  * http://jsbach.net/midi/
  * [musescore.com](http://musescore.com)
* To run the code, simply run the GPwithCV python file. The function should be pointed two csv files formatted as described in the data section. Each file should contain bag-of-notes information about a body of pieces in a single key. We include our own csv files, constructed with midi2bagofratio_2.py, but anything in the same format would also funciton.
