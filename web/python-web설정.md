### atom 설정
1. File > Settings > Install 로 이동
2. Install Packages 에서 패키지 설치
  - autocomplete-python
  - script

====================================================================

### web 설치 & 설정
1. bitnami wamp 설치 - apache, mysql
2. apache 설정 - conf/httpd.conf
  - LoadModule cgi_module modules/mod_cgi.so 사용, 주석여부 확인
  - 확장자가 py 인 파일이 실행되도록 추가
    <Directory "C:/Bitnami/wampstack-7.1.15-0/apache2/htdocs">
      Options Indexes FollowSymLinks
      AllowOverride None
      Require all granted
      <Files "*.py">
        Options ExecCGI
        AddHandler cgi-script .py
      </Files>
    </Directory>
3. py 파일 상단에 추가
  #!python
  print('content-type: text/html; charset=utf-8')



====================================================================

pkg 설치

pip install html-sanitizer  #XSS

====================================================================
