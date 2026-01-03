from instagrapi import Client
import os
from app.core.config import USERNAME, PASSWORD

SESSION_FILE = "session.json"

def login_user():
    cl = Client()

    login_via_session = False
    login_via_pw = False

    # load session
    if os.path.exists(SESSION_FILE):
        try:
            print("Loading session from file")

            session = cl.load_settings(SESSION_FILE)
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # kiểm tra session còn sống không
            try:
                cl.get_timeline_feed()
                login_via_session = True
                print("Login via session success")

            except LoginRequired:
                print("Session expired, relogin via password")

                old_session = cl.get_settings()
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])
                cl.login(USERNAME, PASSWORD)
                login_via_pw = True

        except Exception as e:
            print(f"Session login failed: {e}")

    else:
        print("Session file not found, login via password")

    # Nếu chưa login được → login bằng username/password
    if not login_via_session and not login_via_pw:
        try:
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
                print("Login via username/password success")
        except Exception as e:
            print(f"Password login failed: {e}")

    # Fail toàn bộ
    if not login_via_session and not login_via_pw:
        raise Exception("Couldn't login user")

    # Lưu lại session cho lần sau
    cl.dump_settings(SESSION_FILE)

    return cl

def url_media(url: str):
    cl = login_user()

    mpk = cl.media_pk_from_url(url=url)
    media_info = cl.media_info(media_pk=mpk)

    media_type = media_info.media_type
    urls = []
    if media_type == 8:
        for item in media_info.resources:
            if item.media_type == 1:
                url = item.thumbnail_url
            else:
                url = item.video_url
            urls.append(url)
        
    elif media_type == 1:
        candidates = media_info.image_versions2.get('candidates')
        for item in candidates:
            if item['width'] == 1080:
                url = item['url']
                break
        
        if url == None:
            url = candidates[0].url

        urls.append(url)

    elif media_type == 2:
        urls.append(media_info.video_url)

    else:
        urls = media_info

    return urls