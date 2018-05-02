Milestone 4
===========

* We re-ran all of our previous tests (linear model, Gaussian, and Gaussian with PCA) with tenfold cross validation
  * For the linear model, we ran it on the updated dataset
  * We compared the mean average percent errors using a t-Test and found that with a high confidence (low p value), the unmodified Gaussian Process was superior to the other methods 
  
Specifically, we found that on one tailed t-Tests, it was extrememly likely that the mean average percent error of the Gaussian Process runs without dimensionality reduction was lower than that of the other two methods. Intuitively this makes sense, since dimensionality reduction isn't especially useful on our relatively small dataset, and the linear model is less flexible.

The biggest challenge we faced was ultimately determining how we wanted to compare the data. Based on just the raw results, it seemed clear to us that the unmodified Gaussian Process was superior, so we opted to check if it's mean average percent error was lower than that of the other tests.

In order to run these tests, simply use the files in this folder on the data from previous milestones.

Resources used:
  * Excel Analysis Tool-pack
  * Python's SciPy
