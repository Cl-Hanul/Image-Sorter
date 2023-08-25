# from os import chdir
# chdir(".")
#--------------------
import base64 as _base64
import hashlib as hashlib
from Crypto.Cipher import AES as _AES
#----------------------------------
#----------------------------------

_BS = 16 # blocksize를 16바이트로 고정시켜야 함(AES의 특징)

# AES에서는 블럭사이즈가 128bit 즉 16byte로 고정되어 있어야 하므로 문자열을 encrypt()함수 인자로 전달시
# 입력 받은 데이터의 길이가 블럭사이즈의 배수가 아닐때 아래와 같이 패딩을 해주어야 한다.
# 패딩: 데이터의 길이가 블럭사이즈의 배수가 아닐때 마지막 블록값을 추가해 블록사이즈의 배수로 맞추어 주는 행위
_pad = (lambda s: s+ (_BS - len(s) % _BS) * chr(_BS - len(s) % _BS).encode())
_unpad = (lambda s: s[:-ord(s[len(s)-1:])])

#오브젝트 출처:https://pagichacha.tistory.com/54
class _AESCipher(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest() # 키가 쉽게 노출되는 것을 막기 위해 키를 어렵게 처리하는 과정으로 보통 해시를 적용

    def encrypt(self, message): # 암호화 함수
        message = message.encode() # 문자열 인코딩
        raw = _pad(message) # 인코딩된 문자열을 패딩처리
        cipher = _AES.new(self.key, _AES.MODE_CBC, self.__iv().encode('utf8')) # AES 암호화 알고리즘 처리(한글처리를 위해 encode('utf8') 적용)
        enc = cipher.encrypt(raw) # 패딩된 문자열을 AES 알고리즘으로 암호화
        return _base64.b64encode(enc).decode('utf-8') # 암호화된 문자열을 base64 인코딩 후 리턴

    def decrypt(self, enc): # 복호화 함수 -> 암호화의 역순으로 진행
        enc = _base64.b64decode(enc) # 암호화된 문자열을 base64 디코딩 후
        cipher = _AES.new(self.key, _AES.MODE_CBC, self.__iv().encode('utf8')) # AES암호화 알고리즘 처리(한글처리를 위해 encode('utf8') 적용)
        dec = cipher.decrypt(enc) # base64 디코딩된 암호화 문자열을 복호화
        return _unpad(dec).decode('utf-8') # 복호화된 문자열에서 패딩처리를 풀고(unpading) 리턴

    def __iv(self):
        return chr(0) * 16

#-------------------------------------

def HanulEncrypt(key,value)-> str:
    '''
    ### 개요
    AES를 이용한 `암호화` 함수 이며,
    
    `문자열`을 반환합니다.
    
    ---
    ### 원리
    `key`를 받으면 `key`를 통해 `value`의 값을 변경합니다.
    
    ---
    ### 파라미터
    
    | 파라미터 |\| 타입 |\| 설명                                  |
    |   :-:   |  :-:   |  :------------------------------------ |
    |---------|--------|----------------------------------------|
    |  `key`  |\| `str`|\| AES 암호화에 사용되는 `문자열`입니다.   |    
    | `value` |\| `str`|\| AES를 통해 암호화될 `문자열`입니다.     |
    '''
    
    return _AESCipher(key).encrypt(value)



def HanulDecrypt(key,value):
    '''
    ### 개요
    AES를 이용한 `복호화` 함수 이며,
    
    `문자열`을 반환합니다.
    
    ---
    ### 원리
    `key`를 받으면 `key`를 통해 `value`의 값을 변경합니다.
    
    ---
    ### 파라미터
    
    | 파라미터 |\| 타입 |\| 설명                                  |
    |   :-:   |  :-:   |  :------------------------------------ |
    |---------|--------|----------------------------------------|
    |  `key`  |\| `str`|\| AES 복호화에 사용되는 `문자열`입니다.   |    
    | `value` |\| `str`|\| AES를 통해 복호화될 암호화된 `문자열`입니다.     |
    '''
    
    return _AESCipher(key).decrypt(value)