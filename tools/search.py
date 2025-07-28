import requests
from base import get_brave_client
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)

def brave_search(
    query,
    count=5,
    country=None,
    search_lang=None,
    ui_lang=None,
    offset=None,
    safesearch=None,
    spellcheck=None,
    freshness=None,
    text_decorations=None,
    result_filter=None,
    units=None,
    goggles=None,
    extra_snippets=None,
    summary=None,
    enable_rich_callback=None,
    x_loc_lat=None,
    x_loc_long=None,
    x_loc_timezone=None,
    x_loc_city=None,
    x_loc_state=None,
    x_loc_state_name=None,
    x_loc_country=None,
    x_loc_postal_code=None
) -> dict:
    """
    Perform a Brave search query with optional parameters.

    Args:
        query (str): Search query string.
        country, search_lang, ui_lang, count, offset, safesearch, spellcheck, freshness,
        text_decorations, result_filter, units, goggles, extra_snippets, summary, enable_rich_callback:
            Optional query parameters to refine the search.
        x_loc_*: Optional location headers to personalize search results.

    Returns:
        dict: JSON response from Brave Search API or an error message.
    """
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": get_brave_client()
    }

    # Add optional location headers
    header_list = [
        ("x-loc-lat", x_loc_lat),
        ("x-loc-long", x_loc_long),
        ("x-loc-timezone", x_loc_timezone),
        ("x-loc-city", x_loc_city),
        ("x-loc-state", x_loc_state),
        ("x-loc-state-name", x_loc_state_name),
        ("x-loc-country", x_loc_country),
        ("x-loc-postal-code", x_loc_postal_code)
    ]
    for k, v in header_list:
        if v is not None:
            headers[k] = str(v)

    params = {"q": query,
              "count": count}

    param_list = [
        ("country", country),
        ("search_lang", search_lang),
        ("ui_lang", ui_lang),
        ("offset", offset),
        ("safesearch", safesearch),
        ("spellcheck", spellcheck),
        ("freshness", freshness),
        ("text_decorations", text_decorations),
        ("result_filter", result_filter),
        ("units", units),
        ("goggles", goggles),
        ("extra_snippets", extra_snippets),
        ("summary", summary),
        ("enable_rich_callback", enable_rich_callback)
    ]
    for k, v in param_list:
        if v is not None:
            params[k] = v

    logger.info(f"Sending Brave search request: {query}")
    try:
        response = requests.get(url, headers=headers, params=params)
        logger.info("Received Brave search response")
        return response.json()
    except Exception as e:
        logger.error(f"Brave search failed: {e}")
        return {"error": f"Could not complete Brave search for query: {query}"}

def brave_image_search(
    query,
    count=5,
    search_lang=None,
    country=None,
    safesearch=None,
    spellcheck=None,
    x_loc_lat=None,
    x_loc_long=None,
    x_loc_timezone=None,
    x_loc_city=None,
    x_loc_state=None,
    x_loc_state_name=None,
    x_loc_country=None,
    x_loc_postal_code=None
) -> dict:
    """
    Perform a Brave image search.

    Args:
        query (str): Search query string.
        All other args are optional filters or location headers.

    Returns:
        dict: JSON response from Brave Search API or error message.
    """
    token = get_brave_client()
    if not token:
        logger.error("Could not get Brave subscription token")
        return {"error": "Missing Brave subscription token"}

    url = "https://api.search.brave.com/res/v1/images/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": token
    }

    # Optional location headers
    header_list = [
        ("x-loc-lat", x_loc_lat),
        ("x-loc-long", x_loc_long),
        ("x-loc-timezone", x_loc_timezone),
        ("x-loc-city", x_loc_city),
        ("x-loc-state", x_loc_state),
        ("x-loc-state-name", x_loc_state_name),
        ("x-loc-country", x_loc_country),
        ("x-loc-postal-code", x_loc_postal_code)
    ]
    for k, v in header_list:
        if v is not None:
            headers[k] = str(v)

    # Always include query
    params = {"q": query,
              'count': count}

    # Optional query params
    param_list = [
        ("search_lang", search_lang),
        ("country", country),
        ("safesearch", safesearch),
        ("spellcheck", spellcheck)
    ]
    for k, v in param_list:
        if v is not None:
            params[k] = v

    logger.info(f"Sending Brave image search request: {query}")
    try:
        response = requests.get(url, headers=headers, params=params)
        logger.info("Received Brave image search response")
        return response.json()
    except Exception as e:
        logger.error(f"Brave image search failed: {e}")
        return {"error": f"Could not complete Brave image search for query: {query}"}


