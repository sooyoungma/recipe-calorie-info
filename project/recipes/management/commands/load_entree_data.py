from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from recipes.models import Entree



ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
	# Show this when the user types help
	help = "Loads data from nutritioninfo.csv into our Entree model"

	def handle(self, *args, **options):
		if Entree.objects.exists():
			print('Nutritional data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		print("Loading entree data for nutritional data")
		for row in DictReader(open('./nutritioninfo.csv')):
			entree = Entree()
			print(Entree)
			entree.name = row['Entree']
			entree.calories = row['Calories']
			entree.calories_from_fat = row['Calories From Fat']
			entree.total_fat = row['Total Fat (g)']
			entree.saturated_fat = row['Saturated Fat (g)']
			entree.trans_fat = row['Trans Fat (g)']
			entree.cholesterol = row['Cholesterol (mg)']
			entree.sodium = row['Sodium (mg)']
			entree.carbohydrates = row['Carbohydrates (g)']
			entree.fiber = row['Fiber (g)']
			entree.sugar = row['Sugars (g)']
			entree.protein = row['Protein (g)']
			entree.category = row['Category']
			entree.restaurant = row['Restaurant']
			entree.save()
