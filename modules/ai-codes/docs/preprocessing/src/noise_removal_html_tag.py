########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

import re 
 
text = "<p>This is a paragraph</p>" 
result = re.sub(r'<.?p>', '', text)
 
print(result) 
