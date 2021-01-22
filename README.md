![](https://tokei.rs/b1/github/jobyid/strive_build_good_reads)
[![License: WTFPL](https://img.shields.io/badge/License-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# KMeans From Scratch
 
KMeans and KMeans++ implementation coded to understand the algorithm and add some tweaks. 

## Getting Started 

Call the class with KMeans() the following parameters are settable and the defaults are as below: 

- clusters = 2
	- The number of clusters you hope to separate your data into
- tolerance = 0.001
	- The percentage difference the centroids can tolerate before we stop seeking improvements  
- max_iterations = 500
	- Maximum number of times we try to improve centroids positioning, while tolerance level not met.   
- verification_loops = 1
	- Number of different centroid start positions we should test. This allows us to find the best start positions. 

You can the run the following methods. 

- fit(data)
	- Requires data in np.array format, and fits the data to the centroids with parameters as set above 
- predict(data)
	- Takes your data as an input and returns an array of cluster classifications 
- plot_results(data,d1,d2,c1,c2)
	- takes your data, and 4 coordinates for the data you want to plot. The 4 coordinates represent dimensions fo data, typically 0 and 1 are used. 