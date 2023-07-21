from bs4 import BeautifulSoup
import requests

# -- Challenge of the day -- #
request = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = request.text

# Make it into BeautifulSoup object
movies_soup = BeautifulSoup(movies_page, "html.parser")
movie_titles = [title.string for title in movies_soup.select(".title")]

for rank, movie in enumerate(movie_titles[::-1]):
    if rank > 99:
        break
    else:
        with open('movies.txt', 'a') as file:
            file.write(f"{movie}\n")

        


# --- Exercise of the day --- #
# # Retrieve the live text version of the website using requests
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# # Make it a BeautifulSoup object
# soup_page = BeautifulSoup(yc_web_page, "html.parser")

# # Getting the first article of the page:
# # article_tag = soup_page.find(name="span", class_="titleline")

# titles = [storyline.find(name="a").string for storyline in soup_page.select(".titleline")]
# links = [storyline.find(name="a").get('href') for storyline in soup_page.select(".titleline")]
# upvotes = [int(storyline.string.split(" ")[0]) for storyline in soup_page.select(".score")]

# print(titles[upvotes.index(max(upvotes))])
# print(links[upvotes.index(max(upvotes))])




# ------ Examples of the day ------ #
# To open a local website/file we can use built-in function
# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # Finding all anchor tags using find_all function
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print("anchor tag:",tag.getText())

# # Finding all headings using find all and class_ attribute
# class_is_heading = soup.find_all(class_="heading")
# for heading in class_is_heading:
#     print(heading.getText())
#     # or you could do print(heading.string)

# # Finding first id using CSS selectors
# name = soup.select_one("#name")
# print("Selecting the id '#name': ",name)

# # Finding the headings using CSS selector:
# headings = soup.select(".heading")
# print("Selecting the class 'heading': ", headings)

