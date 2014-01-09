// MARI FUNCTION LIB 1.06

// ---------------------------------------------
// ---------------------------------------------
// OVERVIEW OVER CONTENTS OF MARI FUNCTION LIBRARY
// Each Function has a short description, a reference to 
// the source file it lives in and hints/descriptions
// you might need to understand its functionality
// ---------------------------------------------
// ---------------------------------------------

// ---------------------------------------------
// CONTENT:
// 
// 1) Noise Functions
// 2) multiFractal Functions
// 3) Voronoi Functions
// 4) Gabor Noise Functions
// 6) Vector/Position Modification Functions
// 7) Value Functions
// 8) Value Interpolation Functions
// ---------------------------------------------









// ---------------------------------------------
// ---------------------------------------------
// Noise Functions
// ---------------------------------------------
// ---------------------------------------------


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Noise type picker function
//   Noise is all returned in signed form -1,1
//   returns type = 0:value,1:perlin,2:simplex,3:hermite
//
float NoiseType(vec3 p, int type);


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//	 Value Noise 3D
//   Return value range of -1.0->1.0
//   http://briansharpe.files.wordpress.com/2011/11/valuesample1.jpg
//
float Value3D( vec3 P );

//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Perlin Noise 3D  ( gradient noise )
//   Return value range of -1.0->1.0
//   http://briansharpe.files.wordpress.com/2011/11/perlinsample.jpg
//
float Perlin3D( vec3 P );


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   SimplexPerlin3D  ( simplex gradient noise )
//   Perlin noise over a simplex (tetrahedron) grid
//   Return value range of -1.0->1.0
//   http://briansharpe.files.wordpress.com/2012/01/simplexperlinsample.jpg
//
//   Implementation originally based off Stefan Gustavson's and Ian McEwan's work at...
//   http://github.com/ashima/webgl-noise
//
float SimplexPerlin3D(vec3 P);


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Hermite3D
//   Return value range of -1.0->1.0
//   http://briansharpe.files.wordpress.com/2012/01/hermitesample.jpg
//
float Hermite3D( vec3 P );


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Value3D_Deriv
//   Value3D noise with derivatives
//   returns vec3( value, xderiv, yderiv, zderiv )
//
vec4 Value3D_Deriv( vec3 P );


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   PerlinSurflet3D_Deriv
//   Perlin Surflet 3D noise with derivatives
//   returns vec4( value, xderiv, yderiv, zderiv )
//
vec4 PerlinSurflet3D_Deriv( vec3 P );


//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Hermite3D_Deriv
//   Hermite3D noise with derivatives
//   returns vec3( value, xderiv, yderiv, zderiv )
//
vec4 Hermite3D_Deriv( vec3 P );

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// vector noise function range of -1.0->1.0
vec3 vnoise(vec3 P);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// fractional Brownian motion
// Inputs: 
// p              position and approximate inter-pixel spacing
// octaves        max # of octaves to calculate
// lacunarity     frequency spacing between successive octaves
// gain           scaling factor between successive octaves
//
float fBm(vec3 p, int octaves = 4, float lacunarity = 2.0, float gain = 0.5);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// turbulence 
// Inputs: 
// p              position and approximate inter-pixel spacing
// octaves        max # of octaves to calculate
// lacunarity     frequency spacing between successive octaves
// gain           scaling factor between successive octaves
//
float turbulence(vec3 p, int octaves = 4, float lacunarity = 2.0, float gain = 0.5);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// perlin noise
vec4 DT3D_PerlinNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, float threshold, bool invert, int unsign, int modSet);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// turbulence fractal noise
vec4 DT3D_TurbNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, int octaves, float lacunarity, float gain, float threshold, bool invert);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// vector-valued Perlin noise on 3-D domain.
float vsnoise(vec3 p);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// The stuff that Ken Musgrave calls "VLNoise"
float VLNoise (vec3 Pt, float scale);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// brownian fractal noise
vec4 DT3D_fBmNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, int octaves, float lacunarity, float gain, float threshold, bool invert);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// A Variation of FBM without hardcoded values and added functionality
float rmfBm (vec3 P, float octaves, float lacunarity, float gain, float amp, float freqOffset);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// A Variation of FBM without hardcoded values and added functionality
// Most incoming values are smoothed so this function is suitable for non-constant in-values.
float smoothfBm (vec3 P, float octaves, float lacunarity, float gain, float amp, float freqOffset);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// A Variation of Vector FBM without hardcoded values and added functionality
// Most incoming values are smoothed so this function is suitable for non-constant in-values.
float smoothVfBm (vec3 P, float octaves, float lacunarity, float gain, float amp, float scale, float freqOffset);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// A Variation of Vector FBM, generally with better performance but different results than smoothVfbm
float VLfBm (vec3 P, float octaves, float lacunarity, float gain, float amp, float scale);













