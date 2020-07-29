import constants

players_copy = constants.PLAYERS[:]


def main():
    while True:
        def start_tool():
            welcome = ("Welcome to the Basketball Team Stats Tool")
            welcome_length = (len(welcome)+3)
            print("*" * welcome_length)
            print(welcome)
            print("*" * welcome_length)

        start_tool()

        def menu_choice2():
                print("\n Here is your choice of Teams:")
                print("1) Panthers")
                print("2) Bandits")
                print("3) Warriors\n")
                submenu = 1
                while submenu == 1:
                    try:
                        team_answer = int(input(
                            "Please enter 1 to see stats for Panthers, "
                            "2 to see stats for Bandits, "
                            "3 to see stats for Warriors:  "))
                        if team_answer not in range(1, 4):
                            print("Sorry, that number is not 1, 2, or 3.  "
                                  "Please try again.")
                            continue
                        if team_answer == 1:
                            print("\nTeam:"
                                  "Panthers Stats\n---------------------")
                            print("Total players: {}".format(total_panthers_players))
                            print("Total experienced: {}".format(total_exp_panthers))
                            print("Total inexperienced: {}".format(total_inexp_panthers))
                            print("Players on Team:\n  ")
                            print(', '.join(final_panthers_roster))
                            input("\nPress any key to continue...  ")
                            break
                        if team_answer == 2:
                            print("\nTeam: Bandits Stats\n---------------------")
                            print("Total players: {}".format(total_bandits_players))
                            print("Total experienced: {}".format(total_exp_bandits))
                            print("Total inexperienced: {}".format(total_inexp_bandits))
                            print("Players on Team:\n  ")
                            print(', '.join(final_bandits_roster))
                            input("\nPress any key to continue...  ")
                            break
                        if team_answer == 3:
                            print("\nTeam: Warriors Stats\n---------------------")
                            print("Total players: {}".format(total_warriors_players))
                            print("Total experienced: {}".format(total_exp_warriors))
                            print("Total inexperienced: {}".format(total_inexp_warriors))
                            print("Players on Team:\n  ")
                            print(', '.join(final_warriors_roster))
                            input("\nPress any key to continue...  ")
                            break

                    except ValueError:
                        print("Oh no!  That is not the number 1, 2, or 3.  Try again...")

        def menu_choice():
                user_name = input("\nWhat is your name?  ")
                print("\nHello, {}.  Please make a choice from menu below for team statistics".format(user_name))
                print("\n------MENU-----")
                print("\n  Here are your choices:")
                print("\n   1.  Display Team Statistics")
                print("   2.  Quit")
                while user_name is not None:
                    try:
                        menu_answer = int(input("\nPlease enter 1 for team stats, or 2 to quit:  "))
                        if menu_answer not in range(1, 3):
                            print("Sorry, that number is not 1 or 2.  Please try again.")
                            continue
                        if menu_answer == 1:
                            menu_choice2()
                        if menu_answer == 2:
                            print("\nThanks for playing, {}.  Have a nice day!\n".format(user_name))
                            exit()
                    except ValueError:
                        print("Oh no!  That is not the number 1 or 2.  Try again...")
                        continue

        menu_choice()


def clean_data(players_copy):
    for player in players_copy:
        if player['experience'] == "YES":
            player['experience'] = True
        else:
            player['experience'] = False
        player['height'] = player['height'].split()[0]
        player['guardians'] = player['guardians'].replace(" and ", ", ")


if __name__ == '__main__':
    clean_data(players_copy)

    panthers_experienced_players = []
    panthers_no_experience_players = []
    panthers_total_players = len(panthers_experienced_players) + len(panthers_no_experience_players)
    bandits_experienced_players = []
    bandits_no_experience_players = []
    bandits_total_players = len(bandits_experienced_players) + len(bandits_no_experience_players)
    warriors_experienced_players = []
    warriors_no_experience_players = []
    warriors_total_players = len(warriors_experienced_players) + len(warriors_no_experience_players)

    for player in players_copy:
        if panthers_total_players < 7:
            if len(panthers_experienced_players) < 3:
                if player['experience'] is True:
                    panthers_experienced_players.append(player['name'])
                    continue
            if len(panthers_no_experience_players) < 3:
                if player['experience'] is False:
                    panthers_no_experience_players.append(player['name'])
                    continue

        if bandits_total_players < 7:
            if len(bandits_experienced_players) < 3:
                if player['experience'] is True:
                    bandits_experienced_players.append(player['name'])
                    continue

            if len(bandits_no_experience_players) < 3:
                if player['experience'] is False:
                    bandits_no_experience_players.append(player['name'])
                    continue

        if warriors_total_players < 7:
            if len(warriors_experienced_players) < 3:
                if player['experience'] is True:
                    warriors_experienced_players.append(player['name'])
                    continue

            if len(warriors_no_experience_players) < 3:
                if player['experience'] is False:
                    warriors_no_experience_players.append(player['name'])
                    continue

    final_panthers_roster = panthers_experienced_players + panthers_no_experience_players
    final_bandits_roster = bandits_experienced_players + bandits_no_experience_players
    final_warriors_roster = warriors_experienced_players + warriors_no_experience_players

    # Roster counts
    total_panthers_players = len(final_panthers_roster)
    total_bandits_players = len(final_bandits_roster)
    total_warriors_players = len(final_warriors_roster)

    # Experience counts
    total_exp_panthers = len(panthers_experienced_players)
    total_exp_bandits = len(bandits_experienced_players)
    total_exp_warriors = len(warriors_experienced_players)

    # Inexperience counts
    total_inexp_panthers = len(panthers_no_experience_players)
    total_inexp_bandits = len(bandits_no_experience_players)
    total_inexp_warriors = len(warriors_no_experience_players)

    main()
