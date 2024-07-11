import qrcode

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 20,
                   border = 2)

#Creates QR and Names the file
def link(website, img_name):
    qr.add_data(website)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{img_name}.png')

#Main
def main():
    print("Welcome to the QR Code Generator!")
    print("Enter in 1 to Continue or 0 to Exit")
    inp = input()

    #Loop till break
    while True:

        #Prompt User for link and file name
        if(inp == '1'):
            print("Please enter in a website link:")
            website = input()
            print(website)

            print("Please enter in a name for the link:")
            img_name = input()
            print(img_name)
            link(website, img_name)

        #Exit
        elif(inp == '0'):
            return
        
        #Error Catch for Invalid Numbers
        else:
            print("ERROR: INVALID INPUT")
            print("Enter in 1 to Continue or 0 to Exit")
            inp = input()

        #Re-Prompt User
        print("Enter in 1 to Continue or 0 to Exit")
        inp = input()

main()