/*
 * File: 103-python.c
 * Author: Olorundamisi Dunmade <github.com/olorundamisi>
 */


#include <Python.h>


void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_list - Print basic information about Python list objects.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	const char *type;
	const int alloced = list->allocated;
	const int size = var->ob_size;	/* Is this different from Py_SIZE(p); */
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloced);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;

		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes( list->ob_item[i] );
	}
}


/**
 * print_python_bytes - Print basic information about Python byte objects.
 * @p: A PyObject byte object.
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	unsigned char size;
	unsigned char i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", var->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if ( var->ob_size > 10 )
		size = 10;
	else
		size = var->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			putchar('\n');
		else
			putchar(' ');
	}
}
