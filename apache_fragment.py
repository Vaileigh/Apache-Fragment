#!/usr/bin/python3 -tt
# DJS 2016
import re
import sys

# Global empty dictionaries store [url,domain,email]
sanitized_urls      = {}    
sanitized_domains   = {}
sanitized_emails    = {}

def sanitize(input_file):   # Collect data of [url,domain,email]
    apache_contents = input_file.readlines()                       # Assign all content in to apache_contents line by line
    if(isinstance(apache_contents,bytes)):                         # If statement: convert bytes to string if necessary
        apache_contents = apache_contents.decode('utf-8','ignore') # Page_ contents was decode('utf-8')
    
    for line in apache_contents:    # For loop: loop each line in a apache_fragment.log
        
        # Get all URLs |eg: "http://www.apple.com/go/applebot" : 1)
        url = re.findall(r'(?<=http://)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',line)  # Get url by regex
        url = re.sub(r"\)",'',str(url)) # Delete braket if url url included
        if url in sanitized_urls:       # If statement: url exist in sanitized_urls
            sanitized_urls[url] += 1    # Increase the frequency by 1
        else:                           # Else statement: url doesn't exist in sanitized_urls
            sanitized_urls[url] = 1     # Add new url
        # Counts the number of requests made to each domain |eg: '80 156.53.200.217': 1
        domain = re.findall(r'(?<=uk:).*?(?=\s\-\s\-)',line)  # Get domain by regex
        domain = str(domain)                # Make sure domain is string
        if domain in sanitized_domains:     # If statement: url exist in sanitized_domains
            sanitized_domains[domain] +=1   # Increase the frequency by 1
        else:                               # Else statement: domain doesn't exist in sanitized_domains
            sanitized_domains[domain] = 1   # Add new domain
        
        # Makes a list of all the email addresses it finds | eg: fizz.cmp.uea.ac.uk: 1
        email = re.findall(r'^\w+.cmp.uea.ac.uk',line)  # Get email by regex
        email = str(email)                  # Make sure email is string
        if email in sanitized_emails:       # If statement: url exist in sanitized_emails
            sanitized_emails[email] +=1     # Increase the frequency by 1
        else:                               # Else statement: email doesn't exist in sanitized_emails
            sanitized_emails[email] = 1     # Add new email

    
def main():
    if len(sys.argv) != 2:                          # User doesn't input second arguments or more than 2
        print ('usage: ./apache_fragment.py file')
        print (sys.argv)
        sys.exit(1)             # Program terminated
    filename = sys.argv[1]      # Second user input as filename
    
    try:        # Try: try to open user input file
        input_file = open(filename, 'r')    # Open the file
    except (IOError) as ex:                 # Except: failed to open the file
        print('Cannot open ', filename, '\n Error: ', ex)

    else:
        sanitize(input_file)   # Function call - sanitize()
    
        # Print urls with frequence
        sanitized_url = {val[0] : val[1] for val in sorted(sanitized_urls.items(), key = lambda x: (-x[1], x[0]))}          # Sort by frequence
        print("\n///////\tURLs\t///////\n")
        count_urls = 0
        for x in sanitized_url:     # For loop: loop each url to print
            count_urls +=1
            print(count_urls,'.\t',x[1:-1], ':', sanitized_url[x],'\n')
            
            
        # Print domains with frequence
        sanitized_domain = {val[0] : val[1] for val in sorted(sanitized_domains.items(), key = lambda x: (-x[1], x[0]))}    # Sort by frequence
        print("\n///////\tDOMAINS\t///////\n")
        count_domains = 0
        for y in sanitized_domain:  # For loop: loop each domain to print
            count_domains +=1
            print(count_domains,'|\t',y[1:-1], ':', sanitized_domain[y])
            
        
        # Print urls with frequence
        sanitized_email = {val[0] : val[1] for val in sorted(sanitized_emails.items(), key = lambda x: (-x[1], x[0]))}      # Sort by frequence
        print("\n///////\tEMAILs\t///////\n")
        count_emails = 0
        for z in sanitized_email:   # For loop: loop each email to print
            count_emails +=1
            print(count_emails,'.\t',z[1:-1], ':', sanitized_email[z])
        
        # Calculate all total frequence [url,domain,email]
        count_urls = len(sanitized_url.keys())
        count_domains = len(sanitized_domain.keys())
        count_emails = len(sanitized_email.keys())
        
        # Print all total frequence [url,domain,email]
        print('\n\nURLS: ',count_urls,'\tDOMAINS: ',count_domains,'\tEMAILS: ',count_emails)

    finally:
        input_file.close()

    
if __name__ == '__main__':
  main()
