DigiTecK3D Procedural Shader Library
=====================================================================================
Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
                      	
Author: Miguel A Santiago Jr.       	
Web: www.digiteck3d.com				
Email: miguel@digiteck3d.com
    		
License
-----------------

This program is free software: you can redistribute it and/or modify it under the terms 
of the GNU General Public License as published by the Free Software Foundation, either 
version 3 of the License, or (at your option) any later version.										
																			
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.								
																			
You should have received a copy of the GNU General Public License along with this program.  
If not, see <http://www.gnu.org/licenses/>.

Info
-----------------

This is a Mari procedural library that adds new procedural types like Cellular, Gabor, 
Perlin, Value, Simplex, Brownian, Turbulence, Inigo Multi-Fractal, Ridged Fractal noise and 
more planned for the future. This isn't simply just a shader library that adds new nodes 
to Mari, but overall adds new functionality to the shader API that other shader writers 
can access and modify to create there own shaders from the various new noise functions 
added in code to the Mari shader API. Currently the library adds a totally new GPU 
noise library from the great work of Brian Sharpe, which is far more efficient and accurate 
than the standard noise library. This is the core of the library that allows to implement 
various other standard noise functions that are normally found in basic procedural libraries. 
The library also finally adds back in the full featured cellular noise function with various 
feature sets to mimic organic cellular patterns. Along with these new additions the library 
also introduces a port of the Gabor noise function into the library, This is a special type 
of noise with anisotropic noise properties.

Best of all the library will fall into the open source domain under the GNU General Public 
License and will include all of the source code for you to modify, learn, or just continue 
to improve and add to it yourself. So you are free to do with it what you will.

Installation
-----------------

Take scripts and put them into your user preference script directory. Or any startup
script path that Mari has set. Once these are in place, Mari on startup will run through
the scripts folder and load the procedural library. Going to the Python tab and showing
the console will allow you to see the modules loading up. This is where if in any case
the loading fails it will let you know. 

Example:
	• On Linux: /Mari/Scripts/
	• On Windows: Documents/Mari/Scripts/	

History
-----------------

10/15/13
-Initial release of the Mari Procedural Library.

Credits
-----------------


 
        