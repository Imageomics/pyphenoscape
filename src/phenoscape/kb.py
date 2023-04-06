import os
import requests

KB_API_URL = os.environ.get("KB_API_URL", "https://kb.phenoscape.org/api/v2")


def _get_kb_json_response(path, params):
    """Performs GET request to KB API for path and params.

    Parameters:
    path (str): Path added to end of the KB API URL.
    params (dict): Key/values to be passed to KB API.

    Returns:
    dict: Dictionary or list from KB API.
    """
    response = requests.get(f"{KB_API_URL}{path}", params=params)
    response.raise_for_status()
    return response.json()


def get_term(iri):
    """Returns a dictionary of info for a term IRI.

    Parameters:
    iri (str): IRI of the term to fetch info about.

    Returns:
    dict: Dictionary response from /term KB API
    """
    return _get_kb_json_response("/term", {"iri": iri})


def term_search(text, match_types=None):
    """Returns a list of terms(dict) for search text, optionally filtering by match_types.

    Parameters:
    text (str): Term text to search for.
    match_type ([str]): Array of types of search matches to return.
        Allowable str values are "exact", "partial", and "broad".

    Returns:
    [dict]: list of terms(dicts) found.

    Raises:
        ValueError: If `match_types` contains invalid values.
    """
    if match_types:
        for mt in match_types:
            if not mt in ["exact", "partial", "broad"]:
                raise ValueError(
                    f"Invalid match_types parameter ({match_types}). "
                    "Valid match types are 'exact', 'partial', and 'broad'."
                )

    data = _get_kb_json_response("/term/search", {"text": text})
    items = data["results"]
    if match_types:
        items = [item for item in items if item["matchType"] in match_types]
    return items
