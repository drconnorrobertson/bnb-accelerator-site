"""Hypothetical buyer examples prepared before list-first linking changes.

These are educational inputs, not current market averages, financing quotes,
BNB service prices or client outcomes. No renderer uses this module yet.
"""
from decimal import Decimal, ROUND_CEILING


BEACH_ENTRY = {
    'purchase_price': 800000,
    'down_payment_percent': 25,
    'closing_costs_and_prepaids': 28000,
    'immediate_repairs': 18000,
    'furnishing_allowance': 42000,
    'launch': 5000,
    'operating_reserve': 30000,
    'deductible_liquidity': 12000,
    'earnest_money_credited_at_closing': 20000,
}
FURNISHING = {
    'four_bedrooms_at_4000_each': 16000,
    'living_and_dining': 6500,
    'outdoor_furniture': 3500,
    'kitchen_and_linen_stock': 3500,
    'technology_and_safety': 2000,
    'freight_and_installation': 4500,
}
FOURPLEX = {
    'units': 4, 'calendar_nights_per_unit': 365,
    'unavailable_nights_per_unit': 10, 'adr': 150,
    'variable_cost_per_paid_unit_night': 30, 'revenue_linked_fee_percent': 20,
    'debt_service': 72000, 'tax_and_insurance': 14000,
    'fixed_utilities_and_common_service': 6000, 'replacement_reserve': 6000,
}
CHANDLER_ENTRY = {
    'down_payment': 162500, 'closing': 22500, 'repairs': 12500,
    'furnishing': 35000, 'launch': 4500, 'reserve': 28000,
}
OCCUPANCY_QUARTERS = [
    # calendar nights, unavailable nights, paid nights, realized lodging ADR
    (90, 5, 34, 150), (91, 5, 43, 175),
    (92, 7, 68, 240), (92, 2, 45, 160),
]


def fourplex_threshold(*, adr=150, unavailable_extra=0, leased_units=0, lease_contribution=0):
    """Annual unit-night threshold; equal unit contribution is explicit here."""
    d = FOURPLEX
    fixed = sum(d[k] for k in ('debt_service', 'tax_and_insurance',
                              'fixed_utilities_and_common_service', 'replacement_reserve'))
    available = (d['units'] - leased_units) * (d['calendar_nights_per_unit'] - d['unavailable_nights_per_unit']) - unavailable_extra
    contribution = Decimal(str(adr)) * (1 - Decimal(d['revenue_linked_fee_percent']) / 100) - d['variable_cost_per_paid_unit_night']
    if contribution <= 0 or available <= 0:
        raise ValueError('No feasible paid-night threshold with these inputs')
    required = int((Decimal(fixed - lease_contribution) / contribution).to_integral_value(rounding=ROUND_CEILING))
    return {'fixed_obligations': fixed, 'available_unit_nights': available,
            'contribution_per_paid_unit_night': contribution, 'required_paid_unit_nights': required,
            'occupancy_percent': Decimal(required) / available * 100,
            'feasible_within_inventory': required <= available}


def validate_examples():
    down = BEACH_ENTRY['purchase_price'] * BEACH_ENTRY['down_payment_percent'] // 100
    beach_total = down + sum(BEACH_ENTRY[k] for k in (
        'closing_costs_and_prepaids', 'immediate_repairs', 'furnishing_allowance',
        'launch', 'operating_reserve', 'deductible_liquidity'))
    closing_wire = down + BEACH_ENTRY['closing_costs_and_prepaids'] - BEACH_ENTRY['earnest_money_credited_at_closing']
    assert (down, beach_total, closing_wire) == (200000, 335000, 208000)
    assert sum(FURNISHING.values()) == 36000
    assert Decimal(sum(FURNISHING.values())) * Decimal('1.10') == 39600
    base, lower_rate, unavailable, mixed = (
        fourplex_threshold(), fourplex_threshold(adr=135),
        fourplex_threshold(unavailable_extra=90),
        fourplex_threshold(leased_units=1, lease_contribution=Decimal(1800 * 12) * Decimal('.8')))
    assert (base['available_unit_nights'], base['required_paid_unit_nights']) == (1420, 1089)
    assert lower_rate['required_paid_unit_nights'] == 1257
    assert unavailable['available_unit_nights'] == 1330
    assert (mixed['available_unit_nights'], mixed['required_paid_unit_nights']) == (1065, 897)
    assert sum(CHANDLER_ENTRY.values()) == 265000
    weak_month_cash = Decimal(12 * 160) * Decimal('.82') - 12 * 22 - 4400
    assert weak_month_cash == Decimal('-3089.60')
    revpar_a, revpar_b = Decimal(18 * 200) / 30, Decimal(24 * 160) / 30
    contribution_a = Decimal(18 * 200) * Decimal('.8') - 18 * 25
    contribution_b = Decimal(24 * 160) * Decimal('.8') - 24 * 40
    assert (revpar_a, revpar_b, contribution_a, contribution_b) == (120, 128, 2430, 2112)
    calendar = sum(q[0] for q in OCCUPANCY_QUARTERS)
    available = sum(q[0] - q[1] for q in OCCUPANCY_QUARTERS)
    paid = sum(q[2] for q in OCCUPANCY_QUARTERS)
    revenue = sum(q[2] * q[3] for q in OCCUPANCY_QUARTERS)
    assert (calendar, available, paid, revenue) == (365, 346, 190, 36145)
    assert 200000 - 165000 - 25000 == 10000
    return {'beach_total': beach_total, 'furnishing_total_with_contingency': 39600,
            'fourplex': [str(x['occupancy_percent'].quantize(Decimal('.1'))) for x in (base, lower_rate, unavailable, mixed)],
            'chandler_cash': 265000, 'hypothetical_weak_month_cash': str(weak_month_cash),
            'annual_lodging_revenue': revenue, 'available_occupancy_percent': str((Decimal(paid) / available * 100).quantize(Decimal('.1')))}


if __name__ == '__main__':
    print(validate_examples())
