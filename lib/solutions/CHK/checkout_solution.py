

# noinspection PyUnusedLocal
# skus = unicode string

price_cat = {"A" : {"PRICE" : 50, "OFFER" : {3 : 130}}, "B" : {"PRICE" : 30, "OFFER" : {2 : 45}}, "C" : {"PRICE" : 20}, "D" : {"PRICE" : 15} }

def checkout(skus):
    sku_list = skus.split(",")
    sku_dict = {}
    for sku in sku_list:
        if not price_cat.get(sku,False):
            return -1
        count = sku_dict.get(sku,0) 
        sku_dict[sku] = count +1
    basket = 0
    print(sku_dict)
    for sku in sku_dict.keys():
        price = 0
        print(sku_dict[sku])
        item = price_cat[sku]
        if item.get("OFFER",False):
            quant = list(item['OFFER'].keys())[0]
            if sku_dict[sku] % quant == 0:
                price = (sku_dict[sku] / quant) * item['OFFER'][quant] 
            elif sku_dict[sku] > quant:
                i = 2
                while sku_dict[sku] - quant * i > quant:
                    i = i + 1
                price = i * item['OFFER'][quant] + ((sku_dict[sku] - (quant * i))* item['PRICE'])
        else:
            price = sku_dict[sku] * item['PRICE']
        print(price)
        basket = basket + price
    return basket




print(checkout("A,A"))


