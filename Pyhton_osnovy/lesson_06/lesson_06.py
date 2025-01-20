
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    # [a-zA-Z0-9.-_]@[a-zA-Z0-9].[a-z]
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    print(re.match(pattern, email))

    def is_valid_email(email):
        # [a-zA-Z0-9.-_]@[a-zA-Z0-9].[a-z]
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            print("valid")
        else:
            print("not valid")

    is_valid_email("asdfgfdsd@sda.re")


    import re

    def is_valid_email(email):
        # [a-zA-Z0-9.-_]@[a-zA-Z0-9].[a-z]
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            print("valid")
        else:
            print("not valid")

    is_valid_email("asdfgfdsd@sda.re")

