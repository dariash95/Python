# Write code using find() and string slicing (see section 6.10) to extract the
# number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

text = ('X-DSPAM-Confidence:    0.8475')
pos_0 = text.find('0')
pos_5 = text.find('5',pos_0)
data = text[pos_0:pos_5+1] # +1 porque sino, imprime 0.847.
data = float(data)
print(data)
