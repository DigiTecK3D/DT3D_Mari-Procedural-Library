# ------------------------------------------------------------------------------
# Mari Procedural Shader Library Registration Master
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
# - 10/15/13	V1.0  Release of Procedural Function Library.
# - 12/13/13	V1.06 Restructure of library to be friendlier for development with Mari Ideascale,
# 					  Intergration of Ideascale library for node development.
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

# Import modules to register in order
# Register main functions library
# ------------------------------------------------------------------------------
import RegisterMARIFunctionLibrary

# Import modules to register in order
# Register adjustment layers
# ------------------------------------------------------------------------------
# import RegisterGradePlus
# import RegisterNormalMapIntensity
# import RegisterNormalMapMerge
# import RegisterSetRange
# import RegisterSpotify
# import RegisterThreshold
# import RegisterVibrance

# Import modules to register in order
# Register geometery nodes
# ------------------------------------------------------------------------------
# import RegisterCustomObjectNormal
# import RegisterPolysurfaceCurvature

# Import modules to register in order
# Register procedural nodes
# ------------------------------------------------------------------------------
# import RegisterCamoProcedural
import RegisterDT3DNodeLibrary
# import RegisterFBMPackA
# import RegisterProceduralOptionsPackA

# ------------------------------------------------------------------------------
# Console printing credits information

# Print info into the console
print "Mari Function Library v1.06"
print "Mari Ideascale : www.mari.ideascale.com"
print "--------------------------------"
print "DT3D Mari Procedural Library v1.06"
print "DigiTecK3D : www.digiteck3d.com"
print "--------------------------------"
print 'Functions Library : Loading'

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Main function library

# Call register function from module
RegisterMARIFunctionLibrary.registerAlGaborNoiseHeaderShader()

# Call register function from module
RegisterMARIFunctionLibrary.registerBS_GpuNoiseLibHeaderShader()

# Call register function from module
RegisterMARIFunctionLibrary.registerDT3D_CellularNoiseHeaderShader()

# Call register function from module
RegisterMARIFunctionLibrary.registerDT3D_ProceduralLibHeaderShader()

# Call register function from module
RegisterMARIFunctionLibrary.registerID_ProceduralLibHeaderShader()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Adjustment layers

print "--------------------------------"
print 'Adjustment Library : Loading'

# Call register function from module
# RegisterGradePlus.registerGradePlus()

# Call register function from module
# RegisterNormalMapMerge.registerNormalMapMerge()

# Call register function from module
# RegisterNormalMapIntensity.registerNormalMapIntensity()

# Call register function from module
# RegisterSetRange.registerSetRange()

# Call register function from module
# RegisterVibrance.registerVibrance()

# Call register function from module
# RegisterThreshold.registerThreshold()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Geometery Nodes

print "--------------------------------"
print 'Geometery Library : Loading'

# Call register function from module
# RegisterCustomObjectNormal.registerCustomObjectNormal()

# Call register function from module
# RegisterPolysurfaceCurvature.RegisterPolysurfaceCurvature()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Procedural Nodes

print "--------------------------------"
print 'Procedural Library : Loading'

# Call register function from module
# RegisterCamoProcedural.registerCamoProcedural()

# ------------------------------------------------------------------------------

# Call register function from module
RegisterDT3DNodeLibrary.registerCellularNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerGaborNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerPerlinNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerBrownianNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerTurbulenceNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerInigoNoiseShader()

# Call register function from module
RegisterDT3DNodeLibrary.registerRidgedNoiseShader()

# ------------------------------------------------------------------------------

# Call register function from module
# RegisterFBMPackA.registerFBMPackA_fbm()

# Call register function from module
# RegisterFBMPackA.registerFBMPackA_multifbm()

# Call register function from module
# RegisterFBMPackA.registerFBMPackA_Vfbm()

# ------------------------------------------------------------------------------

# Call register function from module
# RegisterProceduralOptionsPackA.registerProceduralOptionsPackA_Cellular()

# Call register function from module
# RegisterProceduralOptionsPackA.registerProceduralOptionsPackA_Turbulence()

# Call register function from module
# RegisterProceduralOptionsPackA.registerProceduralOptionsPackA_Squiggle()

# Call register function from module
# RegisterProceduralOptionsPackA.registerProceduralOptionsPackA_Perlin()

# Call register function from module
# RegisterProceduralOptionsPackA.registerProceduralOptionsPackA_Cloud()

# ------------------------------------------------------------------------------

# Call register function from module
# RegisterSpotify.registerSpotify()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# End cap console print

print "--------------------------------"
print ""

# ------------------------------------------------------------------------------

