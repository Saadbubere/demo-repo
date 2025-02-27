{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8828beef",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please provide a valid integer.\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "def decimal_to_hex(decimal_value):\n",
    "    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']\n",
    "    hexadecimal = \"\"\n",
    "    num = decimal_value\n",
    "    print(f\"Converting the Decimal Value {num} to Hex...\")\n",
    "    while num != 0:\n",
    "        rem = num % 16\n",
    "        hexadecimal = hex_chars[rem] + hexadecimal\n",
    "        num //= 16\n",
    "    print(f\"Hexadecimal representation is: {hexadecimal}\")\n",
    "    return hexadecimal # Return the hexadecimal value for testing\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    if len(sys.argv) > 1:\n",
    "        try:\n",
    "            decimal_value = int(sys.argv[1])\n",
    "            decimal_to_hex(decimal_value)\n",
    "        except ValueError:\n",
    "            print(\"Please provide a valid integer.\")\n",
    "    else:\n",
    "        print(\"Usage: python script.py <decimal_number>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59b0d680",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7ad53f93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please provide a valid integer.\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e93d81a8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
