"""
Contains classes pertaining to handling exceptions. Lets you abstract out
exception handling in your main code, improving its concision and readability.

Timo Brønseth, January 2020.
"""


class ExceptionHandler:
    """
    Lets you define and handle erroneous user inputs in a much more concise way.
    """

    @classmethod
    def query_options(cls,
                      query: str,
                      error_message: str,
                      options: list,
                      ignore_case: bool = False
                      ) -> str:
        """
        Queries the user for input, recursively calls itself until
        user has entered in one of the values defined in options.
        """

        user_input = input(query)

        if ignore_case:
            # Make both user_input and options lower case,
            # so that they're being compared in same case.
            user_input = user_input.lower()
            for i, option in enumerate(options):
                options[i] = option.lower()

        try:
            # Raise a ValueError if user_input does not match any of the items in options.
            if user_input not in options:
                raise ValueError

        except ValueError:
            # Function recursively calls itself if there's a ValueError,
            # and prompts the user again for a valid entry.
            print(error_message)
            user_input = cls.query_options(query, error_message, options, ignore_case)

        return user_input

    @classmethod
    def query_int(cls, query: str, error_message: str) -> str:
        """
        Queries the user for an integer, and recursively calls
        itself until user has successfully entered an integer.
        """
        user_input = input(query)

        try:
            # Raises a ValueError if user_input cannot be recast as integer type.
            if not user_input.isdigit():
                raise ValueError

        except ValueError:
            # Function recursively calls itself if there's a ValueError,
            # and prompts the user again for a valid entry.
            print(error_message)
            user_input = cls.query_int(query, error_message)

        return user_input
