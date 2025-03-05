from weasyprint import HTML
import datetime, os

current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_filename = f"cv_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
# Create a CVs directory if it doesn't exist
cvs_dir = os.path.join(current_dir, 'CVs')
if not os.path.exists(cvs_dir):
    os.makedirs(cvs_dir)
HTML(filename=os.path.join(current_dir, 'cv.html'), base_url=f"file://{current_dir}/").write_pdf(os.path.join(cvs_dir, pdf_filename))
print(f"PDF generated successfully: {os.path.join(cvs_dir, pdf_filename)}")
