def scriptRewrite(prefix, domain, requestURL, soup):
    for link in soup.find_all('script', src=True): # find all links
        if link['src'][0:2] == "//": # if link starts with //
            link['src'] = f"http:{link['src']}" # add http:
            link['src'] = "https://" + domain  + prefix + link['src'] # add domain and prefix
        elif link['src'][0:1] == "/": # if link starts with /
            link['src'] = "https://" + domain  + prefix + requestURL + link['src'] # add domain and prefix
        elif link['src'][0:4] == "http"or link['src'][0:4] == "https": # if link starts with http or https
            link['src'] = "https://" + domain + prefix + link['src'] # add domain and prefix

    for link in soup.find_all('link', integrity=True):
        del link['integrity']

# TODO: rewrite inner text