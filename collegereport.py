import click
import pymysql
import smtplib


def get_db_config():
    return { 'host' : 'localhost', 'user' : 'root', 'password' : 'root', 'database' : 'testdb'};


def sort_avg(*args):

    if(float(args[0][1]) == float(args[1][1])):
        return cmp(args[0][0], args[1][0])

    return cmp(float(args[0][1]), float(args[1][1]))


def get_college_students_scores(cursor, collegename):
    """Returns Particular College Students and their scores."""

    output = "\n\nDetails of Students of "+collegename+"\n"
    output = output+"StudentName    Score"+"\n"

    sqlQuery = "SELECT DBNAME, MARKS FROM MARKS WHERE DBNAME IN (SELECT DBNAME FROM STUDENTS WHERE COLLEGE = "+collegename+")"

    try:
        cursor.execute(sqlQuery)

        rows = cursor.fetchall()

        for row in rows:
            output = output+str(row[0])+"        "+str(row[1])+"\n"


    except Exception as e:
        print(e)
        return

    return output



def get_college_stat(cursor, collegename):
    """Used to display stats of each college with min, max and avg marks."""


    output = "College   Count   Max     Min     Avg\n"

    cursor.execute("SELECT COUNT(DBNAME) FROM STUDENTS WHERE COLLEGE = " + collegename + "")
    count = cursor.fetchone()[0]
    cursor.execute(
        "SELECT MAX(MARKS) FROM MARKS WHERE DBNAME IN (SELECT DBNAME FROM STUDENTS WHERE COLLEGE=" + collegename + ")")
    max = cursor.fetchone()[0]
    cursor.execute(
        "SELECT MIN(MARKS) FROM MARKS WHERE DBNAME IN (SELECT DBNAME FROM STUDENTS WHERE COLLEGE=" + collegename + ")")
    min = cursor.fetchone()[0]
    cursor.execute(
        "SELECT AVG(MARKS) FROM MARKS WHERE DBNAME IN (SELECT DBNAME FROM STUDENTS WHERE COLLEGE=" + collegename + ")")
    avg = cursor.fetchone()[0]

    output = output + collegename + '       ' + str(count) + '      ' + str(max) + '    ' + str(min) + '    ' + str(avg)+"\n"

    return output






def get_overall_report(cursor, collegename):
    """Give Overall report of all colleges."""

    output = "College       AvgMarks\n"
    colleges_report = []

    try:
        cursor.execute("SELECT DISTINCT COLLEGE FROM STUDENTS")
        all_colleges = cursor.fetchall()
        #print("All colleges ", all_colleges)
        for college in all_colleges:
            college = college[0]
            cursor.execute(
            "SELECT AVG(MARKS) FROM MARKS WHERE DBNAME IN (SELECT DBNAME FROM STUDENTS WHERE COLLEGE='" + college + "')")
            colleges_report.append((college, str(cursor.fetchone()[0])))

        list.sort(colleges_report, cmp=sort_avg, reverse=True)

    except Exception as e:
        print(e)

    for eachClg in colleges_report:
        output = output+eachClg[0]+'         '+eachClg[1]+'\n'

    return output


def send_mail(content, sender_mail, password, receiver_mail):
    """Send mail to some of your friend."""
    try:
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.ehlo()
        mail.starttls()

        message = 'Subject:Regarding College Report \n\n'+content

        mail.login(sender_mail, password)

        mail.sendmail(sender_mail, receiver_mail , message)

        mail.close()

    except Exception as e:
        print(e)



@click.command()
@click.argument('collegename')
@click.argument('sender_mail_id')
@click.argument('sender_password')
@click.argument('receiver_mail_id')

def college_report(collegename, sender_mail_id, sender_password, receiver_mail_id):
    """Gives the statistics of particular college."""

    content = "\n\n"

    db_config = get_db_config()

    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'testdb')

    cursor = db.cursor()

    content = content + get_college_students_scores(cursor, collegename) +"\n\n"

    content = content+get_college_stat(cursor, collegename) + "\n\n"

    content = content+ get_overall_report(cursor, collegename) + "\n\n"


    send_mail(content, sender_mail_id, sender_password, receiver_mail_id)
    
    cursor.close()





if(__name__ == '__main__'):
    college_report()
