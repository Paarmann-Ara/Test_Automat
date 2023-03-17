from services.log_.loging.log_provider import LogProvider
from services.log_.stack.stack_context_provider import StackContextProvider

info = LogProvider(template='Pipeline',config='Pipeline').info_instance
error = LogProvider(template='error',config='error').error_instance
stack = StackContextProvider().stack

print(stack(object_name='jg'))
info(stack())

info('Log_info_0')
info('Log_info_1')
info('Log_info_1')
info('Log_info_3', True)

error('Log_error_0')
error('Log_error_1')

info('Log_info_3')
info('Log_info_2')
info('Log_info_2')
info('Log_info_3')
info('Log_info_3')

info('Log_info_23')
info('Log_info_33')
info('Log_info_33', True)

error('Log_error_0')
error('Log_error_1', True)