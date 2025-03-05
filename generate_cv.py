import os
import datetime
import webbrowser
import argparse
from weasyprint import HTML, CSS

def generate_cv_pdf(view_pdf=True):
    """Generate a PDF from HTML/CSS with a self-contained approach"""
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define file paths
    html_path = os.path.join(current_dir, 'html', 'cv.html')
    css_path = os.path.join(current_dir, 'css', 'style.css')
    
    # Create output directory
    pdf_filename = f"cv_{datetime.datetime.now().strftime('%m%d_%H%M')}.pdf"
    cvs_dir = os.path.join(current_dir, 'CVs')
    if not os.path.exists(cvs_dir):
        os.makedirs(cvs_dir)
    pdf_path = os.path.join(cvs_dir, pdf_filename)
    
    print(f"Generating CV PDF...")
    
    # Read CSS file directly
    with open(css_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Generate PDF using the CSS content directly
    html = HTML(filename=html_path, base_url=f"file://{current_dir}/")
    css = CSS(string=css_content)
    
    # Adding specific print settings for WeasyPrint
    html.write_pdf(
        pdf_path, 
        stylesheets=[css],
        presentational_hints=True  # Respect HTML presentational hints
    )
    
    print(f"CV PDF generated successfully at: {pdf_path}")
    
    # Open the PDF if requested
    if view_pdf:
        print("Opening PDF...")
        webbrowser.open(f"file://{pdf_path}")
    
    return pdf_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate CV PDF")
    parser.add_argument("--no-view", action="store_true", help="Don't open the PDF after generation")
    parser.add_argument("--margins", type=str, default="0.5cm", help="PDF margins (e.g., '0.5cm', '0cm')")
    args = parser.parse_args()
    
    generate_cv_pdf(not args.no_view)
