################################### SCHEMA PRINCIPAL ######################################

from user.user import User
from user_token.user_token import UserToken
from user_module.user_module import UtilizadorModulo
from module.module import Modulo
from province.province import Province
from province.county.county import County


################################### SCHEMA INFRAESTRUTURA ##################################

from infraestrutura.infra_site.infra_site import InfraSite
from infraestrutura.infra_user_site.infra_user_site import InfraUserSite
from infraestrutura.infra_tipo_problema.infra_tipo_problema import InfraTipoProblema
from infraestrutura.infra_ticket.infra_ticket import InfraTicket
from infraestrutura.infra_user_tickets.infra_user_tickets import InfraUserTicket
from infraestrutura.infra_chat.infra_chat import InfraChat
from infraestrutura.infra_equipamento.infra_equipamento import InfraEquipamento
from infraestrutura.infra_historico.infra_historico import InfraHistorico
from infraestrutura.infra_ticket_historicos.infra_ticket_historicos import InfraTicketHistorico
from infraestrutura.infra_roles.infra_roles import InfraRole
from infraestrutura.infra_user_roles.infra_user_roles import InfraUserRole
from infraestrutura.infra_permissions.infra_permission import InfraPermission
from infraestrutura.infra_role_permissions.infra_role_permissions import InfraRolePermission
from infraestrutura.infra_errors.infra_error import InfraError
from infraestrutura.infra_auditoria.infra_auditoria import InfraAuditoria
