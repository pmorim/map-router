# Map Router

> A simple python script to draw routes on a given map.

## Setup & Execution

It should go without saying that, before anything else, you need to clone the repository.

```bash
git clone https://github.com/pmorim/route-map.git
cd map-router
```

To setup you own map and destinations follow the steps below:
- Replace `in/map.png` with your map image;
- Update the `in/destinations.csv` file with your destinations' names and pixel coordinates on your map image;
- Write your routes in the `in/routes.csv`.

Then, you just need to simply execute the `main.py` script.

```bash
python3 main.py
```

After all this, your routes should be on `out/routes.png`

## License

MIT @pmorim
