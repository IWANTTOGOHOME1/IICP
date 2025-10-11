# 소개

IICP는 집가고싶다 통합 통신 프로토콜 (IWANTTOGOHOME Integrated Communication Protocol)의 약자로 집가고싶다 Inc.의 프로젝트에 주로 사용되는 프로토콜이다.

# 통신 방식

[code] [클라이언트→서버] 연결 요청

	[서버→클라이언트] 연결 허용
	
		[서버↔클라이언트] 메시지 전송
		
		[서버→클라이언트] 또는 [클라이언트→서버] 연결 해제 선언

			[서버&클라이언트] 연결 해제

			[서버&클라이언트] 종료

	[서버→클라이언트] 연결 거부

		[서버&클라이언트] 연결 해제

		[서버&클라이언트] 종료

위 처럼 IICP는 [연결 요청] → [연결 허용] → [통신] 순으로 진행된다.

어떻게 보면 TCP/IP 위에서 작동하는 데이터 전송 규격이지만 모르겠고 아무튼 프로토콜이다.

# 프로토콜 구조

IICP는 저사양 장치부터 고사양 장치까지 간단한 형태로 통신하는것이 목표이기 때문에 간결한 구조를 가지고 있다.

# 연결 요청

[code] +HANDSHAKE

HOST: server.iwanttogohome.net
PORT: 888
CLIENT: IRHS101

HOST에는 접속하려는 서버의 주소,

PORT에는 접속하려는 서버의 포트,

CLIENT는 집가고싶다 Inc.의 클라이언트 모델명을 전송한다.

모델명에 대한 자세한 정보를 알아보려면 클릭

# 연결 허용

[code] +ACCEPT

이건 그냥 단순하다.

# 연결 거부

[code] +REJECT

Sorry! The server is still in development.

+REJECT아래 줄바꿈 뒤 내용은 연결 거부 사유이다.

# 연결 해제 선언

[code] +FAREWELL

I'll be back.

연결 거부와 마찬가지로 +FAREWELL 아래 줄바꿈 뒤 내용은 연결 해제 사유이다.

연결 거부와 연결 해제는 쓰이는 상황이 다르니 주의

# 메시지 전송

[code] +MESSAGE

wlqrkrhtlvek
wlqrkrhtlvek
wlqrkrhtlvek

+MESSAGE아래 줄바꿈 뒤 내용은 본문이다.

# 시스템 메시지 (아이디어)

[code] +SYSTEM

DISPLAYCLEAR
KEYSTROKEPRINT
PRINTLN

+SYSTEM 아래 줄바꿈 뒤 내용은 시스템 명령어이다.

예를 들어 DISPLAYCLEAR 은 화면 초기화,

KEYSTROKEPRINT 는 눌린 키 전송 시작 요청,

PRINTLN 은 줄바꿈 등 +MESSAGE 에서는 할 수 없던 작업을 가능하게 해준다.

# 깃허브 링크

[bookmark] 

# 정보

[table] 

