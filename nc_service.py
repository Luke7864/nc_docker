from flask import *
import subprocess
from string import ascii_lowercase,ascii_uppercase

listallow=list(ascii_lowercase)
listallow+=['_','-']
listallow+=['1','2','3','4','5','6','7','8','9','0']

password_allow = listallow
password_allow += list(ascii_uppercase)

print("DEVELOPER: SHIN JAE UK(Y311J)")
print("Every Commercial Use without permission is banned")
print("http://jaeuk.xyz")
print("https://weekhack.tistory.com")
print("Press Ctrl+C to make it run in background")
print("The program must only be run through the run.sh file.")

try:
    password_file = open("./password.txt", 'r')
    password = str(password_file.read())
    password = password.replace("\n", "")
    if password not in password_allow:
        print("Error: Only English Letter and Numbers are allowed for Password")
        exit(0)
    password="/"+password
    password_file.close()

except:
    print("Error: No Password File")
    exit(0)

if password=='/default' or password=='/ ' or password=='/':
    print("Fatal Error!!")
    print("Security Error: No Password Set!! Change Password from password.txt file!!")
    print("Program Closed with Fatal Error.")
    exit(0)

def read_form(formname):
    args=request.form[formname]
    return args

app=Flask(__name__)
@app.route(password, methods=['POST', 'GET'])
def connect():
    if request.method == 'GET':
        return render_template('form.html', link=password)
    if request.method == 'POST':
        try:
            name=read_form('name')
            binary=request.files['binary']
            flag=request.files['flag']

        except:
            return"flag파일을 사용하지 않더라도 아무거나 파일을 flag파일로 만들어(빈파일 가능) 업로드해주시기 바랍니다."

        try:
            for i in range(len(name)):
                if list(name)[i] not in listallow:
                    return "특수문자/대문자 입력은 금지되어 있습니다."

            probmake = subprocess.check_output(["mkdir /home/probs/"+name], shell=True)
            homemake = subprocess.check_output(["mkdir /home/probs/"+name+"/home"], shell=True)
            binary.save('/home/probs/'+name+"/home/"+binary.filename)
            flag.save('/home/probs/'+name+"/home/"+flag.filename)
        except:
            return "오류: 이미 해당명의 문제가 존재하거나, 문제에 특수문자 등 금지된 문자가 포함된 것 같습니다."

        if flag.filename!="flag":
            return "flag파일의 파일명이 flag가 아닙니다."

        try:
            port = open("./port.txt", 'r')
            port_num = str(port.read())
            port_num = port_num.replace("\n", "")
            save_port = port_num
            port.close()

            f=open("/home/probs/"+name+"/xinetd",'w')
            data = "service "+name+"\n" \
                   "{\n" \
                   "disable	= no\n" \
                   "flags	= REUSE\n" \
                    "type   = UNLISTED\n" \
                    "port   = "+port_num+"\n" \
                    "socket_type	=stream\n" \
                   "protocol	=tcp\n" \
                   "user	= "+name+"\n" \
                   "wait	=no\n" \
                   "server	=/home/"+name+"/"+binary.filename+"\n" \
                   "}"
            f.write(data)
            f.close()
        except:
            return "xinetd 파일을 만드는데 오류가 생겼습니다."

        try:
            f=open("/home/probs/"+name+"/Dockerfile",'w')
            data = "FROM ubuntu:16.04\n" \
                   "RUN apt update\n" \
                   "RUN apt install xinetd -y\n" \
                   "RUN apt install libc6-dev-i386 -y\n" \
                   "RUN useradd "+name+" -m -s /bin/bash\n" \
                   "COPY ./home /home/"+name+"\n" \
                   "COPY ./xinetd /etc/xinetd.d/"+name+"\n" \
                   "RUN chmod 750 /home/"+name+" /home/"+name+"/"+binary.filename+"\n" \
                   "RUN chmod 440 /home/"+name+"/flag\n" \
                   "RUN chown -R root:"+name+" /home/"+name+"\n" \
                    "CMD [\"/usr/sbin/xinetd\",\"-dontfork\"]"
            f.write(data)
            f.close()
        except:
            return "Dockerfile 파일을 만드는데 오류가 생겼습니다."

        try:

            setting = subprocess.check_output(["docker build -t "+name+":0.0 /home/probs/"+name+"/"], shell=True)
            setting = subprocess.check_output(["docker run -itd -p "+port_num+":"+port_num+" --name "+name+" "+name+":0.0"], shell=True)

            port = open("./port.txt", 'w')
            port_num = int(port_num)
            port_num += 1
            port_num = str(port_num)
            port.write(port_num)
            port.close()
        except:
            return "도커 실행중 오류가 생겼습니다."

        host=request.host
        host=host.replace(":12345","")
        return "PORT가 설정되었습니다!\nnc "+host+" "+save_port

