Letter = '''Dear <|Name|>
You are selected! 
<|Date|>'''

print(Letter.replace("<|Name|>", "Ojas").replace("<|Date|>", "10 December 2003"))