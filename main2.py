import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "The Real Estate company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your ticket.
        Name: {self.the_customer_name}
        Hotel: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name


hotel = Hotel("134")
print(hotel.available())
print(hotel.watermark)

ticket = ReservationTicket(customer_name="jide egwu", hotel_object=hotel)
print(ticket.generate())
print(ticket.the_customer_name)