def brave_news_search(
    query,
    count=5,
    search_lang=None,
    ui_lang=None,
    country=None,
    safesearch=None,
    offset=None,
    spellcheck=None,
    freshness=None,
    extra_snippets=None,
    goggles=None,
    x_loc_lat=None,
    x_loc_long=None,
    x_loc_timezone=None,
    x_loc_city=None,
    x_loc_state=None,
    x_loc_state_name=None,
    x_loc_country=None,
    x_loc_postal_code=None
) -> dict:
    """
    Perform a Brave news search.

    Args:
        query (str): Required search query.
        count (int, optional): Number of results. Default 5.
        Others are optional filters and location headers.

    Returns:
        dict: JSON response from Brave API or error.
    """
    token = get_brave_client()
    if not token:
        logger.error("Could not get Brave subscription token")
        return {"error": "Missing Brave subscription token"}

    url = "https://api.search.brave.com/res/v1/news/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": token
    }

    # Optional location headers
    header_list = [
        ("x-loc-lat", x_loc_lat),
        ("x-loc-long", x_loc_long),
        ("x-loc-timezone", x_loc_timezone),
        ("x-loc-city", x_loc_city),
        ("x-loc-state", x_loc_state),
        ("x-loc-state-name", x_loc_state_name),
        ("x-loc-country", x_loc_country),
        ("x-loc-postal-code", x_loc_postal_code)
    ]
    for k, v in header_list:
        if v is not None:
            headers[k] = str(v)

    params = {"q": query, "count": count}

    param_list = [
        ("search_lang", search_lang),
        ("ui_lang", ui_lang),
        ("country", country),
        ("safesearch", safesearch),
        ("offset", offset),
        ("spellcheck", spellcheck),
        ("freshness", freshness),
        ("extra_snippets", extra_snippets),
        ("goggles", goggles)
    ]
    for k, v in param_list:
        if v is not None:
            params[k] = v

    logger.info(f"Sending Brave news search request: {query}")
    try:
        response = requests.get(url, headers=headers, params=params)
        logger.info("Received Brave news search response")
        return response.json()
    except Exception as e:
        logger.error(f"Brave news search failed: {e}")
        return {"error": f"Could not complete Brave news search for query: {query}"}

def brave_video_search(
    query,
    count=20,
    safesearch="off",
    search_lang=None,
    ui_lang=None,
    country=None,
    offset=None,
    spellcheck=None,
    freshness=None,
    x_loc_lat=None,
    x_loc_long=None,
    x_loc_timezone=None,
    x_loc_city=None,
    x_loc_state=None,
    x_loc_state_name=None,
    x_loc_country=None,
    x_loc_postal_code=None
) -> dict:
    """
    Perform a Brave video search.

    Args:
        query (str): Required search query.
        count (int, optional): Number of results. Default 20.
        safesearch (str, optional): 'off', 'moderate', or 'strict'. Default 'off'.
        Others are optional filters and location headers.

    Returns:
        dict: JSON response from Brave API or error.
    """
    token = get_brave_client()
    if not token:
        logger.error("Could not get Brave subscription token")
        return {"error": "Missing Brave subscription token"}

    url = "https://api.search.brave.com/res/v1/videos/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": token
    }

    # Optional location headers
    header_list = [
        ("x-loc-lat", x_loc_lat),
        ("x-loc-long", x_loc_long),
        ("x-loc-timezone", x_loc_timezone),
        ("x-loc-city", x_loc_city),
        ("x-loc-state", x_loc_state),
        ("x-loc-state-name", x_loc_state_name),
        ("x-loc-country", x_loc_country),
        ("x-loc-postal-code", x_loc_postal_code)
    ]
    for k, v in header_list:
        if v is not None:
            headers[k] = str(v)

    params = {"q": query, "count": count, "safesearch": safesearch}

    param_list = [
        ("search_lang", search_lang),
        ("ui_lang", ui_lang),
        ("country", country),
        ("offset", offset),
        ("spellcheck", spellcheck),
        ("freshness", freshness)
    ]
    for k, v in param_list:
        if v is not None:
            params[k] = v

    logger.info(f"Sending Brave video search request: {query}")
    try:
        response = requests.get(url, headers=headers, params=params)
        logger.info("Received Brave video search response")
        return response.json()
    except Exception as e:
        logger.error(f"Brave video search failed: {e}")
        return {"error": f"Could not complete Brave video search for query: {query}"}


