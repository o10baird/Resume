# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:58:36 2021

@author: o10ba

Purpose: Creates a series of .txt files converted from a directory of .pdf files

"""

# Imports system tools and the pdf data extraction tool
import os
import pdfplumber

# Sets the path to file directory that holds documents to be parsed.
directory_string = r"E:\Army Regulations"

# Converts the document directory path from a raw string to bytes
directory_byte = os.fsencode(directory_string)

# Runs through every file in the designated directory
for file in os.listdir(directory_string):
    
    # Sets the filename variable equal to the file that is currently being read
    filename = os.fsdecode(file)
    
    # path to the directory that will hold the output .txt files
    save_path = r"C:\Users\o10ba\Desktop\Regulation Texts"
    
    # sets the name of the .txt file equal to the name of the original .pdf
    # but with the .pdf removed
    full_save_name = os.path.join(save_path, filename[:-4])
    
    # print statement to track progress for users in the terminal
    print(full_save_name)
    
    # Creates a new .txt with the name of the original .pdf
    document_text = open(full_save_name+".txt", encoding='utf-8', mode='w+')
    
    # opens the original .pdf with the pdf extraction tool
    with pdfplumber.open(directory_string+"\\"+filename) as pdf:
        
        # Sets the parsing to begin at the first page and end at the last page
        parse_start = 0
        parse_end = len(pdf.pages)
        
        # commented out section includes metadata information for testing
        #document_data = pdf.metadata
        #for k, v in document_data.items():
            #print(k, "--> ", v)
        
        # iterates through every page in the document
        for i in range(parse_end - parse_start):
            
            # sets page variable equal to the desired starting page plus iterator
            page = pdf.pages[i + parse_start]
            
            # sets page_text variage equal to extracted text from the .pdf's page
            page_text = page.extract_text()
            
            # if statement to catch blank pages that return as NoneType vs. strings
            if type(page_text) != str:
                page_text = "Coder Added Text: This was a blank page."
            
            # Adds four newline characters at the end of every page
            page_text += "\n\n\n\n"
            
            # writes the page_text string into the .txt file
            document_text.write(page_text)
    
    # Closes the .txt file
    document_text.close()

    #break