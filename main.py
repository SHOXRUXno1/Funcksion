class User:
    def init(self, ism, familya, tyil, email, mamlakat):
        self.ism = ism
        self.familya = familya
        self.tyil = tyil
        self.email = email
        self.mamlakat = mamlakat

    def get_fullname(self):
        return f"{self.ism}. familyasi {self.familya}"

    def get_email(self):
        return f"{self.email}"

    def get_age(self):
        return f"{self.tyil}"

    def get_form(self):
        return f"{self.mamlakat}"

    def get_info(self):
        print(
            f"Ismi {self.ism} familysai {self.familya} tu'gilgan yili {self.tyil}"
            f" emaili {self.email} mamlakati {self.mamlakat}")


USER = User(f"SHOXRUX", "XASANOV", 2009, "SHOX@com", "UZEBKSITAN")
print(USER.get_info())