# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#
import xml.dom.minidom


def main():
    # use the parse() function to load and parse an XML file
    document = xml.dom.minidom.parse("samplexml.xml")
    
    # print out the document node and the name of the first child tag
    print(document.nodeName)
    print(document.firstChild.tagName)

    # get a list of XML tags from the document and print each one
    skills = document.getElementsByTagName("skill")
    print(skills.length, "skills are listed")
    for skill in skills:
        print(skill.getAttribute("name"))
      
    # create a new XML tag and add it into the document
    newSkill = document.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    document.firstChild.appendChild(newSkill)

    skills = document.getElementsByTagName("skill")
    print(skills.length, "skills are listed")
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()

