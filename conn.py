class ConnectDatabase:

    def __init__(self, port, hostname, username, password):
        self.port = port
        self.hostname = hostname
        self.username = username
        self.password = password

    def  show_details (self):
        print(f"Hostname: {self.hostname}")
        print(f"Port: {self.port}")
        print(f"Username: {self.username}")


conn = ConnectDatabase(443, "localhost", "db_user", "password")
conn.show_details()
