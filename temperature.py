import requests, os
from selectorlib import Extractor

class Temperature:
    """Represent a temperature value extracted from the timeanddate.com/weather webpage"""
    
    headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = "./temperature.yml"
    
    def __init__(self, country, city):
        self.country = country.replace(' ', "-")
        self.city = city.replace(' ', "-")
    
    def _build_url(self):
        """Builds the URL string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return(url)
    
    def _scrape(self):
        """Extracts a value as instructed by the yml file 
        and returns a dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)        
        return raw_content
    
    def get(self):
        """Cleans the output of _scrape"""
        scrapped_content = self._scrape()
        return float(scrapped_content["temp"].replace("°C", "").strip())

if __name__ == "__main__":
    temperature = Temperature(country="croatia", city="zagreb")
    os.system("cls")
    print(f"{temperature.get()} °C")