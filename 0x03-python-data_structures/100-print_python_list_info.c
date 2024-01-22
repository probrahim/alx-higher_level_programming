#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints
 *
 * @p: object
 * Return: not return
 */
void print_python_list_info(PyObject *p)
{
	long int size, s;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (s = 0; s < size; s++)
	{
		item = PyList_GetItem(p, s);
		printf("Element %ld: %s\n", s, Py_TYPE(item)->tp_name);
	}
}
