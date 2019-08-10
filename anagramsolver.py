import string
import sys

class AnagramSolver:
	def __init__(self, soal, wordslist):
		self.soal = soal
		self.wordslist = wordslist
		self.hasil_bf = []
		self.hasil_penyesuaian = []

	def bruteforceWL(self):
		jml_abjad_benar = 0
		with open(self.wordslist, 'r') as f:
			for isi in f.readlines():
				isi = isi.lower().replace('\n', '')
				for abjadsoal in list(self.soal):
					if abjadsoal in isi:
						jml_abjad_benar+=1
					else:
						jml_abjad_benar = 0
				if len(isi) == jml_abjad_benar and len(isi) == len(self.soal):
					self.hasil_bf.append(isi)
					jml_abjad_benar=0
				else:
					jml_abjad_benar=0

	def matchTheResults(self):
		soal_alphabet = []
		soal_match_count = []

		isi_alphabet = []
		isi_match_count = []

		for alphabet in list(string.ascii_lowercase):
			if alphabet in self.soal:
				soal_alphabet.append(alphabet)
				soal_match_count.append(self.soal.count(alphabet))

		soal_b_dict = zip(soal_alphabet, soal_match_count)
		soal_dict = dict(soal_b_dict)

		jml_dict_sesuai = 0
		for isi in self.hasil_bf:
			for alphabet in list(string.ascii_lowercase):
					if alphabet in isi:
						isi_alphabet.append(alphabet)
						isi_match_count.append(isi.count(alphabet))
			isi_b_dict = zip(isi_alphabet, isi_match_count)
			isi_dict = dict(isi_b_dict)
			for soal_alpha in soal_dict.keys():
				if soal_dict[soal_alpha] == isi_dict[soal_alpha]:
					jml_dict_sesuai+=1
				else:
					jml_dict_sesuai=0
			if jml_dict_sesuai == len(soal_dict):
				self.hasil_penyesuaian.append(isi)
				jml_dict_sesuai = 0
			else:
				jml_dict_sesuai = 0

	def printResult(self):
		try:
			f = open(self.wordslist)
			f.close()
		except FileNotFoundError:
			print(self.wordslist,"NOT FOUND")
			return ""
		else:
			self.bruteforceWL()
			self.matchTheResults()
			if self.hasil_penyesuaian is not None:
				return self.hasil_penyesuaian

try:
	anagram = sys.argv[1]
	wordslist = sys.argv[2]
except IndexError:
	print('use: python %s %s %s' % (sys.argv[0],sys.argv[1],sys.argv[2]))
else:
	anagram = anagram.lower().replace(' ', '')
	wordslist = wordslist.lower()
	solv = AnagramSolver(soal=anagram, wordslist=wordslist)
	print(solv.printResult())