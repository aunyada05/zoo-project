class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: # Fix:  0 < to 0 <=
            return 50
        elif 13 <= age <= 20: # Fix: < 20 to <= 20
            return 100
        elif 21 <= age <= 60: # Fix: 21 < to 21 <=
            return 150
        elif age > 60: # Fix: >= 60 to > 60
            return 100
        else:
            return "This is not a valid age"