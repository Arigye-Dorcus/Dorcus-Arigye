class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing ${amount} ")

    def process_payment(self, amount, card_number):
        print(f"Processing ${amount} via card ending in {card_number[-4:]}")
    
class WorkingPaymentProcessor:
    def process_payment(self, amount, card_number=None):
        
        if card_number:
            print(f"Process ${amount}  in {card_number[-4:]}")
        else:
            print(f"Process ${amount} ")
working_processor = WorkingPaymentProcessor()
working_processor.process_payment(100)  
working_processor.process_payment(150, "411")  
