"""
This module calculates the total monthly cell phone bill for a user.

Subscription information:

- Airtime plan: 50 minutes
- Text messages: 50 messages

The cost of the subscription is $15.00

After the subscription is exceeded, the following rates apply:

- Additional minutes: $0.25 per minute
- Additional messages: $0.15 per message

-Additional $0.44 will be added to the bill to cover 911 fees.

The bill will automatically include a 5% sales tax applied to the total cost of the bill.

Note: In the implementation, the user will be charged for each 911 call made. This is not a realistic scenario!
This is just to follow the instructions of the assignment.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

AIRTIME_PLAN: int = 50  # minutes
TEXT_MESSAGES: int = 50  # messages
SUBSCRIPTION_COST: float = 15.00  # monthly subscription cost
AIRTIME_RATE: float = 0.25  # per minute
MESSAGE_RATE: float = 0.15  # per message
ADDITIONAL_911_FEES: float = 0.44  # 911 fees
SALES_TAX: float = 0.05  # 5%


def get_usage_info(usage_type: str) -> int:
    """
    Get the total usage for a specific type of usage.

    Args:
        usage_type: The type of usage to get the total for.

    Returns:
        The total usage for the specified type.
    """
    while True:
        total_usage_input: str = input(
            f"Please enter your total {usage_type} usage for this month: "
        )

        if not total_usage_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        print("--------------------")
        return int(total_usage_input)


print(
    "Hi There! 📱👋 Welcome to the Cell Phone Bill Calculator! Let's calculate your monthly cell phone bill."
)

total_minutes = get_usage_info("minutes")
total_messages = get_usage_info("messages")
total_911_minutes = get_usage_info("911 minutes")

exceeded_min_usage: int | None = None
total_exceeded_min_cost: float | None = None
if total_minutes > AIRTIME_PLAN:
    exceeded_min_usage = total_minutes - AIRTIME_PLAN
    total_exceeded_min_cost = exceeded_min_usage * AIRTIME_RATE

exceeded_messages_usage: int | None = None
total_exceeded_messages_cost: float | None = None
if total_messages > TEXT_MESSAGES:
    exceeded_messages_usage = total_messages - TEXT_MESSAGES
    total_exceeded_messages_cost = exceeded_messages_usage * MESSAGE_RATE

total_911_fees = total_911_minutes * ADDITIONAL_911_FEES

total_bill: float = SUBSCRIPTION_COST  # initial bill

if total_exceeded_min_cost:
    total_bill += total_exceeded_min_cost

if total_exceeded_messages_cost:
    total_bill += total_exceeded_messages_cost

total_bill += total_911_fees

total_bill_with_tax = total_bill + (total_bill * SALES_TAX)

print("============================================================")
print("                    📱 Monthly Cell Phone Bill 📱                    ")
print("============================================================")
print(f"📅 Subscription cost: ${SUBSCRIPTION_COST:.2f}")
if total_exceeded_min_cost:
    print(f"📞  Exceeded minutes: {exceeded_min_usage} minutes")
    print(f"📞  Exceeded minutes cost: ${total_exceeded_min_cost:.2f}")
if total_exceeded_messages_cost:
    print(f"✉️  Exceeded messages: {exceeded_messages_usage} messages")
    print(f"✉️  Exceeded messages cost: ${total_exceeded_messages_cost:.2f}")
print("--------------------")
if total_911_minutes > 0:
    print(f"🚨 Total 911 minutes: {total_911_minutes}")
    print(f"🚑 911 fees: ${total_911_fees:.2f}")
else:
    print("No 911 calls made this month.")
print("--------------------")
print(f"💵 Total bill before tax: ${total_bill:.2f}")
print(f"💲 Sales tax: ${total_bill * SALES_TAX:.2f} (5%)")
print(f"💰 Your total bill for this month: ${total_bill_with_tax:.2f}")
print("============================================================")
print(
    "                    Thank you for using the Cell Phone Bill Calculator! 📱💸                    "
)
print("============================================================")
