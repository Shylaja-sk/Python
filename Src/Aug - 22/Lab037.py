#match - match the o/p amd execute
#syntax -
#match variable:
#case pattern1:
#code block
#case pattern2:
#code block

#write a prg to ask the user which browser he wants to run the program
browser = input("Enter the browser name\n")
browser = browser.lower()
match browser:
    case "firefox":
        print("Execute the firefox code")
    case "Chrome":
        print("Execute the Chrome code")
    case "Safari":
        print("Execute the Safari code")
    case _:
        print("Browser Not found")
