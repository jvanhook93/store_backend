from gettext import Catalog
from flask import Flask, request, abort
import json
import random
from data import me, catalog


app = Flask(__name__)



@app.get("/")
def home():
  return "Hello from flask"



@app.get("/test")
def test():
  return "This is just another endpoint"


# get /about returns your name
@app.get("/about")
def about():
  return "Tom Van Hook"


#API PRODUCTS



@app.get("/api/test")
def test_api():
  return json.dumps("OK")


@app.get("/api/about")
def about_api():
  return json.dumps(me)


@app.get("/api/catalog")
def get_catalog():
  return json.dumps(catalog)

@app.post("/api/catalog")
def save_product():
  product = request.get_json()
  
  if not "title" in product:
    return abort(400, "ERROR: Title is required")

  if len(product["title"]) < 5:
    return abort(400, "ERROR: Title must have a max of 5 characters")

  if not "price" in product:
    return abort(400, "ERROR: Products must include a price.")

  if product["price"] < 1:
    return abort(400, "ERROR: Price should be greater or equal to 1")

  product["_id"] = random.randint(100, 100000)

  catalog.append(product)

  return product

@app.get("/api/product/<id>")
def get_product_by_id(id):
  for prod in catalog:
    if prod["_id"] == id:
      return json.dumps(prod)

  return json.dumps("Error: ID not valid")

# get /api/products/<category>
@app.get("/api/products/<category>")
def get_product_by_category(category):
  results = []
  for prod in catalog:
    if prod["category"].lower() == category.lower():
      results.append(prod)

  return json.dumps(results)

@app.get("/api/count")
def get_count():
  count =len(catalog)
  return json.dumps(count)

# get  /api/catalog/total  
# return the total inv/money/value of the catalog

@app.get("/api/catalog/total")
def price_total():
  total = 0
  for prod in catalog:
    total += prod["price"]

  return json.dumps(total)


@app.get("/api/catalog/cheapest")
def catalog_cheapest():
  cheapest = catalog[0]
  for prod in catalog:
    if prod["price"] < cheapest["price"]:
      # found a better fit
      cheapest = prod

  return json.dumps(cheapest)
  




# play rock, paper, scissors
# /api/game/paper
# return should be a dictionary (as json)
# {
#   "you": paper,
#   "pc": rock,
#   "winner": you
# }

# step 1: create endpoint return {"you": rock }

@app.get("/api/game/<pick>")
def game(pick):
  
  num = random.randint(0,2)
  pc = ""
  
  if num == 0:
    pc = "rock"

  elif num == 1:
    pc = "paper"

  else:
    pc = "scissors"

  
  winner = ""
  if pick == "paper":
    if pc == "rock":
      winner = "you"
    elif pc == "scissors":
      winner = "pc"
    else:
      winner = "draw"
  elif pick == "rock":
    if pc == "rock":
      winner = "draw"
    elif pc == "paper":
      winner = "pc"
    else:
      winner = "you"
  elif pick == "scissors":
    if pc == "rock":
      winner = "pc"
    elif pc == "paper":
      winner = "you"
    else:
      winner = "draw"

  
  results = {
    "you": pick,
    "PC": pc,
    "Winner": winner
  }

  return json.dumps(results)


# step 2: generate a random number between 0 and 2
# change the number to be rock, paper or scissors
# return 
# {
#   "you": paper,
#   "pc": rock,
# }



# step 3
# finish the logic to pick the winner





#app.run(debug=True)