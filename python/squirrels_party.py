"""When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of
 cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number 
 of cigars. Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) = False
cigar_party(50, False) = True
cigar_party(70, True) = True"""

def cigar_party(cnt,is_weekend):
  if is_weekend:
    	if cnt < 40:
      		return "false"
  	return "true"
  else:
    if cnt >= 40 and cnt <= 70:
      return "true"
    return "false"

# res = cigar_party(30,False)
# print(res)

def test_cigar_party():
	assert cigar_party(30, False) == "false"
	assert cigar_party(50, False) == "true"
	assert cigar_party(70, True) == "true"

test_cigar_party()
