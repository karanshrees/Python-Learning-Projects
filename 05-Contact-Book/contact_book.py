contacts = {}  # name_key -> {'display': display_name, 'numbers': [formatted_numbers], 'norms': set(normalized_nums)}
phone_index = {}  # phone_norm -> set(name_keys)
import sys


def normalize_name(name: str) -> str:
    return " ".join(name.strip().split()).lower()


def normalize_phone(phone: str) -> str:
    s = "".join(ch for ch in phone if ch.isdigit() or ch == "+")
    if s.startswith("+"):
        return s
    return s.lstrip("0") or s  # simple normalization: strip leading zeros if any


def _add_number_to_contact_key(name_key: str, display_name: str, phone_number: str) -> bool:
    pk = normalize_phone(phone_number)
    # already on this contact?
    if name_key in contacts and pk in contacts[name_key]['norms']:
        print(f"Contact '{contacts[name_key]['display']}' already has the number {phone_number}.")
        return False
    # number exists under other contacts
    owners = phone_index.get(pk, set()) - ({name_key} if name_key in contacts else set())
    if owners:
        owner_names = [contacts[o]['display'] for o in owners]
        print(f"This number already exists under: {', '.join(owner_names)}")
        resp = input("Add this number to the current contact as well? (y/n): ").strip().lower()
        if resp != 'y':
            print("Skipped adding number.")
            return False
    # ensure contact entry
    if name_key not in contacts:
        contacts[name_key] = {'display': display_name.strip(), 'numbers': [], 'norms': set()}
    # add number
    contacts[name_key]['numbers'].append(phone_number)
    contacts[name_key]['norms'].add(pk)
    phone_index.setdefault(pk, set()).add(name_key)
    print(f"Number {phone_number} added to {contacts[name_key]['display']}.")
    return True


def add_contact(name: str, phone_number: str):
    name_key = normalize_name(name)
    phone_key = normalize_phone(phone_number)

    # If exact name exists
    if name_key in contacts:
        if phone_key in contacts[name_key]['norms']:
            print(f"Contact '{contacts[name_key]['display']}' already has the number {phone_number}.")
            return
        # add provided number then offer to add more
        _add_number_to_contact_key(name_key, contacts[name_key]['display'], phone_number)
        while True:
            resp = input("Add another number to this contact? (y/n): ").strip().lower()
            if resp == 'y':
                new_num = input("Enter phone number: ").strip()
                _add_number_to_contact_key(name_key, contacts[name_key]['display'], new_num)
            else:
                break
        return

    # Name not found - check if phone exists elsewhere
    owners = phone_index.get(phone_key, set())
    if owners:
        owner_names = [contacts[k]['display'] for k in owners]
        print(f"This number already exists under: {', '.join(owner_names)}")
        print("Options:")
        print("1. Add a new contact with this number as well")
        print("2. Move this number from existing contact to the new name")
        print("3. Cancel")
        opt = input("Choose (1/2/3): ").strip()
        if opt == '2':
            # move: remove from all owners and assign to new
            for ok in list(owners):
                idxs = [i for i, n in enumerate(contacts[ok]['numbers']) if normalize_phone(n) == phone_key]
                for i in reversed(idxs):
                    del contacts[ok]['numbers'][i]
                contacts[ok]['norms'].discard(phone_key)
                if not contacts[ok]['numbers']:
                    # remove empty contact
                    del contacts[ok]
            phone_index[phone_key] = {name_key}
            contacts[name_key] = {'display': name.strip(), 'numbers': [phone_number], 'norms': {phone_key}}
            print(f"Moved number to new contact '{name.strip()}'.")
            # offer to add more numbers interactively
            while True:
                resp = input("Add another number to this new contact? (y/n): ").strip().lower()
                if resp == 'y':
                    new_num = input("Enter phone number: ").strip()
                    _add_number_to_contact_key(name_key, name, new_num)
                else:
                    break
            return
        elif opt == '1':
            # add new contact keeping number shared
            contacts[name_key] = {'display': name.strip(), 'numbers': [phone_number], 'norms': {phone_key}}
            phone_index.setdefault(phone_key, set()).add(name_key)
            print(f"Contact '{name.strip()}' added with the number.")
            # offer to add more numbers interactively
            while True:
                resp = input("Add another number to this new contact? (y/n): ").strip().lower()
                if resp == 'y':
                    new_num = input("Enter phone number: ").strip()
                    _add_number_to_contact_key(name_key, name, new_num)
                else:
                    break
            return
        else:
            print("Cancelled.")
            return

    # fresh new contact
    contacts[name_key] = {'display': name.strip(), 'numbers': [phone_number], 'norms': {phone_key}}
    phone_index.setdefault(phone_key, set()).add(name_key)
    print(f"Contact '{name.strip()}' added successfully.")
    # prompt to add more numbers now (fast flow)
    while True:
        resp = input("Add another number to this contact? (y/n): ").strip().lower()
        if resp == 'y':
            new_num = input("Enter phone number: ").strip()
            _add_number_to_contact_key(name_key, name, new_num)
        else:
            break


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("Contact List:")
    for k in sorted(contacts, key=lambda x: contacts[x]['display'].lower()):
        nums = " | ".join(contacts[k]['numbers']) if contacts[k]['numbers'] else "(no numbers)"
        print(f"{contacts[k]['display']}: {nums}")


