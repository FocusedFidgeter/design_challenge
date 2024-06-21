# bank.py
from dataclasses import dataclass
from decimal import Decimal

from stripe_service import PaymentService


@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: str  # Can be 'savings' or 'checking'


class BankService:
    def deposit(
        self, amount: Decimal, account: Account, payment_service: PaymentService
    ) -> None:
        print(
            f"Depositing {amount} into {account.account_type.capitalize()} Account {account.account_number}."
        )
        payment_service.process_payment(amount)
        account.balance += amount

    def withdraw(
        self, amount: Decimal, account: Account, payment_service: PaymentService
    ) -> None:
        print(
            f"Withdrawing {amount} from {account.account_type.capitalize()} Account {account.account_number}."
        )
        payment_service.process_payout(amount)
        account.balance -= amount
