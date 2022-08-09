import re # RegularExpression
import pyperclip # Copy and Paste clipboard function



# create regex for email
emailRegex = re.compile("""
                        ([a-zA-z0-9_+./-]+  # Name Part
                        @                 # @ symbol
                        ([a-zA-z]+          
                        \.[a-zA-z]{2,5}))  # Domain name 
                        """,re.VERBOSE)

# Copy text from website or document
text = pyperclip.paste()


extractedEmail = emailRegex.findall(text)



all_email = []
for j in extractedEmail:
    all_email.append(j[0])
    

result = "\n".join(all_email)
pyperclip.copy(result)
