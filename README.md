DigiTecK3D Procedural Shader Library
Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
=====================================================================================  
                      	
Author: Miguel A Santiago Jr.       	
Web: www.digiteck3d.com				
Email: miguel@digiteck3d.com
    		
License: ============================================================================

This program is free software: you can redistribute it and/or modify it under the terms 
of the GNU General Public License as published by the Free Software Foundation, either 
version 3 of the License, or (at your option) any later version.										
																			
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.								
																			
You should have received a copy of the GNU General Public License along with this program.  
If not, see <http://www.gnu.org/licenses/>.

Info: =============================================================================== 

This is an implementation of the Worley cellular noise function normally found in all 
CG procedural shading packages. The current implementation will output F1, F2, F2-F1, 
F1*F2, and F1+F2/2. F1 or Feature 1 which are the cells and F2 or Feature 2 which are 
the cell cracks. Along with the output type you can set the various distance types 
associated with Voronoi diagram distance types. It supports the Real distance, 
Squared distance, Manhattan distance, Chessboard distance, and the Chebychev distance 
type. Its fully integrated into the blending modes of Mari so it can be blended down 
into various other shader modules or even baked down into texture for output.

Installation: =======================================================================

Take scripts and put them into your user preference script directory. Or any startup
script path that Mari has set. Once these are in place, Mari on startup will run through
the scripts folder and load the procedural library. Going to the Python tab and showing
the console will allow you to see the modules loading up. This is where if in any case
the loading fails it will let you know. 

Example:
	• On Linux: /Mari/Scripts/
	• On Windows: Documents/Mari/Scripts/	

History: ============================================================================

10/15/13
-Initial release of the Mari Procedural Library.

Credits: ============================================================================


 
        