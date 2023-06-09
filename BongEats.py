from bs4 import BeautifulSoup
import requests
import re
import pymongo

links = [
         "https://www.bongeats.com/recipe/pressure-cooker-mutton-curry", 
         "https://www.bongeats.com/recipe/tandoori-pomfret", 
         "https://www.bongeats.com/recipe/mulor-ghonto",
         "https://www.bongeats.com/recipe/doi-begun",
         "https://www.bongeats.com/recipe/luchi",
         "https://www.bongeats.com/recipe/bengali-vegetable-fried-rice",
         "https://www.bongeats.com/recipe/shorshe-posto-diye-machher-jhal",
         "https://www.bongeats.com/recipe/chhanar-payesh",
         "https://www.bongeats.com/recipe/narkeler-naru",
         "https://www.bongeats.com/recipe/rosho-puli",
         "https://www.bongeats.com/recipe/pressure-cooker-mutton-curry",
         "https://www.bongeats.com/recipe/mishti-polao",
         "https://www.bongeats.com/recipe/chicken-curry",
         "https://www.bongeats.com/recipe/mutton-kosha",
         "https://www.bongeats.com/recipe/phirni",
         "https://www.bongeats.com/recipe/plain-mosur-dal",
         "https://www.bongeats.com/recipe/badhakopir-bora",
         "https://www.bongeats.com/recipe/phulkopir-data-chorchori",
         "https://www.bongeats.com/recipe/moog-puli",
         "https://www.bongeats.com/recipe/choshi-pitha",
         "https://www.bongeats.com/recipe/macher-teler-bora",
         "https://www.bongeats.com/recipe/mangsher-ghugni",
         "https://www.bongeats.com/recipe/chicken-pakora",
         "https://www.bongeats.com/recipe/pachmishali-dal",
         "https://www.bongeats.com/recipe/thorer-ghonto",
         "https://www.bongeats.com/recipe/beler-shorbot",
         "https://www.bongeats.com/recipe/dahi-vada",
         "https://www.bongeats.com/recipe/tyangra-macher-jhol",
         "https://www.bongeats.com/recipe/aloor-dum",
         "https://www.bongeats.com/recipe/chingri-paturi",
         "https://www.bongeats.com/recipe/notey-shaak",
         "https://www.bongeats.com/recipe/shutki-mach-bata",
         "https://www.bongeats.com/recipe/shingi-machher-jhol",
         "https://www.bongeats.com/recipe/potoler-dorma-with-dal-stuffing",
         "https://www.bongeats.com/recipe/shutki-mach-bata",
         "https://www.bongeats.com/recipe/shingi-machher-jhol",
         "https://www.bongeats.com/recipe/bhetki-paturi",
         "https://www.bongeats.com/recipe/murgir-lal-jhol",
         "https://www.bongeats.com/recipe/paat-patar-bora",
         "https://www.bongeats.com/recipe/narkeler-naru",
         "https://www.bongeats.com/recipe/labra",
         "https://www.bongeats.com/recipe/mutton-roll",
         "https://www.bongeats.com/recipe/jhal-muri",
         "https://www.bongeats.com/recipe/machher-matha-diye-moog-dal",
         "https://www.bongeats.com/recipe/kumror-chokka",
         "https://www.bongeats.com/recipe/chal-kumror-bora",
         "https://www.bongeats.com/recipe/ilish-maachh-bhaja",
         "https://www.bongeats.com/recipe/bengali-mutton-curry",
         "https://www.bongeats.com/recipe/phuchka",
         "https://www.bongeats.com/recipe/tadka",
         "https://www.bongeats.com/recipe/phulkopir-shingara",
         "https://www.bongeats.com/recipe/chirer-polao",
         "https://www.bongeats.com/recipe/phulkopir-data-chorchori",
         "https://www.bongeats.com/recipe/badhakopir-bora",
         "https://www.bongeats.com/recipe/alu-posto",
         "https://www.bongeats.com/recipe/uchhe-kumro-bhaja",
         "https://www.bongeats.com/recipe/chaal-potol",
         "https://www.bongeats.com/recipe/mughlai-chicken-korma",
         "https://www.bongeats.com/recipe/mochar-paturi",
         "https://www.bongeats.com/recipe/chhatur-porota",
         "https://www.bongeats.com/recipe/chhanar-polao",
         "https://www.bongeats.com/recipe/sheer-khurma",
         "https://www.bongeats.com/recipe/mourola-machher-tok",
 ]

