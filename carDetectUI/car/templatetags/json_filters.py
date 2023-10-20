from django import template
import json

register = template.Library()

@register.filter
def json_to_items(json_data):
    items = json.loads(json_data)
    return items.items()


@register.filter
def json_filter(data):
    return json.dumps(data)