from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def home(request):
    '''
    This is the homepage displayer
    '''
    return render_to_response('index.html')


def dimension(request, values=None, color=None, alpha=None):
    if values is None:
        values = '500x500'

    #split removes the 'x' from the catched values
    output = values.split('x')
    # stores the list into x and y vars
    x, y = output[0], output[1]
    # time to import PIL
    from PIL import Image, ImageDraw

    #for handling the color variations
    if color is None:
        color = (191, 191, 191)
    else:
        a, b, c = color.split('.')
        color = (int(a), int(b), int(c))

    #if alpha != None:
    #   color = color.append(0.5)

    #if alpha != None:
    #   im.convert('RGBA')

    # feeding dimension for use in drawing image
    size = (int(x), int(y))
    # color, by default is line 16
    im = Image.new('RGB', size, color=color)

    # Todo:Anyway to increase font size as
    # per increase in dimension requested??
    draw = ImageDraw.Draw(im)
    text_color = (255, 255, 255)
    text_pos = (size[0]/2, size[1]/2)
    text = str(values)
    draw.text(text_pos, text, fill=text_color)

    # Done drawing. NSA, take the rest!
    del draw

    # Normal Django takes over from here. 
    # Django 1.7+ doesn't support mimetype as argument
    # Using content_type instead
    response = HttpResponse(content_type="image/png")
    # save images as PNG and push to template
    im.save(response, 'PNG')

    return response  # Tadaaaa


# Miscellenous 
def file_not_found_404(request):
    return render(request, '404.html')


def server_error(request):
    return render(request, '500.html')


def perm_denied(request):
    return render(request, '403.html')
