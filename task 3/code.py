def calculate_tax(gross_salary):
    """Applies progressive tax deduction slabs based on gross salary."""
    tax = 0.0
    if gross_salary <= 3000:
        tax = 0.0  # 0% tax for lower bracket
    elif gross_salary <= 6000:
        tax = (gross_salary - 3000) * 0.10  # 10% on amount above 3000
    else:
        tax = (3000 * 0.10) + ((gross_salary - 6000) * 0.20)  # 10% on middle tier + 20% on remainder
    return round(tax, 2)


def generate_payslip(name, basic_pay, allowances, ot_hours, ot_rate, incentives):
    """Calculates payroll components and prints a formatted salary statement."""
    # Earnings calculations
    overtime_pay = ot_hours * ot_rate
    gross_salary = basic_pay + allowances + overtime_pay + incentives

    # Deductions calculations
    provident_fund = basic_pay * 0.08  # 8% of basic pay
    income_tax = calculate_tax(gross_salary)
    health_insurance = 120.00  # Fixed health insurance deduction
    
    total_deductions = provident_fund + income_tax + health_insurance
    net_salary = gross_salary - total_deductions

    # Formatted Salary Statement Output
    print("=" * 45)
    print(f"{'EMPLOYEE SALARY STATEMENT':^45}")
    print("=" * 45)
    print(f"Employee Name : {name}")
    print("-" * 45)
    print(f"{'EARNINGS':<30} | {'AMOUNT ($)':<10}")
    print("-" * 45)
    print(f"{'Basic Pay':<30} | ${basic_pay:>9.2f}")
    print(f"{'Allowances':<30} | ${allowances:>9.2f}")
    print(f"{'Overtime Pay (' + str(ot_hours) + ' hrs)':<30} | ${overtime_pay:>9.2f}")
    print(f"{'Performance Incentives':<30} | ${incentives:>9.2f}")
    print(f"{'Gross Salary':<30} | ${gross_salary:>9.2f}")
    print("-" * 45)
    print(f"{'DEDUCTIONS':<30} | {'AMOUNT ($)':<10}")
    print("-" * 45)
    print(f"{'Provident Fund (8% Basic)':<30} | ${provident_fund:>9.2f}")
    print(f"{'Income Tax (Progressive)':<30} | ${income_tax:>9.2f}")
    print(f"{'Health Insurance':<30} | ${health_insurance:>9.2f}")
    print(f"{'Total Deductions':<30} | ${total_deductions:>9.2f}")
    print("=" * 45)
    print(f"{'NET SALARY':<30} | ${net_salary:>9.2f}")
    print("=" * 45)


# --- Sample Execution ---
if __name__ == "__main__":
    # Sample Input Data
    emp_name = "Alex Johnson"
    basic = 4500.00
    allowances = 850.00
    overtime_hours = 12
    overtime_rate = 25.00
    incentive_amount = 400.00

    generate_payslip(emp_name, basic, allowances, overtime_hours, overtime_rate, incentive_amount)
