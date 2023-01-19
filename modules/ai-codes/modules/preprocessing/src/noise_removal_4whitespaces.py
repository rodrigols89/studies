########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

import re 
 
text = "    This is a paragraph"
result = re.sub(r'\s{4}', '', text)
 
print(result)
