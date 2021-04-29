names=["たんじろう","ぎゆう","ねずこ","むざん"]
# names = ["たんじろう","ねずこ","むざん"]

def test(findname):
  found = False

  for name in names:
    if name == findname:
      found = True
      break
    
  if found:
    print(findname + 'は含まれます')
  else:
    print(findname + 'は含まれません')


test("ぎゆう")