#input income
inc = int(input('type your income per month : '))
#all year income
ayinc = inc*12

#other income
#oth = int(input())
#all year other income
#ayoth = oth*12

#outcome
out = int(input('type your outcome per month : '))
#all year outcome
ayout = out*12

#=================================================================================

#tax deduction
status = input('type your status(single/married with income,no income) : ')
if status == 'single' :
    deduction = 60000
    parent = int(input('how many parent : '))*30000
    disable = int(input('how many disable : '))*60000
    moneysoodti = (ayinc-ayout-(deduction+parent+disable))
    
elif status == 'married with no income' :
    children = input('how many children(number&year) : ').split()
    deduction = 60000+60000
    parent = int(input('how many parent : '))*30000
    disable = int(input('how many disable : '))*60000
    if int(children[1]) < 2561 :
        kidde = int(children[0])*30000
        moneysoodti = (ayinc-ayout-(deduction+parent+disable+kidde))
    elif int(children[1]) > 2561 :
        kidde = int(children[0])*60000
        moneysoodti = (ayinc-ayout-(deduction+parent+disable+kidde))

elif status == 'married with income' :
    children = input('how many children(number&year) : ').split()
    deduction = 60000
    parent = int(input('how many parent : '))*30000
    disable = int(input('how many disable : '))*60000
    if int(children[1]) < 2561 :
        kidde = int(children[0])*30000
        moneysoodti = (ayinc-ayout-(deduction+parent+disable+kidde))
    elif int(children[1]) > 2561 :
        kidde = int(children[0])*60000
        moneysoodti = (ayinc-ayout-(deduction+parent+disable+kidde))
        
#=================================================================================
        
#insurance
lifesave = int(input('type your life and saving insurance : '))
health = int(input('type your health insurance : '))
lh = lifesave + health
if lh > 100000 :
    lh == 100000
else : lh == lh 
social = int(input('type your social security insurance : '))
if social > 6300 :
    social == 6300
else : social == social
ph = int(input('type your parent health insurance : '))
if ph > 15000 :
    ph == 15000
else : ph == ph
se = int(input('type your social enterprise : '))
if se > 100000 :
    se == 100000
else : se == se

#=================================================================================

#investment
rmf = int(input('type your retirement mutual fund : '))
if rmf >= ayinc*0.3 and rmf > 500000 :
    rmf == 500000
elif rmf <= ayinc*0.3 and rmf > 500000 :
    rmf == 500000
elif rmf >= ayinc*0.3 and rmf < 500000 :
    rmf == rmf
else : rmf == rmf
ssf = int(input('type your super saving funds : '))
if ssf >= ayinc*0.3 and ssf > 200000 :
    ssf == 200000
elif ssf <= ayinc*0.3 and ssf > 200000 :
    ssf == 200000
elif ssf >= ayinc*0.3 and rmf < 200000 :
    ssf == ssf
else : ssf == ssf
pen = int(input('type your pension life insurance : '))
if pen >= ayinc*0.15 and pen > 200000 :
    pen == 200000
elif pen <= ayinc*0.15 and pen > 200000 :
    pen == 200000
elif pen >= ayinc*0.15 and pen < 200000 :
    pen == pen
else : pen == pen
allinvest = rmf + ssf +pen
if allinvest > 500000 :
    allinvest = 500000
else : allinvest = allinvest

#=================================================================================
alll = moneysoodti - lh - ph - se - allinvest
#donation
normal = int(input('type your normal donation : '))
if normal > alll*0.1 :
    normal = alll*0.1
else : normal = normal
ed = int(input('type your education and sport donation : '))
eddy = ed*2
if eddy > alll*0.1 :
    eddy = alll*0.1
else : eddy = eddy

lastmoney = alll - normal - eddy
   
#=================================================================================

#tax calculation
if lastmoney <= 150000:  
    tax = 0
elif 300000 >= lastmoney > 150000 : 
    tax = (lastmoney - 150000) * 0.05
elif 500000 >= lastmoney > 300000 : 
    tax = (lastmoney - 300000) * 0.10 + 7500 
elif 750000 >= lastmoney > 500000 : 
    tax = (lastmoney - 500000) * 0.15 + 27500 
elif 1000000 >= lastmoney > 750000 : 
    tax = (lastmoney - 750000) * 0.20 + 65000 
elif 2000000 >= lastmoney > 1000000 : 
    tax = (lastmoney - 1000000) * 0.25 + 115000 
elif 5000000 >= lastmoney > 2000000 :
    tax = (lastmoney - 2000000) * 0.30 + 365000
elif lastmoney > 5000000 :
    tax = (lastmoney - 5000000) * 0.35 + 1265000
print("tax = ",tax)