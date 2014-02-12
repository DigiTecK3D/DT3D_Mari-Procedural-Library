# ------------------------------------------------------------------------------
# Mari Shader Library Registration Master
# Copyright (c) 2013 DigiTecK3D. All Rights Reserved.
# ------------------------------------------------------------------------------
# Author: Ben Neall
# Web: www.bneall.blogspot.com
# Email: bneall@gmail.com
# Master Git: https://github.com/bneall/bnMariTools/tree/master/misc
# ------------------------------------------------------------------------------
# Contributors:
# Author: Miguel A Santiago Jr.
# Web: www.digiteck3d.com
# Email: miguel@digiteck3d.com
# Master Git: https://github.com/DigiTecK3D/DT3D_Mari-Procedural-Library
# ------------------------------------------------------------------------------
# History:
# - 02/04/14    New Auto-Loader Script Intergration.
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
import os
import glob
import xml.etree.ElementTree as ET

# global variables
base_path = os.path.dirname(__file__)
default_shader_path = '%s/NodeLibrary' % base_path
default_lib_path = '%s/FunctionLibrary' % base_path
lib_version = '1.06'
min_mari_version = '2.5'
current_mari_version = '2.5'

def mariVersion():
    '''Loads current mari version'''

    # grab our global variable
    global current_mari_version

    current_mari_version = '%d.%d' % (mari.app.version().major(), mari.app.version().minor())

def libNamerNode():
    '''Check to see if library renamer is in place'''

    # check to see if library is in path
    libNamer = os.path.isfile(default_lib_path + "/LibraryNamer.xml")
    if libNamer: # found library parse xml file
        xml = ET.parse('%s/%s' % (default_lib_path, "LibraryNamer.xml"))
        root = xml.getroot()

    return (libNamer,root) # return check, xml root
        
def libVersion():
    '''Loads current library version'''

    # grab our global variable
    global default_lib_version

    # run check and grab xml
    libNamer, root = libNamerNode()

    # if check grab version
    if libNamer: 
        # check for lib version in xml
        libVersion = root.find("LibraryVersion")
        if libVersion != None: 
            # lib xml version found
            default_lib_version = libVersion.text
            # print '-----------------------------------------'
            # print 'Library Version Found v' + (default_lib_version)
        else: 
            # lib version min default
            print '-----------------------------------------'
            print 'Library Version Not Set'
            print 'Using Min Version v' + (default_lib_version)

def loadLibraries():
    '''Loads custom shader libraries'''

    # run check and grab xml
    libNamer, root = libNamerNode()

    # find the library paths
    libDict = {}
    for path, subdirs, files in os.walk(default_lib_path):
        for name in files:
            libDict[name]=path

    # find the library paths for the libraries
    for lib in libDict:
        full_lib_path = libDict[lib]
        libPath = '%s/%s' % (full_lib_path, lib)
        libPath = libPath.replace("\\", "/")
        libNode = lib.split(".")[0]

        # if namer in place grab register names
        if libNamer:
            # check for matching node name
            libXml = root.find('%s' % (libNode))
            if libXml != None:
                # grab our node register name
                libName = libXml.text
            else:
                # default to file name
                libName = libNode
        else:
            # no namer file default file name
            libName = libNode

        # grad our function library header and source
        # files so we can load them up
        try:
            if lib.endswith('glslh'):
            	# function library glsl header file
                mari.gl_render.registerCustomHeaderFile(libNode, libPath)
            elif lib.endswith('glslc'):
            	# function library glsl source file
                mari.gl_render.registerCustomCodeFile(libNode, libPath)
                print 'Registered Library: %s' % libName
        except Exception as exc:
                print 'Error Registering Library: %s : %s' % (libName, str(exc))

