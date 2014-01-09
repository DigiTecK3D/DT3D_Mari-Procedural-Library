# ------------------------------------------------------------------------------
# Requirements: This Node Library requires DT3D_FunctionLibary 1.0
# Available at: https://github.com/DigiTecK3D/DT3D_Mari-Procedural-Library
# ------------------------------------------------------------------------------
# DigiTecK3D Procedural Node Registration
# Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
# ------------------------------------------------------------------------------
# Author: Miguel A Santiago Jr.
# Web: www.digiteck3d.com
# Email: miguel@digiteck3d.com
# Master Git: https://github.com/DigiTecK3D/DT3D_Mari-Procedural-Library
# ------------------------------------------------------------------------------
# History:
# - 10/15/13	Release 1.0 of DT3D Procedural Node Library
# - 12/14/13	Release of 1.06 of DT3D Procedural Node Library
#				Final Python and Folder Structure for mari.ideascale.com
#				Exponential Frequency Growth
#				Flow Paintable Gabor Noise
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

def registerCellularNoiseShader():
	"Register a new custom shader module that implements cellular noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/Voronoi/Cellular Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/Noise/DT3D_CellularNoise.xml")
		print 'Registered Procedural Node : Cellular Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node: Cellular Noise : ' + str(exc)

def registerGaborNoiseShader():
	"Register a new custom shader module that implements gabor noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomAdjustmentLayerFromXMLFile("/Custom/Paintable Gabor Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/Noise/DT3D_GaborNoise.xml")
		print 'Registered Procedural Node : Paintable Gabor Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Paintable Gabor Noise : ' + str(exc)

def registerPerlinNoiseShader():
	"Register a new custom shader module that implements perlin noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/Noise/Perlin Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/Perlin/DT3D_PerlinNoise.xml")
		print 'Registered Procedural Node : Perlin Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Perlin Noise : ' + str(exc)

def registerBrownianNoiseShader():
	"Register a new custom shader module that implements brownian noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/FBM/Brownian Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/FBM/DT3D_BrownianNoise.xml")
		print 'Registered Procedural Node : Brownian Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Brownian Noise : ' + str(exc)

def registerTurbulenceNoiseShader():
	"Register a new custom shader module that implements Turbulence noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/Noise/Turbulence Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/Perlin/DT3D_TurbulenceNoise.xml")
		print 'Registered Procedural Node : Turbulence Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Turbulence Noise : ' + str(exc)

def registerInigoNoiseShader():
	"Register a new custom shader module that implements Inigo noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/Noise/Inigo Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/Perlin/DT3D_InigoMultiNoise.xml")
		print 'Registered Procedural Node : Inigo Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Inigo Noise : ' + str(exc)

def registerRidgedNoiseShader():
	"Register a new custom shader module that implements Ridged noise"
	# Register the code as a new custom shader module
	try:
		mari.gl_render.registerCustomProceduralLayerFromXMLFile("Procedural/Custom/MultiFractal/Ridged Noise",mari.resources.path(mari.resources.USER_SCRIPTS) + "/NodeLibrary/Procedurals/MultiFractal/DT3D_RidgedMultiNoise.xml")
		print 'Registered Procedural Node : Ridged Noise'
	except Exception as exc:
		print 'Error Registered Procedural Node : Ridged Noise : ' + str(exc)

# ------------------------------------------------------------------------------