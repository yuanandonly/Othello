import time
top =	  0x00000000000000FF
left =	  0x0101010101010101
right =   0x8080808080808080
bottom =  0xFF00000000000000
topr = top | right
topl = top | left
botr = bottom | right
botl = bottom | left
border = top | right | left | bottom

def h_frontiers(player, opp):
	board = player | opp
	notboard = ~ board
	shift = board & (notboard >> 8|notboard << 8|(notboard & ~left) << 1|(notboard & ~right) >> 1|(notboard & ~botr) >> 9|(notboard & ~botl) >> 7|(notboard & ~topl) << 9|(notboard & ~topr) << 7)
	return bin(shift&opp).count('1') - bin(shift&player).count('1')


def h_stable(player, opp):
	#returns player stable pieces - opp stable pieces
	return 1.4*bin(stable_pieces(player)).count('1') - bin(stable_pieces(opp)).count('1') 

def h_stablee(player, opp):
	#returns player stable pieces - opp stable pieces
	return 1.4*bin(stable_piecess(player)).count('1') - bin(stable_piecess(opp)).count('1') 

def stable_pieces(board):#****************************************
	stable = 0
	while True:
		topbot_c = ((stable >> 8 | top) | (bottom << 8 | bottom)) & board
		leftright_c = ((stable >> 1 | left) | (right << 1 | right)) & board
		diag1_c = ((stable >> 7 | topr) | (botl << 7 | botl)) & board
		diag2_c = ((stable >> 9 | topl) | (botr << 9 | botr)) & board
		newstable = topbot_c & leftright_c & diag1_c & diag2_c
		print(bin(topbot_c), bin(leftright_c), diag1_c, diag2_c)
		print(newstable)
		if not newstable ^ stable: break
		stable |= newstable
	return stable 

def stable_piecess(board):#****************************************
	stable = 0
	while True:
		table = board & ((stable >> 8 | top) | (bottom << 8 | bottom)) & ((stable >> 1 | left) | (right << 1 | right)) & ((stable >> 7 | topr) | (botl << 7 | botl)) & ((stable >> 9 | topl) | (botr << 9 | botr))
		print(table)
		if not (table ^ stable): break
		stable |= table
	return stable 

def h_symmetricmoves(player, opp):

	return bin(possible_moves(player, opp)).count('1')-bin(possible_moves(opp, player)).count('1') #returns player moves - opp moves


def local_moves (player, opp_e, shift):#****************************************
	level = ((player << shift) | (player >> shift)) & opp_e
	for i in range(5):
		level |= ((level << shift) | (level >> shift)) & opp_e
	return (level << shift) | (level >> shift) #across 4 axis--->SHIFTTT

def possible_moves(player, opp):#****************************************
	mask = 0x7E7E7E7E7E7E7E7E
	opp_e = opp & mask
	full = 0xFFFFFFFFFFFFFFFF
	moves = local_moves(player, opp_e, 1) | local_moves(player, opp, 8) | local_moves(player, opp_e, 7) | local_moves(player, opp_e, 9)
	p = moves & (full ^ (player|opp))
	return p

def unsafe_x(player):
	#returns number of unsafe x pieces
	count = 0
	if (1 << 9) & player and not (1 << 0) and player: count += 1
	if (1 << 14) & player and not (1 << 7) and player: count += 1
	if (1 << 49) & player and not (1 << 56) and player: count += 1
	if (1 << 54) & player and not (1 << 63) and player: count += 1
	return count 

def unsafe_xx(player):
	#returns number of unsafe x pieces
	count = 0
	if (1 << 9) & player and not (1 << 0) & player: count += 1
	if (1 << 14) & player and not (1 << 7) & player: count += 1
	if (1 << 49) & player and not (1 << 56) & player: count += 1
	if (1 << 54) & player and not (1 << 63) & player: count += 1
	return count 

p, o = 0x0000000000001400, 0x0000001c1c1e000f
a = time.time()
print(h_frontiers(p, o))
print(time.time() - a)
b = time.time()
print(h_symmetricmoves(p, o))
print(time.time() - b)
c = time.time()
print(h_stable(p, o))
print(time.time() - c)
d = time.time()
print(h_stablee(p, o))
print(time.time() - d)
