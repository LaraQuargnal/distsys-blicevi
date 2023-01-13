def f2(x, y):
    assert isinstance(x, dict) and isinstance(y, dict)
    assert all(isinstance(v, list) for v in x.values()) and all(isinstance(v, list) for v in y.values())
    assert all(k in x.keys() for k in ['valute', 'cijena']) and all(k in y.keys() for k in ['valute', 'cijena'])
    return [(x['cijena'][i], x['valute'][i]) for i in range(len(x['valute'])) if x['valute'][i] == y['valute'][i] and x['cijena'][i] == y['cijena'][i]]
  
"""
def func2(x,y):
    assert isinstance(x, dict) and isinstance(y, dict)
    assert all([isinstance(i,list) for _,i in x.items()]) and all([isinstance(i,list) for _,i in y.items()])
    assert (x.get("valute") and x.get("cijena")) and (y.get("valute") and y.get("cijena"))
    return [(a,b) for a,d,b,c in zip(x["cijena"],y["cijena"], x["valute"], y["valute"]) if (a==d) and (b==c)]
"""

print(f2({"valute":["GBP", "USD", "CZK", "Error"], "cijena":[8.5,7.7,0.3,10.3]}, {"valute":["EUR", "USD", "CZK", "Error"], "cijena":[7.5,7.7,0.3,5.5]}))
