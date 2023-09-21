from enum import Enum
import tkinter as tk
import logging

## When iterating through UnitsTable to access Unit instances, use .value.
## When working with individual Unit instances obtained from the enumeration, access their attributes and methods directly (without .value).


class UnitType(Enum):
    LENGTH = {'EN': 'length', 'PT': 'comprimento'}
    AREA = {'EN': 'area', 'PT': 'área'}
    VOLUME = {'EN': 'volume', 'PT': 'volume'}
    TIME = {'EN': 'time', 'PT': 'tempo'}  
    VELOCITY = {'EN': 'velocity', 'PT': 'velocidade'}  
    ACCELERATION = {'EN': 'acceleration', 'PT': 'aceleração'}
    MASS = {'EN': 'mass', 'PT': 'massa'}  
    DENSITY = {'EN': 'density', 'PT': 'densidade'}  
    FORCE = {'EN': 'force', 'PT': 'força'}  
    PRESSURE = {'EN': 'pressure', 'PT': 'pressão'}  
    ENERGY = {'EN': 'energy', 'PT': 'energia'}
    POWER = {'EN': 'power', 'PT': 'potência'} 
    
    
    def get_name_by_language(self, lang):
        return self.value[lang]


    @staticmethod
    def get_unit_type_by_name(name: str):
        """
        Searchs for the passed string instance "name" in each
        UnitType enumerator value, despite its language, returning
        the respective enum value according to the said name.
        """
        for ut in UnitType:
            if name in ut.value.values():
                return ut

   
    @staticmethod
    def get_tkVar_of_unit_types_in(lang):
        """
        Returns a tkinter Variable instance to use in Listbox instances
        with the names of the unit types registered at UnitType enumerator
        according to the language passed.
        """
        list_for_var = [ut.get_name_by_language(lang) for ut in UnitType]
        return tk.Variable(value=list_for_var)



class Unit():
    def __init__(self, en_name, pt_name, symbol, conversion_factor, unit_type):
        self.__en_name = en_name
        self.__pt_name = pt_name
        self.__symbol = symbol
        self.__conversion_factor = conversion_factor
        self.__type = unit_type


    def __str__(self):
        return 'EN: ' + self.__en_name + ' PT: ' + self.__pt_name + ' SY: ' + self.__symbol + ' CF: ' + str(self.__conversion_factor)


    def get_name(self, lang):
        if lang == 'PT':
            return self.__pt_name
        else:
            return self.__en_name


    def get_symbol(self):
        return self.__symbol


    def get_conversion_factor(self):
        return self.__conversion_factor


    def get_unit_type(self):
        return self.__type



