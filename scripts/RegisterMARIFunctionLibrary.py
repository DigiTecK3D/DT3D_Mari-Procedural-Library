# ------------------------------------------------------------------------------
# MARI Function Library Registration v1.06
# Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
# ------------------------------------------------------------------------------
# Author: Miguel A Santiago Jr.
# Web: www.digiteck3d.com
# Email: miguel@digiteck3d.com
# Master Git: https://github.com/DigiTecK3D/DT3D_Mari-Procedural-Library
# ------------------------------------------------------------------------------
# Contributors:
# Author: Jens Kafitz | Mari Ideascale
# Web: www.campi3d.com
# Web: www.mari.ideascale.com
# Email: info@campi3d.com
# Git Branch: https://github.com/campi3d/DT3D_Mari-Procedural-Library
# ------------------------------------------------------------------------------
# History:
# - 10/15/13	V1.0  Release of DT3D procedural shader library.
# - 12/14/13	V1.06 Release of procedural function library,
# 					  Restructure of library for global development library,
# 					  Fixed bug in vec4 softthreshold function.
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

def registerBS_GpuNoiseLibHeaderShader():
	"Register a new custom shader module that implements gpu noise lib"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("BS_GPU_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("BS_GPU_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc")
		print 'Registered Library : Brian Sharpe GPU Noise Lib'
	except Exception as exc:
		print 'Error Registered Library : Brian Sharpe GPU Noise Lib : ' + str(exc)

def registerDT3D_CellularNoiseHeaderShader():
	"Register a new custom shader module that implements cellular noise"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("DT3D_Cellular_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/DT3D_CellularNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("DT3D_Cellular_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/DT3D_CellularNoiseLib.glslc")
		print 'Registered Library : DT3D Cellular Lib'
	except Exception as exc:
		print 'Error Registered Library : DT3D Cellular Lib : ' + str(exc)

def registerAlGaborNoiseHeaderShader():
	"Register a new custom shader module that implements gabor noise"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("AL_Gabor_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/AL_GaborNoiseLib.glslh")
		mari.gl_render.registerCustomCodeFile("AL_Gabor_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/AL_GaborNoiseLib.glslc")
		print 'Registered Library : Anders Langlands Gabor Lib'
	except Exception as exc:
		print 'Error Registered Library : Anders Langlands Gabor Lib : ' + str(exc)

def registerDT3D_ProceduralLibHeaderShader():
	"Register a new custom shader module that implements procedural noise lib"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("DT3D_Procedural_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslh")
		mari.gl_render.registerCustomCodeFile("DT3D_Procedural_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc")
		print 'Registered Library : DT3D Procedural Lib'
	except Exception as exc:
		print 'Error Registered Library : DT3D Procedural Lib : ' + str(exc)

def registerID_ProceduralLibHeaderShader():
	"Register a new custom shader module that implements procedural noise lib"
	# Register the code as glsl header and source files
	try:
		mari.gl_render.registerCustomHeaderFile("ID_Procedural_Noise_Header", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslh")
		mari.gl_render.registerCustomCodeFile("ID_Procedural_Noise_Source", mari.resources.path(mari.resources.USER_SCRIPTS) + "/FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc")
		print 'Registered Library : Ideascale Procedural Lib'
	except Exception as exc:
		print 'Error Registered Library : Ideascale Procedural Lib : ' + str(exc)

# ------------------------------------------------------------------------------
