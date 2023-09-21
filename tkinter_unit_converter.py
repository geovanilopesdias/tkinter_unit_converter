import tkinter as tk
from tkinter import ttk
from units_for_converter import UnitType
from units_for_converter import UnitsTable


class ConverterFrame(ttk.Frame):
    def __init__(self, container, language, converter):
        super().__init__(container)

        self.language = language
        self.converter = converter
        
        lbl_pad = {'padx': 10, 'pady': 10}
        dpl_pad = {'padx': 5, 'pady': 5}

        # Window title
        self.title_label = ttk.Label(self,
                       text=self.language["title"],
                       font=("Courier", 12))
        self.title_label.grid(column=0, row=0, columnspan=7, **lbl_pad)

        # Input section
        ## Default values of listboxes
        self.DEFAULT_UNIT_TYPE = UnitType.get_tkVar_of_unit_types_in(self.language["id"])
        self.DEFAULT_IO_UNITS = UnitsTable.get_tkVar_names(self.language["id"], UnitType.LENGTH)

        ## Listboxes, its labels and selection variables (string and Unit)
        self.lbl_unit_type = ttk.Label(self, text=self.language["unit type label"])
        self.lbx_unit_type = tk.Listbox(self, listvariable=self.DEFAULT_UNIT_TYPE, height=1)

        self.lbl_original_unit = ttk.Label(self, text=self.language["original unit label"])
        self.lbx_original_unit = tk.Listbox(self, listvariable=self.DEFAULT_IO_UNITS, height=1)
        self.sel_original_unit = {'string': 'meter', 'unit': UnitsTable.METER}

        self.lbl_desired_type = ttk.Label(self, text=self.language["desired unit label"])
        self.lbx_desired_unit = tk.Listbox(self, listvariable=self.DEFAULT_IO_UNITS, height=1)       
        self.sel_desired_unit = {'string': 'meter', 'unit': UnitsTable.METER}

        self.DEFAULT_QUANTITY_VALUE = tk.StringVar(value='0')
        self.input_value = tk.Entry(self, font=("Courier", 20), textvariable=self.DEFAULT_QUANTITY_VALUE)
        self.output_value = tk.Label(self, height="1", width="8", font=("Courier", 20))
        self.btn_convertion = ttk.Button(self,
                                          text=self.language["button"])
        self.btn_convertion.configure(command=self.convert)
        
        ### Griding and biding
        self.lbl_unit_type.grid(column=0, row=2, **lbl_pad)
        self.lbx_unit_type.grid(column=1, row=2, columnspan=1, **dpl_pad)

        self.input_value.grid(column=0, row=3, columnspan=1, **dpl_pad)
        self.lbl_original_unit.grid(column=1, row=3, **lbl_pad)
        self.lbx_original_unit.grid(column=2, row=3, columnspan=1, **dpl_pad)

        self.lbl_desired_type.grid(column=3, row=3, **lbl_pad)
        self.lbx_desired_unit.grid(column=4, row=3, columnspan=1, **dpl_pad)       
        self.btn_convertion.grid(column=0, row=4, columnspan=1)
        self.output_value.grid(column=0, row=5, columnspan=1, **dpl_pad)
        
        self.lbx_unit_type.bind("<<ListboxSelect>>", self.set_unit_io_listvariables)
        self.lbx_original_unit.bind("<<ListboxSelect>>", self.set_original_unit)
        self.lbx_desired_unit.bind("<<ListboxSelect>>", self.set_desired_unit)
        
        # Frame Layout
        self.grid(column=0, row=2, padx=5, pady=5)


    # Event Handlers
    def set_unit_type_listvariable(self):
        lbx_var = UnitType.get_tkVar_of_unit_types_in(self.language["id"])
        self.lbx_unit_type['listvariable'] = lbx_var


    def set_unit_io_listvariables(self, event):
        """
        Sets the original and desired unit tkinter Listbox instances according
        to the selection on unit type tkinter Listbox instance.
        """
        try:            
            selected_indices = self.lbx_unit_type.curselection()
            if selected_indices:
                index = int(selected_indices[0])
                lbx_var = UnitsTable.get_tkVar_names(self.language["id"], self.lbx_unit_type.get(index))
                self.lbx_original_unit['listvariable'] = lbx_var
                self.lbx_desired_unit['listvariable'] = lbx_var
        except RuntimeError:
            print('RuntimeError in set_unit_io_listvariables()')


    def set_original_unit(self, event):
        try:
            selected_indices = self.lbx_original_unit.curselection()
            if selected_indices:
                index = int(selected_indices[0])
                self.sel_original_unit['string'] = self.lbx_original_unit.get(index)
                self.sel_original_unit['unit'] = UnitsTable.get_unit_by_lang_and_name(self.language["id"], self.sel_original_unit['string'])
        except RuntimeError:
            print('RuntimeError in set original unit')
        

    def set_desired_unit(self, event):
        try:
            selected_indices = self.lbx_desired_unit.curselection()
            if selected_indices:
                index = int(selected_indices[0])
                self.sel_desired_unit['string'] = self.lbx_desired_unit.get(index)
                self.sel_desired_unit['unit'] = UnitsTable.get_unit_by_lang_and_name(self.language["id"], self.sel_desired_unit['string'])
        except RuntimeError:
            print('RuntimeError in set desired unit')


    def convert(self):
        """
        Handle conversion button click event.
        """            
        try:            
            input_value = float(self.input_value.get())
            result = self.converter(input_value, self.sel_original_unit['unit'], self.sel_desired_unit['unit'])
            self.output_value.config(text = str(result))
        except ValueError:            
            print('ValueError: string couldn\'t be converted to float')
        except AttributeError as e:            
            print(e)

        
        

class LanguageChoiceFrame(ttk.LabelFrame):
    def __init__(self, container):
        
        super().__init__(container)
        self['text'] = 'Escolha seu idioma / Choose your language:'

        radio_settings = {'row': 0, 'padx': 5, 'pady': 5}
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Português',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, **radio_settings)

        ttk.Radiobutton(
            self,
            text='English',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, **radio_settings)
        
        self.grid(column=0, sticky='ew', **radio_settings)

        self.PT_LANG = {'id': 'PT', 'title': 'Conversor de medidas',
                   'unit type label': 'Tipo de unidade',
                   'original unit label': 'Converter de ',
                   'desired unit label': ' para ',
                   'button': 'Converter'}
        self.EN_LANG = {'id': 'EN', 'title': 'Quantity Converter',
                   'unit type label': 'Unit type',
                   'original unit label': 'Convert from ',
                   'desired unit label': ' to ',
                   'button': 'Convert'}
        
        self.frames = {}
        self.frames[0] = ConverterFrame(container, self.PT_LANG, UnitsTable.convert_units)
        self.frames[1] = ConverterFrame(container, self.EN_LANG, UnitsTable.convert_units)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.tkraise()


# App initiliazier
class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gheowin Unit Converter')
        self.geometry('1000x1000')
        self.resizable(False, False)


        
if __name__ == "__main__":
    app = ConverterApp()
    LanguageChoiceFrame(app)
    app.mainloop()
