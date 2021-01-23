from kmeans import KMeans
import test_data
import data_prep as dp
two_d_test = test_data.two_d_data()
km_2d = KMeans(clusters=4, tolerance=0.01, verification_loops=5)
#km_2d.fit(two_d_test)
#print(km_2d.find_error())
#km_2d.plot_results(two_d_test, 0, 1,0,1)
#print(km_2d.predict(two_d_test))
#print("Loops: ", len(km_2d.loops))
km_2d.fit(dp.prep_file('cars_test.csv'))
lo = km_2d.loops
for l in lo:
    x = 0
    for key in l.classes.keys():
        x += len(l.classes[key])
    print("error Score: ", l.es ,'Class Len: ', x )
#km_2d.plot_results(dp.prep_file('cars_test.csv'), 0,1,0,1)
