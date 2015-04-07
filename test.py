__author__ = 'Agnieszka'
# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
#
# def grades_sum(grades):
#     total = 0
#     for grade in grades:
#         total = total + grade
#     return total
#
# print grades_sum(grades)

# garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# garbled = garbled[::-1]
# message = ''
# for g in garbled:
#     if g != 'X':
#         message = message + g
# print message

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-1]
print message
message = message[::2]
print message

