""""
R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.

Programmer: Anna Le
"""

#Program from Textbook
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman)
        bank the name of the bank (e.g., California Savings)
        acnt the account identifier (e.g., 5391 0375 9387 5309)
        limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        #Added Code/Exceptions
        if not isinstance (price, (int, float)):
             raise TypeError ("The price must be a numerical value")
        #End of Added Code
        
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False                         # cannot accept charge
        else:
            self._balance += price
            return True
        

    def make_payment(self, amount):
        #Added Code/Exceptions
        if not isinstance (amount, (int, float)):
            raise TypeError ("The payment must be a numerical value")
        #End of Added Code

        """Process customer payment that reduces balance."""
        self._balance -= amount
        
        
# Test
cc = CreditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000) #user instance used in textbook

#These are checkers of each method running as expected
print (cc.charge(1000))
print (cc.make_payment(50.51))

#These are checks of the type eroor to raise after the added code, to test the exceptions, uncomment the respective line
#print (cc.charge ('hello'))
#print (cc.make_payment('test'))