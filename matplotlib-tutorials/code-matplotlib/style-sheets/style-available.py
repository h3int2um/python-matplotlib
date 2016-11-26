import matplotlib.pyplot as plt
import numpy as np
import os

style_list = plt.style.available # Liet ke tat ca cac style co san

print style_list

folder = 'styles-availabe'
if not os.path.exists(folder):
	os.makedirs(folder)

for style in  style_list:
	with plt.style.context((style)):
		plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
		plt.title('Plot ' + style)
		plt.savefig(folder + '/' + style + '.png', bbox_inches='tight')
