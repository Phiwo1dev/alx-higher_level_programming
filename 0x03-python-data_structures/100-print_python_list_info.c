#include <Python.h>

/**
 * print_python_list_info - A function that prints basic info
 * about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)

{
	int s, allo, i;
	PyObject *obj;

	s = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allo);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
