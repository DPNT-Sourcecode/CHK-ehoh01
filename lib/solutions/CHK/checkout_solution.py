

# noinspection PyUnusedLocal
# skus = unicode string

price_cat = {"A" : {"PRICE" : 50, "OFFER" : {3 : 130 , 5 : 200}}, "B" : {"PRICE" : 30, "OFFER" : {2 : 45}}, "C" : {"PRICE" : 20}, "D" : {"PRICE" : 15}, "E" : {"PRICE" : 40, "FREE" : {2 : {"B" : 1 }}}}

def split(word):
    return [char for char in word]

def checkout(skus):
    sku_list = split(skus)
    sku_dict = {}
    for sku in sku_list:
        if not price_cat.get(sku,False):
            return -1
        count = sku_dict.get(sku,0) 
        sku_dict[sku] = count +1
    key_list = []
    discounted_list =[]
    for sku in sku_dict.keys():
        if price_cat[sku].get("FREE",False):
            discounted_list.append(sku)
        else:
            key_list.append(sku)
    discounted_list.extend(key_list)
    basket = 0
    for sku in discounted_list:
        price = 0
        item = price_cat[sku]
        prices = []
        if sku_dict[sku] > 0:
            if item.get("FREE",False):
                quant = list(item['FREE'].keys())[0]
                other_item =  list(item['FREE'][quant].keys())[0]
                if sku_dict[sku] % quant == 0:
                    if sku_dict.get(other_item,False):
                        sku_dict[other_item] = sku_dict[other_item] - (sku_dict[sku] / quant) * item['FREE'][quant][other_item]
                elif sku_dict[sku] > quant:
                    i = 1
                    while sku_dict[sku] - quant * i > quant:
                        i = i + 1
                    if sku_dict.get(other_item,False):
                        sku_dict[other_item] = sku_dict[other_item] - (sku_dict[sku] / quant) * item['FREE'][quant][other_item]
                        sku_dict[other_item] = sku_dict[other_item] - (quant * i / quant) * item['FREE'][quant][other_item]
            if item.get("OFFER",False):
                for quant in item['OFFER'].keys():
                    if sku_dict[sku] % quant == 0:
                        price = (sku_dict[sku] / quant) * item['OFFER'][quant] 
                        prices.append(price)
                    elif sku_dict[sku] > quant:
                        i = 1
                        while sku_dict[sku] - quant * i > quant:
                            i = i + 1
                        price = i * item['OFFER'][quant] + ((sku_dict[sku] - (quant * i))* item['PRICE'])
                        prices.append(price)
                    elif sku_dict[sku] < quant:
                        price = sku_dict[sku] * item['PRICE']
                        prices.append(price)
                price = min(prices)
            else:
                price = sku_dict[sku] * item['PRICE']
            print(price)
            basket = basket + price
    return int(basket)

print(checkout("AAAAAAAA"))