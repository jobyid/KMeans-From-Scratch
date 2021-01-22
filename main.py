import sys
import click


@click.command()
@click.option("-KMeans",'-k', help="Enter your CSV data path in quotes")
@click.option("-KMeans++",'-k++', help="Enter your CSV data path in quotes")

def k_means_away():
    print("Now we are clustering")
if __name__ == '__main__':
    k_means_away()
