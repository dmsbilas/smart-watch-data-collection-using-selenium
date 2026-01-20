import get_daraz_smart_watches

daraz_website_url_with_search_query = "https://www.daraz.com.bd/catalog/?q=smart%20watch"

daraz_watch_finder  = get_daraz_smart_watches.DarazSmartWatchFinder(daraz_website_url_with_search_query)


divs = daraz_watch_finder.get_product_divs()
daraz_watch_finder.write_product_urls_to_file(divs)


