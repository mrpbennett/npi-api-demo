# Pulsepoints NPI API demo repo

Here we have a working Python class that performs each task of the API.

To get started clone this repo

```bash
git clone https://github.com/mrpbennett/npi-api-demo.git
```

If you haven't already please install
[pipenv](https://pipenv.pypa.io/en/latest/)

```bash
pip install --user pipenv
```

OR

```bash
brew install pipenv
```

If you're using [Homebrew](https://brew.sh/)

Once the repo has been cloned, from the command line enter the root directory
and run the following:

```bash
pipenv install
```

This will install all the dependencies. Next, you will need to create a
`config.toml` file in the root directory of this project. The file should have
the following layout: (please replace `xxx` with your details, your account
manager will need to provide you with the pp_auth info.)

```toml
[pp_auth]
client_id = 'xxx'
client_secret = 'xxx'
url = 'https://lifeapi.pulsepoint.com/RestApi/oauth/token'


[user]
username = "xxx"
password = "xxx"
account = "xxx"
```

### Our current API request restrictions are as follows

- `GET`: 1 request per 1 second
- `PUT`, `POST`, `PATCH`, `DELETE`: 10 requests per 60 seconds

### Get Started

Now you're ready to test the API. Head over to `main.py` where you're able to
call each one of the endpoints via the `NPIListsOnly` in
[`npi_lists_only.py`](https://github.com/mrpbennett/npi-api-demo/blob/main/npi_lists_only.py).

Or if you wish to create an NPI list with attributes please use the endpoints in
the class `NPIListsWithAttributes` located in
[`npi_lists_with_attributes.py`](https://github.com/mrpbennett/npi-api-demo/blob/main/npi_lists_with_attributes.py)
To do this please follow the instructions within the comments. You will also
need to choose / create a list to test with. The ID in the code `11105` **will
need to be changed**

When you're ready to test the endpoints, you will need to change the
[`choice`](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/main.py#L25)
variable to the relevant number depending on which endpoint you wish to test.
The choices are as follows:

1. [Get a single NPI list](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L70)
2. [Get all NPI lists from an account](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L98)
3. [Create an NPI list](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L126)
4. [Replace NPIs within a list](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L164)
5. [Add NPIs to a list](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L198)
6. [Remove NPIs from a list](https://github.com/mrpbennett/npi-api-demo/blob/07dbb63143cb9393b695c665ef0e5d4dc28d1509/npi_lists_only.py#L234)

For NPI lists with attributes please choose from 7 onwards.

7. [Create a single list with attributes](...)
8. [Replace an NPI list with attributes](...)
9. [Get an NPI list with attributes](...)

Once this is changed you will need to create an environment by running the
following in the terminal:

```bash
pipenv shell
```

Once an environment has been created we can then run the program with your
choice selected.

```bash
pipenv run python main.py
```
