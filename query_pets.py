#Import Statements
import sqlite3
import argparse

def main(args):
    '''Querying the Pets database'''

    con = sqlite3.connect('pets.db')

    with con:

        cur = con.cursor()
        choice = args.id
        while choice != '-1':
            #If the user id does not exist print an error message
            try:
                cur.execute("SELECT person_pet.pet_id, person_pet.person_id, person.first_name, person.last_name,person.age, pet.age, pet.name, pet.breed, pet.dead "
                                "FROM person_pet "
                                "LEFT JOIN person on person_pet.person_id = person.id "
                                "LEFT JOIN pet on person_pet.pet_id = pet.id "
                                "where person.id ="+choice)

                row = cur.fetchall()
                print(f"{row[0][2]} {row[0][3]}, is {row[0][4]} years old")
                for r in row:
                    if r[8] == 1:
                            #If the animal is dead print accordingly
                        print(f"{r[2]} {r[3]} owned {r[6]}, a {r[7]}, that was {r[5]} years old")
                    else:
                            #Else print as if the animal is alive
                        print(f"{r[2]} {r[3]} owns {r[6]}, a {r[7]}, that is {r[5]} years old")
            except:
                print('Error There is no Person with that ID')

            #Read in the users choice
            print("Enter the person ID")

            choice = input()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="Person ID, -1 to Exit", type=str, required=True)
    args = parser.parse_args()
    main(args)