# Unit Converter with Tkinter
**Abstract**: A small script that runs a dual language unit converter (English and Portuguese) for many unit types (length, time, energy etc.) and their respective units (meter, day, joule and so on).

## Background
In order to deeply learn Tkinter, after the [basic calculation project](https://github.com/geovanilopesdias/tkinter_common_calculator), I proceed to work with other gadjets as well as multiple frames.

## How it works
The app exhibits at the top radiobuttons to change between the languages, managed by dictionaries that contains the labels for each one. One of their key is the language ID (EN and PT strings) that is passed to the ControlFrame to exhibit label and listbox contents properly.

There are three listboxes: for the unit type (that handle the available units to conversion) and for the original and desired units in conversion.

The "convert" button handle the conversion according to original and desired listbox selections, which will, in turn, set the unit instances with their respective properties, such as names (in both languages) and factor for conversion.

In the background, there's the units_for_converter module that provides the following classes to manage the said listboxes:

**- UnitType**: enumerator to restric the possibilities of the available unit types for both unit ype listbox and Unit's type property (see below).

**- Unit**: a class to abstract the unit of a quantity.

**- UnitsTable**: enumerator to limit the possibilities of the available units for both unit listboxes and the conversion functionality. It contains a number of Unit instances each one representing different units. The choice for an enumerator is to avoid database or csv handling for now and, as I understand, a more versatile option than dictionaries for this context.
