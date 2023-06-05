/*
 * File: 102-python.c
 * Author: Olorundamisi Dunmade <github.com/olorundamisi>
 */

#include "Python.h"

/**
 * print_python_string - Print basic information about Python strings.
 *						 PyASCIIObject *
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	PyASCIIObject *ascii_str_obj = (PyASCIIObject *)(p);

	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ascii_str_obj->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
