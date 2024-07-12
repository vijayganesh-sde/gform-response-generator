from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By 
from random_word import RandomWords


def generate_responses(total_responses,form_link):
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver= webdriver.Chrome(options=options)
  
  r=RandomWords()
  while total_responses:
    form_page = driver.get(form_link)
    time.sleep(3)
    try:
      questions = driver.find_elements(By.CLASS_NAME,"Qr7Oae")
      for question in questions:
        try:
          input_texts = question.find_element(By.CLASS_NAME,"whsOnd.zHQkBf")
          input_texts.send_keys(r.get_random_word())
          continue
        except:
          print("no inputs")
        try:
          textboxes = question.find_element(By.CLASS_NAME,"KHxj8b.tL9Q4c") 
          textboxes.send_keys(r.get_random_word())
          continue
        except:
          print("no Textboxes")
        try:
          radiobuttons = question.find_elements(By.CLASS_NAME,"Od2TWd.hYsg7c")
          rand_choice=random.randrange(0,len(radiobuttons))
          radiobuttons[rand_choice].click()
          continue
        except:
          print("no radio buttons")
        try:
          checkBoxes = question.find_elements(By.CLASS_NAME,"uVccjd.aiSeRd.FXLARc.wGQFbe.BJHAP.oLlshd")
          no_of_choices=random.randrange(1,len(checkBoxes)) 
          print(no_of_choices,"kjnkjn")
          rand_choices = random.sample(list(range(len(checkBoxes))),no_of_choices)
          print(rand_choices,"jn")
          for c in rand_choices:
            checkBoxes[c].click()
            time.sleep(1)
          continue
        except:
          print("no check Boxes")
        try:
          insert_box = question.find_element(By.CLASS_NAME,"jgvuAb.ybOdnf.cGN2le.t9kgXb.llrsB")
          insert_box.click()
          time.sleep(2)
          options = driver.find_element(By.CLASS_NAME,"OA0qNb.ncFHed.QXL7Te").find_elements(By.CLASS_NAME,"MocG8c.HZ3kWc.mhLiyf.OIC90c.LMgvRb")
          opt_choice=random.randrange(1,len(options)) 
          
          options[opt_choice].click()
          time.sleep(1)
          continue
        except:
          print("no Options")
      try:
        SubmitBtn = driver.find_element(By.CLASS_NAME,"uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd") 
        SubmitBtn.click()
        
      except:
        print("no Submit BTN")

      total_responses-=1
    except:
      print("cant get")
    time.sleep(2)

  