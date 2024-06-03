# Kantele-program
The aim of this programme is to help Kantele manufacturers in their work by making theoretical calculations and thus enabling them to dimension the strings they are going to use more easily.

# How it works ?

The program is consist of 4 parts : 
- Calcul on Preset Kantele
- Characteristic and caculation on one string
- Informations about strings
- Display of length of strings

## Preset Kantele
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/PresetKantele.PNG" width="600" /></p> 

This part already have all the information about strings save in the program. The pitch, the number of strings et the diameter of the strings are already in the porgram. You can choose the materials of the string, the tension of the strings and if you want, put the same diameter for all the strings.
The formula used for the calculations come from a ***D'Addario*** document [^1].

### There are 4 Kantele in this program.

The fisrt one have 5 strings :
- Pitch: D4, E4, F4#, G4, A4.
- Diameter: 0.5mm, 0.45mm, 0.4mm, 0.4mm, 0.35mm.

The second one is a 11 strings Kantele :
- Pitch: A3, B3, C4#, D4, E4, F4#, G4, A4, B4, C5#, D5.
- Diameter: 0.55mm, 0.5mm, 0.45mm, 0.45mm, 0.4mm, 0.4mm, 0.35mm, 0.35mm, 0.3mm, 0.3mm, 0.3mm.

The third one is a 18 strings Kantele :
- Pitch: G3, A3, B3, C4, D4, E4, F4, G4, A4, B4, C5, D5, E5, F5, G5, A5, B5, C6.
- Diameter: 0.65mm, 0.55mm, 0.5mm, 0.5mm, 0.45mm, 0.45mm, 0.4mm, 0.4mm, 0.4mm, 0.35mm, 0.35mm, 0.35mm, 0.35mm, 0.3mm, 0.3mm, 0.25mm, 0.25mm, 0.25mm, 0.25mm.

The last one is a 26 strings Kantele :
- Pitch: C3, D3, E3, F3, G3, A3, B3, C4, D4, E4, F4, G4, A4, B4, C5, D5, E5, F5, G5, A5, B5, C6, D6, E6, F6, G6.
- Diameter: 0.9mm, 0.9mm, 0.75mm, 0.75mm, 0.75mm, 0.7mm, 0.7mm, 0.7mm, 0.65mm, 0.65mm, 0.65mm, 0.6mm, 0.6mm, 0.6mm, 0.55mm, 0.55mm, 0.55mm, 0.5mm, 0.5mm, 0.5mm, 0.45mm, 0.45mm, 0.45mm, 0.4mm, 0.4mm, 0.4mm.

Those Kantele are based on the kantele sale on the websitw Baltic psalteries [^2].
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Pourcentage_of_tension.PNG" width="600" /></p> 

You can choose to put the tension of the strings in Newton or choose the pourcentage of maximum tension.
When you select the option **"Pourcentage of max tension"** you must put a number between 0 and 100 in the box **"Tension"**. The programme will calculate the maximum tension the rope can be subjected to, based on the maximal strength of the material and the diameter of the rope. 
It will then take the value of the percentage entered by the user and take this percentage of the value of the maximum tension. 
> [!CAUTION]
> Keep a value between 35% and 85% because under 35% the tension will too low, so it will be difficult to play with this string and above 85% the risk of breaking are high because with the wear

When you clic on the Submit button all the informations of the strings are print in the **"Information about strings"** part and the length of the strings are display on the graph.

## Characteristic of the string
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Characteristic%20of%20the%20string.PNG" width="800" /></p>

In this part you can put every caracteristic of your string and calculate the tension, or the diameter or the length of your string.
You can also choose if your string is wounden or not and put the note you want and the frequencie of the reference note.
You can choose between 5 materials : Iron, Brass, Nylon, Gut and Carbon.
You can choose if you string is wound or not. It will change the formula to calculate the linear mass.

> [!CAUTION] 
> If your string have non linear density this programme can't calculate its linear mass. 

After enter all characteristic of your string you can clic the ***"Add String"*** button. This button take all informations about your string and stock it in table and display all informations in the ***"Information about strings"*** part. It also display le length of the string on the graph. 
If you want to remove all the previous string, all you have to do is click on the ***"Clear#*** button and everything disapear.

## Information about strings
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Informatiom%20about%20strings.PNG" width="1000" /></p>

This part display all information of your string. You have the length in meter, the tension in Newton, the Diameter in meter and the pitch of the string in Hz or it display the note.

## Display of length of strings
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Display%20of%20strings.PNG" width="600" /></p>

This part display the length of string to get an idea of the shape of the Kantele.

[^1]: https://www.daddario.com/globalassets/pdfs/accessories/tension_chart_13934.pdf
[^2]: https://balticpsalteries.com/
