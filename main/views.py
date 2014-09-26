from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'index.html')

def dimension(request, values, color=None, alpha=None):
	output = values.split('x') # split removes the 'x' from the catched values
	x, y = output[0], output[1] # stores the list into x and y vars

	from PIL import Image, ImageDraw 
	
	#for handling the color variations
	if color == None:
		color = (191,191,191)
	else:
		a, b, c = color.split('.')
		color = (int(a), int(b), int(c))
	
	#if alpha != None:
	#	color = color.append(0.5)

	#if alpha != None:
	#	im.convert('RGBA')

	size = (int(x), int(y)) # feeding dimension for use in drawing image
	im = Image.new('RGB', size, color=color) # color, by default is line 16

	#anyway to increase font size as per increase in dimension requested??
	draw = ImageDraw.Draw(im)
	text_color = (255,255,255)
	text_pos = (size[0]/2, size[1]/2)
	text = str(values)
	draw.text(text_pos, text, fill=text_color)

	del draw # Done drawing. NSA, take the rest!

	# Normal Django takes over from here. Django 1.7 Plus doesn't support mimetype as argument
	response = HttpResponse(content_type="image/png")
	# save images as PNG and push to template
	im.save(response, 'PNG')

	return response # Tadaaaa

def file_not_found_404(request):
	return render(request, '404.html')

def server_error(request):
	return render(request, '500.html')

def perm_denied(request):
	return render(request, '403.html')