# generate_docs.py
import os
import subprocess
import shutil
import sys



class DocumentationGenerator:
    def __init__(self, source_dir, output_dir):
        """
        Args:
            source_dir (str): The directory containing the source code.
            output_dir (str): The directory where the generated documentation
                will be written.
        """
        self.source_dir = source_dir
        self.output_dir = output_dir

    def generate(self):
        """
        Generates HTML documentation for each Python module in the source
        directory, excluding special and specific files. The documentation
        is created using the `pydoc` module and then moved to the specified
        output directory.

        Raises:
            FileNotFoundError: If the output file is not created.
        """

        sys.path.insert(0, self.source_dir)
        env = os.environ.copy()
        env["PYTHONPATH"] = self.source_dir

        for file in os.listdir(self.source_dir):
            if file.endswith('.py') and not file.startswith('__') and file != 'generate_docs.py':
                module_name = file[:-3]
                print(f"Generating docs for {module_name}...")

                result = subprocess.run(
                    [sys.executable, '-m', 'pydoc', '-w', module_name],
                    env=env,
                    capture_output=True,
                    text=True
                )

                print(result.stdout)
                if result.returncode != 0:
                    print(result.stderr)

                output_file = f"{module_name}.html"
                if os.path.exists(output_file):
                    shutil.move(output_file, os.path.join(self.output_dir, output_file))
                else:
                    print(f"Failed to generate documentation for {module_name}")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, 'docs')
    os.makedirs(output_dir, exist_ok=True)

    docgen = DocumentationGenerator(current_dir, output_dir)
    docgen.generate()
