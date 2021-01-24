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
- k_plus_plus = False 
	- Bool which turns KMeams++ on or off 
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
	- takes your data, and 4 coordinates for the data you want to plot. The 4 coordinates represent dimensions fo data, typically 0 and 1 are used. returns a scatter plot of your data as classified by the best classifier loop.

## Command line
If you want to run a quick classification analysis then you can use the library from the command line. Either producing a plot of your data or an array of classifications matching your data. The command line can be controlled with the following options: 

Options:
  -fit_predict, -pr / -fit_plot, -pl
                                  Choose to run a prediction or a plot of your
                                  data

  -cl, --clusters INTEGER         Set the number of clusters default=2
                                  [default: 2]

  -t, --tolerance FLOAT           Tolerance level for fitting centroids,
                                  default=0.001  [default: 0.001]

  -m, --max_it INTEGER            Max number of iterations to converge
                                  centroids, default=500  [default: 500]

  -e, --error_loops INTEGER       Number of tries to get best centroid start
                                  point, default=1  [default: 1]

  -p, --plus_plus / -s, --standard
                                  Choose between standard Kmeans or Kmeans++,
                                  default is standard  [default: False]

  -f, --file                 Enter the file path, the file should be a
                                  csv and contain numbers only
  --help                          Show this message and exit.