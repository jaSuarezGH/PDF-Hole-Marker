import pymupdf

HOLE_MARGIN: int = 10

def draw_holes_by_number(hole_number:int, doc: any, hole_margin: int = HOLE_MARGIN):

    try:
        for page_index in range(len(doc)): # Iterate over pdf pages
            hole_y_pos = 0 # Reset initial hole position
            page = doc[page_index] # Get the page
            rect = page.rect # Get page rectangle (dimentions)
            
            # Draw holes
            for x in range(hole_number):

                # Calculate hole Y position
                hole_y_pos += rect.height / (hole_number + 1)

                page.draw_circle((hole_margin, hole_y_pos), radius=3, color=(0, 0, 0), width=1.2)

    except Exception as e:
        print("An exception occurred", e)

def draw_holes_by_number_and_space(hole_number:int, hole_distance:int, doc: any, hole_margin: int = HOLE_MARGIN):

    try:
        for page_index in range(len(doc)): # Iterate over pdf pages
            page = doc[page_index] # Get the page
            rect = page.rect # Get page rectangle (dimentions)
            hole_y_pos = ((rect.height - (hole_distance*(hole_number-1))))/2
            
            # Draw holes
            for x in range(hole_number):

                page.draw_circle((hole_margin, hole_y_pos), radius=3, color=(0, 0, 0), width=1.2)

                hole_y_pos += hole_distance

    except Exception as e:
        print("An exception occurred", e)

def clean_file_name(file_name:str) -> str:
    if not file_name.endswith(".pdf"):
        return file_name + ".pdf"
    
def set_ouput_file_name(file_name:str) -> str:
    return f"{file_name.removesuffix(".pdf")} - Hole Puncher Marker Result.pdf"

if __name__ == "__main__":

    #file_name: str = clean_file_name(input("Enter PDF file name:"))
    file_name: str = "documento.pdf"
    output_file_name: str = set_ouput_file_name(file_name)

    try:
        doc = pymupdf.open(file_name) # Open a document
        #draw_holes_by_number(5, doc)
        draw_holes_by_number_and_space(3, 141, doc)
        doc.save(output_file_name) # Save the document with a new filename
    except Exception as e:
        print("An exception occurred", e)
    finally:
        doc.close()
    