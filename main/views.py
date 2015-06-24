# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


def homepage(request):
    return render(request, 'index.html')


class PlaceholderView(View):
    def get(self, request, width, height, background, color, text, format):
        width = int(width)
        height = int(height or width)
        background = Color('#{}'.format(background or 'ccc'))
        color = Color('#{}'.format(color or '969696'))
        text = text or '{} x {}'.format(width, height)
        format = format or 'gif'

        with Image(width=width, height=height, background=background) as image:
            with Drawing() as draw:
                draw.fill_color = color
                draw.font_size = width / 2
                draw.text_alignment = 'center'

                while True:
                    metrics = draw.get_font_metrics(image, text)

                    if metrics.text_width < width / 2:
                        break

                    draw.font_size -= 1

                draw.text(int(width / 2), int(height / 2 + (metrics.text_height - metrics.ascender - metrics.descender) / 2), text)
                draw(image)

            return HttpResponse(image.make_blob(format), content_type='image/{}'.format(format))
