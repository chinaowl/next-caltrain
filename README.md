# Next Caltrain

## GTFS file

1. Download the latest GTFS file from Caltrain [here](http://www.caltrain.com/developer.html).
2. Replace the contents of `scripts/gtfs`.

## Database setup

1. On Mac, install [Postgres.app](https://postgresapp.com/) and follow the instructions to create a new server.
2. I also had to add this line to my `.zshrc` file: `export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin`.
3. From the command line, run `createdb next_caltrain` and `createuser next_caltrain_user`.
4. In `scripts/create_tables.sql`, replace `path` with the correct absolute path.
5. Run `psql -U next_caltrain_user -d next_caltrain -a -f scripts/create_tables.sql`.

## Python environment

1. I'm using `python2` and `pip2`, installed with `homebrew`. See [here](https://docs.brew.sh/Homebrew-and-Python.html) as a starting point.
2. Make sure you have `virtualenvwrapper` installed. See instructions [here](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).
3. `mkvirtualenv next-caltrain`
4. `workon next-caltrain`
5. `pip2 install -r requirements.txt`
