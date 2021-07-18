import PyPDF2
from gtts import gTTS

pdfFile = open('text.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

myText = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    myText += pageObj.extractText()

print(myText)
pdfFile.close()

tts = gTTS(text=myText, lang='en')
tts.save("story.mp3")

