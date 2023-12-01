import requests
import tomli
from authlib.integrations.requests_client import OAuth2Session
from requests.exceptions import HTTPError

# LOAD IN CONFIG FILE
with open("config.toml", mode="rb") as conf:
    config = tomli.load(conf)


class NPIListsOnly:
    def __init__(self, token=None, account_id=0):
        self.token = token
        self.account_id: int = account_id

    # USER AUTHENTICATION
    @staticmethod
    def get_user_token(username, password):
        """
        Generates user token for connection

        Params:
            - username (string): The users username
            - password (string): The users password

        Returns:
            Created user token via .fetch_token
        """
        try:
            if (
                not config["pp_auth"]["client_id"]
                or not config["pp_auth"]["client_secret"]
            ):
                raise ValueError("client_id or client_secret missing")

            client = OAuth2Session(
                config["pp_auth"]["client_id"], config["pp_auth"]["client_secret"]
            )

            return client.fetch_token(
                config["pp_auth"]["url"],
                authorization_response=config["pp_auth"]["url"],
                username=username,
                password=password,
                grant_type="password",
            )
        except HTTPError as err:
            raise err

    def return_client(self, token):
        """
        Creates client requiered to connect

        Params:
            - token (string): Returned token

        Returns
            OAuth2 Session
        """
        return OAuth2Session(
            config["pp_auth"]["client_id"],
            config["pp_auth"]["client_secret"],
            token=token,
        )

    def establish_connection(self, token):
        return self.return_client(token)

    # GET NPIS FROM A LIST
    def get_a_single_npi_list(self, token: str, list_id: int):
        """
        Method for getting a single NPI list

        Params:
            - token (string): Generated token from main.py
            - list_id (int): List ID the user wishes to collect

        Returns:
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.get(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}"
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(res.json())

                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error

    # GET ALL NPI LISTS ASSOCIATED WITH AN ACCOUNT
    def get_all_account_npi_lists(self, token: str, account_id: int):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use

        Returns
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.get(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/{account_id}"
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(res.json())

                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error

    # CREATE AN NPI LIST
    def create_an_npi_list(self, token, account_id: int, new_list: dict):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use
            - new_list (dict): Dictonary of new list

            Example of new_list:

            {
                "name":"TEST_2022_1",
                "npis":["3137933127","3134730121"],
                "advertisers": ["Demo"],
                "application": "signal"
            }

            Application can take the following: "signal" / "life". If application is not present "life" is default.

        Returns
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.post(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/{account_id}",
                json=new_list,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"New List Successfully create:\n{new_list}")

                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error

    # REPLACE AN NPIS IN A LIST
    def replace_npis_in_list(self, token, list_id, npis):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use
            - npis (list): List of NPI numbers

            Example of npis:

            {
                "npis":["3137933127","3134730121"]
            }

        Returns
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.put(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}",
                json=npis,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"Succssfully replaced:\n{npis}")

        except requests.exceptions.HTTPError as error:
            raise error

    # ADD NPIS TO A LIST
    def add_npis_to_a_list(self, token, list_id, npis):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use
            - npis (list): List of NPI numbers

            Example of npis:

        {
            "operation":"add",
            "npis":["3137933122", "3134730123"]
        }


        Returns
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.patch(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}",
                json=npis,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"Succssfully added:\n{npis}")

        except requests.exceptions.HTTPError as error:
            raise error

    # DELETE NPIS FROM A LIST
    def remove_npis_from_list(self, token, list_id, npis):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use
            - npis (list): List of NPI numbers

            Example of npis:

        {
            "operation":"remove",
            "npis":["3137933122", "3134730123"]
        }


        Returns
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        try:
            res = conn.patch(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}",
                json=npis,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"Succssfully removed:\n{npis}")
                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error
