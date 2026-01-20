import get_daraz_smart_watches

daraz_website_url_with_search_query = "https://www.daraz.com.bd/catalog/?q=smart%20watch"
page_current_count = 25
daraz_watch_finder  = get_daraz_smart_watches.DarazSmartWatchFinder(daraz_website_url_with_search_query)
total_search_result_pages = daraz_watch_finder.GetPageCount()
#daraz_watch_finder.GetPageCount()
while   page_current_count <= total_search_result_pages:
    daraz_watch_finder  = get_daraz_smart_watches.DarazSmartWatchFinder(daraz_website_url_with_search_query+"&page="+str(page_current_count) +"")
    divs = daraz_watch_finder.get_product_divs()
    daraz_watch_finder.write_product_urls_to_file(divs)
    print("Completed page: ", page_current_count, " of ", total_search_result_pages)
    page_current_count += 1






