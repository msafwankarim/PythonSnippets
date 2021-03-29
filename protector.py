'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Saturday, 6 March 2021 1:56:21 AM                                       #
#                                                                                           #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sqlite3
import argparse
import os

db_conn = ""
def init():
    global db_conn
    user = os.environ.get('USERNAME')
    
    db_conn = sqlite3.connect(f"C:\\Users\\{user}\\file_name.db")
    if db_conn is None:
        raise ConnectionError("Error in finding file")


def find(domain):
    query = "SELECT * FROM temporary WHERE domain='"+domain+"';"
    # print(query)
    cursor = db_conn.execute(query)
    for row in cursor:
        print(f"{row[2]}")


def main():
    init()
    parser = argparse.ArgumentParser(description="Argument Switch parser")
    parser.add_argument("-d", "--domain", metavar='domain',
                        type=str, help='title for the phrase')
    parser.add_argument("-a", "--all", action='store_true',
                        help='Get list of all domains')
    # parser.add_argument("-p", "--phrase", action="store",
                        # help="Phrase to store")
    # parser.add_argument('-p','--phrase',metavar='phrase',type=str, help='pharase to store')

    listall = parser.parse_args().all
    domain = parser.parse_args().domain
    # phrase = parser.parse_args().phrase

    # print(parser.parse_args())
    if domain is None and not listall:
        parser.print_help()
    elif listall:
        cursor = db_conn.execute("SELECT domain FROM tablename")
        print("Domain\n=======")
        for row in cursor:
            print(row[0])

    elif domain:
        find(domain)


main()
