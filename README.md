This programm is meant to be used for rodbuilding
  It calculates measurements for Fishing-Rods

main.py starts a GUI window based on the PySide6 Framework (Copyright © The Qt Company).

Using the:
  - Rodlength-dial  -- for adjusting the rodlength
  - Ringcount-dial  -- for adjusting number of rings
  - Modifier-slider -- for adjusting the gap relation
   
   You can tweak around and adjust your measurements.
   A small graphic will be displayed as soon as you provide
   a Rodlenght and Rings, via the Modifier you are able to
   change the relation of the gaps between the rings.

   A higher Modifier will shift the rings more to the tip
       wich may be better for fast or short blanks 
   A lower modifier will place the rings much more even 
       wich may be better for slow or long blanks

 <img width="690" height="816" alt="Rodbuilding-Calculator" src="https://github.com/user-attachments/assets/96d6b562-be6a-4b5b-924b-f9f87866bf05" />
 
 The programm will also calculate the following measurements:

   - position for the center of the reel_seat 
   - position for the start_ring from bottom up
   - length of the ringed section
   - gaps between the rings, from the tip to startring
           and with it their exact position.
           You measure from each ring to the next one:
             {"Ring 1":0:0, "Ring 2: 8.75","Ring 3": 12.50}
                             **means**
             | Tip-Ring--> 8.75 -->Ring 2--> 12.50 -->Ring 3
    
     ****All measurements are in Centimeters****

 The programm will automaticaly create or overwrite an 
 existing Rod_Specs.txt file, with your last setup,
 listing all measurements.
 
 
<img width="1598" height="207" alt="Rodbuilding-Output" src="https://github.com/user-attachments/assets/96d64f4a-3df2-483c-8773-85596d7f2a8d" />


If you don't want to use the GUI you could just use blank_separator.py in the utils directory.
Just uncomment the bottom lines and adjusting it as needed.

Author: Jens Michalik     E-Mail: vox288@gmail.com

This project is licensed under the MIT License

This application uses PySide6 (Copyright © The Qt Company),
licensed under the GNU Lesser General Public License (LGPL) version 3.
The source code of PySide6 is available at www.qt.io.
