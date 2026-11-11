# Google Maps API
[HasData](https://hasdata.com/) - Web Scraping API with Proxy Rotation. Get valuable data at scale in HTML format from any website without need for a proxy.

Interface to call [Google Maps Scraper](https://hasdata.com/scrapers/google-maps) easily from Python.

## Install

    pip install sc-google-maps-api

## Usage
Signup to HasData to  [get your API key](https://app.hasdata.com/sign-up)  and some free credits to get started.

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
    '{"requestMetadata":{"id":"...","status":"ok","url":"https://www.google.com/maps/search/plumber+in+new+york?hl=en&gl=us"},"localResults":[{"position":1,"title":"Plumbing NYC","phone":"(646) 580-7524","address":"510 W 45th St Apt 11g, New York, NY 10036","website":"https://plumbingnyc.com/","rating":4.7,"reviews":45,"type":"Plumber",...},{"position":2,"title":"24 Hour Plumber NYC","phone":"(646) 693-6598","address":"101 Lexington Ave, New York, NY 10016","website":"http://24hourplumber.nyc/","rating":3.9,"reviews":15,"type":"Plumber",...},...]}'
    >>>

You can find all the supported parameters on [HasData documentation](https://docs.hasdata.com/apis/google-maps/search). The old names `keyword`, `country` and `domain: "com"` still work and are sent as `q`, `gl` and `domain: "google.com"`.
