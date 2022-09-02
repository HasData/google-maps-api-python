# Google Maps API
[Scrapeit Cloud](https://scrape-it.cloud/) - Web Scraping API with Proxy Rotation. Get valuable data at scale in HTML format from any website without need for a proxy.

Interface to call [Google Maps Scraper](https://scrape-it.cloud/google-maps-scraper) easily from Python.

## Install

    pip install sc-google-maps-api

## Usage
Signup to Scrapeit Cloud to  [get your API key](https://app.scrape-it.cloud/sign-up)  and some free credits to get started.

    >>> from sc_google_maps_api import ScrapeitCloudClient
    >>>
    >>> client = ScrapeitCloudClient(api_key='INSERT_YOUR_API_KEY_HERE')
    >>>
    >>> response = client.scrape(
        params={
            "keyword": "plumber in new york",
            "country": "US",
            "domain": "com"
        }
    )
    >>>
    >>> response.text
    '{"status":"ok","scrapingResult":{"pagination":{"start":0},"locals":[{"position":1,"title":"Hub Plumbing & Mechanical","phone":"+1 917-634-8888","address":"103 Charles St, New York, NY 10014, United States","website":"http://www.hubplumbingnyc.com/","rating":4.6,"reviews":53,"type":"Plumber"},{"position":2,"title":"Rite Plumbing & Heating","phone":"+1 347-502-6441","address":"750 Lexington Ave 9th Floor, New York, NY 10022, United States","website":"http://www.riteplumbingnyc.com/","rating":4.3,"reviews":37,"type":"Plumber"},{"position":3,"title":"RR Plumbing Roto-Rooter","phone":"+1 212-687-1215","address":"450 7th Ave Ste B, New York, NY 10123, United States","website":"https://www.rotorooter.com/manhattan/","rating":4.7,"reviews":702,"type":"Plumber"},{"position":4,"title":"Plumbing NYC","phone":"+1 347-973-9186","address":"510 W 45th St apt 11g, New York, NY 10036, United States","website":"https://plumbingnyc.com/","rating":4.9,"reviews":48,"type":"Plumber"},{"position":5,"title":"Plumber New York","phone":"+1 646-604-0862","address":"134 W 28th St, New York, NY 10001, United States","website":"null","rating":4.9,"reviews":48,"type":"Plumber"},{"position":6,"title":"WaterHouse Plumbing Company","phone":"+1 212-777-3003","address":"171 Attorney St, New York, NY 10002, United States","website":"https://waterhouse.nyc/","rating":4.4,"reviews":14,"type":"Plumber"},{"position":7,"title":"Emergency Plumbing Solutions","phone":"+1 646-374-3144","address":"106 W 19th St, New York, NY 10011, United States","website":"null","rating":5,"reviews":43,"type":"Plumber"},{"position":8,"title":"Near Plumber CO","phone":"+1 646-736-6681","address":"7 Waverly Pl, New York, NY 10003, United States","website":"null","rating":4.9,"reviews":47,"type":"Plumber"},{"position":9,"title":"Emergency Plumb CO","phone":"+1 646-736-6297","address":"398 Broome St, New York, NY 10013, United States","website":"null","rating":5,"reviews":45,"type":"Plumber"},{"position":10,"title":"Manhattan Sewer Drain","phone":"+1 212-641-0256","address":null,"website":"http://www.manhattansewerdrain.com/","rating":4.9,"reviews":28,"type":"Plumber"},{"position":11,"title":"L & R Plumbing","phone":"+1 646-760-3415","address":"491 3rd Ave, New York, NY 10016, United States","website":"null","rating":5,"reviews":29,"type":"Plumber"},{"position":12,"title":"The Pump Guys LLC. Pump & Motor Specialist","phone":"+1 212-239-1094","address":"1177 6th Ave 5th floor, New York, NY 10036, United States","website":"https://thepumpguys.solutions/","rating":5,"reviews":42,"type":"Plumber"},{"position":13,"title":"Super Plumbers Heating and Air Conditioning","phone":"+1 201-345-5128","address":null,"website":"https://superplumbersnj.com/services/nj/hudson-county/hoboken/","rating":4.6,"reviews":92,"type":"Plumber"},{"position":14,"title":"24 Hour Plumber NYC","phone":"+1 646-693-6598","address":"101 Lexington Ave, New York, NY 10016, United States","website":"http://24hourplumber.nyc/","rating":4.4,"reviews":13,"type":"Plumber"},{"position":15,"title":"Neo Plumbing & Heating Corp Plumber service in Manhattan","phone":"+1 646-860-0149","address":"10 E 39th St Suite 909, Manhattan, NY 10016, United States","website":"https://neoplumbingnyc.com/","rating":5,"reviews":14,"type":"Plumber"},{"position":16,"title":"New York Drain Restoration inc","phone":"+1 212-693-7246","address":"225 W 12th St, New York, NY 10011, United States","website":"null","rating":4.7,"reviews":16,"type":"Plumber"},{"position":17,"title":"X Y T Plumbing & Heating Chelsea","phone":"+1 646-588-0266","address":"125 W 33rd St, New York, NY 10001, United States","website":"null","rating":5,"reviews":12,"type":"Plumber"},{"position":18,"title":"24 HR Emergency Plumber NYC INC","phone":"+1 866-219-9182","address":null,"website":"https://24hremergencyplumber.info/nyc/","rating":5,"reviews":45,"type":"Plumber"},{"position":19,"title":"Super Sewer Man","phone":"+1 212-799-1605","address":"3 Little W 12th St, New York, NY 10014, United States","website":"null","rating":5,"reviews":15,"type":"Plumber"},{"position":20,"title":"Tri Star Plumbing & Heating Inc","phone":"+1 212-925-0006","address":null,"website":"null","rating":5,"reviews":7,"type":"Plumber"}]}}'
    >>>

You can find all the supported parameters on [Scrapeit Cloud documentation](https://scrape-it.cloud/docs/).
