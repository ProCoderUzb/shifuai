from django import template
import markdown as md

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    # This converts markdown symbols into real HTML tags
    return md.markdown(text, extensions=['extra'])