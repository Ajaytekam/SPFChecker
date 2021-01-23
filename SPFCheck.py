#!/usr/bin/python3  

import requests
import re
import sys
from bs4 import BeautifulSoup  
import argparse  

def Write_data(dat):
    file = open("/tmp/spfRecord.html", "w")
    print("[+] Data written into '/tmp/spfRecord.html'")
    file.write(dat)
    file.close()

def Print_data(DErr):
    print("========| SPF Configuration |=========")
    for item in DErr:
        print(item.strip("\n"))
    print("======================================")

def main():
    # parsing 1st argument 
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Domain name to perform SPF Check", required=True)  
    args = parser.parse_args() 
    url = "https://www.kitterman.com/spf/getspf3.py"
    data = {'serial':'fred12', 'domain':args.domain}
    req = requests.post(url, data)
    req.text
    soup = BeautifulSoup(req.text, "html.parser")

    if(soup.body.findAll(text=re.compile(r'No valid SPF record found'))):
        print("[!] SPF record does not exsists") 
        print("[!] Domain is vulnerable to email spoofing.")
        Write_data(req.text)
        sys.exit()
    else:
        DataErr=soup.body.findAll(text=re.compile(r'\w*all\b'))  
        if len(DataErr):
            p_count=0
            n_count=0
            s_count=0
            for item in DataErr:
                if(re.findall("-all", item)):
                    p_count+=1
                elif re.findall("~all", item):
                    n_count+=1
                else:
                    s_count+=1
            if p_count == len(DataErr):
                print("[+] SPF record exists and secured.")
                Write_data(req.text)
                Print_data(DataErr) # create a function
            elif n_count <= len(DataErr):
                print("[!] The SPF Configuration is not secure.")
                print("[!] Domain is vulnerable to email spoofing.")
                Write_data(req.text)
                Print_data(DataErr) # create a function
                sys.exit
            elif s_count:
                print("[!] The SPF Configuration may not be secure.")
                print("[!] There is a possibility of email spoofing.")
                print("[!] Please check manually.")
                Write_data(req.text)
                Print_data(DataErr) # create a function
                sys.exit            
        else:
            print("[!] The SPF Configuration is not secure.")
            print("[!] Domain is vulnerable to email spoofing.")
            Write_data(req.text)
            sys.exit

if __name__ == "__main__":
    main()
