# domain/energy/services.py

from domain.energy.value_objects import EnergyQuantity


class EnergyDomainService:

    @staticmethod
    def calculate_total(records) -> EnergyQuantity:

        total = sum(
            r.quantity.value if hasattr(r.quantity, "value") else float(r.quantity)
            for r in records
        )

        # FIX: non creare mai EnergyQuantity(0) come base interna implicita
        return EnergyQuantity(total if total > 0 else 0.01)