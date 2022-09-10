from deep_translator import GoogleTranslator
import random as rd
from config import time_random_list
import time

def g_translation_function_mr_en(inText):
  try:
    time_random = rd.choice(time_random_list)
    time.sleep(2*time_random)
    if len(inText)<=4999:
      outText = GoogleTranslator(source='mr', target='en').translate(inText)
      return outText
    else:
      return ""
  except Exception as e:
    print(e)
    pass
  
def g_translation_function_mr_hi(inText):
  try:
    time_random = rd.choice(time_random_list)
    time.sleep(2*time_random)
    if len(inText)<=4999:
      outText = GoogleTranslator(source='mr', target='hi').translate(inText)
      return outText
    else:
      return ""
  except Exception as e:
    print(e)
    pass