Recipes = []

x = 0

while x <= len(links)-1:
    link = links[x]

    # starting the scrapping
    html_texts = requests.get(link).text

    soup = BeautifulSoup(html_texts, 'lxml')

    # to find the name of the recipe
    recipe = soup.find('div', class_='text-container').h1
    recipe = recipe.text

    # to find the servings
    serving = soup.find('div', class_='column-3 w-col w-col-6')
    serving = serving.p.text[0]

    # to find the cooking time
    cook_time = soup.find('div', class_='column-4 w-col w-col-6')
    cook_time = cook_time.p.text

    cook_time = re.split('\s', cook_time)
    time = float(cook_time[0])

    ##to convert the time into minute
    if (cook_time[1] == 'hours' or cook_time[1] == 'hour'):
        time *= 60

    # to find the ingredients
    ingredients = soup.findAll('ul')

    ingredients.pop()
    ingredients.pop()
    final_ingredients = ''

    for ing in ingredients:
        for li in ing.find_all("li"):

            if (li.strong and li.strong.text[-1] != 'ml'):
                # for quantity
                quantity = li.strong.text
                quantity = re.split('\s', quantity)

                f = len(quantity)

                # print(quantity)
                # print(len(quantity))

                if (len(quantity) > 1):
                    if (quantity[1] == 'kg'):
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(float(quantity[0]) * 1000) + 'g'

                    elif (quantity[1] == 'tsp'):
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(float(quantity[0]) * 4.2) + 'g'

                    elif (quantity[1] == 'tbsp'):
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(float(quantity[0]) * 15) + 'g'

                    elif (quantity[1] == 'cup'):
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(float(quantity[0]) * 250) + 'g'

                    elif (quantity[1] == 'pinch'):
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(float(quantity[0]) * 1.5) + 'g'

                    else:
                        if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                            quantity[0] = 0.5
                        elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                            quantity[0] = 0.25
                        elif (quantity[0] == 'Â¾'):
                            quantity[0] = 0.75
                        elif (quantity[0] == '1Â½'):
                            quantity[0] = 1.5
                        quantity[0] = str(quantity[0]) + 'g'

                else:
                    if (quantity[0] == 'Â½' or quantity[0] == '1â „2'):
                        quantity[0] = 0.5
                    elif (quantity[0] == 'Â¼' or quantity[0] == '1â „4'):
                        quantity[0] = 0.25
                    elif (quantity[0] == 'Â¾'):
                        quantity[0] = 0.75
                    elif (quantity[0] == '1Â½'):
                        quantity[0] = 1.5
                    quantity[0] = quantity[0] + 'g'

                # for ingredients name
                names = re.split('\s', li.text)

                n = quantity[0]
                b = False
                k = 0

                for name in names:

                    f -= 1

                    if (f == 0): b = True
                    if (name[0] == '('): b = False
                    if (b):
                        n += ' ' + name
                final_ingredients += n + ', '

    final_ingredients = final_ingredients[:len(final_ingredients) - 2]

    rrecipe = {}

    rrecipe['name'] = recipe
    rrecipe['ingredients'] = final_ingredients
    rrecipe['time'] = time
    rrecipe['serving'] = serving

    Recipes.append(rrecipe)

    #ss = str(input('continue? y/n'))
    x = x + 1
    #if xnxx == 3:
       # break

print(Recipes)

uri = "mongodb+srv://tanviropy:tanviropy@cluster0.lftvw.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient("mongodb+srv://tanviropy:tanviropy@cluster0.lftvw.mongodb.net/?retryWrites=true&w=majority")
cluster = client["BD-Cuisine"]
db = cluster["Res"]


try:
    db.insert_many(Recipes)
    print("MongoDB Connected")
except:
      print('Error occurred')    