print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import requests
from bs4 import BeautifulSoup

# Define the list of websites to scan
websites = ['http://example.com', 'http://example2.com']

# Loop through each website and run WPScan
for website in websites:
    # Run WPScan using the subprocess library
    output = subprocess.check_output(['wpscan', '--url', website])

    # Parse the output using BeautifulSoup
    soup = BeautifulSoup(output, 'html.parser')

    # Extract the relevant data and save it to a file
    vulns = soup.find_all('div', {'class': 'vuln'})
    with open('output.txt', 'a') as f:
        f.write(f"Vulnerabilities for {website}:\n")
        for vuln in vulns:
            f.write(f"{vuln.text}\n")
