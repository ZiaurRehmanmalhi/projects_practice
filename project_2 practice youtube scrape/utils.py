import time
import os
import pandas as pd
from bs4 import BeautifulSoup


def scroll_to_page_end(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        time.sleep(1.5)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def extract_comments_data(soup):
    comment_sections = soup.find_all('ytd-comment-thread-renderer')
    comments = []

    for comment in comment_sections:
        user_info = comment.find('ytd-comment-renderer').find('a', {'id': 'author-text'})
        user_name = user_info.text.strip()
        comment_text = comment.find('yt-formatted-string', {'id': 'content-text'}).text.strip()
        likes = comment.find('span', {'id': 'vote-count-middle'}).text.strip()
        comment_time = comment.find('a', {'class': 'yt-simple-endpoint style-scope yt-formatted-string'}).text.strip()
        thumbnail_url_tag = comment.find('yt-img-shadow', {"class": "style-scope ytd-comment-renderer no-transition"})
        if thumbnail_url_tag is not None:
            thumbnail_url = thumbnail_url_tag.find('img').get('src')

        comments.append([user_name, thumbnail_url, comment_time, likes, comment_text])

    return comments


def get_channel_directory(channel_url):
    channel_name = channel_url.split("/")[-2].replace('@', '')
    channel_dir = os.path.join(os.getcwd(), channel_name)
    if not os.path.exists(channel_dir):
        os.mkdir(channel_dir)
    return channel_dir


def get_video_links(soup):
    video_links = []
    for video in soup.find_all('ytd-rich-grid-media'):
        video_url = 'https://www.youtube.com' + video.find('a', {'id': 'video-title-link'}).get('href')
        video_links.append(video_url)
    return video_links


def process_video_comments(video_link, channel_dir, driver):
    driver.get(video_link)

    time.sleep(5)

    scroll_to_page_end(driver)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    comments_data = extract_comments_data(soup)

    video_name = soup.title.string.split(" - YouTube")[0]
    video_title = video_name.replace('/', '-')

    file_name = video_title + '.csv'
    file_path = os.path.join(channel_dir, file_name)
    df = pd.DataFrame(comments_data, columns=['User Name', 'Thumbnail URL', 'Comment Time', 'Likes', 'Comment Text'])
    df.to_csv(file_path, index=False)
    print(f"Comments for video {video_title} saved to CSV file {file_name}")


def process_channel_videos(channel_url, driver):
    channel_url += "/videos"
    driver.get(channel_url)

    time.sleep(5)

    scroll_to_page_end(driver)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    channel_dir = get_channel_directory(channel_url)
    video_links = get_video_links(soup)

    for video_link in video_links:
        process_video_comments(video_link, channel_dir, driver)

    print("Data successfully saved to CSV files.")
