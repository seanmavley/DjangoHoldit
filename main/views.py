from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont


def home(request):
    '''
    This is the homepage displayer
    '''
    return render_to_response('index.html')


def dimension(request, values=None, color=None, text=None):
    if values is None:
        values = '500x500'

    # split removes the 'x' from the catched values
    output = values.split('x')
    # stores the list into x and y vars
    # but if no y value provided, display
    # square image based on single value provided
    try:
        x, y = output[0], output[1]
    except:
        x = output[0]
        y = x

    # for handling the color variations
    if color is None:
        color = (191, 191, 191)
    else:
        a, b, c = color.split('.')
        color = (int(a), int(b), int(c))

    # Try doing some Alpha of image?
    # Not necessary, but just for the fun of it? ;)

    # if alpha != None:
    #   color = color.append(0.5)

    # if alpha != None:
    #   im.convert('RGBA')

    # feeding dimension for use in drawing image
    size = (int(x), int(y))
    im = Image.new('RGB', size, color=color)

    if text == None:
        text_show = '[' + str(values) + ']'
    else:
        text_show = str(text)

    fontsize = 1
    img_fraction = 0.50


    draw = ImageDraw.Draw(im)
    text_color = (255, 255, 255)
    # text_pos = (10, 25)
    text_pos = (size[0]/8, size[1]/8)

    font = ImageFont.truetype("arial.ttf", fontsize)

    while font.getsize(text_show)[0] < img_fraction*im.size[0]:
        fontsize += 1
        font = ImageFont.truetype("arial.ttf", fontsize)
    draw.text(text_pos, text_show, font=font, fill=text_color)

    del draw

    # Normal Django takes over from here.
    # Django 1.7+ doesn't support mimetype as argument
    # Using content_type instead
    response = HttpResponse(content_type="image/png")
    # save images as jpeg and push to template
    im.save(response, 'png')

    return response


# Error Pages
def file_not_found_404(request):
    return render(request, '404.html')


def server_error(request):
    return render(request, '500.html')


def perm_denied(request):
    return render(request, '403.html')
