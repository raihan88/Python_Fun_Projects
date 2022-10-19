import pywhatkit as pw
text = """
My dearest Saru

My letter I am sure has piqued your interest and left you surprised.
 But trust me, this letter is real.

You, my dear Saru are the reason I am no longer alone, because of 
you and your love, I look forward to each day. And because of you,
I have a beautiful family now. You make my life complete. My day
starts and ends by looking at your face.

So thank you, for giving me so much happiness.
Your Rai
"""

pw.text_to_handwriting(text,"sample.png")
print("Done")