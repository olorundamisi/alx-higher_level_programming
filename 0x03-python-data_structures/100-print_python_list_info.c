/**
 * File: 100-print_python_list_info.c
 *
 * Author: Olorundamisi Dunmade <github.com/olorundamisi>
 */


#include <Python.h>


/**
 * print_python_list_info - Print basic information about Python lists.
 *
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *object;

	static const int size = Py_SIZE(p);
	const int alloced = ((PyListObject *)p)->allocated;
	int i;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloced);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
