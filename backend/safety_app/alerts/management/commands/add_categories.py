from django.core.management.base import BaseCommand
from alerts.models import Category

class Command(BaseCommand):
    help = 'Add default categories to the database'

    def handle(self, *args, **kwargs):
        categories = [
            "Altele",
            "Animale",
            "Apă și canalizare",
            "Construcții și terenuri",
            "Garaje, coșerit, cimitire și toalete publice",
            "Iluminat public",
            "Mediu, locuri de joacă și spații verzi",
            "Ordine publică",
            "Organizare și funcționare asociații de proprietari",
            "Piețe agroalimentare",
            "Probleme de integritate",
            "Probleme de integritate referitoare la angajați",
            "Salubrizare, dezinsecție, deratizare și deszăpezire",
            "Șantiere",
            "Străzi și trotuare",
            "Trafic rutier și semne de circulație",
            "Transport în comun",
            "Urbanism",
            "Website și platformă de sesizări"
        ]

        for category_name in categories:
            Category.objects.get_or_create(name = category_name)
            self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" added.'))
        
        self.stdout.write(self.style.SUCCESS('All categories have been added successfully!'))