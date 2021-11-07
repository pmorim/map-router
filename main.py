import click

from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


@click.command()
@click.option("-d", "--dest", "dest_csv", required=True, help="The CSV of the destinations")
@click.option("-r", "--routes", "routes_csv", required=True, help="The CSV of the routes")
@click.option("-m", "--map", "map_img", required=True, help="The map image")
@click.option("-o", "--out", "out_img", required=True, help="The output image")
def main(dest_csv, routes_csv, map_img, out_img):
    """Draw individual routes on a given map."""

    # Plotting settings
    plt.figure(dpi=300)
    sns.set_style('white')
    sns.set_context('talk')

    # Read the given data
    coords = pd.read_csv(dest_csv, index_col='Destination')
    routes = pd.read_csv(routes_csv, header=None)
    routes.fillna('-', inplace=True)  # Replace 'NaN' with '-'
    img = Image.open(map_img)

    # Initialize the plot
    width, height = img.size
    plt.figure(figsize=(width / 100, height / 100))

    # Draw the map and destinations
    plot = sns.scatterplot(data=coords, x='x', y='y', color='black')
    plot.imshow(img)

    # Close the original map image
    img.close()

    # Iterate through all routes
    for _, route in routes.iterrows():
        # Create a DataFrame for the route
        df = pd.DataFrame(columns=['x', 'y'])

        # Iterate through all locations in the route
        for location in route:
            if location != '-':
                df = df.append(coords.loc[location])

        # Convert coordinates to integers
        df = df.astype({'x': int, 'y': int})

        # Draw the route
        plot.plot('x', 'y', '', data=df)

    # Remove axis
    plot.set(xticklabels=[], yticklabels=[], xlabel=None, ylabel=None)
    sns.despine(left=True, bottom=True)

    # Set the correct size and ratio
    plot.set_xlim(0, width)
    plot.set_ylim(height, 0)

    # Save the final image
    plt.savefig(out_img, pad_inches=0, bbox_inches='tight')

    # Signal end of script
    print('Routes drawn successfully')


if __name__ == '__main__':
    main()
