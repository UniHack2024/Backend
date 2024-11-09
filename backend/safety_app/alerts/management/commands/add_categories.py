from django.core.management.base import BaseCommand
from alerts.models import Category

class Command(BaseCommand):
    help = 'Add default categories to the database'

    def handle(self, *args, **kwargs):
        categories = [
            "Avertizări de interes public privind încălcări ale legii",
            "Animale fără stăpân",
            "Cadavre de animale",
            "Capac canalizare lipsă",
            "Inundații",
            "Clădire în paragină",
            "Teren ocupat ilegal",
            "Iluminat nefuncțional",
            "Alee murdara în parc",
            "Defrișare",
            "Loc de joacă deteriorat",
            "Plante alergeni",
            "Poluare",
            "Distrugere proprietate publică/privată",
            "Furt",
            "Persoane fără adăpost",
            "Tulburarea liniștii",
            "Coșuri de gunoi lipsă/deteriorate",
            "Deratizare/dezinsectie/dezinfectie",
            "Deșeuri abandonate",
            "Drum înzăpezit",
            "Șantiere",
            "Groapă",
            "Trotuar/Pistă de biciclete deteriorată",
            "Parcare ilegală",
            "Stradă blocată",
            "Semafor defect",
            "Semn de circulație poziționat greșit",
            "Vehicul abandonat",
            "Accident"
        ]

        for category_name in categories:
            Category.objects.get_or_create(name = category_name)
            self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" added.'))
        
        self.stdout.write(self.style.SUCCESS('All categories have been added successfully!'))