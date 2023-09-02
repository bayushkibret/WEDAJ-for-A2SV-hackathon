def calculate_financial_data(total_income, total_expenditures, simple_interest_earned):
  """This function calculates the financial data given the total income, total expenditures, and simple interest earned.

  Args:
    total_income: The total income.
    total_expenditures: The total expenditures.
    simple_interest_earned: The simple interest earned.

  Returns:
    The positive cash flow, the total savings, and the total return.
  """

  postive_cash_flow = total_income - total_expenditures
  total_savings = postive_cash_flow + simple_interest_earned
  total_return = total_savings / total_income * 100

  # Print the financial data.
  result = {'postive_cash_flow':postive_cash_flow, 'total_savings':total_savings, 'total_return':total_return}
  return result

