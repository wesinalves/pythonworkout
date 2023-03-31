def apply_discount(prod):
    name = prod[0]
    value = prod[1] * 0.9
    return name, value

if __name__ == '__main__':
    products = [
        ('celular' , 800), 
        ('camera', 2500), 
        ('televisao', 5000)]    
    discounted_products = list(map(apply_discount, products))
    print(discounted_products)
