def personal_info(**kwargs):
    return kwargs

print(personal_info(
    name = input('name: '),
    surname = input('surname: '),
    birthday = input('birthday: '),
    city = input('city: '),
    email = input('email: '),
    phone = input('phone: '),
))