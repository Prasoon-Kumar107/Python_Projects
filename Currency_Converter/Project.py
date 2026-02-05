indian_rupee=["Argentine Peso","Australian Dollar","Bahraini Dinar","Botswana Pula","Brazilian Real","British Pound","Bruneian Dollar","Bulgarian Lev","Canadian Dollar","Chilean Peso","Chinese Yuan Renminbi","Colombian Peso","Czech Koruna","Danish Krone","Emirati Dirham","Euro","Hong Kong Dollar","Hungarian Forint","Icelandic Krona","Indonesian Rupiah","Iranian Rial","Israeli Shekel","Japanese Yen","Kazakhstani Tenge","Kuwaiti Dinar","Libyan Dinar","Malaysian Ringgit","Mexican Peso","Nepalese Rupee","New Zealand Dollar","Norwegian Krone","Omani Rial","Pakistani Rupee","Philippine Peso","Polish Zloty","Qatari Riyal","Romanian New Leu","Russian Ruble","Saudi Arabian Riyal","Singapore Dollar","South African Rand","South Korean Won","Sri Lankan Rupee","Swedish Krona","Swiss Franc","Taiwan New Dollar","Thai Baht","Trinidadian Dollar","Turkish Lira","US Dollar"]
value=[0.067963,56.488524,228.282218,6.431693,15.402916,115.784516,67.033069,51.272975,62.676522,0.089998,11.972762,0.021422,4.062432,13.440063,23.372121,100.281222,10.934272,0.250749,0.704164,0.005292,0.002040,25.762844,0.582267,0.163826,280.652772,15.892705,20.184053,1.890686,4.580500,0.624707,51.584006,8.475729,223.050241,0.301852,1.519487,23.516475,23.580801,19.734782,1.100230,22.889097,67.033069,4.784591,0.062366,0.285522,8.983993,107.660027,2.937455,2.648201,12.649474,2.136444,85.834114]
con_dict=dict(zip(indian_rupee,value))
print(con_dict.keys())
i=input("Choose in which currency you want to convert your rupees in from above list : ")
v=float(input("Please enter the amount of currency you want to convert : "))
if i in con_dict:
    o=con_dict.get(i)
    converted_value=v*o
    print(f"value of {v} {i} in rupees is : {converted_value} rupees")
else:
    print("Please enter the correct input/currency available in the list.")