from bs4 import BeautifulSoup

def get_top_artists(soup_object):
    
    artist_first = [soup_object.find(class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet").getText().strip()]

    artist_rest = [' '.join(artist.string.split()) for artist in soup_object.find_all(class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]

    artist_list_100 = artist_first+artist_rest

    return artist_list_100

def get_top_tracks(soup_object):
    # Retrieving the track name first and top 99
    billboard_first = soup_object.find("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet",id="title-of-a-story").string.split()

    billboard_rest = [' '.join(title.string.split()) for title in soup_object.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",id="title-of-a-story")]

    # Final list of music names
    music_list_100 = billboard_first + billboard_rest
    return music_list_100