class UnitsTable(Enum):
    METER = Unit('meter', 'metro', 'm', 1, UnitType.LENGTH)
    DECIMETER = Unit('decimeter', 'decímetro', 'dm', 1e-1, UnitType.LENGTH)
    CENTIMETER = Unit('centimeter', 'centímetro', 'cm', 1e-2, UnitType.LENGTH)
    MILIMETER = Unit('milimeter', 'milímetro', 'mm', 1e-3, UnitType.LENGTH)
    DECAMETER = Unit('decameter', 'decâmetro', 'dam', 1e1, UnitType.LENGTH)
    HECTOMETER = Unit('hectometer', 'hectômetro', 'hm', 1e2, UnitType.LENGTH)
    KILOMETER = Unit('kilometer', 'quilômetro', 'km', 1e3, UnitType.LENGTH)
    INCH = Unit('inch', 'polegada', 'in', .0254, UnitType.LENGTH)
    FOOT = Unit('foot', 'pé', 'ft', .3048, UnitType.LENGTH)
    YARD = Unit('yard', 'jarda', 'yd', .9144, UnitType.LENGTH)
    MILE = Unit('mile', 'milha', 'mi', 1609.34, UnitType.LENGTH)
    ASTRO_UNIT = Unit('astronomic unit', 'unidade astronômica', 'AS', 6.6846e-12, UnitType.LENGTH)
    LIGHT_YEAR = Unit('light-year', 'ano-luz', 'ly', 1.057e-16, UnitType.LENGTH)
    PARSEC = Unit('parsec', 'parsec', 'pc', 3.24078e-17, UnitType.LENGTH)

    SQUARE_METER = Unit('square meter', 'metro quadrado', 'm²', 1, UnitType.AREA)
    SQUARE_CENTIMETER = Unit('square centimeter', 'centímetro quadrado', 'cm²', 1e-4, UnitType.AREA)
    SQUARE_MILIMETER = Unit('square milimeter', 'milímetro quadrado', 'mm²', 1e-6, UnitType.AREA)
    SQUARE_KILOMETER = Unit('square kilometer', 'quilômetro quadrado', 'km²', 1e6, UnitType.AREA)
    HECTARE = Unit('hectare', 'hectare', 'ha', 1e4, UnitType.AREA)
    SQUARE_INCH = Unit('square inch', 'polegada quadrada', 'in²', 0.000645, UnitType.AREA)
    SQUARE_FEET = Unit('square foot', 'pé quadrado', 'ft²', 0.092903, UnitType.AREA)

    CUBIC_METER = Unit('cubic meter', 'metro cúbico', 'm²', 1, UnitType.VOLUME)
    CUBIC_CENTIMETER = Unit('cubic centimeter', 'centímetro cúbico', 'cm²', 1e-6, UnitType.VOLUME)
    CUBIC_MILIMETER = Unit('cubic milimeter', 'milímetro cúbico', 'mm²', 1e-9, UnitType.VOLUME)
    CUBIC_KILOMETER = Unit('cubic kilometer', 'quilômetro cúbico', 'km²', 1e9, UnitType.VOLUME)
    LITER = Unit('liter', 'litro', 'L', 1e-3, UnitType.VOLUME)
    FLUID_OUNCE = Unit('fluid ounce', 'onça fluida', 'fl oz', 2.84131e-5, UnitType.VOLUME)
    GALLON_IMPERIAL = Unit('imperial gallon', 'galão imperial', 'gal (imp)', 0.004546, UnitType.VOLUME)
    GALLON_US = Unit('US gallon', 'galão americano', 'gal (US)', 0.003785, UnitType.VOLUME)
    CUBIC_INCH = Unit('cubic inch', 'polegada cúbico', 'in²', 0.000645, UnitType.VOLUME)
    CUBIC_FEET = Unit('cubic foot', 'pé cúbico', 'ft²', 0.092903, UnitType.VOLUME)

    SECOND = Unit('second', 'segundo', 's', 1, UnitType.TIME)
    MINUTE = Unit("minute", "minuto", "min", 60, UnitType.TIME)
    HOUR = Unit("hour", "hora", "h", 3600, UnitType.TIME)
    DAY = Unit("day", "dia", "d", 86400, UnitType.TIME)

    METER_PER_SECOND = Unit("meter per second", "metro por segundo", "m/s", 1, UnitType.VELOCITY)
    KILOMETER_PER_HOUR = Unit("kilometer per hour", "quilômetro por hora", "km/h", 0.277778, UnitType.VELOCITY)
    MILE_PER_HOUR = Unit("mile per hour", "milha por hora", "mi/h", 0.44704, UnitType.VELOCITY)
    KNOT = Unit("knot", "nó", "kn", 0.514444, UnitType.VELOCITY)
    MACH = Unit("Mach", "Mach", "Mach", 0.002915, UnitType.VELOCITY)

    METER_PER_SECOND_SQUARED = Unit("meter per second squared", "metro por segundo ao quadrado", "m/s²", 1, UnitType.ACCELERATION)
    G = Unit("g", "g", "g", 9.80665, UnitType.ACCELERATION)
    KILOMETER_PER_HOUR_PER_SECOND = Unit("kilometer per hour per second", "quilômetro por hora por segundo", 'km/(h'+u'2219'+'s)', 0.277777, UnitType.ACCELERATION)
    MILE_PER_HOUR_PER_SECOND = Unit("mile per hour per second", "milha por hora por segundo", 'mi/(h'+u'2219'+'s)', 0.447047, UnitType.ACCELERATION)

    KILOGRAM = Unit('kilogram', 'quilograma', 'kg', 1, UnitType.MASS)
    GRAM = Unit('gram', 'grama', 'g', 1e-3, UnitType.MASS)
    DECIGRAM = Unit('decigram', 'decigrama', 'dg', 1e-4, UnitType.MASS)
    CENTIGRAM = Unit('centigram', 'centigrama', 'mg', 1e-5, UnitType.MASS)
    MILIGRAM = Unit('miligram', 'miligrama', 'mg', 1e-6, UnitType.MASS)
    DECAGRAM = Unit('decagram', 'decagrama', 'dm', 1e-2, UnitType.MASS)
    HECTOGRAM = Unit('hectogram', 'hectograma', 'hm', 1e-1, UnitType.MASS)
    OUNCE = Unit('ounce', 'onça', 'oz', 10.028349, UnitType.MASS)
    POUND = Unit('pound', 'libra', 'lb', 0.453592, UnitType.MASS)
    STONE = Unit('stone', 'stone', 'st', 6.35029318, UnitType.MASS)
    TONNE = Unit('tonne', 'tonelada', 'ton', 1000, UnitType.MASS)
    EARTH_MASS = Unit('earth\'s mass', 'massa terrestre', 'M'+u'2295', 5.972e24, UnitType.MASS)
    SOLAR_MASS = Unit('solar mass', 'massa solar', 'M'+u'2299', 1.989e30, UnitType.MASS)

    KILOGRAM_PER_CUBIC_METER = Unit("kilogram per cubic meter", "quilograma por metro cúbico", "kg/m³", 1, UnitType.DENSITY)
    GRAM_PER_CUBIC_CENTIMETER = Unit("gram per cubic centimeter", "grama por metro cúbico", "g/cm³", 1000, UnitType.DENSITY)

    NEWTON = Unit('newton', 'newton', 'N', 1, UnitType.FORCE)
    DYNE = Unit("dyne", "dina", "dyn", 1e-5, UnitType.FORCE)
    KGF = Unit("quilogram-force", "quilograma-força", "kgf", 9.80665, UnitType.FORCE)

    PASCAL = Unit("pascal", "pascal", "Pa", 1, UnitType.PRESSURE)
    BAR = Unit("bar", "bária", "bar", 100000, UnitType.PRESSURE)
    PSI = Unit("pound per square inch", "libra por polegada quadrada", "psi", 6894.76, UnitType.PRESSURE)
    MM_HG = Unit("milimiters of mercury", "milímetro de mercúrio", "mmHg", 133.322, UnitType.PRESSURE)
    ATMOSPHERE = Unit("atmosphere", "atmosfera", "atm", 101325, UnitType.PRESSURE)

    JOULE = Unit("joule", "joule", "J", 1, UnitType.ENERGY)
    BTU = Unit("british thermal unit", "unidade térmica britânica", "BTU", 1055.06, UnitType.ENERGY)
    WATT_HOUR = Unit("quilowatt-hour", "quilowatt-hora", "kWh", 3.6e3, UnitType.ENERGY)
    KILOWATT_HOUR = Unit("quilowatt-hour", "quilowatt-hora", "kWh", 3.6e6, UnitType.ENERGY)
    MEGAWATT_HOUR = Unit("quilowatt-hour", "quilowatt-hora", "kWh", 3.6e9, UnitType.ENERGY)
    GIGAWATT_HOUR = Unit("quilowatt-hour", "quilowatt-hora", "kWh", 3.6e12, UnitType.ENERGY)
    ERG = Unit("erg", "erg", "erg", 1e-7, UnitType.ENERGY)
    ELECTRON_VOLT = Unit("electron-volt", "elétron-volt", "eV", 1.60218e-19, UnitType.ENERGY)

    WATT = Unit("watt", "watt", "W", 1, UnitType.POWER)
    KILOWATT = Unit("kilowatt", "quilowatt", "kW", 1000, UnitType.POWER)
    HORSE_POWER = Unit("horse-power", "cavalo", "hp", 745.7, UnitType.POWER)
    BTU_PER_HOUR = Unit("BTU per hour", "BTU por hora", "BTU/h", 0.293071, UnitType.POWER)

    
    @staticmethod
    def get_units_of(utype):
        if isinstance(utype, str):
            utype_enum = UnitType.get_unit_type_by_name(utype)
        elif isinstance(utype, UnitType):
            utype_enum = utype
        else:
            raise ValueError("Invalid unit type passed to get_units_of method in UnitsTable Class")
        return [unit.value for unit in UnitsTable if unit.value.get_unit_type() == utype_enum]


    @staticmethod
    def get_unit_by_lang_and_name(lang, name):
        """
        Searchs for the passed string instance "name" in each
        UnitType enumerator value, despite its language, returning
        the respective enum value according to the said name.
        """
        for u in UnitsTable:
            if u.value.get_name(lang) == name:
                return u

            
    @staticmethod
    def get_tkVar_names(lang, utype):
        """
        Returns an iterable tkinter Variable instance with all the unit names
        (e.g. meter, inch), according to the unit type (e.g. length, time)
        and lang passed, to be used in tkinter Listbox instances.
        """
        list_for_var = [unit.get_name(lang) for unit in UnitsTable.get_units_of(utype)]
        return tk.Variable(value = list_for_var)


    @staticmethod
    def convert_units(value: float, original_unit, desired_unit):
        """
            Returns the value of the original unit converted to the desired one.
            Assumes that an International Standard Unit has an unitary conversion factor,
            as well as the quantities aren't temperatures.
        """
        if original_unit.value.get_unit_type() != desired_unit.value.get_unit_type():
            raise AttributeError

        try:
            if original_unit.value.get_conversion_factor() == 1:
                return value / desired_unit.value.get_conversion_factor()
            elif desired_unit.value.get_conversion_factor() == 1:
                return value * original_unit.value.get_conversion_factor()
            else:
                return value * original_unit.value.get_conversion_factor() / desired_unit.value.get_conversion_factor()
        except Exception as e:
            print(f'{e}')
