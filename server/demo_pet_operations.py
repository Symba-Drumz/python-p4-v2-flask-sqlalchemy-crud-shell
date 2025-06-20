from app import app
from models import db, Pet
from sqlalchemy import func

def main():
    with app.app_context():
        # Add pet1
        pet1 = Pet(name="Fido", species="Dog")
        db.session.add(pet1)
        db.session.commit()
        print(f"Added pet1: {pet1} with id {pet1.id}")

        # Add pet2
        pet2 = Pet(name="Whiskers", species="Cat")
        db.session.add(pet2)
        db.session.commit()
        print(f"Added pet2: {pet2} with id {pet2.id}")

        # Query all pets
        all_pets = Pet.query.all()
        print(f"All pets: {all_pets}")

        # Filter pets by species 'Cat'
        cats = Pet.query.filter(Pet.species == 'Cat').all()
        print(f"Cats: {cats}")

        # Filter pets by name starting with 'F'
        f_pets = Pet.query.filter(Pet.name.startswith('F')).all()
        print(f"Pets with names starting with 'F': {f_pets}")

        # Filter by species using filter_by
        cats_filter_by = Pet.query.filter_by(species='Cat').all()
        print(f"Cats (filter_by): {cats_filter_by}")

        # Filter by id using filter_by
        pet_id_1 = Pet.query.filter_by(id=1).first()
        print(f"Pet with id=1 (filter_by): {pet_id_1}")

        # Get pet by primary key using db.session.get
        pet_get_1 = db.session.get(Pet, 1)
        print(f"Pet with id=1 (db.session.get): {pet_get_1}")

        pet_get_20 = db.session.get(Pet, 20)
        print(f"Pet with id=20 (db.session.get): {pet_get_20}")

        # Order by species ascending
        ordered_pets = Pet.query.order_by(Pet.species).all()
        print(f"Pets ordered by species: {ordered_pets}")

        # Count pets using func.count
        pet_count = db.session.query(func.count(Pet.id)).first()
        print(f"Number of pets: {pet_count[0]}")

        # Update pet1's name
        pet1.name = "Fido the mighty"
        db.session.commit()
        print(f"Updated pet1: {pet1}")

        # Delete pet1
        db.session.delete(pet1)
        db.session.commit()
        remaining_pets = Pet.query.all()
        print(f"Remaining pets after deleting pet1: {remaining_pets}")

        # Delete all pets
        deleted_count = Pet.query.delete()
        db.session.commit()
        print(f"Deleted {deleted_count} pets")

        # Confirm no pets remain
        no_pets = Pet.query.all()
        print(f"Pets after deleting all: {no_pets}")

if __name__ == '__main__':
    main()
