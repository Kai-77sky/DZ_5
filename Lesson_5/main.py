"""

Regular Expressions

"""

"""

Basic Patterns

"""

""" jack@gmail.com """

# email = input()
#
#
# def is_valid_email(mail):
#     try:
#         if mail.split('@')[0] \
#                 and mail.split('.')[0].split('@')[1] and mail.split('.')[1]:
#             print("Is Valid email!")
#         else:
#             raise ValueError
#     except:
#         print("Invalid email")
#
#
# is_valid_email(email)

import re

# email = input("eMail: ")
# is_valid = re.search(
#     r".+[a-zA-Z0-9]@(gmail|yandex|outlook|mail)\.(com|ru)",
#     email
# )
#
# try:
#     if is_valid.end() == len(email):
#         print("Email address Valid!")
#     else:
#         raise ValueError
# except:
#     print("Invalid email address!")

"""
+996-707-77-77-77
"""

phone = input("enter the number: ")
is_valid = re.search(
    r"\+996-([0-9]{3})-([0-9]{2})-([0-9]{2})-([0-9]{2})",
    phone
)
try:
    if is_valid.end() == len(phone):
        print("Phone number is valid!")
    else:
        raise ValueError
except:
    print("Phone number invalid!")

print(re.findall('Hello!', phone))

# """
# +996-707-77-77-77
# """
# phone = input()
# is_valid = re.search(
#     r"\+996-([0-9]{3})-([0-9]{2})-([0-9]{2})-([0-9]{2})",
#     phone
# )
# try:
#     if is_valid.end() == len(phone):
#         print("Phone number is Valid!")
#     else:
#         raise ValueError
# except:
#     print("Phone number invalid!")
#
# print(re.findall('hello', phone))
