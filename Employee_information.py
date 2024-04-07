import mysql.connector
cnx=mysql.connector.connect(user='kian', password='Kian.py192',host='127.0.0.1', database='info')#If you want to use this code, enter your database information in this line
cursor=cnx.cursor()
cursor.execute("SELECT name,height,weight FROM employees ORDER BY height desc")
result=cursor.fetchall()
final_result = None
old_row = 0
final=0
for row in result:
    row=list(row)
    if row[1]==final:
        if row[2]>old_row[2]:
            old_now=old_row
            delete_query="DELETE FROM employees WHERE name = %s AND height = %s AND weight = %s"
            cursor.execute(delete_query,(old_row[0],old_row[1],old_row[2]))

            select_query="INSERT INTO employees VALUES(%s,%s,%s);"
            cursor.execute(select_query,(old_now[0],old_now[1],old_now[2]))
            cursor.execute("SELECT height FROM employees ORDER BY height desc;")
            final_result=cursor.fetchall()
        elif row[2]<old_row[2]:
            now_row=row
            delete_query2="DELETE FROM employees WHERE name = %s AND height = %s AND weight = %s"
            cursor.execute(delete_query2,(row[0],row[1],row[2]))
            
            select_query2="INSERT INTO employees VALUES(%s,%s,%s);"
            cursor.execute(select_query2,(now_row[0],now_row[1],now_row[2]))
            cursor.execute("SELECT name,height,weight FROM employees ORDER BY height desc")
            final_result=cursor.fetchall()
        cnx.commit()
    final=row[1]
    old_row=row
cursor.close()
final_list=[]
for i in final_result:
    final_list.append(i)
for item in final_list:
    print(item[0],item[1],item[2])
cnx.close()
#In order for the code to work on your system, the name of the user with their height and weight must exist in your database, 
#and in the second line of the code, you must have entered your database information, and be careful that this code only works with the MySQL database.