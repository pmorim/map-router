import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Plotting settings
plt.figure(dpi=1200)
sns.set_style('white')
sns.set_context('talk')

# Read the data from .csv files
coords = pd.read_csv('./data/localidades.csv', index_col='Localidade')
routes = pd.read_csv('./data/rotas.csv', header=None)
routes.fillna('-', inplace=True) # Replace 'NaN' for '-'

# Plot the locations
plt.figure(figsize=(9.35, 18.12)) # Size of the original map (in inches)
plot = sns.scatterplot(data=coords, x='x', y='y', color='black')

# Use the map as background
img = plt.imread("./img/map.png")
plot.imshow(img)

# Iterate through all routes
for i, route in routes.iterrows():
    # Create a DataFrame for the route
    df = pd.DataFrame(columns=['x', 'y'])

    # Iterate through all locations in the route
    for location in route:
        if location != '-':
          df = df.append(coords.loc[location])

    # Draw the route
    df = df.astype({'x': int, 'y': int}) # Convert coordinates to integers
    plot.plot('x', 'y', '', data=df)

# Remove axis
plot.set(xticklabels=[], yticklabels=[], xlabel=None, ylabel=None)
sns.despine(left=True, bottom=True)

# Set the correct size and ratio
plot.set_xlim(0, 935)
plot.set_ylim(1812, 0)

# Save the plot
plt.savefig('./img/rotas.png', pad_inches=0, bbox_inches='tight')

# Signal end of script
print('Script executada com sucesso')