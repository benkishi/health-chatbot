import random
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root", password="", database="healthdb")

cursor=conn.cursor()
query='select * from dataset where disease="gerd"'
cursor.execute(query)
records=cursor.fetchmany()

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]



def health_varchar():
    
    for row in records:

        print("Bot: ""Disease" ,row[0], "and its symptoms ",row[0],row[1],row[2],row[3],row[4],row[5])

    return records

    

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_HEALTH = records
    
#if(health_varchar):
    #query='select * from dataset where disease="gerd"'
    #cursor.execute(query)
    #records=cursor.fetchmany()
    #for row in records:
       # print(records)

        
