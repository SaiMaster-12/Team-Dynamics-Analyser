import time
import webbrowser
import matplotlib.pyplot as plt

class TeamSelector:
    def __init__(self, project_choice):
        self.project_choice = project_choice
        self.cost = [0, 0, 0, 0, 0]
        self.Team = ["Team 1 with 2y exp", "Team 2 with 4y exp", "Team 3 with 1y exp", "Team 4 with 4y exp"]

    def choose_team(self):
        while True:
            print("   Available teams are:")
            for i in range(len(self.Team)):
                print(f"   {i + 1}. {self.Team[i]}")

            print("   5. Exit\n   (Think before you select the team)")
            try:
                team_choice = int(input("   Select Team (Enter only numbers): "))
                if 1 <= team_choice <= 4:
                    self.cost[team_choice] = [400, 600, 200, 800][team_choice - 1]
                    print(f"   Selected team is {self.Team[team_choice - 1]} and cost is {self.cost[team_choice]}")
                    break
                elif team_choice == 5:
                    return
                else:
                    print("   Invalid choice. Try again...")
            except ValueError:
                print("   Invalid input. Please enter a number.")

    def update_team(self):
        try:
            team_index = int(input("   Enter the team number you want to update: "))
            if 1 <= team_index <= 4:
                self.choose_team()
                self.display_payment_info()
            else:
                print("   Invalid team number. Try again...")
        except ValueError:
            print("   Invalid input. Please enter a number.")

    def delete_team(self):
        print("\n   Your selected team is deleted Successfully.\n   You can choose team again...")
        self.choose_team()
        self.display_payment_info()

    def display_payment_info(self):
        total_cost = sum(self.cost)
        gst = 80.46

        if total_cost == 0:
            print("   Thank you...Visit again.")
        else:
            print(f"   Cost is: {total_cost}")
            print(f"   GST is: {gst}")
            print(f"   Total Amount = {total_cost + gst}\n")

            # Payment
            print("   Directing to Browser...Please wait 10 sec")
            for i in range(11):
                time.sleep(1)
                print(f"   Seconds remaining: {10 - i}")

            pay_link = 'https://paypal.me/saimaster8660'
            webbrowser.open(pay_link)


# Graph
x = [1, 2, 3, 4]
y = [2, 4, 1, 4]

plt.plot(x, y, color='#31e060', ls='-.', marker='*')
plt.xlabel("Teams")
plt.ylabel("Experience in y")
plt.title("Team Dynamics Analyzer.")

for i in range(len(x)):
    plt.text(x[i], y[i], f"({x[i]}, {y[i]})")

plt.show()

# Main
print("---------------------------------------")
print("   Welcome to Master's organisation    ")
print("---------------------------------------")
print("   The projects available are:\n\n"
      "   1. Password checking\n   2. Lift Scenario\n   3. Chatbox\n   4. ATM\n   5. Exit")

project_choice = input("   Enter your choice: ")
print("\n")

if project_choice.isdigit() and 1 <= int(project_choice) <= 5:
    team_selector = TeamSelector(project_choice)
    team_selector.choose_team()

    # update and delete options
    print("   Options:\n   1. Update Team\n   2. Delete Team\n   3. Display Payment Info\n   4. Exit")
    try:
        option = int(input("   Select Option (Enter only numbers): "))
        if option == 1:
            team_selector.update_team()
        elif option == 2:
            team_selector.delete_team()
        elif option == 3:
            team_selector.display_payment_info()
        elif option == 4:
            print("   Exiting...")
        else:
            print("   Invalid option. Exiting...")
    except ValueError:
        print("   Invalid input. Please enter a number.")

else:
    print("   Invalid choice. Exiting...")
