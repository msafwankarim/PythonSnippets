
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Friday, 19 March 2021 8:47:58 PM                                        #
#       Brief:      Following code will base64 encoded churan with custom domain lock.      #
#                 > This script wrap the input(JS) code into a condition and encodes string #
#                   to base64.                                                              #
#                 > Code will generate infinite alertboxes on site if it is used on any     #
#                   other than domains given in input                                       #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import base64
import ctypes
import tkinter as tk
import random

h_userdll = ctypes.WinDLL("User32.DLL")
frame = tk.Tk()

inputtxt = tk.Text(frame,
                   height=20,
                   width=80)
outputTxt = tk.Text(frame, height=20, width=80)
storeLink = tk.Text(frame, height=1,width=30)
myShopifyLink = tk.Text(frame, height=1,width=30)


def gen_varname():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='_0x'+ hex_number[2:]
    return hex_number

def main():
    domain1 = str(storeLink.get(1.0,"end"))
    domain2 = str(myShopifyLink.get(1.0,"end"))
    code = get_code()

    if len(domain1) == 1  or len(domain2) == 1 or code is None:
        h_userdll.MessageBoxW(None, "Some input is missing","Error",0)
        # print("Some input is missing")
        return
    
    code = domain_lock(get_code(),[domain1,domain2])
    code = code.strip()
    code = gen_obfuscated_code(code)
    code = bytes(code).decode("UTF-8")
    varname = gen_varname()
    code = f'''let {varname} = "{code}";Function(window["\\x61\\x74\\x6F\\x62"]({varname}))();'''
    print(code)
    outputTxt.delete(1.0,"end")
    outputTxt.insert(1.0, code)
    
    # with open("output.txt") as file:
    #   pass
    pass


printButton = tk.Button(frame,
                        text="Encode",
                        command=main)

printButton.grid(row = 10,column =10)


def get_code():
    
    source_str = inputtxt.get(1.0, "end")
    if len(source_str) == 1:
        return None
    return ''.join(source_str.split('\n'))


def domain_lock(code: str, domains: list) -> str:
    # print(domains)
    condition_string = f'''
    if(window.location.href.indexOf(\"{domains[0]}\") > -1 || window.location.href.indexOf(\"{domains[1]}\") > -1  || window.location.href.indexOf(\"shopifypreview.com\") > -1) {{ {code} }}
    else {{ while(true) alert("Unauthorized use of code detected") }}
    '''
    condition_string = ''.join(condition_string.split('\n'))
    condition_string = ' '.join(condition_string.split(' '))

    print(condition_string)
    return condition_string


def gen_obfuscated_code(s_code: str) -> str:
    bytecode = s_code.encode("utf-8")
    b_64 = base64.b64encode(bytecode)
    return b_64
    pass


frame.title("JS code Obfuscator")
frame.geometry('900x850')

tk.Label(frame,text="Shopify store link").grid(row=1,column=1,padx=10,pady=10)
storeLink.grid(row=1,column=2,pady=10)
tk.Label(frame,text="MyShopify link").grid(row=1,column=3,padx=10,pady=10)
myShopifyLink.grid(row=1,column=4,padx=5,pady=10)
printButton.grid(row=1,column=5)
tk.Label(frame,text="Source").grid(row=2,column=3,padx=10,pady=10)
inputtxt.grid(row=3,column =2,columnspan=3,pady=10)
tk.Label(frame,text="Output").grid(row=4,column=3,padx=10,pady=10)
outputTxt.grid(row=5, column=2,columnspan=3,pady=10)

frame.mainloop()