if __name__ == "__main__":

    # Test cases for brave_search()
    print("Testing brave_search()...")
    test1 = brave_search("spacex", count=3, country="us", search_lang="en")
    print("Test 1 - Basic SpaceX search:", test1.keys() if isinstance(test1, dict) else test1)
    time.sleep(1)
    test2 = brave_search("elon musk", freshness="week", safesearch="strict")
    print("Test 2 - Elon Musk with freshness filter:", test2.keys() if isinstance(test2, dict) else test2)
    time.sleep(1)
    test3 = brave_search("python programming", search_lang="en", result_filter="web")
    print("Test 3 - Python programming filtered to web:", test3.keys() if isinstance(test3, dict) else test3)
    time.sleep(1)
    test4 = brave_search("latest news", country="gb", ui_lang="en-GB", freshness="day")
    print("Test 4 - UK news from today:", test4.keys() if isinstance(test4, dict) else test4)
    time.sleep(1)
    test5 = brave_search("weather in new york", units="imperial", x_loc_country="us")
    print("Test 5 - Weather with location headers:", test5.keys() if isinstance(test5, dict) else test5)
    time.sleep(1)
    # Test cases for brave_image_search()
    print("\nTesting brave_image_search()...")
    test6 = brave_image_search("tesla cybertruck", count=5, country="us")
    print("Test 6 - Tesla Cybertruck images:", test6.keys() if isinstance(test6, dict) else test6)
    time.sleep(1)
    test7 = brave_image_search("mars rover", safesearch="strict", search_lang="en")
    print("Test 7 - Mars rover with safesearch:", test7.keys() if isinstance(test7, dict) else test7)
    time.sleep(1)
    test8 = brave_image_search("ai generated art", count=10, spellcheck="true")
    print("Test 8 - AI art with spellcheck:", test8.keys() if isinstance(test8, dict) else test8)
    time.sleep(1)
    test9 = brave_image_search("tokyo skyline", country="jp", x_loc_country="jp")
    print("Test 9 - Tokyo with location header:", test9.keys() if isinstance(test9, dict) else test9)
    time.sleep(1)
    test10 = brave_image_search("abstract painting", count=3, safesearch="off")  # or 'strict'
    print("Test 10 - Abstract painting limited:", test10.keys() if isinstance(test10, dict) else test10)
    time.sleep(1)
    # Test cases for brave_news_search()
    print("\nTesting brave_news_search()...")
    test11 = brave_news_search("spacex launch", freshness="day", count=5)
    print("Test 11 - SpaceX launch news today:", test11.keys() if isinstance(test11, dict) else test11)
    time.sleep(1)
    test12 = brave_news_search("tech news", country="us", search_lang="en", offset=5)
    print("Test 12 - Tech news with offset:", test12.keys() if isinstance(test12, dict) else test12)
    time.sleep(1)
    test13 = brave_news_search("climate change", freshness="month", safesearch="strict")
    print("Test 13 - Climate change strict safesearch:", test13.keys() if isinstance(test13, dict) else test13)
    time.sleep(1)
    test14 = brave_news_search("european politics", country="fr", search_lang="fr")
    print("Test 14 - European politics in French:", test14.keys() if isinstance(test14, dict) else test14)
    time.sleep(1)
    test15 = brave_news_search("latest iphone", extra_snippets="true", goggles="https://www.apple.com/iphone/")
    print("Test 15 - iPhone news with goggles:", test15.keys() if isinstance(test15, dict) else test15)
    time.sleep(1)
    # Test cases for brave_video_search()
    print("\nTesting brave_video_search()...")
    test16 = brave_video_search("spacex starship", count=10, safesearch="off")
    print("Test 16 - SpaceX Starship videos:", test16.keys() if isinstance(test16, dict) else test16)
    time.sleep(1)
    test17 = brave_video_search("cooking tutorials", freshness="week", country="us")
    print("Test 17 - Cooking videos from this week:", test17.keys() if isinstance(test17, dict) else test17)
    time.sleep(1)
    test18 = brave_video_search("yoga for beginners", safesearch="moderate", search_lang="en")
    print("Test 18 - Yoga videos moderate safesearch:", test18.keys() if isinstance(test18, dict) else test18)
    time.sleep(1)
    test19 = brave_video_search("travel vlog japan", count=5, offset=3)
    print("Test 19 - Japan travel vlogs with offset:", test19.keys() if isinstance(test19, dict) else test19)
    time.sleep(1)
    test20 = brave_video_search("machine learning", spellcheck="true", freshness="month")
    print("Test 20 - Machine learning videos:", test20.keys() if isinstance(test20, dict) else test20)
