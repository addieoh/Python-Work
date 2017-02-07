kwh_used = 1000

if kwh_used <= 500:
    print (kwh_used * 0.53 + (kwh_used * 0.53 * .20))
elif kwh_used > 500 and kwh_used <= 1500:
    print (265 + (kwh_used - 500)* .79 + ((265 + (kwh_used - 500)* .79) * .20))
elif kwh_used > 1500 and kwh_used <= 2500:
    print (265 + 790 + (kwh_used - 1500) * 1.11 + ((265 + 790 + (kwh_used - 1500) * 1.11) * .20))
else:
    print (265 + 790 + 1110 + (kwh_used - 2500) * 1.89 + ((265 + 790 + 1110 + (kwh_used - 2500) * 1.89) * .20))
