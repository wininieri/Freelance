import requests
import json
from bs4 import BeautifulSoup


def get_info_for_company(paths):
    address = 'https://www.glassdoor.com'
    result = []
    for i in paths:
        url_string = address + i
        response = get_ratings(url_string, i)
        data = response
        result.append(data.json())

    with open('response.json', 'w') as out:
        json.dump(result, out)


def get_ratings(url_string, path):
    headers = {"authority": "www.glassdoor.com",
               "method": "GET",
               "path": path,
               "scheme": "https",
               "accept": "* / *",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "en - US, en;q = 0.8",
               "cookie": "trs=https%3A%2F%2Fwww.google.com%2Furl%3Fq%3Dhttps%253A%252F%252Fwww.glassdoor.com%252FOverview%252FWorking-at-Amazon-EI_IE6036.11%252C17.htm%2523%26sa%3DD%26sntz%3D1%26usg%3DAFQjCNELae2lGdklO6YkAiNVJE9Wajrpyw:SEO:SEO:2017-11-01+03%3A05%3A41.797:undefined:undefined; ARPNTS_AB=917; ht=%7B%22quantcast%22%3A%5B%22D%22%5D%7D; __gads=ID=86b7fa895ed5a394:T=1509530746:S=ALNI_Ma07eRiebvpOdb-J_X1C-j1xfV_aQ; __qca=P0-585165595-1509530752033; G_ENABLED_IDPS=google; JSESSIONID=D92B4F648C9152119D138CA65A0C95B3; mp_5d4806b773713d93bd344cf2365e6df0_mixpanel=%7B%22distinct_id%22%3A%20%2215f77bbff2c105-0cd83ab12f9c0a-1227170b-1fa400-15f77bbff2d5bc%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.glassdoor.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.glassdoor.com%22%7D; _uetsid=_uet3dc04eb9; mp_mixpanel__c=1; _ga=GA1.2.1508202680.1509530743; _gid=GA1.2.1493526175.1509530743; GSESSIONID=D92B4F648C9152119D138CA65A0C95B3; gdId=7b215757-056e-4790-9f93-614912a7ab31; cass=1; ARPNTS=2858789056.64288.0000",
               "referer": "https: // www.glassdoor.com /",
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
               "x-requested-with": "XMLHttpRequest"}
    response = requests.get(url_string, headers=headers)
    return response


def get_company_id(company_name):
    url = "https://www.glassdoor.com/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn" + \
          "&typedKeyword=" + company_name + "&sc.keyword=" + company_name + "&locT=&locId=&jobType="
    path = "/Reviews/company-reviews.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=google&sc.keyword=google&locT=&locId=&jobType="

    headers = {"authority": "www.glassdoor.com",
               "method": "GET",
               "path": path,
               "scheme": "https",
               "accept": "* / *",
               "accept-encoding": "gzip, deflate, br",
               "accept-language": "en - US, en;q = 0.8",
               "cache-control": "no-cache",
               "cookie": "trs=https%3A%2F%2Fwww.google.com%2Furl%3Fq%3Dhttps%253A%252F%252Fwww.glassdoor.com%252FOverview%252FWorking-at-Amazon-EI_IE6036.11%252C17.htm%2523%26sa%3DD%26sntz%3D1%26usg%3DAFQjCNELae2lGdklO6YkAiNVJE9Wajrpyw:SEO:SEO:2017-11-01+03%3A05%3A41.797:undefined:undefined; ARPNTS_AB=917; ht=%7B%22quantcast%22%3A%5B%22D%22%5D%7D; __gads=ID=86b7fa895ed5a394:T=1509530746:S=ALNI_Ma07eRiebvpOdb-J_X1C-j1xfV_aQ; __qca=P0-585165595-1509530752033; G_ENABLED_IDPS=google; JSESSIONID=D92B4F648C9152119D138CA65A0C95B3; mp_5d4806b773713d93bd344cf2365e6df0_mixpanel=%7B%22distinct_id%22%3A%20%2215f77bbff2c105-0cd83ab12f9c0a-1227170b-1fa400-15f77bbff2d5bc%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.glassdoor.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.glassdoor.com%22%7D; _uetsid=_uet3dc04eb9; mp_mixpanel__c=1; _ga=GA1.2.1508202680.1509530743; _gid=GA1.2.1493526175.1509530743; GSESSIONID=D92B4F648C9152119D138CA65A0C95B3; gdId=7b215757-056e-4790-9f93-614912a7ab31; cass=1; ARPNTS=2858789056.64288.0000",
               "pragma": "no-cache",
               "referer": "https: // www.glassdoor.com /",
               "upgrade-insecure-requests": "1",
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
               "x-requested-with": "XMLHttpRequest"}

    response = requests.get(url, headers=headers)

    # soup = BeautifulSoup(response.content)
    # mydivs = soup.findAll("div", {"class": " margBotXs"})
    with open('search_response.html', 'wb') as out:
        out.write(response.content)


def main():
    company_name = "Google"
    id = get_company_id(company_name)
    company_id = '6036'

    paths = []
    paths.append("/api/employer/-rating.htm?locationStr=&jobTitleStr=&filterCurrentEmployee=false")
    paths.append(
        "/api/employer/-rating.htm?dataType=trend&category=overallRating&locationStr=&jobTitleStr=&filterCurrentEmployee=false")
    paths.append("/api/employer/-rating.htm?dataType=distribution&category=overallRating")

    for path_index, i in enumerate(paths):
        index = i.index('-rating')
        paths[path_index] = i[:index] + company_id + i[index:]

    get_info_for_company(paths)


if __name__ == '__main__':
    main()
