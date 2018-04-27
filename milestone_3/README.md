Milestone 3
===========

README
------

* We used python's SciPy machine learning laboratory to implement SVD with PCA.
  * We used the PCA object from SKLearn
    * We tried automatically determining the dimensions by leaving the _end components_ attribute of the object unset
    * We also decided to just reduce to 8 dimensions, since that is the number of distinct notes in the G and D major scales combined.
  * Our dataset was constructed using manually downloaded MIDI files as described in the data section
  * We visualized the data using the SKLearn manifold's t-distributed stochastic neighbor embedding (TSNE).
    * This was done using PCA with automatically decided dimensions
    * The reduced data was projected into two dimensions. In our implementation, the key of D major is blue and the key of G major is red
* The biggest difficulty in dimensionality reduction was just ensuring that the matricies lined up so that PCA would reduce the number of dimensions, rather than the number of samples. We also had a bit of trouble choosing how many dimensions to manually reduce to, since we weren't sure how many notes were actually important, and the automatic reduction would waver between 11 and 8 out of 12 different pitches.
* Resources used:
  * SciPy
  * [http://jsbach.net/midi/](http://jsbach.net/midi/)
  * [musescore.com](http://musescore.com)

* Running the code: To run the Gaussian process with dimensionality reduction, execute the PCA_GPwithCV.py function, ensuring that the gKeyData.csv and dKeyData.csv files are in the same directory. It will print the average percent error of tenfold cross validation in three different ways:
  * With all 12 dimensions
  * With dimensions automatically determined by SKLearn
  * With the number of dimensions manually set to 8
In order to visualize it, run the data_vis.py. A graph of the data projected onto two dimensions using the TSNE function will be shown.

* We think that dimensionality reduction doesn't give good results on our data, because each dimension is fairly important. The dimensions are each possible semitone pitch classes, so depending on the specific musical pieces, different pitch classes might be more useful than others. The keys of D major and G major share 6 out of the 7 pitches in their major scale, so it might be the case that the best way to discern which is which is to look at the accidentals that are more common in one key versus another. On the other hand, accidentals (pitches on in the major scale of the key) appear infrequently and might be misleading, particularly if the accidental in one key is part of the major scale of the other key. We think that the variability in what pitches are important is what causes dimensionality reduction to give slightly worse results than the full 12 dimensional Gaussian process.
