def get_user_information():
    print("=" * 40)
    print("      User Information Form")
    print("=" * 40)

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")
    city = input("Enter your city: ")

    print("\n" + "=" * 40)
    print("       User Information")
    print("=" * 40)
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Gender : {gender}")
    print(f"Email  : {email}")
    print(f"City   : {city}")
    print("=" * 40)


if __name__ == "__main__":
    get_user_information()