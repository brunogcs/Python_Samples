import requests
import lxml.html as lh
import pandas as pd

url = 'sampleurl.html'  # URL from the website with the table
page = requests.get(url)  # Store the contents of the website under doc
doc = lh.fromstring(page.content)  # Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

# Check the length of the first 12 rows (should return the number of columns)
[len(T) for T in tr_elements[:12]]
#print([len(T) for T in tr_elements[:12]])

#print(tr_elements[0]),exit()

tr_elements = doc.xpath('//tr')  # Create empty list
col = []
i = 0
# For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    #print ('%d:"%s"' % (i, name))
    col.append((name, []))

# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # i is the index of our column
    i = 0

    #All the elements needs to have the same size, this if is to make sure that we are taking information from the right <tr>
    if len(T) == 32:

    # Iterate through each element of the row
        for t in T.iterchildren():
            data = t.text_content()
            # Check if row is empty
            if i > 0:
                # Convert any numerical value to integers
                try:
                    data = int(data)
                except:
                    pass
            # Append the data to the empty list of the i'th column
            col[i][1].append(data)
            # Increment i for the next column
            i += 1

[len(C) for (title, C) in col]

# OUTPUT: [800, 800, 800, 800, 800, 800, 800, 800, 800, 800]

Dict = {title: column for (title, column) in col}
df = pd.DataFrame(Dict)

print(df.head(5))