def find_matching_names(query: str):
    q = normalize_name(query)
    matches = [k for k in contacts if q in k]
    return matches


def delete_contact_or_number():
    query = input("Enter contact name (or part of it) to delete contact/number: ").strip()
    matches = find_matching_names(query)
    if not matches:
        print("No matching contacts found.")
        return
    if len(matches) > 1:
        print("Multiple matches found:")
        for i, k in enumerate(matches, 1):
            print(f"{i}. {contacts[k]['display']} ({len(contacts[k]['numbers'])} numbers)")
        sel = input("Choose contact number to manage (index): ").strip()
        if not sel.isdigit() or not (1 <= int(sel) <= len(matches)):
            print("Invalid selection.")
            return
        sel_key = matches[int(sel) - 1]
    else:
        sel_key = matches[0]

    print(f"Selected: {contacts[sel_key]['display']}")
    print("1. Delete entire contact")
    print("2. Delete a specific number")
    opt = input("Choose (1/2): ").strip()
    if opt == '1':
        # remove from phone_index
        for num in contacts[sel_key]['numbers']:
            phone_index.get(normalize_phone(num), set()).discard(sel_key)
            if phone_index.get(normalize_phone(num)) == set():
                phone_index.pop(normalize_phone(num), None)
        del contacts[sel_key]
        print("Contact deleted.")
    elif opt == '2':
        nums = contacts[sel_key]['numbers']
        for i, n in enumerate(nums, 1):
            print(f"{i}. {n}")
        seln = input("Choose number index to delete: ").strip()
        if not seln.isdigit() or not (1 <= int(seln) <= len(nums)):
            print("Invalid selection.")
            return
        idx = int(seln) - 1
        num = nums.pop(idx)
        nk = normalize_phone(num)
        phone_index.get(nk, set()).discard(sel_key)
        if phone_index.get(nk) == set():
            phone_index.pop(nk, None)
        contacts[sel_key]['norms'].discard(nk)
        if not contacts[sel_key]['numbers']:
            del contacts[sel_key]
            print("Last number removed; contact deleted.")
        else:
            print("Number deleted.")
    else:
        print("Invalid option.")


def search_contacts(query: str):
    q = query.strip()
    if not q:
        print("Empty query.")
        return

    # If query contains any digit, treat as phone search (exact or partial)
    if any(ch.isdigit() for ch in q):
        q_digits = "".join(ch for ch in q if ch.isdigit() or ch == "+")
        norm_q = normalize_phone(q_digits)
        results = []
        # exact normalized lookup
        owners = phone_index.get(norm_q, set()) if norm_q else set()
        if owners:
            for k in owners:
                v = contacts[k]
                results.append((v['display'], v['numbers']))
        else:
            # partial match: check normalized stored numbers for substring match
            for k, v in contacts.items():
                for num in v['numbers']:
                    if norm_q and norm_q in normalize_phone(num):
                        results.append((v['display'], v['numbers']))
                        break
        if not results:
            print("No matching contacts found.")
            return
        for name, nums in results:
            display_nums = " | ".join(nums) if nums else "(no numbers)"
            print(f"{name}: {display_nums}")
        return

    # Otherwise do name-based search (case-insensitive, partial)
    qn = normalize_name(q)
    results = []
    for k, v in contacts.items():
        if qn in k:
            results.append((k, v['display'], v['numbers']))
    if not results:
        print("No matching contacts found.")
        return
    # If exact name match, show that contact details directly
    exact_key = None
    for k, disp, nums in results:
        if k == qn:
            exact_key = k
            break
    if exact_key:
        v = contacts[exact_key]
        display_nums = " | ".join(v['numbers']) if v['numbers'] else "(no numbers)"
        print(f"{v['display']}: {display_nums}")
        return
    # otherwise list matches
    for _, name, nums in results:
        display_nums = " | ".join(nums) if nums else "(no numbers)"
        print(f"{name}: {display_nums}")


def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact / Delete Number")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            name = input("Enter contact name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            add_contact(name, phone_number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact_or_number()
        elif choice == '4':
            name = input("Enter contact name (or part of it) or phone number to search: ").strip()
            search_contacts(name)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt. Exiting.")
        sys.exit(0)
