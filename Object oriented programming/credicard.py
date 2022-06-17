from sre_constants import SUCCESS


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        
        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt: the account identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit
    
    def set_limit(self, limit):
        self._limit = limit

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """An extension of CreditCard that charges interest on a fee."""
    def __init__(self,customer,bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)
        self._apr = apr
    
    def process_month(self):
        """monthly interset on outstending balance"""
        if self._balance>0:
            monthly_factor=pow(1+self.apr,1/12)
            self._balance*=monthly_factor
        
    def charge(self,price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        success = super().charge(price)
        if not success:
            self._balance+=5
        return success    