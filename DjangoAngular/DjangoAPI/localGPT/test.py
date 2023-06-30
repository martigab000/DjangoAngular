import sqlite3





#within While loop
conn = sqlite3.connect(r'C:\Users\gabriel.martin\OneDrive - Office Ally Inc\Desktop\AngularAI\chatbox-ui\DjangoAngular\DjangoAPI\db.sqlite3')
cursor = conn.cursor()
cursor.execute('SELECT * FROM EmployeeApp_questions WHERE Response = "none"')
inp = cursor.fetchone()
if inp:
    print(inp)
    id = inp[0]
    print(id)
    #generate the response


    # inp = inp[0]
    res = "changed it"

    # insert and update response

    cursor.execute('UPDATE EmployeeApp_questions SET Response = (?) WHERE QuestionID = (?)', (res, id))
    conn.commit()
    cursor.close()
    conn.close()

