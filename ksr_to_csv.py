import pandas as pd

with open ("output.txt", "r", encoding='utf-8') as text_file:

	text = text_file.read()
	lines = text.split('\n')
	lines = list(filter(None, lines))
	array = []
	for i in range(0, len(lines),3):
		try:
			item = (lines[i],lines[i+1],lines[i+2])
			array.append(item)
		except:
			pass
	data = pd.DataFrame(array)
	print(data)
	data.to_csv('KSR.csv', index=None)