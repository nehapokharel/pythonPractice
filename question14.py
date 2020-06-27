def add_tag(tag, string):
    return "<%s> %s </%s>" %(tag, string, tag)

print(add_tag("i","Python"))
print(add_tag("b","Python Tutorial"))
