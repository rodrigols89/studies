########################################################
# Rodrigo Leite - drigols                              #
# Last update: 29/12/2021                              #
########################################################

import re
 
text = "Five fantastic fish flew off to find faraway functions. Maybe find another five fantastic fish? Find my fish with a function please!"
print("Original text:", text)

# Remove punctuation.
result = re.sub(r'[\.\?\!\,\:\;\"]', '', text)
print("Noise Removal: ", result)
