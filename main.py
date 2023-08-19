import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_secure_card = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
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


class HotelSpa(Hotel):
    def book_spa(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your ticket.
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Thank you for spar your reservation!
        Here is your spa ticket.
        Name: {self.customer_name}
        Hotel: {self.hotel_object.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, cvc, holder):
        cards = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": holder}
        if cards in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, user_password):
        password = df_secure_card.loc[df_secure_card["number"] == self.number, "password"].squeeze()
        if password == user_password:
            return True
        else:
            return False


print(df)
h_id = input("Enter a hotel id: ")


hotel = HotelSpa(h_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", cvc="123", holder="JOHN SMITH"):
        if credit_card.authenticate(user_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa = input("Would you want a spa package?: ")
            if spa == "yes":
                hotel.book_spa()
                spar_ticket = SpaReservationTicket(name, hotel)
                print(spar_ticket.generate())
        else:
            print("Credit card authentication issue")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not available")