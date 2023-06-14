#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print informations of bytes
 * @py: Python Object
 */
void print_python_bytes(PyObject *py)
{
	char *string;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(py))->ob_size;
	string = ((PyBytesObject *)py)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - print informations of lists
 * @py: Python Object
 */
void print_python_list(PyObject *py)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(py))->obj_size;
	list = (PyListObject *)py;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)py)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->obj_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
