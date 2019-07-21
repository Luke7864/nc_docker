# nc_docker
CTF와 워게임의 포너블 문제를 위한 nc서버를 자동으로 docker에 올려 생성해주는 웹 기반 툴입니다. 누구나 문제이름, 바이너리, flag만 입력하면 자동으로 netcat 서버가 도커위에서 생성되며, 주소와 포트를 할당해 출력합니다. 허가 없는 상업적 이용을 금합니다. 소스코드 변형 및 사용은 원 저작자 표기 하에 허용합니다.

사용법:
0. git clone https://github.com/Luke7864/nc_docker 해주세요.
1. install_requirement.sh파일을 이용하여 필수설정을 설치해줍니다.
2. 만약 도커가 설치되어있지 않은 경우 docker_install.sh파일을 이용해 도커를 설치해 줍니다.
3. password 파일을 이용하여 password를 설정해줍니다. 외부인의 접근을 방지하기 위해 password파일은 접속링크의 일부로 사용됩니다.
4. run.sh파일을 실행해 줍니다.

주의 사항:
1. 해당 프로그램의 작동은 반드시 sudo를 사용 가능한 권한이 있는 사용자로 진행하여야 합니다.
2. 상업적 용도가 아닌 소스코드 변형 및 사용은 원 저작자명(신재욱) 표기 하에 사용이 가능합니다.
3. 상업적 용도의 사용은 개인적으로 shin@jaeuk.xyz에게 연락하여 허락을 받아주시기 바랍니다.

오류해결:
1. Fatal Security Error: 패스워드 파일을 수정하지 않아 기본 패스워드 일 경우 발생합니다. 패스워드를 수정해주세요.
2. 그 외의 오류: 파일을 임의로 수정하거나 삭제할 경우 발생할 수 있습니다. 다시 설치해주세요.

기타: 
1. 저는 해당 소프트웨어를 사용하며 발생하는 모든 사건 사고에 대해 책임지지 않습니다.
2. 취약점 등 발생 시 POC, 수정방안과 함께 shin@jaeuk.xyz로 제보해주세요.



It is a web-based tool that automatically creates an nc server for the CTF and wargame issue on the docker. If anyone types in the problem name, binary, or flag, the netcat server is automatically created on the docker, and the address and port are assigned and output. Unauthorized commercial use is prohibited. Source code variations and use are permitted under the original author notation.

How to use:
0. git clone https://github.com/Luke7864/nc_docker please.
1. Install the required settings using the install_requirement.sh file.
2. If the driver is not installed, use the docker_install.sh file to install the docker.
3. Set password using password file. To prevent access by outsiders, the password file is used as part of the connection link.
4. Run the run.sh file.

Precautions:
1. The operation of the program must be performed by a user who has the authority to use sudo.
2. Transformation and use of source code other than commercial purpose can be used under original author name (Shin Jae-uk) notation.
3. For commercial use, please contact shin@jaeuk.xyz for personal permission.

Resolving the error:
1. Fatal Security Error: Occurs when the default password is not modified. Please correct your password.
2. Other errors: It may occur when you randomly modify or delete a file. Please reinstall.

Miscellaneous: 
1. I am not responsible for any incidents that occur using the software.
2. Please report POC, fix plan and shin@jaeuk.xyz when vulnerability occurs.
3. This translation has been translated by Google and may contain errors. I am not responsible for any linguistic errors. 
