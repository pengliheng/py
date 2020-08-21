# F_MT700_30 = 2
# F_MT700_31 = 3
# a = isIncluded(F_MT700_30, 'today')
# if (a%2==1):
#   print('odd')
# else:
#   print('even')
rule = {
  'R_INV_1': """
a=1
if isIncluded(F_MT700_36, 'invoice'):
  return not isIncluded(F_INV_1, 'Proforma Invoice') 
return true
  """
}