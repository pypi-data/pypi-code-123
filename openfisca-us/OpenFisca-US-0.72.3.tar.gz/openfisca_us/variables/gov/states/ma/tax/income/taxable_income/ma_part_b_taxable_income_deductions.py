from openfisca_us.model_api import *


class ma_part_b_taxable_income_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "MA Part B taxable income deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.mass.gov/info-details/mass-general-laws-c62-ss-3"

    def formula(tax_unit, period, parameters):
        tax = parameters(period).states.ma.tax.income
        # (B)(a)(3): Taxes for retirement programs.
        # NB: The law only mentions FICA and FRRA, but mass.gov includes SECA.
        # https://www.mass.gov/service-details/learn-about-business-and-professional-income
        person = tax_unit.members
        SS_MEDICARE_VARIABLES = [
            "employee_social_security_tax",
            "employee_medicare_tax",
            "self_employment_social_security_tax",
            "self_employment_medicare_tax",
        ]
        fica_person = add(person, period, SS_MEDICARE_VARIABLES)
        fica_head = min_(
            tax.deductions.public_retirement_contributions,
            fica_person * person("is_tax_unit_head", period),
        )
        fica_spouse = min_(
            tax.deductions.public_retirement_contributions,
            fica_person * person("is_tax_unit_spouse", period),
        )
        fica = tax_unit.sum(fica_head) + tax_unit.sum(fica_spouse)
        # (B)(a)(6): Interest and dividends deduction.
        interest_and_dividends = add(
            tax_unit, period, ["interest_income", "dividend_income"]
        )
        filing_status = tax_unit("filing_status", period)
        interest_and_dividends = min_(
            tax.exemptions.interest[filing_status],
            interest_and_dividends,
        )
        # (B)(a)(9): Rent deduction.
        rent = add(tax_unit, period, ["rent"])
        rent_deduction = tax.deductions.rent.share * rent
        rent_deduction = min_(
            rent_deduction,
            tax.deductions.rent.cap[filing_status],
        )
        # (B)(b): Exemptions.
        # (1A) and (2A): Personal exemption based on filing status.
        personal_exemptions = tax.exemptions.personal[filing_status]
        # (1B) and (2B): Blind exemptions.
        blind = person("is_blind", period)
        dependent = person("is_tax_unit_dependent", period)
        count_blind = tax_unit.sum(~dependent & blind)
        blind_exemption = tax.exemptions.blind * count_blind
        # (1C) and (2C): Aged exemptions.
        age = person("age", period)
        count_aged = tax_unit.sum(
            ~dependent & (age >= tax.exemptions.aged.age)
        )
        aged_exemption = tax.exemptions.aged.amount * count_aged
        # (3): Dependent exemptions.
        count_dependents = tax_unit("tax_unit_dependents", period)
        dependent_exemption = tax.exemptions.dependent * count_dependents
        # (4): Medical expense deduction for itemizers.
        itemizes = tax_unit("tax_unit_itemizes", period)
        federal_medical_expense_deduction = tax_unit(
            "medical_expense_deduction", period
        )
        medical_dental_exemption = itemizes * federal_medical_expense_deduction
        # Total deductions and exemptions.
        return (
            fica
            + interest_and_dividends
            + rent_deduction
            + personal_exemptions
            + dependent_exemption
            + aged_exemption
            + blind_exemption
            + medical_dental_exemption
        )
