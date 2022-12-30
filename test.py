# import googletrans
# from googletrans import Translator

# print(googletrans.LANGUAGES)
# text1 = "Hello welcome to my website!"

# translator = Translator()
# print(translator.detect(text1))
# trans1 = translator.translate(text1, src='en', dest='ko')
# print("English to Japanese: ", trans1.text)
from gtts import gTTS
st = """류현진의 국내 매니지먼트를 맡고 있는 에이스펙코퍼레이션은 "류현진이 오는 29일 미국으로 출국한다"고 밝혔다. 류현진의 12월 출국은 이례적이다. 종전에는 MLB 일정 종료 후 귀국해 국내에서 훈련을 하다 대개 스프링캠프를 앞둔 2월 출국했다. 매년 초 일본 오키나와나 제주도 등에서 몸 상태를 끌어올린 후 미국으로 돌아갔다.  """
tts = gTTS(st, lang="ko")
tts.save('hello.mp3')