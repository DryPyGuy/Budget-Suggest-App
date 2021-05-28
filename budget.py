def budget(monthly_income):
    max_mortgage = int(monthly_income) * .25
    savings_retirement = int(monthly_income) * .10
    food = int(monthly_income) * .15
    giving = int(monthly_income) * .10
    utilities = int(monthly_income) * .05
    transportation = int(monthly_income) * .10
    health = int(monthly_income) * .05
    insurance = int(monthly_income) * .10
    recreation = int(monthly_income) * .05
    misc = int(monthly_income) * .05
    print(f"Your maximum monthly mortgage or rent payment should not exceed ${max_mortgage}.")
    print(f"You should try to save ${savings_retirement} a month.")
    print(f"Try to keep your food budget around ${food} a month or ${food / 4} a week.")
    print(f"Giving is an important aspect of growing wealth. We reccomend that you give around ${giving} a month.")
    print(f"Try to keep your monthly utilities costs around ${utilities}.")
    print(f"Costs for transportation, gas and upkeep of your car should not exceed ${transportation} monthly")
    print(f"Health costs, such as perscriptions and vitamins should be kept at ${health} a month.")
    print(f"Insurances expeanses, like car and health should be capped at ${insurance}.")
    print(f"Fun money would be good kept at ${recreation}.")
    print(f"Misc expenses, things unseen but planned for, we should set aside ${misc} a month.")


monthly_income = input("Okay, what is your total monthly, after tax, take home pay? Inlcluding your spouses income. ")
budget(monthly_income)