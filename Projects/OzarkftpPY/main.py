import pyodbc
import os
import paramiko

def Loadtxt(name):
    conn=pyodbc.connect('Driver={SQL Server};Server=W2811;Database=lsg;Trusted_Connection=yes;')

    cursorobj=conn.cursor()

    cursorobj.execute('select * from openquery(jde,\'select * from ftpoutbnd.f5541826\')')

    file='C:\\projects\\oftp\\upldnsqoh.txt'
    fileisthere=os.path.isfile(file)
    print(fileisthere)
    if fileisthere==True:
        os.remove(file)

    for c in cursorobj:

        with open('C:\\projects\\oftp\\upldnsqoh.txt', 'a') as f:
            f.write(c[0])
            f.write('\n')
        print(c[0])
    fileisthere=os.path.isfile(file)
    print(fileisthere)

    if fileisthere==True:
        host = 'oasftp.oreillyauto.com'  # hard-coded
        port = 22
        transport = paramiko.Transport((host, port))

        password = 'klahsef8742lr'  # hard-coded
        username = 'sftp_lincoln'  # hard-coded
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        filepath = os.listdir('C:\\projects\\oftp')
        for item in filepath:
            print(item)
            sftp.put('C:\\projects\\oftp\\' + item, '/upload/' + item)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Loadtxt('Running a sql')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