@app.route(password+'/python2', methods=['POST', 'GET'])
def connect2():
    if request.method == 'GET':
        return render_template('form_python2.html', link=password)
    if request.method == 'POST':
        try:
            name=read_form('name')
            binary=request.files['binary']
            flag=request.files['flag']

        except:
            return"flag파일을 사용하지 않더라도 아무거나 파일을 flag파일로 만들어(빈파일 가능) 업로드해주시기 바랍니다."

        try:
            for i in range(len(name)):
                if list(name)[i] not in listallow:
                    return "특수문자/대문자 입력은 금지되어 있습니다."

            probmake = subprocess.check_output(["mkdir /home/probs/"+name], shell=True)
            homemake = subprocess.check_output(["mkdir /home/probs/"+name+"/home"], shell=True)
            binary.save('/home/probs/'+name+"/home/"+binary.filename)
            flag.save('/home/probs/'+name+"/home/"+flag.filename)
        except:
            return "오류: 이미 해당명의 문제가 존재하거나, 문제에 특수문자 등 금지된 문자가 포함된 것 같습니다."

        if flag.filename!="flag":
            return "flag파일의 파일명이 flag가 아닙니다."

        try:
            port = open("./port.txt", 'r')
            port_num = str(port.read())
            port_num = port_num.replace("\n", "")
            save_port = port_num
            port.close()

            f=open("/home/probs/"+name+"/xinetd",'w')
            data = "service "+name+"\n" \
                   "{\n" \
                   "disable	= no\n" \
                   "flags	= REUSE\n" \
                    "type   = UNLISTED\n" \
                    "port   = "+port_num+"\n" \
                    "socket_type	=stream\n" \
                    "server = /usr/bin/python\n" \
                    "protocol	=tcp\n" \
                   "user	= "+name+"\n" \
                   "wait	=no\n" \
                   "server_args	=/home/"+name+"/"+binary.filename+"\n" \
                   "}"
            f.write(data)
            f.close()
        except:
            return "xinetd 파일을 만드는데 오류가 생겼습니다."

        try:
            f=open("/home/probs/"+name+"/Dockerfile",'w')
            data = "FROM ubuntu:16.04\n" \
                   "RUN apt update\n" \
                   "RUN apt install xinetd -y\n" \
                   "RUN apt install libc6-dev-i386 -y\n" \
                   "RUN apt install python -y\n" \
                   "RUN apt install python-pip -y\n" \
                   "RUN apt install python-dev -y\n" \
                   "RUN useradd "+name+" -m -s /bin/bash\n" \
                   "COPY ./home /home/"+name+"\n" \
                   "COPY ./xinetd /etc/xinetd.d/"+name+"\n" \
                   "RUN chmod 750 /home/"+name+" /home/"+name+"/"+binary.filename+"\n" \
                   "RUN chmod 440 /home/"+name+"/flag\n" \
                   "RUN chown -R root:"+name+" /home/"+name+"\n" \
                    "CMD [\"/usr/sbin/xinetd\",\"-dontfork\"]"
            f.write(data)
            f.close()
        except:
            return "Dockerfile 파일을 만드는데 오류가 생겼습니다."

        try:

            setting = subprocess.check_output(["docker build -t "+name+":0.0 /home/probs/"+name+"/"], shell=True)
            setting = subprocess.check_output(["docker run -itd -p "+port_num+":"+port_num+" --name "+name+" "+name+":0.0"], shell=True)

            port = open("./port.txt", 'w')
            port_num = int(port_num)
            port_num += 1
            port_num = str(port_num)
            port.write(port_num)
            port.close()
        except:
            return "도커 실행중 오류가 생겼습니다."

        host=request.host
        host=host.replace(":12345","")
        return "PORT가 설정되었습니다!\nnc "+host+" "+save_port

