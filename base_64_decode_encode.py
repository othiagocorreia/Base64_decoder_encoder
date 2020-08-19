
import base64
choice=input('What you want to do?\n Decode\n Encode\n')

if choice=='Encode':
    data=input('Give me a data\n')
    encodedBytes=base64.b64encode(data.encode("utf-8"))
    encodedStr= str(encodedBytes, "utf-8")

    print(encodedStr)

if choice=='Decode':
    dataFind=input('Give me a data\n')
    decodeBytes=base64.b64decode(dataFind)
    decodeStr=str(decodeBytes, "utf-8")

    print(decodeStr)

else:
    print(choice)


