# Map Router

> A simple Python CLI tool that draws routes/paths on a given map.

## Index

- [Installation](#installation)
- [Usage](#usage)
- [Docs](#docs)
- [Why?](#why)
- [License](#license)
- [Support](#support)

## Installation

> *Coming soon...*

## Usage

To use this tool you need the some files, lets say the files are, for example, like this:

- `map.png` is the image of your map;
- `dest.csv` is the CSV file with your destinations' names and pixel coordinates on your map;
- `routes.csv` is the CSV file with your routes.

> Examples of such files can be found [here](/example).

You would then use the CLI like this:

```bash
route-map -d dest.csv -r routes.csv -m map.png -o routes.png
```

And you would get a `routes.png` file with the routes drawn on top of the map.

## Docs

You can check the updated docs by using the `--help` flag:

```bash
route-map --help
```

## Why?

A friend of mine had an assignment where he needed to calculate the most optimal routes for a transportation company. Then, in order to help him, I created this tool to aid him in verifying and displaying the routes results.

## License

MIT @pmorim

## Support

If you found this plugin useful, consider buying me a coffee ☕ (or a beer 🍺) and leaving a thank you message.

<a href="https://www.buymeacoffee.com/pmorim" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 42px !important;width: 150px !important;" ></a>