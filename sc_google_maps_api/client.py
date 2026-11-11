from requests import request, Response

from .default_headers import default_headers


def _to_api_params(params: dict) -> dict:
    # Old parameter names (keyword, country, domain: "com") still work
    result = dict(params)
    keyword = result.pop("keyword", None)
    country = result.pop("country", None)

    if keyword is not None:
        result.setdefault("q", keyword)

    if country is not None:
        result.setdefault("gl", str(country).lower())

    domain = result.get("domain")
    if domain and not str(domain).startswith("google."):
        result["domain"] = f"google.{domain}"

    return result


class ScrapeitCloudClient:
    api_url = "https://api.hasdata.com/scrape/google-maps/search"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def scrape(
        self,
        params: dict,
        **kwargs
    ) -> Response:
        headers = {
            "x-api-key": self.api_key
        }

        headers.update(default_headers)
        params["source"] = "python_sdk"

        return request(
            "GET",
            self.api_url,
            params=_to_api_params(params),
            headers=headers,
            **kwargs
        )