def loadShaders():
    '''Loads custom shaders'''

    # find shaders
    shaderDict = {}
    for path, subdirs, files in os.walk(default_shader_path):
        for name in files:
            shaderDict[name]=path

    # storage for our found nodes to call in order later
    nodePs, nodeAd, nodeDf, nodeSp, nodeSt = [], [], [], [], []

    # determine attributes
    for shader in shaderDict: 
        full_shader_path = shaderDict[shader]
        xml = ET.parse('%s/%s' % (full_shader_path, shader))
        root = xml.getroot()

        # check for the name id tag
        shaderName = root.find('ID')
        # check to see if tag is set
        if shaderName != None:
            # grab our xml set name
            shaderName = shaderName.text
        else:
            # no id name set in node
            print 'XML Name Not Set'

        # assume all default procedural type
        shaderType = 'Procedural'
        # look into the default xml tag setup
        # if present and figure out node type
        for xmlTag in root.findall('Tags'):
            # find all of the child tag
            for xmlTagType in xmlTag.findall('Tag'):
                # found standalone shader
                if xmlTagType.text == '_standalone':
                    shaderType = 'Standalone'
                # found diffuse shader
                elif xmlTagType.text == '_diffuse':
                    shaderType = 'Diffuse'
                # found specular shader
                elif xmlTagType.text == '_specular':
                    shaderType = 'Specular'
                # found adjustment shader
                elif xmlTagType.text == '_adjustment':
                    shaderType = 'Adjustment'

        # if procedural or adjustment grab shader category info
        if shaderType == 'Procedural' or shaderType == 'Adjustment':
            # check for the category tag
	        shaderPath = root.find('Category')
            # check to see if tag is set
	        if shaderPath != None:
                # grab our xml set category
	            shaderPath = shaderPath.text + shaderName
	        else:
                # no category set in node
	            print 'XML Category Not Set'

	    # grab our node path to the shader
        nodePath = "%s/%s" % (full_shader_path, shader)
        nodePath = nodePath.replace("\\", "/")

        # grab our shader from our library and store
        # into our array so we can call them later
        try:
            if shaderType == 'Procedural':
            	# procedural node
                nodePs.append((shaderType,shaderName,shaderPath,nodePath))
            elif shaderType == 'Adjustment':
            	# adjustment node
                nodeAd.append((shaderType,shaderName,shaderPath,nodePath))
            elif shaderType == 'Diffuse':
            	# diffuse shader node
                nodeDf.append((shaderType,shaderName,nodePath))
            elif shaderType == 'Specular':
            	# specular shader node
                nodeSp.append((shaderType,shaderName,nodePath))
            elif shaderType == 'Standalone':
            	# standalone shader node
                nodeSt.append((shaderType,shaderName,nodePath))
        except Exception as exc:
            print 'Error Storing %s Node : %s : %s' % (shaderType, shaderName, str(exc))

    # check if list is not empty
    nodeSize = range(len(nodeAd))
    # if list load up
    if nodeSize:
        print '-----------------------------------------'
        print 'Adjustment Library : Loading'
        print '-----------------------------------------'
        for adjustments in nodeAd:
            try:
                mari.gl_render.registerCustomAdjustmentLayerFromXMLFile(adjustments[2],adjustments[3])
                print 'Registered %s Node: %s' % (adjustments[0], adjustments[1])
            except Exception as exc:
                print 'Error Registering %s Node : %s : %s' % (adjustments[0], adjustments[1], str(exc))
                print '-----------------------------------------'

    # check if list is not empty
    nodeSize = range(len(nodePs))
    # if list load up
    if nodeSize:
        print '-----------------------------------------'
        print 'Procedural Library : Loading'
        print '-----------------------------------------'
        for procedurals in nodePs:
            try:
                mari.gl_render.registerCustomProceduralLayerFromXMLFile(procedurals[2],procedurals[3])
                print 'Registered %s Node: %s' % (procedurals[0], procedurals[1])
            except Exception as exc:
                print 'Error Registering %s Node : %s : %s' % (procedurals[0], procedurals[1], str(exc))

    # check if list is not empty
    nodeSize = range(len(nodeDf))
    # if list load up
    if nodeSize:
        print '-----------------------------------------'
        print 'Diffuse Library : Loading'
        print '-----------------------------------------'
        for diffuse in nodeDf:
            try:
                mari.gl_render.registerCustomDiffuseShaderFromXMLFile(diffuse[1],diffuse[2])
                print 'Registered %s Node: %s' % (diffuse[0], diffuse[1])
            except Exception as exc:
                print 'Error Registering %s Node : %s : %s' % (diffuse[0], diffuse[1], str(exc))

    # check if list is not empty
    nodeSize = range(len(nodeSp))
    # if list load up
    if nodeSize:
        print '-----------------------------------------'
        print 'Specular Library : Loading'
        print '-----------------------------------------'
        for specular in nodeSp:
            try:
                mari.gl_render.registerCustomSpecularShaderFromXMLFile(specular[1],specular[2])
                print 'Registered %s Node: %s' % (specular[0], specular[1])
            except Exception as exc:
                print 'Error Registering %s Node : %s : %s' % (specular[0], specular[1], str(exc))

    # check if list is not empty
    nodeSize = range(len(nodeSt))
    # if list load up
    if nodeSize:
        print '-----------------------------------------'
        print 'Standalone Library : Loading'
        print '-----------------------------------------'
        for standalone in nodeSt:
            try:
                mari.gl_render.registerCustomStandaloneShaderFromXMLFile(standalone[1],standalone[2])
                print 'Registered %s Node: %s' % (standalone[0], standalone[1])
            except Exception as exc:
                print 'Error Registering %s Node : %s : %s' % (standalone[0], standalone[1], str(exc))

# check to make sure we meet the min mari version
mariVersion()

# if we meet the mari min version load library
if current_mari_version >= min_mari_version:
    # load all functions and shaders
    # Print our info into the console
    print ""
    libVersion() # call and check for library version
    print '-----------------------------------------'
    print "Mari Shader Library v" + lib_version
    print '-----------------------------------------'
    print "DigiTecK3D     : www.digiteck3d.com"
    print "Mari Ideascale : www.mari.ideascale.com"
    print '-----------------------------------------'
    print 'Functions Library : Loading'
    print '-----------------------------------------'
    loadLibraries() # load up our function library
    loadShaders() # load up our shader library
    print '-----------------------------------------'
    print ""

# ------------------------------------------------------------------------------
