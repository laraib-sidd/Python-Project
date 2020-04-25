import requests
import sys, hashlib


def request_api_data(query_char):
#this fucntion will take data query data and return response
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines( ))       #This line breaks the returned result into tuples of hash code and the times the password is hacked
    
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        

    
def pwned_api_check(password):
#Checks if passowrd exists in api response
    sha1password = hashlib.sha1(password.encode("utf-8 ")).hexdigest().upper()  #this line encodes the normal password in hexadecimal encoding with sha1 hashing
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response,tail)
    

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f"Your password {password} has been pwned {count} times ")
        else:
            print(f"Your passowrd {password} is super secure")
    return 'done!'


if __name__ == '__main__': 
    sys.exit(main(sys.argv[1:]))
  
