class PopcatAPI():
  def __init__(self):
    self.BASE_URL = "https://api.popcat.xyz/"
    
  def __convert_iso8601(self, timestamp: str) -> int:
    return str(time.mktime(time.strptime(timestamp.replace('T', ' ')[:timestamp.find('.')], '%Y-%m-%d %H:%M:%S')))[:-2]
    
  def welcome_card(self, top_text: str, middle_text: str, bottom_text: str, avatar_url: str, background_url: str = "https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png"):
    return rq.get(f"{self.BASE_URL}welcomecard", params = {"background": background_url, "text1": top_text, "text2": middle_text, "text3": bottom_text, "avatar": avatar_url}).url
    
  def color(self, color_hex: str) -> dict:
    return rq.get(f"{self.BASE_URL}color/{color_hex.replace('#', '')[0:6]}").json()
  
  def lyrics(self, song_name: str) -> dict:
    return rq.get(f"{self.BASE_URL}lyrics", params = {"song": song_name[0:119]}).json()
  
  def periodic_table(self, element: str) -> dict:
    return rq.get(f"{self.BASE_URL}periodic-table", params = {"element": element[0:119]}).json()
  
  def pickup_lines(self) -> str:
    return rq.get(f"{self.BASE_URL}pickuplines").json()["pickupline"]
  
  def imdb(self, query: str) -> dict:
    r = rq.get(f"{self.BASE_URL}imdb", params = {"q": query}).json()
    vratings = []
    for i in r["ratings"]:
      vstr = ": ".join(v for v in i.values())
      vratings.append(vstr)
    r["ratings"] = vratings
    r["released"] = self.__convert_iso8601(r["released"])
    r["dvd"] = self.__convert_iso8601(r["dvd"])
    return r

  def jail(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}jail", params = {"image": image_url}).url
    
  def unforgivable(self, text: str = "Popcat api so trash") -> str:
    return rq.get(f"{self.BASE_URL}unforgivable", params = {"text": text}).url
  
  def screenshot(self, url: str = "https://google.com") -> str:
    return rq.get(f"{self.BASE_URL}screenshot", params = {"url": url if url.startswith(("https://", "http://")) else (("https://" + url[url.find("//") + 2:]) if "//" in url else "https://" + url)}).url
  
  def random_color(self) -> dict:
    return self.color(color_hex = rq.get(f"{self.BASE_URL}randomcolor").json()["hex"])
  
  def steam(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}steam", params = {"q": query}).json()
  
  def sad_cat(self, text: str = "people hating me for being innocent") -> str:
    return rq.get(f"{self.BASE_URL}sadcat", params = {"text": text}).url
  
  #def oogway_quote
  #does not work right now
  
  def communism(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}communism", params = {"image": image_url}).url
  
  def car_pictures(self) -> dict:
    return rq.get(f"{self.BASE_URL}car").json()
  
  def chat_bot(self, msg: str, owner: str, botname: str) -> str:
    return rq.get(f"{self.BASE_URL}chatbot", params = {"msg": msg, "owner": owner, "botname": botname}).json()["response"]
  
  def pooh(self, top_text: str, bottom_text: str) -> str:
    return rq.get(f"{self.BASE_URL}pooh", params = {"text1": top_text, "text2": bottom_text}).url
  
  def shower_thoughts(self) -> str:
    r = rq.get(f"{self.BASE_URL}showerthoughts").json()
    return f"{r['result']}\n> {r['author']}"
  
  def quote(self) -> str:
    return rq.get(f"{self.BASE_URL}quote").json()["quote"]
  
  def wanted(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}wanted", params = {"image": image_url}).url
  
  def subreddit(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}subreddit/{query}").json()
  
  def github(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}github/{query}").json()
  
  def weather(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}weather", params = {"q": query}).json()
  
  def who_would_win(self, image1_url: str = "https://cdn.iconscout.com/icon/free/png-512/javascript-2752148-2284965.png", image2_url: str = "https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png") -> str:
    return rq.get(f"{self.BASE_URL}whowouldwin", params = {"image1": image1_url, "image2": image2_url}).url
  
  def gun(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}gun", params = {"image": image_url}).url
  
  def lulcat(self, text: str) -> str:
    return rq.get(f"{self.BASE_URL}lulcat", params = {"text": text}).json()["text"]
  
  #def opinion
  #doesn't work for now
  
  def drake(self, top_text: str, bottom_text: str) -> str:
    return rq.get(f"{self.BASE_URL}drake", params = {"text1": top_text, "text2": bottom_text}).url
  
  #def instagram
  #doesn't work for now
  
  def npm(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}npm", params = {"q": query}).json()
  
  def fact(self) -> str:
    return rq.get(f"{self.BASE_URL}fact").json()["fact"]
  
  def ship(self, image1_url: str = "https://cdn.popcat.xyz/popcat.png", image2_url: str = "https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png") -> str:
    return rq.get(f"{self.BASE_URL}ship", params = {"user1": image1_url, "user2": image2_url}).url
  
  def joke(self) -> str:
    return rq.get(f"{self.BASE_URL}joke").json()["joke"]
  
  def biden_tweet(self, text: str = "Popcat API sucks!!") -> str:
    return rq.get(f"{self.BASE_URL}biden", params = {"text": text}).url
  
  def pikachu(self, text: str = "Hello :O") -> str:
    return rq.get(f"{self.BASE_URL}pikachu", params = {"text": text}).url
  
  def mock(self, text: str) -> str:
    return rq.get(f"{self.BASE_URL}mock", params = {"text": text}).json()["text"]
  
  def would_you_rather(self) -> dict:
    return rq.get(f"{self.BASE_URL}wyr").json()
  
  def meme(self) -> dict:
    return rq.get(f"{self.BASE_URL}meme").json()
  
  def colorify(self, image_url: str = "https://cdn.popcat.xyz/popcat.png", color: str = None):
    return rq.get(f"{self.BASE_URL}colorify", params = {"image": image_url, "color": color if color else self.random_color()["hex"][1:]}).url
  
  def drip(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}drip", params = {"image": image_url}).url
  
  def clown(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}clown", params = {"image": image_url}).url
  
  def translate(self, translate_to: str, text: str):
    return rq.get(f"{self.BASE_URL}translate", params = {"to": translate_to, "text": text}).json()["translated"]
  
  def encode(self, text: str):
    return rq.get(f"{self.BASE_URL}encode", params = {"text": text}).json()["binary"]
  
  def decode(self, binary: str):
    return rq.get(f"{self.BASE_URL}decode", params = {"binary": binary}).json()["text"]
  
  def uncover(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}uncover", params = {"image": image_url}).url
  
  def ad(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}ad", params = {"image": image_url}).url
  
  def blur(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}blur", params = {"image": image_url}).url
  
  def invert(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}invert", params = {"image": image_url}).url
  
  def grayscale(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}grayscale", params = {"image": image_url}).url
  
  def eight_ball(self) -> str:
    return rq.get(f"{self.BASE_URL}8ball").json()["answer"]
  
  #def playstore
  #endpoint in maintenance
  
  def itunes(self, query: str) -> dict:
    return rq.get(f"{self.BASE_URL}itunes", params = {"q": query}).json()
  
  def reverse(self, text: str) -> str:
    return rq.get(f"{self.BASE_URL}reverse", params = {"text": text}).json()["text"]
  
  def joke_overhead(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}jokeoverhead", params = {"image": image_url}).url
  
  def double_struck(self, text: str) -> str:
    return rq.get(f"{self.BASE_URL}doublestruck", params = {"text": text}).json()["text"]
  
  def mnm(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}mnm", params = {"image": image_url}).url
  
  def pet(self, image_url: str = "https://cdn.popcat.xyz/popcat.png") -> str:
    return rq.get(f"{self.BASE_URL}pet", params = {"image": image_url}).url
  
  def text_to_morse(self, text: str) -> str:
    return rq.get(f"{self.BASE_URL}texttomorse", params = {"text": text}).json()["morse"]
  
  def caution(self, text: str = "Sample Text") -> str:
    return rq.get(f"{self.BASE_URL}caution", params = {"text": text}).url
  
  def alert(self, text: str = "Sample Text") -> str:
    return rq.get(f"{self.BASE_URL}alert", params = {"text": text}).url
  
  def facts(self, text: str = "Sample Text") -> str:
    return rq.get(f"{self.BASE_URL}facts", params = {"text": text}).url
