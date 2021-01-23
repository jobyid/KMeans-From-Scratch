import sys
import click
import data_prep as dp
import kmeans as km

@click.command()
@click.option("-fit_predict/-fit_plot",'-pr/-pl',default=True, help="Choose to run a prediction or a plot of your data")
#@click.option("-fit_plot",'-k++', help="Enter your CSV data path in quotes")
@click.option("--clusters","-cl", default=2,  type=int, show_default=True, help="Set the number of clusters default=2")
@click.option("--tolerance","-t", default=0.001,  type=float, show_default=True, help='Tolerance level for fitting centroids, default=0.001')
@click.option("--max_it", "-m", default=500,  type=int, show_default=True, help="Max number of iterations to converge centroids, default=500")
@click.option("--error_loops","-e", default=1,  type=int, show_default=True, help="Number of tries to get best centroid start point, default=1")
@click.option("--plus_plus/--standard","-p/-s", default=False,show_default=True, help="Choose between standard Kmeans or Kmeans++, default is standard")
@click.option('--file', '-f', prompt="Please provide a file path to check, file must only contain numbers string or object columns will cause an error ")

def k_means_away(fit_predict, clusters, tolerance, max_it, error_loops, plus_plus, file):
    print("Now we are clustering")
    X = dp.prep_file(file)
    k_m = km.KMeans(clusters=clusters, tolerance=tolerance,k_plus_plus=plus_plus, max_iterations=max_it, verification_loops=error_loops)
    if fit_predict:
        # run the fit predict module
        k_m.fit_predict(X)
    else:
        # run fit plot
        k_m.fit_plot(X,0,1,0,1)
    del k_m

if __name__ == '__main__':
    k_means_away()
