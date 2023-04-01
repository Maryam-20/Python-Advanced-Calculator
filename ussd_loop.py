num_attempt = ["4","3","2","1", "0"]
ussd = input("Enter your USSD code> ")
if ussd == "*141#":
    print("""
    1. My Offer
    2. Data Bundle
    3. 5000/22GB/30days
    4. 3000/11GB/30days
    """)
    user_response = input("which operation do you want to perform? ")
    if user_response == "1":
       print("""
       My Airtel Offer
       1. N50/250MB/14days
       2. N100/500MB/7days
       3. MORE DATA OFFER
       4. VOICE OFFER
       """)
    elif user_response == "2":
        print("""
        1. Daily/Weekly Bundles
        2. Weekly Bundle
        3. Montly Bundles
        4. More Data (Data++)
        """)
    elif user_response == "3":
        print("""
        22GB for 30days at N5000.
        After your plan finishes?
        1. Continue browsing from
        Airtime/160MB Exra
        2. Stop my Data
        """ )
    elif user_response == "4":
        print("""
        11GB for 30days at N5000.
        After your plan finishes?
        1. Continue browsing from
        Airtime/160MB Exra
        2. Stop my Data
        """)
    else:
        print("Invalid request")
else:
    print("Invalid input!!")
    num = 0
    for error in num_attempt:
       print(error[num] + " attempt left ")
       ussd = input("Enter your USSD code> ")
       if ussd == "*141#":
        print("""
        1. My Offer
        2. Data Bundle
        3. 5000/22GB/30days
        4. 3000/11GB/30days
        """)
        user_response = input("which operation do you want to perform? ")
        if user_response == "1":
            print("""
            My Airtel Offer
            1. N50/250MB/14days
            2. N100/500MB/7days
            3. MORE DASTA OFFER
            4. VOICE OFFER
            """)
        elif user_response == "2":
            print("""
            1. Daily/Weekly Bundles
            2. Weekly Bundle
            3. Montly Bundles
            4. More Data (Data++)
            """)
        elif user_response == "3":
            print("""
            22GB for 30days at N5000.
            After your plan finishes?
            1. Continue browsing from
            Airtime/160MB Exra
            2. Stop my Data
            """ )
        elif user_response == "4":
            print("""
            11GB for 30days at N5000.
            After your plan finishes?
            1. Continue browsing from
            Airtime/160MB Exra
            2. Stop my Data
            """)
        else:
            print("Invalid request")
        break
    num += 1