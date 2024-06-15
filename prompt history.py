
# V1
"""
    I have a PDF document in Dutch that includes text, tables, and images across multiple pages. 
    I need assistance with several tasks for each page of the document. 
    First, translate all the text from Dutch to English. 
    For any images that depict tables, interpret and extract the data, then represent this data as an editable text table in English. 
    Additionally, provide descriptions and relevant interpretations for other images within the document, if not possible to make them as table and leave a placeholder for this images/figures. 
    so, if a figure image was as table and you replicated it as table, you should NOT write a placeholder for that image.
    This will ensure that both the textual and visual content are fully accessible and usable in English.
    also i want you to just directly to go respond, and you dont need for example to say that this is translated.
    we need to replicate each page.
    Finally, everything need to be written in latex format, i mean if it is section write as section if it is table write as table. 
    
    ps. document class article, usepackage graphicx begin document,  end are all already defined and you shouldnt not write them
    text: {text}
    """

#system_message = create_message(
#            "I have a PDF document in Dutch that includes text, tables, and images across multiple pages. I need assistance with several tasks for each page of the document. First, translate all the text from Dutch to English. For any images that depict tables, interpret and extract the data, then represent this data as an editable text table in English. Additionally, provide descriptions and relevant interpretations for other images within the document, if not possible to make them as table and leave a placeholder for this images/figures. so, if a figure image was as table and you replicated it as table, you should NOT write a placeholder for that image. This will ensure that both the textual and visual content are fully accessible and usable in English. also i want you to just directly to go respond, and you dont need for example to say that this is translated.  we need to replicate each page. Finally, everything need to be written in latex format, i mean if it is section write as section if it is table write as table. ps. document class article, usepackage graphicx begin document,  end are all already defined and you shouldnt not write them ",
#            "system"