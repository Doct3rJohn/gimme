import base64

UNIVERSAL = "Usage: gimme.py [-h][-l] [-t/--type] [-i/--lhost] [-p/--lport] [-s][-o]"

def help_me():
    print(UNIVERSAL)

    print("""Optional Arguments:
    -t, --type      type of reverse shell
    -i, --lhost     local ip address
    -p, --lport     listening port
    -s, --shell     type of shell
    -o, --output    save it to the file
    -e, --encoding  encode the reverse shell
    """)

    print("""Options:
    -h, --help      show this help message and exit
    -l, --list      list all the available reverse shell
    """)

    print("Example: gimme.py -t bash -i 10.10.10.10 -p 4444")
    print("Example: gimme.py -t bash -i 10.10.10.10 -p 4444 -s /bin/sh")
    print("Example: gimme.py -t python3 -i 10.10.10.10 -p 4444 -o shell.py ")

def output_file(name, shell):
    with open(name, 'w') as file:
        file.writelines(shell)

def encode_base64(data):
    encoded_bytes = base64.b64encode(data.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    return encoded_string

def list_all():
    print("""[!] All list of reverse shell available
    01) bash
    02) nc
    03) awk
    04) python2
    05) python3
    06) golang
    07) ruby
    """)

    print("""[!] All list of encoding available
    01) base64
    """)



