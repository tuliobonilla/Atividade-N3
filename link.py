import psycopg2

class Link():
#conectar com o database
  def linkDatabase(self):
    link = psycopg2.connect(
      host="localhost",
      database="",
      user="",
      password="",)

    return link