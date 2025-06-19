que=["Which notable award-winning Bollywood movie was shot in J&K?",
     "What is the website of eUNNAT?",
     "Which of the following services can be accessed through the UMANG platform?",
     "Basholi paintings, a renowned art form in Jammu and Kashmir, are characterized by the influence of which artistic style?",
     "Which of the following is a popular traditional tea beverage in Jammu and Kashmir?",
     "The Martand sun temple is situated at which district of Jammu and Kashmir?",
     "Which historical fort in Jammu offers panoramic views of the Tawi River and the city?",
     "Famous tourist spot Gulmarg located in which district of Jammu and Kashmir?",
     "Which famous festival of Jammu and Kashmir celebrates the blooming of tulips and showcases cultural performances?",
     "​The famous Vaishno Devi shrine is located in which town of Jammu and Kashmir"]

ops=[
    {"A":"Haidar","B":"Rockstar","C":"Bajrangi Bhaijaan","D":"Tubelight"},
    {"A":"eunnat.jk.gov.in","B":"eunnat.jk@gov.in","C":"eunnat@jk.gov.in","D":"eunnat.gov.in"},
    {"A":"Government services","B":"Online banking","C":"Social Media","D":"Mobile gaming"},
    {"A":"Mughal","B":"Persian","C":"Rajput","D":"Tibetan"},
    {"A":"Lassi","B":"Masala Chai","C":"Kashmiri kahwa","D":"Thupka"},
    {"A":"Jammu","B":"Shopian","C":"Anantnag","D":"Samba"},
    {"A":"Jaigarh Fort","B":"Jaisalmer Fort","C":"Mubarak Mandi Complex","D":"Bahu Fort"},
    {"A":"Budgam","B":"Reasi","C":"Shopian","D":"Baramulla"},
    {"A":"Baisakhi","B":"Hemis Festival","C":"Lohri","D":"Tulip Festival"},
    {"A":"Katra","B":"Akhnoor","C":"Udhampur","D":"Reasi"},
    ]

ans=["Bajrangi Bhaijaan",
     "eunnat@jk.gov.in",
     "Government services",
     "Mughal",
     "Kashmiri kahwa",
     "Anantnag",
     "Bahu Fort",
     "Baramulla",
     "Tulip Festival",
     "Katra",
    ]

score=0
print("=======welcome int the world of GK about Jambu Kasmir======")
for i in range(0,10):
    print(f"{i+1}) {que[i]}")
    print()
    for key,value in ops[i].items():
        print(f"[{key}] {value}")
    x=input("answer: ")
    print()
    if x==ans[i]:
        score += 1
        print("CORRECT ANSWER..........")
    else:
        print("WRONG ANSWER !!!")   
    print()     

print(f"YOUR TOTAL SCORE IS : {score}") 

































