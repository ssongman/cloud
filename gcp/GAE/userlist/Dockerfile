FROM    java
MAINTAINER ssongmantop@gmail.com
#RUN     apt-get -y update

# 2. 소스 복사
ADD ./userlist.jar /usr/src/app/userlist.jar

# 3. 실행 디렉토리 설정
WORKDIR /usr/src/app

# 4. App 서버 실행 (Listen 포트 정의)
EXPOSE 8080
CMD     java -jar userlist.jar
