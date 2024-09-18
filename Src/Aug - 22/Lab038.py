user = input("Enter the user type - admin, Manager or guest\n")
match user:
    case "admin" |  "manager":
        print ("Hello sir")
    case "guest":
        print ("Hello guest")
    case _:
        print("Hello there")
