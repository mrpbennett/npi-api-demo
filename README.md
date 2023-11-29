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

Now you're ready to test the API. Head over to `main.py` where you're able to
call each one of the endpoints via the `NPIListAPIClass` in `npi_api_class.py`.
To do this please follow the instructions within the comments. You will also
need to choose / create a list to test with. The ID in the cose `11105` **will
need to be changed**

When you're ready to test the endpoints, you will need to change the `choice`
selection to the relevant number.

Once this is changed you will need to create an environment by running the
following in the terminal:

```bash
pipenv shell
```

Once an environment has been created we can then run the program with our choice
selected.

```bash
pipenv run python main.py
```
