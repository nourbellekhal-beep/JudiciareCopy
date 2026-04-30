from services.models import Service, Category
import random

def run():
    # Ensure categories exist or rename existing ones
    categories = list(Category.objects.all())
    if not categories:
        Category.objects.create(name="Droit des Affaires")
        Category.objects.create(name="Droit Pénal")
        Category.objects.create(name="Droit Civil")
        categories = list(Category.objects.all())

    lawyers = [
        {"name": "Me. Mehdi EL MANSOURI", "desc": "Spécialiste en droit pénal, il intervient dans la défense des personnes physiques et morales devant les juridictions pénales.", "cat": "Droit Pénal"},
        {"name": "Me. Asmae BENKIRANE", "desc": "Experte en droit des affaires et en droit commercial, elle accompagne les entreprises dans leurs projets et contentieux.", "cat": "Droit des Affaires"},
        {"name": "Me. Youssef TAZI", "desc": "Intervient en matière de droit civil : contrats, responsabilités, dommages et intérêts et résolution des litiges.", "cat": "Droit Civil"},
        {"name": "Me. Kawtar EL HASSANI", "desc": "Spécialiste en droit de la famille, elle vous accompagne dans les procédures de divorce, garde d'enfants et successions.", "cat": "Droit Civil"},
        {"name": "Me. Rachid AMRANI", "desc": "Conseil et représentation en droit du travail et en relations sociales, aussi bien pour les salariés que pour les employeurs.", "cat": "Droit des Affaires"},
        {"name": "Me. Lina BOUSSAIDI", "desc": "Experte en droit immobilier, elle vous assiste dans vos transactions, baux et litiges immobiliers.", "cat": "Droit des Affaires"},
    ]

    existing_services = list(Service.objects.all())
    
    for i, lawyer_data in enumerate(lawyers):
        # Create category if it doesn't exist
        cat, _ = Category.objects.get_or_create(name=lawyer_data['cat'])
        
        if i < len(existing_services):
            service = existing_services[i]
            service.name = lawyer_data['name']
            service.description = lawyer_data['desc']
            service.category = cat
            service.save()
            print(f"Updated service {service.id} to {service.name}")
        else:
            service = Service.objects.create(
                name=lawyer_data['name'],
                description=lawyer_data['desc'],
                category=cat,
                price=random.randint(150, 400)
            )
            print(f"Created service {service.name}")

if __name__ == "__main__":
    run()
