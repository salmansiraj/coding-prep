'''
    Amazon Prime Functionalities

    - Would require servers to have replicates if a server breaks down the request can still have a response using another server
    - CAP THEOREM
        * Consistency - No need to keep updated responses as much as having partial tolerence
        * Availability - Important because each request must not fail
        * Partial Tolerence - Important to keep the system working even after break down

    - Latency
        * There will be a larger number of requests maybe based on video streaming and accessing
            - May require a load balancer to distribute the large number of requests

    - Do we need sharding?
        * Sharding would need to be required as the database for videos will keep expanding everyday, will need to scale horizontally
            in order to increase the number of servers
        * To prevent a shard to go down along with machine, each shard would require two copies of a server which will be the
            child servers and one parent server

    - System
        * Adding users to system
        * Adding videos to system
            * Video categories

        - User
            * Account info
            * Liked Videos

        - Video
            * Duration
            * Genre
'''


class System:
    def __init__(self) -> None:
        self.videos = list(Video)
        self.users = list(User)


class User:
    def __init__(self, userId, fullName, password) -> None:
        self.userId = userId
        self.fullName = fullName
        self.password = password


class Video:
    def __init__(self, id, duration=0) -> None:
        self.id = id
        self.duration = duration
        self.likes = 0
