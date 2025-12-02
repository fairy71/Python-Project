from notes import add_note, list_notes, delete_note
from utils import print_note

def menu():
    print("\n=== NoteManager ===")
    print("1. Add note")
    print("2. List notes")
    print("3. Delete note")
    print("4. Exit")
    return input("Choose: ")

while True:
    choice = menu()

    if choice == "1":
        title = input("Title: ")
        content = input("Content: ")
        note = add_note(title, content)
        print("Note added!")
        print_note(note)

    elif choice == "2":
        notes = list_notes()
        if not notes:
            print("No notes yet.")
        for n in notes:
            print_note(n)

    elif choice == "3":
        note_id = int(input("Enter note ID to delete: "))
        delete_note(note_id)
        print("Deleted.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid input.")
