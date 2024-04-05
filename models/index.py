from models.user.users import users
from models.province.province import provinces
from models.province.county.county import counties
from models.module.module import modules
from models.user_module.user_module import user_modules
from models.user_token.user_token import user_tokens
from models.login_attempts.login_attempts import login_attempts

############################# INFRAESTRUTURA ####################################

from models.infraestrutura.infra_site.infra_site import sites
from models.infraestrutura.infra_user_site.infra_user_site import user_sites
from models.infraestrutura.infra_tipo_problema.infra_tipo_problema import infra_tipo_problemas
from models.infraestrutura.infra_ticket.infra_ticket import infra_tickets
from models.infraestrutura.infra_user_tickets.infra_user_tickets import user_tickets
from models.infraestrutura.infra_chat.infra_chat import infra_chats
from models.infraestrutura.infra_equipamento.infra_equipamento import infra_equipamento
from models.infraestrutura.infra_historico.infra_historico import infra_historicos
from models.infraestrutura.infra_ticket_historicos.infra_ticket_historicos import infra_ticket_historicos
from models.infraestrutura.infra_roles.infra_roles import infra_roles
from models.infraestrutura.infra_user_roles.infra_user_roles import infra_user_roles
from models.infraestrutura.infra_permissions.infra_permission import infra_permissions
from models.infraestrutura.infra_role_permissions.infra_role_permissions import infra_role_permissions
from models.infraestrutura.infra_errors.infra_error import infra_errors
from models.infraestrutura.infra_auditoria.infra_auditoria import infra_auditoria