import requests
import tomli
from authlib.integrations.requests_client import OAuth2Session
from requests.exceptions import HTTPError

# LOAD IN CONFIG FILE
with open("config.toml", mode="rb") as conf:
    config = tomli.load(conf)


class NPIListsWithAttributes:
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

    # CREATE NPI LIST WITH ATTRIBUTES
    def create_npi_list_with_attributes(self, token, account_id: int, new_list: dict):
        """
        Method to get all npi lists for an account

        Params:
            - token (string): Generated token from main.py
            - account_id (string): Account ID from the account user wants to use
            - new_list (dict): Dictonary of new list

            Example of new_list:

            {
                "attributeValues": [
                    [ "SomeCampaignName_1, "PulsePoint Inc." ],
                    [ "SomeCampaignName_2, "PulsePoint Inc." ],
                ],
                "attributes" ["CampaignName", "CompanyName" ]
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

        # TODO: Test EP to see if we can create a list with attributes

        try:
            res = conn.post(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/{account_id}/attributes",
                json=new_list,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"New List Successfully create:\n{new_list}")

                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error

    # REPLACE A NPI LIST WITH ATTRIBUTES
    def replace_a_list_with_attributes(self, token, list_id: int, npis: dict):
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

        # TODO: Test the EP with the attributes

        try:
            res = conn.put(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}/attributes",
                json=npis,
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(f"Succssfully replaced:\n{npis}")

        except requests.exceptions.HTTPError as error:
            raise error

    # VIEW A NPI LIST WITH ATTRIBUTES
    def view_a_list_with_attributes(self, token, list_id: int):
        """
        Method for getting a single NPI list

        Params:
            - token (string): Generated token from main.py
            - list_id (int): List ID the user wishes to collect

        Returns:
            JSON response from succesful call to EP or an HTTPError if False
        """
        conn = self.establish_connection(token)

        #  TODO: Test EP to see it can retrieve list attributes

        try:
            res = conn.get(
                f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}/attributes"
            )
            res.raise_for_status()

            if res.status_code == requests.codes.ok:
                print(res.json())

                return res.json()

        except requests.exceptions.HTTPError as error:
            raise error
