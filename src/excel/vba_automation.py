#!/usr/bin/env python3
"""VBA Automation Module"""
import os
import subprocess
import tempfile
import platform

class VBAAutomation:
    def __init__(self, excel_path=None):
        self.excel_path = excel_path
        self.system = platform.system()
        
        # Check if we're on Windows
        if self.system != 'Windows':
            print("Warning: VBA automation works best on Windows. Limited functionality on other platforms.")

    def run_macro(self, excel_file, macro_name, *args):
        """
        Run a VBA macro in an Excel file
        
        Parameters:
        -----------
        excel_file : str
            Path to the Excel file
        macro_name : str
            Name of the macro to run
        *args : list
            Arguments to pass to the macro
            
        Returns:
        --------
        bool
            True if successful
        """
        if self.system == 'Windows':
            try:
                import win32com.client
                
                # Create Excel application object
                excel = win32com.client.Dispatch("Excel.Application")
                
                # Make Excel visible (optional)
                excel.Visible = False
                
                # Open the workbook
                workbook = excel.Workbooks.Open(os.path.abspath(excel_file))
                
                # Run the macro
                macro_with_args = f"{macro_name}"
                if args:
                    macro_with_args += f" {','.join([str(arg) for arg in args])}"
                
                excel.Run(macro_with_args)
                
                # Save and close
                workbook.Save()
                workbook.Close()
                excel.Quit()
                
                return True
            except Exception as e:
                print(f"Error running macro: {e}")
                return False
        else:
            print("VBA macro execution is only supported on Windows.")
            return False
