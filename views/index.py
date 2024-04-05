from fastapi import APIRouter
from .user.user_controller import user_router
from .province.province_controller import province_router
from .province.county.county_controller import county_router
from .auth.auth_controller import auth_router
from views.user_module.user_module_controller import user_module_router
from .module.module_controller import module_router

index_router = APIRouter()

index_router.include_router(user_router, prefix='/users')
index_router.include_router(province_router, prefix='/provinces')
index_router.include_router(county_router, prefix='/counties')
index_router.include_router(auth_router, prefix='/auth')
index_router.include_router(module_router, prefix='/modules')
index_router.include_router(user_module_router, prefix='/user_modules')

########################### INFRAESTRUTURA ROUTERS ####################################

from .infraestrutura.infra_site.infra_site_controller import infra_site_router
from .infraestrutura.infra_user_site.infra_user_site_controller import infra_user_site_router
from .infraestrutura.infra_tipo_problema.infra_tipo_problema_controller import infra_tipo_problema_router
from .infraestrutura.infra_ticket.infra_ticket_controller import infra_tickets_router
from .infraestrutura.infra_user_tickets.infra_user_tickets_controller import infra_user_ticket_router
from .infraestrutura.infra_chat.infra_chat_controller import infra_chat_router
from .infraestrutura.infra_equipamento.infra_equipamento_controller import infra_equipamento_router
from .infraestrutura.infra_historico.infra_historico_controller import infra_historicos_router
from .infraestrutura.infra_ticket_historicos.infra_ticket_historicos_controller import infra_ticket_historicos_router
from .infraestrutura.infra_roles.infra_role_controller import infra_roles_router
from .infraestrutura.infra_user_roles.infra_user_role_controller import infra_user_roles_router
from .infraestrutura.infra_permissions.infra_permission_controller import infra_permissions_router
from .infraestrutura.infra_role_permissions.infra_role_permission_controller import infra_role_permissions_router
from .infraestrutura.infra_errors.infra_error_controller import infra_errors_router
from .infraestrutura.infra_auditoria.infra_auditoria_controller import infra_auditoria_router

index_router.include_router(infra_site_router, prefix='/infra_sites')
index_router.include_router(infra_user_site_router, prefix='/infra_user_sites')
index_router.include_router(infra_tipo_problema_router, prefix='/infra_tipo_problemas')
index_router.include_router(infra_tickets_router, prefix='/infra_tickets')
index_router.include_router(infra_user_ticket_router, prefix='/infra_user_tickets')
index_router.include_router(infra_chat_router, prefix='/infra_chats')
index_router.include_router(infra_equipamento_router, prefix='/infra_equipamentos')
index_router.include_router(infra_historicos_router, prefix='/infra_historicos')
index_router.include_router(infra_ticket_historicos_router, prefix='/infra_ticket_historicos')
index_router.include_router(infra_roles_router, prefix='/infra_roles')
index_router.include_router(infra_user_roles_router, prefix='/infra_user_roles')
index_router.include_router(infra_permissions_router, prefix='/infra_permissions')
index_router.include_router(infra_role_permissions_router, prefix='/infra_role_permissions')
index_router.include_router(infra_errors_router, prefix='/infra_errors')
index_router.include_router(infra_auditoria_router, prefix='/infra_auditorias')
