import os
from display import Display
from test_output_html_generator import TestOutputHtmlGenerator
from spec_section import SpecSection

# Test profiles for B2B, B2C, middleground

if __name__ == "__main__":
    # display = Display()
    # display.display("spec.txt")
    
    # design_errors = display.get_design_errors()
    # functionality_passed = display.get_functionality_errors()
    # spec_tested_against = display.get_spec()
    
    # test_output_html_generator = TestOutputHtmlGenerator("output.html", design_passed, functionality_passed, spec_tested_against)
    spec_section1 = SpecSection("Category1")
    spec_section1.add_task("task1")
    spec_section1.add_task("task2")
    
    spec_section2 = SpecSection("Category2")
    spec_section2.add_task("task3")
    spec_section2.add_task("task4")
    
    test_output_html_generator = TestOutputHtmlGenerator("output.html", 
                                                         ["Design failure 1","Design failure 2"], 
                                                         ["Functionality failure 1", "Functionality failure 2"],
                                                         [spec_section1,spec_section2])
    test_output_html_generator.generate_test_output_html()
    test_output_html_generator.show_html()
            
    
    
def check_design_passed():
    design_passed = input("Design passed? (y/n)")
    match design_passed:
        case 'y':
            return "Design passed<br>"