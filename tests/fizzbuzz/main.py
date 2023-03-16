 
class Solution:

	def run(self, N, M):
		seq = list(range(N,M+1))
		fb_seq = []
		sequence = ""

		for i in range(0,len(seq)):
			fb_seq.append('')
			if seq[i]%3 == 0:
				fb_seq[i] += "fizz"
			if seq[i]%5 == 0:
				fb_seq[i] += "buzz"
			if fb_seq[i] == '':
				fb_seq[i] = seq[i]
	
		sequence = ','.join([str(elem) for elem in fb_seq])
		return sequence