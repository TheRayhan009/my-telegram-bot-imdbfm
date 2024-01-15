from PyMovieDb import IMDB
import json

imdb = IMDB()

def scrapeimdb(title):
    """
    This function uses the PyMovieDb API to scrape information about a movie from the Internet Movie Database (IMDB).

    Parameters:
    title (str): The title of the movie

    Returns:
    str: A Markdown-formatted string containing the scraped information about the movie

    Raises:
    ValueError: If the movie title is not provided

    """
    if not title:
        raise ValueError("Movie title must be provided")

    imdb = IMDB()

    data = json.loads(imdb.get_by_name(title))

    title_type = data["type"]
    movie_name = data["name"]
    movie_url = data["url"].replace("https://www.imdb.com/", "https://www.imdb.com/title/")
    poster_url = data["poster"]
    description = data["description"]
    review_author = data["review"]["author"]
    review_date = data["review"]["dateCreated"]
    review_heading = data["review"]["heading"]
    # review_body = data["review"]["reviewBody"]
    review_rating = data["review"]["reviewRating"]["ratingValue"]
    total_ratings = data["rating"]["ratingCount"]
    content_rating = data["contentRating"]
    genres = data["genre"]
    release_date = data["datePublished"]
    keywords = data["keywords"]
    duration = data["duration"]
    actors = [(actor["name"], actor["url"]) for actor in data["actor"]]
    director = [(director["name"], director["url"]) for director in data["director"]]
    creators = [(creator["name"], creator["url"]) for creator in data["creator"]]

    post = f"""
*{title_type} Name:* [{movie_name}]({movie_url})
*Description:* `{description}`

*Review:*
- *Author:* `{review_author}`
- *Date:* `{review_date}`
- *Heading:* `{review_heading}`
- *Rating:* `{review_rating}/10`

*General Information:*
- *Total Ratings:* `{total_ratings}`
- *Content Rating:* `{content_rating}`
- *Genres:* `{", ".join(genres)}`
- *Release Date:* `{release_date}`
- *Keywords:* `{keywords}`
- *Duration:* `{duration}`

*Actors:*
{"".join([f"[{actor[0]}]({actor[1]}), " for actor in actors]) if len(actors) > 0 else "`No Information available.`"}

*Director:*
{"".join([f"[{director[0]}]({director[1]}), " for director in director]) if len(director) > 0 else "`No Information available.`"}

*Creators:*
{"".join([f"[{creator[0]}]({creator[1]}), " for creator in creators]) if len(creators) > 0 else "`No Information available.`"}

"""

    return post, poster_url