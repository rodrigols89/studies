#include "vectors.h"
#include <cmath>
#include <cfloat>

// Macro to comparing floating point numbers to vectors.cpp.
#define CMP(x, y) \
    (fabsf(x - y) <= FLT_EPSILON * fmaxf(1.0f, fmaxf(fabsf(x), fabsf(y))))

// Operator Overloading (implementation) for Add (+) operation.
vec2 operator+(const vec2 &l, const vec2 &r)
{
    return {l.x + r.x, l.y + r.y};
}

// Operator Overloading (implementation) for Add (+) operation.
vec3 operator+(const vec3 &l, const vec3 &r)
{
    return {l.x + r.x, l.y + r.y, l.z + r.z};
}

// Operator Overloading (implementation) for Sub (-) operation.
vec2 operator-(const vec2 &l, const vec2 &r)
{
    return {l.x - r.x, l.y - r.y};
}

// Operator Overloading (implementation) for Sub (-) operation.
vec3 operator-(const vec3 &l, const vec3 &r)
{
    return {l.x - r.x, l.y - r.y, l.z - r.z};
}

// Operator Overloading (implementation) for Scalar Multiplication (*) operation.
vec2 operator*(const vec2 &l, float r)
{
    return {l.x * r, l.y * r};
}

// Operator Overloading (implementation) for Scalar Multiplication (*) operation.
vec3 operator*(const vec3 &l, float r)
{
    return {l.x * r, l.y * r, l.z * r};
}

// Operator Overloading (implementation) for Component-wise multiplication (*) operation.
vec2 operator*(const vec2 &l, const vec2 &r)
{
    return {l.x * r.x, l.y * r.y};
}

// Operator Overloading (implementation) for Component-wise multiplication (*) operation.
vec3 operator*(const vec3 &l, const vec3 &r)
{
    return {l.x * r.x, l.y * r.y, l.z * r.z};
}

// Operator Overloading (implementation) for check equal (==) operation.
bool operator==(const vec2 &l, const vec2 &r)
{
    return CMP(l.x, r.x) && CMP(l.y, r.y);
}

// Operator Overloading (implementation) for check equal (==) operation.
bool operator==(const vec3 &l, const vec3 &r)
{
    return CMP(l.x, r.x) && CMP(l.y, r.y) && CMP(l.z, r.z);
}

// Operator Overloading (implementation) for check not equal (!=) operation.
bool operator!=(const vec2 &l, const vec2 &r)
{
    return !(l == r);
}

// Operator Overloading (implementation) for check not equal (!=) operation.
bool operator!=(const vec3 &l, const vec3 &r)
{
    return !(l == r);
}

// Dot Product implementation.
float Dot(const vec2 &l, const vec2 &r)
{
    return ((l.x * r.x) + (l.y * r.y));
}

// Dot Product implementation.
float Dot(const vec3 &l, const vec3 &r)
{
    return ((l.x * r.x) + (l.y * r.y) + (l.z * r.z));
}
