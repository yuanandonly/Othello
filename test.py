import sys
def unsafe_x(player):
	#returns number of unsafe x pieces
	count = 0
	if (1 << 9) & player and not (1 << 0) & player: count += 1
	if (1 << 14) & player and not (1 << 7) & player: count += 1
	if (1 << 49) & player and not (1 << 56) & player: count += 1
	if (1 << 54) & player and not (1 << 63) & player: count += 1
	return count 

def unsafe_xx(player):
	#returns number of unsafe x pieces
	count = 0
	if (1 << 9) & player & (0 << 0): count += 1
	if (1 << 14) & player & (0 << 7): count += 1
	if (1 << 49) & player & (0 << 56): count += 1
	if (1 << 54) & player & (0 << 63): count += 1
	return count 
var = 0xC242000000000000
print(unsafe_x(var), unsafe_xx(var))