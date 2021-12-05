class Person:
    name = []

    def set_name(self, username):
        self.name.append(username)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name) or user_id < 0:
            return "There is no such user here"
        else:
            return self.name[user_id]