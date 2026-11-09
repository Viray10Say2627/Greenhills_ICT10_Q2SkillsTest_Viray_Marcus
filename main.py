# Q2 Skills Test
from pyscript import display, document


non_metals = {

    "H":{
    'Atomic Number': '1',
    'Element': 'Hydrogen',
    'Symbol': 'H',
    'Atomic Mass': '1.008',
    },

    "He":{
    'Atomic Number': '2',
    'Element': 'Helium',
    'Symbol': 'He',
    'Atomic Mass': '4.0026',
    },

    "C":{
    'Atomic Number': '6',
    'Element': 'Carbon',
    'Symbol': 'C',
    'Atomic Mass': '12.011',
    },

    "N":{
    'Atomic Number': '7',
    'Element': 'Nitrogen',
    'Symbol': 'N',
    'Atomic Mass': '14.007',
    },

    "F":{
    'Atomic Number': '9',
    'Element': 'Fluorine',
    'Symbol': 'F',
    'Atomic Mass': '18.998',
    },

    "Ne":{
    'Atomic Number': '10',
    'Element': 'Neon',
    'Symbol': 'Ne',
    'Atomic Mass': '20.180',
    },

    "P":{
    'Atomic Number': '15',
    'Element': 'Phosphorus',
    'Symbol': 'P',
    'Atomic Mass': '30.974',
    },

    "S":{
    'Atomic Number': '16',
    'Element': 'Sulfur',
    'Symbol': 'S',
    'Atomic Mass': '32.06',
    },

    "Cl":{
    'Atomic Number': '17',
    'Element': 'Chlorine',
    'Symbol': 'Cl',
    'Atomic Mass': '35.45',
    },

    "Ar":{
    'Atomic Number': '18',
    'Element': 'Argon',
    'Symbol': 'Ar',
    'Atomic Mass': '39.948',
    },

    "Se":{
    'Atomic Number': '34',
    'Element': 'Selenium',
    'Symbol': 'Se',
    'Atomic Mass': '78.971',
    },

    "Br":{
    'Atomic Number': '35',
    'Element': 'Bromine',
    'Symbol': 'Br',
    'Atomic Mass': '79.904',
    },

    "Kr":{
    'Atomic Number': '36',
    'Element': 'Krypton',
    'Symbol': 'Kr',
    'Atomic Mass': '83.798',
    },

    "I":{
    'Atomic Number': '53',
    'Element': 'Iodine',
    'Symbol': 'I',
    'Atomic Mass': '126.904',
    },

    "Xe":{
    'Atomic Number': '54',
    'Element': 'Xenon',
    'Symbol': 'Xe',
    'Atomic Mass': '131.293',
    },

    "Rn":{
    'Atomic Number': '86',
    'Element': 'Radon',
    'Symbol': 'Rn',
    'Atomic Mass': '222',
    },

    "O":{
    'Atomic Number': '8',
    'Element': 'Oxygen',
    'Symbol': 'O',
    'Atomic Mass': '15.999',
    },

}

def element(e):
    symbol = document.getElementById('input1').value().strip().capitalize()
    document.getElementById('result').innerHTML = ''

    details = non_metals.get(symbol, {'Error': 'Not a recognized non-metal symbol'})

    for label, value in details.items():
        display(f"{label}: {value}", target='result')