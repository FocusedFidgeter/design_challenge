# main.py
from decimal import Decimal

from bank import Account, BankService
from stripe_service import StripePaymentService


def main() -> None:
    savings_account = Account("SA001", Decimal("1000"), "savings")
    checking_account = Account("CA001", Decimal("500"), "checking")

    bank_service = BankService()
    payment_service = StripePaymentService()
    payment_service.set_api_key("sk_test_1234567890")

    bank_service.deposit(Decimal("200"), savings_account, payment_service)
    bank_service.deposit(Decimal("300"), checking_account, payment_service)

    bank_service.withdraw(Decimal("100"), savings_account, payment_service)
    bank_service.withdraw(Decimal("200"), checking_account, payment_service)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
