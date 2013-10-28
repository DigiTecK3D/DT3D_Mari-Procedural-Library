# ------------------------------------------------------------------------------
# DigiTecK3D Procedural Shader Library Registration
# Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
# ------------------------------------------------------------------------------                         	
# Author: Miguel A Santiago Jr.       	
# Web: www.digiteck3d.com				
# Email: miguel@digiteck3d.com
# ------------------------------------------------------------------------------			                                   	
# Date: Oct 15, 2013	         		
# ------------------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify		
# it under the terms of the GNU General Public License as published by		
# the Free Software Foundation, either version 3 of the License, or		
# (at your option) any later version.										
#																			
# This program is distributed in the hope that it will be useful,			
# but WITHOUT ANY WARRANTY; without even the implied warranty of			
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the			
# GNU General Public License for more details.								
#																			
# You should have received a copy of the GNU General Public License		
# along with this program.  If not, see <http://www.gnu.org/licenses/>.	
# ------------------------------------------------------------------------------

import mari	

def registerGpuNoiseLibHeaderShader():
	"Register a new custom shader module that implements gpu noise lib"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("GPU_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/GpuNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("GPU_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/GpuNoiseLib.glslc")
		print 'Registered Header Module : GPU Noise Lib Header Files'
	except Exception as exc:
		print 'Error Registered Header Module : GPU Noise Lib Header Files : ' + str(exc)

def registerCellularNoiseHeaderShader():
	"Register a new custom shader module that implements cellular noise"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("DT3D_Cellular_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/CellularNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("DT3D_Cellular_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/CellularNoiseLib.glslc")
		print 'Registered Header Module : Cellular Header Files'
	except Exception as exc:
		print 'Error Registered Header Module : Cellular Header Files : ' + str(exc)

def registerGaborNoiseHeaderShader():
	"Register a new custom shader module that implements gabor noise"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("DT3D_Gabor_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/GaborNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("DT3D_Gabor_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/GaborNoiseLib.glslc")
		print 'Registered Header Module : Gabor Header Files'
	except Exception as exc:
		print 'Error Registered Header Module : Gabor Header Files : ' + str(exc)

def registerProceduralLibHeaderShader():
	"Register a new custom shader module that implements procedural noise lib"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("DT3D_Procedural_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/ProceduralLib.glslh")
		mari.gl_render.registerCustomCodeFile("DT3D_Procedural_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/FunctionLibrary/ProceduralLib.glslc")
		print 'Registered Header Module : Procedural Lib Header Files'
	except Exception as exc:
		print 'Error Registered Header Module : Procedural Lib Header Files : ' + str(exc)
		
# ------------------------------------------------------------------------------
		
def registerCellularNoiseShader():
	"Register a new custom shader module that implements cellular noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Cellular Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/CellularNoise.xml")
		print 'Registered Shader Module : Cellular Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Cellular Noise : ' + str(exc)

def registerGaborNoiseShader():
	"Register a new custom shader module that implements gabor noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Gabor Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/GaborNoise.xml")
		print 'Registered Shader Module : Gabor Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Gabor Noise : ' + str(exc)

def registerPerlinNoiseShader():
	"Register a new custom shader module that implements perlin noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Perlin Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/PerlinNoise.xml")
		print 'Registered Shader Module : Perlin Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Perlin Noise : ' + str(exc)

def registerBrownianNoiseShader():
	"Register a new custom shader module that implements brownian noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Brownian Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/BrownianNoise.xml")
		print 'Registered Shader Module : Brownian Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Brownian Noise : ' + str(exc)
		
def registerTurbulenceNoiseShader():
	"Register a new custom shader module that implements Turbulence noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Turbulence Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/TurbulenceNoise.xml")
		print 'Registered Shader Module : Turbulence Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Turbulence Noise : ' + str(exc)
		
def registerInigoNoiseShader():
	"Register a new custom shader module that implements Inigo noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Inigo Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/InigoMultiNoise.xml")
		print 'Registered Shader Module : Inigo Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Inigo Noise : ' + str(exc)
		
def registerRidgedNoiseShader():
	"Register a new custom shader module that implements Ridged noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/DT3D/Ridged Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/DT3D_ShaderLibrary/Nodes/RidgedMultiNoise.xml")
		print 'Registered Shader Module : Ridged Noise'
	except Exception as exc:
		print 'Error Registering Shader Module : Ridged Noise : ' + str(exc)
		
# ------------------------------------------------------------------------------

# Print info into the console
print "DT3D Mari Procedural Library"		
print "DigiTecK3D : www.digiteck3d.com"
print 'Procedural Library : Loading'

# Read in all of the source from the string
registerGpuNoiseLibHeaderShader()

# Read in all of the source from the string
registerCellularNoiseHeaderShader()

# Read in all of the source from the string
registerGaborNoiseHeaderShader()

# Read in all of the source from the string
registerProceduralLibHeaderShader()

# Read in all of the source from the string
registerCellularNoiseShader()

# Read in all of the source from the string
registerGaborNoiseShader()

# Read in all of the source from the string
registerPerlinNoiseShader()

# Read in all of the source from the string
registerBrownianNoiseShader()

# Read in all of the source from the string
registerTurbulenceNoiseShader()

# Read in all of the source from the string
registerInigoNoiseShader()

# Read in all of the source from the string
registerRidgedNoiseShader()