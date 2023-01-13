def f3(proizvodi):
    assert isinstance(proizvodi, list) and all(isinstance(p, dict) for p in proizvodi)
    sve_kat = {p["kategorija"] for p in proizvodi}
    return {kategorija: sum(p["ocjena"] for p in proizvodi if p["kategorija"] == kategorija) for kategorija in sve_kat}

"""
def f3(x):
    assert isinstance(x,list) and all([isinstance(y, dict) for y in x])
    c = {k for d in x for a,k in d.items() if a=="kategorija"}
    return {k:sum([v["ocjena"] for v in x if v["kategorija"] == k]) for d in x for _,k in d.items() if k in c}
"""
  
print(f3([{"naziv":"Burek","kategorija":"pite", "ocjena":1},{"naziv":"Ramsteak","kategorija":"steak", "ocjena":9},{"naziv":"Ribeye","kategorija":"steak", "ocjena":4},{"naziv":"Sirnica","kategorija":"pite", "ocjena":5}]))
