from bs4 import BeautifulSoup
import csv

output = open("output.csv", "w", newline="")
writer = csv.writer(output)
writer.writerow(['name','designation','@image'])

with open("cs_mbcet.html", "r", encoding='utf8') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")
    tags = soup.find_all(class_ = "faculty-item")
    i = 0
    for tag in tags:
        i = i + 1
        name = tag.div.h3.a.text
        name = ' '.join(name.split())
        designation = tag.p.text
        designation = ' '.join(designation.split())
        image = "F:/Downloads/files/" +str(tag.img['src']).split("/")[-1]
        writer.writerow([name, designation, image])
        # print(name + " working as " + designation + ", image: " + image)

output.close()
print(i)