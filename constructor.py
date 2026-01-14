class Bus:
    def __init__(self,name,number,route,seats,ticket_price,refund,cancel_charge):
        self.name=name
        self.number=number
        self.route=route
        self.seats=seats
        self.ticket_price=ticket_price
        self.refund=refund
        self.cancel_charge=cancel_charge

        self.total_booked=0
        self.total_cancelled=0

    def book_ticket(self,count):
        self.total_booked+=count
    def cancel_ticket(self,count):
        self.total_cancelled+=count

    def summary(self):
        total_travellers=self.total_booked - self.total_cancelled
        if total_travellers > self.seats:
            total_travellers=self.seats
        total_collection=self.total_booked * self.ticket_price
        refund_amount=self.total_cancelled * self.refund
        final_amount=total_collection - refund_amount

        print(f"Bus name: {self.name}")
        print(f"Bus number: {self.number}")
        print(f"Bus route: {self.route}")
        print(f"Total travellers: {total_travellers}")
        print(f"Total collection: {total_collection}")
        print(f"total cancellation: {self.total_cancelled}")
        print(f"Refund amount: {refund_amount}")
        print(f"Final amount Earned : {final_amount}")

bus=Bus("Dolphin","OR 33 KS 0108","Bhubaneswar to puri",60,100,70,30)
bus.book_ticket(40)
bus.cancel_ticket(13)
bus.book_ticket(20)
bus.cancel_ticket(8)
bus.summary()