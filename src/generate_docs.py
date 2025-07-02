# generate_docs.py
import os
import subprocess
import shutil
import sys

class DocumentationGenerator:
    def __init__(self, source_dir):
        self.source_dir = source_dir
    def generate(self):
        # Add source_dir to PYTHONPATH so pydoc can find modules
        sys.path.insert(0, self.source_dir)

        for file in os.listdir(self.source_dir):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]  # strip .py
                subprocess.run([sys.executable, '-m', 'pydoc', '-w', module_name])
                shutil.move(f"{module_name}.html", os.path.join(output_dir, f"{module_name}.html"))


if __name__ == "__main__":
    current_dir=os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(os.path.dirname(__file__), 'docs')
    os.makedirs(output_dir, exist_ok=True)
    source_dir = current_dir
    docgen = DocumentationGenerator(source_dir)
    docgen.generate()
