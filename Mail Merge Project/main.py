import os

starting_letter_path = "./Input/Letters/starting_letter.txt"

invited_names_path = "./Input/Names/invited_names.txt"

save_path = "./Output/ReadyToSend"

with open(starting_letter_path, "r") as starting_letter_file, open(invited_names_path, "r") as invited_names_file:

    starting_letter_content = starting_letter_file.read()
    invited_names = invited_names_file.readlines()

    for name in invited_names:
        name = name.replace('\n', '').strip()
        file_name = f"letter_for_{name}.txt"
        invitation = os.path.join(save_path, file_name)

        with open (invitation, "w") as invitation_file:
            invitation_file.write(starting_letter_content.replace("[name]", name))