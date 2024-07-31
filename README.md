# Kantele-program
The aim of this programme is to assist Kantele makers in their work by providing theoretical calculations to help them to dimension the strings they are going to use more easily.

# How it works ?

The program is consist of 4 parts : 
- Calcul on Preset Kantele
- Characteristic and caculation on one string
- Informations about strings
- Display of length of strings

## Preset Kantele
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/PresetKantele.PNG" width="600" /></p> 
In this part, all the information about the string is already stored in the programme. The pitch, the number of strings and the diameter of the strings are already in the porgramme. You can choose the material of the strings, the tension of the strings and if you wish, set the same diameter for all the strings.
The formula used for the calculations comes from a ***D'Addario*** document [^1].

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
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Pourcentage_of_tension.PNG" width="400" /></p> 

You can choose to enter the tension of the string in Newton or choose the percentage of maximum tension.
If you select the option **"Percentage of max tension"** you must enter a number between 0 and 100 in the **"Tension"** field. The programme will calculate the maximum tension that the rope can be subjected to, based on the maximum strength of the material and the diameter of the rope. 
It will then takes the value of the percentage entered by the user and aoolies this percentage to the value of the maximum tension. 
> [!CAUTION]
> Keep a value between 35% and 85% because below 35% the tension will be too low and it will be difficult to play with this string, and above 85% the risk of breaking are high because with wear, the maximum tension it can withstand reduced.

When you click on the ***"Submit"*** button, all the information about the strings will be printed in the **"Information about strings"** section and the length of the strings will be displayed on the graph.

## Characteristic of the string
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Characteristic%20of%20the%20string.PNG" width="800" /></p>

In this section you can enter all the characteristics of your string and calculate the tension, or the diameter or the length of your string.
You can also choose if your string is wound or not and enter the note you want and the frequency of the reference note.
You can choose between 5 materials : Iron, Brass, Nylon, Gut and Carbon.
You can choose whether your string is wound or not. This will change the formula used to calculate the linear mass.

> [!CAUTION] 
> If your string have non-linear density this programme can't calculate its linear mass. 

After entering all characteristics of your string, you can clic the ***"Add String"*** button. This button will take all information about your string and stock it in table and display all informations in the ***"Information about strings"*** part. It also displays the length of the string on the graph. 
If you want to remove all the previous string, all you have to do is click on the ***"Clear#*** button and everything will disapear.

## Information about strings
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Informatiom%20about%20strings.PNG" width="1000" /></p>

This section displays all the information about your string. You have the length in meters, the tension in Newtons, the diameter in meters and the pitch of the string in Hz or it displays the note.

## Display of length of strings
<p align="center"><img src="https://github.com/JolanTho/Kantele-program/blob/main/Kantele_program_Pictures/Display%20of%20strings.PNG" width="600" /></p>

This part shows the length of the string to give an idea of the shape of the Kantele.

[^1]: https://www.daddario.com/globalassets/pdfs/accessories/tension_chart_13934.pdf
[^2]: https://balticpsalteries.com/
