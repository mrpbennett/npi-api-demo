import tomli

from npi_api_class import NPIListAPIClass

# LOAD IN CONFIG FILE
with open("config.toml", mode="rb") as conf:
    config = tomli.load(conf)


# Token generation
auth_token = NPIListAPIClass.get_user_token(
    config["user"]["username"], config["user"]["password"]
)

# Class instance
npi_class_instance = NPIListAPIClass(auth_token)


def main():
    """
    NOTE:
    We will pass the above auth_token in all out function calls. Please change the list ID 11105 to the one you require testing
    """

    choice = 3

    if choice == 1:
        # GET NPIS FROM A LIST
        """
        Here we are passing the list id of the list we want to see.
        """
        npi_class_instance.get_a_single_npi_list(auth_token, 11105)

    if choice == 2:
        # GET ALL NPI LISTS IN ACCOUNT
        """
        Here we are passing the account ID of the account we wish to see the NPIS lists from.
        """
        npi_class_instance.get_all_account_npi_lists(
            auth_token, config["user"]["account"]
        )

    if choice == 3:
        # CREATE AN NPI LIST
        """
        Here we pass the account ID of the account we wish to create a new list in. We then pass a dictonary that makes up the new list.
        """

        npi_class_instance.create_an_npi_list(
            auth_token,
            config["user"]["account"],
            {
                "name": "NPI_API_Test",
                "npis": [
                    "8764993000",
                    "5543273120",
                    "1946244481",
                    "4643250396",
                    "5434452949",
                    "1869330916",
                    "7345557628",
                    "7058916326",
                    "7377085327",
                    "6327354843",
                ],
                "advertisers": ["Demo_Test"],
            },
        )

    if choice == 4:
        # REPLACE NPIS IN A LIST
        """
        Here we pass the list ID of the list we wish to replace NPIs on. We then pass a dictonary with a list of NPIs we wish to replace.
        """
        npi_class_instance.replace_npis_in_list(
            auth_token,
            11105,
            {
                "npis": [
                    "1829357489",
                    "3954877148",
                    "5013953921",
                    "4532758659",
                    "6669093303",
                ]
            },
        )

    if choice == 5:
        # ADD NPIS TO A LIST
        """
        Here we pass the list ID we wish to add NPIs to. Then we pass a dictonary with the operation of "add" and a list of NPIs.
        """
        npi_class_instance.add_npis_to_a_list(
            auth_token,
            11105,
            {
                "operation": "add",
                "npis": ["9210415290", "3148428680"],
            },
        )

    if choice == 6:
        # DELETE NPIS FROM A LIST
        """
        Here we pass the list ID we wish to delete from. Then we pass a dictonary with the operation of "remove" and a list of NPIs.
        """
        npi_class_instance.remove_npis_from_list(
            auth_token,
            11105,
            {
                "operation": "remove",
                "npis": [
                    "5543273120",
                    "1946244481",
                    "4643250396",
                    "5434452949",
                    "1869330916",
                    "7345557628",
                    "7058916326",
                    "7377085327",
                    "6327354843",
                ],
            },
        )


if __name__ == "__main__":
    main()