// ---------------------------------------------
// ---------------------------------------------
// multiFractal Functions
// ---------------------------------------------
// ---------------------------------------------


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// inigo multi-fractal
// Inputs: 
// p              position and approximate inter-pixel spacing
// octaves        max # of octaves to calculate
// lacunarity     frequency spacing between successive octaves
// gain           scaling factor between successive octaves
//
float iqmf(vec3 p, int octaves = 4, float lacunarity = 2.0, float gain = 0.5);




//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// ridged multi-fractal
// Inputs: 
// p              position and approximate inter-pixel spacing
// octaves        max # of octaves to calculate
// lacunarity     frequency spacing between successive octaves
// gain           scaling factor between successive octaves
// offset         a factor to offset the octaves
//
float ridgedmf(vec3 p, int octaves = 4, float lacunarity = 2.0, float gain = 0.5, float offset = 1.0);


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// inigo multi fractal noise
vec4 DT3D_InigoNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, int octaves, float lacunarity, float gain, float threshold, bool invert);

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// ridged multi fractal noise
vec4 DT3D_RidgedNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, int octaves, float lacunarity, float gain, float offset, float threshold, bool invert);















// ---------------------------------------------
// ---------------------------------------------
// Voronoi Functions
// ---------------------------------------------
// ---------------------------------------------

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// CellularNoiseLib.glslc
// voronoi cellular pattern
vec4 DT3D_CellularNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, float jitter, float stepSize, 
						float threshold, bool invert, int outSet, int distSet, int modSet);

//   /FunctionLibrary/DT3D_FunctionLibrary/BS_GpuNoiseLib.glslc
//   Generate grid cells random noise
//	 returns value random cell values
//
vec4 CellNoise( vec3 gridcell );  










// ---------------------------------------------
// ---------------------------------------------
// Gabor Noise Functions
// ---------------------------------------------
// ---------------------------------------------

// /FunctionLibrary/DT3D_FunctionLibrary/DT3D_GaborNoiseLib.glslc
// gabor noise function
vec4 DT3D_GaborNoise(vec3 Po, vec4 colorA, vec4 colorB, float frequency, vec3 orientation, 
					 float bandwidth, float truncate, float impulses, int seeds, int typeSet);










// ---------------------------------------------
// ---------------------------------------------
// Vector/Position Modification Functions
// ---------------------------------------------
// ---------------------------------------------

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// translate the position point in xyz
vec3 translate( vec3 P, vec3 trans);

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// build a rotation matrix in the 
// desired axis to multiply the position point 
mat3 rotation(float angle, vec3 axis);

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// scale the position point in xyz
vec3 scale( vec3 P, vec3 scale);

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// tranform the position with translate,scale,rotation 
vec3 positionTransform(vec3 P, vec3 Trans, vec3 Rot, vec3 Scale);








// ---------------------------------------------
// ---------------------------------------------
// Value Functions
// ---------------------------------------------
// ---------------------------------------------

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// bias function on a givin value 
float pxslBias( float bias, float value );

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// gain function on a givin value
float pxslGain( float gain, float value );

//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// threshold function for the givin value
float pxslThreshold(float threshold, float value);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// threshold function for the given float value with a feathering value 
float softThreshold(float threshold, float bound, float value);

//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// threshold function for the given color with a feathering value 
vec4 softThreshold(float threshold, float bound, vec4 colorInput)

//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
//Remap Function for Floats, vec4s and vec3s
float remap(float input, float OldMin, float OldMax, float NewMin, float NewMax, float Multiplier);
vec4 remap(vec4 input, float OldMin, float OldMax, float NewMin, float NewMax, float Multiplier);
vec3 remap(vec3 input, float OldMin, float OldMax, float NewMin, float NewMax, float Multiplier);











// ---------------------------------------------
// ---------------------------------------------
// Value Interpolation Functions
// ---------------------------------------------
// ---------------------------------------------

//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// Box filtered Step function 
// The boxstep function is somewhere between step and smoothstep. It is the result of the convolution of a box filter with a step edge. 
float boxStep(float low, float high, float value);


//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// Smooth function using combination of smoothstep and boxstep to smooth out values
float rsmooth(float x, float a_n, float b_n);

//   /FunctionLibrary/JK_FunctionLibrary/ID_ProceduralLib.glslc
// Frequency Smooth function using combination of smoothstep and boxstep to smooth out noise frequencies.
float FreqSmooth(float d, float x, float a_n, float b_n)


//   /FunctionLibrary/DT3D_FunctionLibrary/DT3D_ProceduralLib.glslc
// a anti-aliased version of step for procedurals  
// 'threshold' is constant , 'value' is smoothly varying
float aastep(float threshold , float value);











