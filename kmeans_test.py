from kmeans import KMeans
import test_data

two_d_test = test_data.two_d_data()
km_2d = KMeans(clusters=4, tolerance=0.01, verification_loops=5)
#km_2d.fit(two_d_test)
#print(km_2d.find_error())
#km_2d.plot_results(two_d_test, 0, 1,0,1)
#print(km_2d.predict(two_d_test))
#print("Loops: ", len(km_2d.loops))
km_2d.fit_plot(two_d_test,0,1,0,1)
