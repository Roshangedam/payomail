from abc import ABC, abstractmethod
import os

class Template(ABC):
    def __init__(self):
        self.content = None
        self.file_path = None

    @abstractmethod
    def set_template(self, content):
        """
        Set the content of the template.

        Parameters:
            content (str): The content of the template.
        """
        pass

    def set_file_path(self, file_path):
        """
        Set the file path of the template.

        Parameters:
            file_path (str): The file path of the template.
        """
        self.file_path = file_path        
        try:  
            with open(self.file_path, 'r') as file:
                self.content = file.read()             
        except Exception as e:
             print({'status': 'Template adding Failure', 'error_message': f"error: {str(e)}"})

        return self

    @abstractmethod
    def set_value(self, key, value):
        """
        Set additional values for the template.

        Parameters:
            key (str): The key of the value.
            value (any): The value to be set.
        """
        pass

    @abstractmethod
    def build(self):
        """
        Build the template.
        This method should be overridden in subclasses if additional processing is needed.
        """
        pass

class HTMLTemplate(Template):
    def __init__(self):
        super().__init__()
        self.content_type = "text/html"

    def set_template(self, content):
        """
        Set the content of the HTML template.

        Parameters:
            content (str): The content of the HTML template.
        """
        # You can perform additional processing specific to HTML templates here if needed
        self.content = content
        return self

    def set_value(self, key, value):
        """
        Set additional values for the HTML template.

        Parameters:
            key (str): The key of the value.
            value (any): The value to be set.
        """
        if self.content:
            self.content = self.content.replace("{{" + key + "}}", str(value))
        return self

    def build(self):
        """
        Build the HTML template.
        This method reads the content from the file path and sets it as the template content.
        """
        pass

# # Example usage:
# html_template = HTMLTemplate()
# html_template.set_file_path('payomail/template/test.html')
# html_template.set_value('name', 'John Doe')
# html_template.set_value('age', '123 Main Street')
# print(html_template.content)  # Output the modified HTML content with replaced values
