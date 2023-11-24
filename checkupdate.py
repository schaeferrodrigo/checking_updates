import requests
from bs4 import BeautifulSoup
import hashlib

def get_webpage_content(url):
    response = requests.get(url)
    return response.text

def get_hash(data):
    # Using hashlib to create a hash of the data
    return hashlib.sha256(data.encode()).hexdigest()


def main():

    webpages = { 'UAB': "https://www.uab.cat/web/personal-uab/personal-uab/personal-academic-i-investigador/convocatories-1345661836642.html" ,
            'UPC': "https://treballa.upc.edu/ca/convocatories-de-concursos/Concursos-pdi-laboral-temporal" ,
            'UPF' :"https://www.upf.edu/web/personal/ofertes-pdi",
            'UdG' : "https://www.udg.edu/ca/coneix/treballa-a-la-udg/personal-docent-i-investigador/convocatoria-de-places-de-professorat-contractat",
            'UdG_posdoc' : "https://www.udg.edu/ca/coneix/treballa-a-la-udg/personal-docent-i-investigador/Ofertes-de-treball-temporal/Detall?convo=9179",
            'CRM': "https://www.crm.cat/job-board/"
    }

    for key in webpages:
        
        url = webpages[key]
        previous_data_filename = key+"previous_data.txt"

        # Fetching current data from the webpage
        current_data = get_webpage_content(url)
        current_hash = get_hash(current_data)

        try:
            # Reading the previous hash from a file
            with open(previous_data_filename, "r") as file:
                previous_hash = file.read()

            # Comparing current hash with the previous hash
            if current_hash == previous_hash:
                print(key+' '  + "No new information.")
            else:
                print(key + ' ' + "Webpage has new information!")

        except FileNotFoundError:
            # If the file doesn't exist, treat it as the first run
            print("First run. Storing current information.")
    
        # Storing the current hash for future comparisons
        with open(previous_data_filename, "w") as file:
            file.write(current_hash)

if __name__ == "__main__":
    main()
