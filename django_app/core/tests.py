from django.test import TestCase
from django.utils import timezone
from datetime import datetime, timezone as tz

from .models import User, Contract, RecurrentContract


class ContractsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            date_joined=timezone.now(), username="jho", name="Jho", first_name="Jho"
        )
        user2 = User.objects.create(
            date_joined=timezone.now(), username="Doe", name="Doe", first_name="Jhon"
        )

        contract = Contract.objects.create(
            start_date=datetime(2020, 1, 1, tzinfo=tz.utc), product_id=1, user=user
        )

        contract2 = Contract.objects.create(
            start_date=datetime(2020, 1, 1, tzinfo=tz.utc), product_id=2, user=user2
        )

        rec = RecurrentContract.objects.create(contract=contract2)

    def test_contract_retrieval(self):
        """Test the retrieval of contracts."""
        contract = Contract.objects.get(user__username="jho")
        self.assertEqual(contract.user.username, "jho")
        self.assertEqual(contract.product_id, 1)

    def test_query(self):
        """
        Using Django's ORM, retrieve contracts with a start_date in the year 2020
        that are not in the recurrent_contracts table and have a "name"
        field containing the text "Jho".
        """
        contracts = Contract.objects.filter(
            start_date__year=2020, user__name__icontains="Jho"
        ).exclude(
            id__in=RecurrentContract.objects.values_list("contract_id", flat=True)
        )
        self.assertEqual(contracts.count(), 1)
