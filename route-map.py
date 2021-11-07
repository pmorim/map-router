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
@click.option("--size-ratio", default=100, show_default=True, help="Change this value if you are experiencing issues with the resolution of the output image")
def route_map(dest_csv, routes_csv, map_img, out_img, size_ratio):
    """Draw individual routes on a given map."""

    # Plotting settings
    click.echo("Applying initial styles... ", nl=False)
    plt.figure(dpi=300)
    sns.set_style('white')
    sns.set_context('talk')
    click.echo('Done')

    # Read the given data
    click.echo("Reading the given data... ", nl=False)
    coords = pd.read_csv(dest_csv, index_col='Destination')
    routes = pd.read_csv(routes_csv, header=None)
    routes.fillna('-', inplace=True)  # Replace 'NaN' with '-'
    img = Image.open(map_img)
    click.echo('Done')

    # Initialize the plot
    width, height = img.size
    figsize = (width / size_ratio, height / size_ratio)
    plt.figure(figsize=figsize)

    # Draw the map and destinations
    click.echo("Drawing the destination points... ", nl=False)
    plot = sns.scatterplot(data=coords, x='x', y='y', color='black')
    plot.imshow(img)
    click.echo('Done')

    # Iterate through all routes
    with click.progressbar(
        routes.iterrows(),
        length=len(routes.index),
        label="Drawing the routes..."
    ) as bar:
        for _, route in bar:
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

    # Add final style touches
    click.echo("Applying final styles... ", nl=False)
    plot.set(xticklabels=[], yticklabels=[], xlabel=None, ylabel=None)
    sns.despine(left=True, bottom=True)
    plot.set_xlim(0, width)
    plot.set_ylim(height, 0)
    click.echo('Done')

    # Save the final image
    click.echo(f"Saving output as \"{out_img}\"... ", nl=False)
    plt.savefig(out_img, pad_inches=0, bbox_inches='tight')
    click.echo('Done')

    # Close the original map
    img.close()


if __name__ == '__main__':
    route_map()
