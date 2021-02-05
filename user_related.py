class User:
    def __init__(self, username, user_type, follow_list=None, tracks=None):
        # user_type="follow_list" or "init"
        self.username = username
        self.user_type = user_type

        if user_type == "init":
            self.url = "https://soundcloud.com/" + username + "/follow_list"
        elif user_type == "follow_list":
            self.url = "https://soundcloud.com/" + username + "/tracks"
        else:
            raise Exception("Invalid user type!")
        self.follow_list = follow_list
        self.tracks = tracks

    def get_url(self):
        return self.url

    def set_follow_list(self, follow_list):
        self.follow_list = follow_list

    def get_follow_list(self):
        return self.follow_list

    def set_url(self, url):
        self.url = url

    def set_tracks(self, tracks):
        self.tracks = tracks

    def get_tracks(self):
        return self.tracks


class track:
    def __init__(self, url, date,track_name="",artist=""):
        self.url = url
        self.date = date
        self.track_name=track_name
        self.artist=artist
