# type_file = input("Put the type of file: ")

# if type_file.endswith(".gif" )  :
#     print("image/gif" ) 
# elif  type_file.endswith(".png")  :
#     print("image/png")
# elif type_file.endswith(".jpg") or type_file.endswith(".jpeg") :
#     print("image/jpg")
# elif type_file.endswith(".pdf") :
#     print("application/pdf")
# elif type_file.endswith(".zip"):
#     print("application/zip")
# elif type_file.endswith(".txt"):
#     print("text/txt")
# else:
#     print("application/octet-stream")

type_file = input("Put the type of file: ").lower().strip()

if type_file.endswith((".gif", ".png", ".jpg", ".jpeg")):
    print("image/" + type_file.split(".")[-1])
elif type_file.endswith((".pdf", ".zip")):
    print("application/" + type_file.split(".")[-1])
elif type_file.endswith(".txt"):
    print("text/plain")
else:
    print("application/octet-stream")