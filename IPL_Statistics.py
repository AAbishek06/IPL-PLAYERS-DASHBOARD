import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("ipl_players.csv")
df["StrikeRate"]=(df["Runs"]/df["Balls"])*100
while True:
    print("\n===== IPL DASHBOARD =====")
    print("1. Top Run Scorers")
    print("2. Highest Strike Rate")
    print("3. Team-wise Runs")
    print("4. Overall Statistics")
    print("5. Exit")
    choice=input("Enter Number: ")
    if choice=="1":
        print("\n===== TOP RUN SCORERS =====")
        top=df.sort_values(by="Runs",ascending=False)
        print(top[["Player","Runs"]])
        plt.figure(figsize=(8,5))
        plt.bar(top["Player"],top["Runs"],color="green")
        plt.title("Top Run Scorers")
        plt.xticks(rotation=45)
        plt.show()
    elif choice=="2":
        print("\n===== STRIKE RATE =====")
        sr=df.sort_values(by="StrikeRate",ascending=False)
        print(sr[["Player","StrikeRate"]])
        plt.figure(figsize=(8,5))
        plt.bar(sr["Player"],sr["StrikeRate"],color="orange")
        plt.title("Strike Rate Comparison")
        plt.xticks(rotation=45)
        plt.show()
    elif choice == "3":
        print("\n===== TEAM WISE RUNS =====")
        team=df.groupby("Team")["Runs"].sum()
        print(team)
        team.plot(kind="pie",autopct="%1.1f%%")
        plt.title("Team Contribution")
        plt.show()
    elif choice=="4":
        print("\n===== STATISTICS =====")
        print("Average Runs:",round(np.mean(df["Runs"]),2))
        print("Highest Runs:",np.max(df["Runs"]))
        print("Lowest Runs:",np.min(df["Runs"]))
        print("Average Strike Rate:",round(np.mean(df["StrikeRate"]),2))
    elif choice=="5":
        print("Thank You")
        break
    else:
        print("Wrong Number! Try Again")