@app.route(password+'/python3', methods=['POST', 'GET'])
def connect3():
    if request.method == 'GET':
        return render_template('form_python3.html', link=password)
    if request.method == 'POST':
        try:
            name=read_form('name')
            binary=request.files['binary']
            flag=request.files['flag']

        except:
            return"flag파일을 사용하지 않더라도 아무거나 파일을 flag파일로 만들어(빈파일 가능) 업로드해주시기 바랍니다."

        try:
            for i in range(len(name)):
                if list(name)[i] not in listallow:
                    return "특수문자/대문자 입력은 금지되어 있습니다."

            probmake = subprocess.check_output(["mkdir /home/probs/"+name], shell=True)
            homemake = subprocess.check_output(["mkdir /home/probs/"+name+"/home"], shell=True)
            binary.save('/home/probs/'+name+"/home/"+binary.filename)
            flag.save('/home/probs/'+name+"/home/"+flag.filename)
        except:
            return "오류: 이미 해당명의 문제가 존재하거나, 문제에 특수문자 등 금지된 문자가 포함된 것 같습니다."

        if flag.filename!="flag":
            return "flag파일의 파일명이 flag가 아닙니다."

        try:
            port = open("./port.txt", 'r')
            port_num = str(port.read())
            port_num = port_num.replace("\n", "")
            save_port = port_num
            port.close()

            f=open("/home/probs/"+name+"/xinetd",'w')
            data = "service "+name+"\n" \
                   "{\n" \
                   "disable	= no\n" \
                   "flags	= REUSE\n" \
                    "type   = UNLISTED\n" \
                    "port   = "+port_num+"\n" \
                    "socket_type	=stream\n" \
                    "server = /usr/bin/python3\n" \
                    "protocol	=tcp\n" \
                   "user	= "+name+"\n" \
                   "wait	=no\n" \
                   "server_args	=/home/"+name+"/"+binary.filename+"\n" \
                   "}"
            f.write(data)
            f.close()
        except:
            return "xinetd 파일을 만드는데 오류가 생겼습니다."

        try:
            f=open("/home/probs/"+name+"/Dockerfile",'w')
            data = "FROM ubuntu:16.04\n" \
                   "RUN apt update\n" \
                   "RUN apt install xinetd -y\n" \
                   "RUN apt install libc6-dev-i386 -y\n" \
                   "RUN apt install python3 -y\n" \
                   "RUN apt install python3-pip -y\n" \
                   "RUN apt install python3-dev -y\n" \
                   "RUN useradd "+name+" -m -s /bin/bash\n" \
                   "COPY ./home /home/"+name+"\n" \
                   "COPY ./xinetd /etc/xinetd.d/"+name+"\n" \
                   "RUN chmod 750 /home/"+name+" /home/"+name+"/"+binary.filename+"\n" \
                   "RUN chmod 440 /home/"+name+"/flag\n" \
                   "RUN chown -R root:"+name+" /home/"+name+"\n" \
                    "CMD [\"/usr/sbin/xinetd\",\"-dontfork\"]"
            f.write(data)
            f.close()
        except:
            return "Dockerfile 파일을 만드는데 오류가 생겼습니다."

        try:

            setting = subprocess.check_output(["docker build -t "+name+":0.0 /home/probs/"+name+"/"], shell=True)
            setting = subprocess.check_output(["docker run -itd -p "+port_num+":"+port_num+" --name "+name+" "+name+":0.0"], shell=True)

            port = open("./port.txt", 'w')
            port_num = int(port_num)
            port_num += 1
            port_num = str(port_num)
            port.write(port_num)
            port.close()
        except:
            return "도커 실행중 오류가 생겼습니다."

        host=request.host
        host=host.replace(":12345","")
        return "PORT가 설정되었습니다!\nnc "+host+" "+save_port

@app.route(password+'/del', methods=['POST', 'GET'])
def del_docker():
    if request.method == 'GET':
        dockerlist = subprocess.check_output(["docker ps -a"], shell=True)
        dockerlist = dockerlist.decode('utf-8')
        dockerlist = dockerlist.replace("\n","<br />")
        return render_template('del_docker.html', link=password, docker=dockerlist)
    if request.method == 'POST':
        try:
            docker_name = read_form('doc_name')
            for i in range(len(docker_name)):
                if list(docker_name)[i] not in listallow:
                    return "특수문자/대문자 입력은 금지되어 있습니다."
        except:
            return '오류: 문제명 또는 도커 ID가 비어있습니다.'

        try:
            setting = subprocess.check_output(["rm -R /home/probs/" + docker_name], shell=True)
            setting = subprocess.check_output(["docker stop "+docker_name], shell=True)
            setting = subprocess.check_output(["docker rm " + docker_name], shell=True)
            try:
                setting = subprocess.check_output(["docker rmi -f $(docker images -q)"], shell=True)
            except:
                pass
            return docker_name+' 삭제 완료!'
        except:
            setting = subprocess.check_output(["docker restart " + docker_name], shell=True)
            return '오류가 발생했습니다. 입력하신 컨테이너명은 다음과 같습니다: '+docker_name

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="12345")
