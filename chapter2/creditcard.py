class CreditCard:
    ”””A consumer credit card.”””
    
    def init (self, customer, bank, acnt, limit):
     ”””Create a new credit card instance.

     The initial balance is zero.

     customer the name of the customer (e.g., John Bowman )
     bank the name of the bank (e.g., California Savings )
     acnt the acount identifier (e.g., 5391 0375 9387 5309 )
     limit credit limit (measured in dollars)
     ”””
     self. customer = customer
     self. bank = bank
     self. account = acnt
     self. limit = limit
     self. balance = 0

     def get customer(self):
     ”””Return name of the customer.”””
     return self. customer

     def get bank(self):
     ”””Return the bank s name.”””
     return self. bank

     def get account(self):
     ”””Return the card identifying number (typically stored as a string).”””
     return self. account

     def get limit(self):
     ”””Return current credit limit.”””
     return self. limit

     def get balance(self):
     ”””Return current balance.”””
     return self. balance

    def charge(self, price):
     ”””Charge given price to the card, assuming sufficient credit limit.

     Return True if charge was processed; False if charge was denied.
     ”””
     if price + self. balance > self. limit: # if charge would exceed limit,
     return False # cannot accept charge
     else:
     self. balance += price
     return True

     def make payment(self, amount):
     ”””Process customer payment that reduces balance.”””
     self. balance −= amount


     #testing
if name == __main__ :
    54 wallet = [ ]
 wallet.append(CreditCard( John Bowman , California Savings , 5391 0375 9387 5309 , 2500) )
 wallet.append(CreditCard( John Bowman , California Federal , 3485 0399 3395 1954 , 3500) )
 wallet.append(CreditCard( John Bowman , California Finance , 5391 0375 9387 5309 , 5000) )

 for val in range(1, 17):
 wallet[0].charge(val)
 wallet[1].charge(2 val)
 wallet[2].charge(3 val)

 for c in range(3):
 print( Customer = , wallet[c].get customer( ))
 print( Bank = , wallet[c].get bank())
 print( Account = , wallet[c].get account( ))
 print( Limit = , wallet[c].get limit( ))
 print( Balance = , wallet[c].get balance())
 while wallet[c].get balance( ) > 100:
 wallet[c].make payment(100)
 print( New balance = , wallet[c].get balance())
 print( )


#Extension and example of inheritance
class PredatoryCreditCard(CreditCard):
    ”””An extension to CreditCard that compounds interest and fees.”””

    def init (self, customer, bank, acnt, limit, apr):
    ”””Create a new predatory credit card instance.
    
    The initial balance is zero.
    
    customer the name of the customer (e.g., John Bowman )
     bank the name of the bank (e.g., California Savings )
     acnt the acount identifier (e.g., 5391 0375 9387 5309 )
     limit credit limit (measured in dollars)
     apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
     ”””
     super(). init (customer, bank, acnt, limit) # call super constructor
     self. apr = apr
    
     def charge(self, price):
     ”””Charge given price to the card, assuming sufficient credit limit.
    
     Return True if charge was processed.
     Return False and assess 5 fee if charge is denied.
     ”””
     success = super( ).charge(price) # call inherited method
     if not success:
     self. balance += 5 # assess penalty
     return success # caller expects return value
    
     def process month(self):
     ”””Assess monthly interest on outstanding balance.”””
     if self. balance > 0:
     # if positive balance, convert APR to monthly multiplicative factor
     monthly factor = pow(1 + self. apr, 1/12)
     self. balance = monthly factor
    
    