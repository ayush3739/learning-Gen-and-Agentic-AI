def chai(flavor='masala'):
    '''Return the type of chai'''
    chai='ginger'
    return flavor

print(chai.__doc__)
print(chai.__name__)


# help(len)

def generate_bill(chai=0,samosa=0):
    '''
    Docstring for generate_bill
    
    :param chai: Number of chai cups
    :param samosa: Number of samosa 
    :return (totalamount,thankyou message)
    '''
    total=chai*10+samosa*15
    return total,"thank you for visiting chaicode.com"
