import tomli

from npi_lists_only import NPIListsOnly
from npi_lists_with_attributes import NPIListsWithAttributes

# LOAD IN CONFIG FILE
with open("config.toml", mode="rb") as conf:
    config = tomli.load(conf)


# Token generation
npi_lists_only_auth = NPIListsOnly.get_user_token(
    config["user"]["username"], config["user"]["password"]
)

npi_lists_with_attributes_auth = NPIListsWithAttributes.get_user_token(
    config["user"]["username"], config["user"]["password"]
)

# Class instances
npi_lists_only = NPIListsOnly(npi_lists_only_auth)
npi_lists_with_attributes = NPIListsWithAttributes(npi_lists_with_attributes_auth)


def main():
    """
    NOTE:
    We will pass the above npi_lists_only_auth in all out function calls. Please change the list ID 11105 to the one you require testing
    """

    choice = 3

    if choice == 1:
        # GET NPIS FROM A LIST
        """
        Here we are passing the list id of the list we want to see.
        """
        npi_lists_only.get_a_single_npi_list(npi_lists_only_auth, 11105)

    if choice == 2:
        # GET ALL NPI LISTS IN ACCOUNT
        """
        Here we are passing the account ID of the account we wish to see the NPIS lists from.
        """
        npi_lists_only.get_all_account_npi_lists(
            npi_lists_only_auth, config["user"]["account"]
        )

    if choice == 3:
        # CREATE AN NPI LIST
        """
        Here we pass the account ID of the account we wish to create a new list in. We then pass a dictonary that makes up the new list.
        """

        npi_lists_only.create_an_npi_list(
            npi_lists_only_auth,
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
        npi_lists_only.replace_npis_in_list(
            npi_lists_only_auth,
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
        npi_lists_only.add_npis_to_a_list(
            npi_lists_only_auth,
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
        npi_lists_only.remove_npis_from_list(
            npi_lists_only_auth,
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

    """
    NPI list with attributes is an NPI list that appends a client's metadata to their list of NPIs. This  endpoint allows users to create an NPI list with attributes, replace an NPI list with attributes and view an  NPI list with attributes. 
    """

    if choice == 7:
        npi_lists_with_attributes.create_npi_list_with_attributes(
            npi_lists_with_attributes_auth, 12345, {"something": "..."}
        )

    if choice == 8:
        npi_lists_with_attributes.replace_a_list_with_attributes(
            npi_lists_with_attributes_auth, 12345, {"something": "..."}
        )

    if choice == 9:
        npi_lists_with_attributes.view_a_list_with_attributes(
            npi_lists_with_attributes_auth, 12345
        )


if __name__ == "__main__":
    main()
