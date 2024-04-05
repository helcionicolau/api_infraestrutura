-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 22-Mar-2024 às 20:37
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd_infraestrutura`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.chats`
--

CREATE TABLE `infra.chats` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `comentario` text DEFAULT NULL,
  `file` text DEFAULT NULL,
  `utilizador_id` bigint(20) UNSIGNED NOT NULL,
  `ticket_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.equipamento`
--

CREATE TABLE `infra.equipamento` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `temperatura` varchar(255) DEFAULT '0',
  `humidade` varchar(255) DEFAULT '0',
  `rede` varchar(255) DEFAULT '0',
  `ups` varchar(255) DEFAULT '0',
  `gerador` varchar(255) DEFAULT '0',
  `inundacao` varchar(255) DEFAULT '0',
  `combustivel` varchar(255) DEFAULT '0',
  `agua` varchar(255) DEFAULT '0',
  `mac_address` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `estado` int(11) NOT NULL DEFAULT 1,
  `tipo` int(11) NOT NULL DEFAULT 1,
  `min_val_temp` varchar(255) DEFAULT NULL,
  `max_val_temp` varchar(255) DEFAULT NULL,
  `site_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.equipamento_historicos`
--

CREATE TABLE `infra.equipamento_historicos` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `equipamento_id` bigint(20) UNSIGNED DEFAULT NULL,
  `historico_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.errors`
--

CREATE TABLE `infra.errors` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `descricao` text DEFAULT NULL,
  `estado` int(11) NOT NULL DEFAULT 0,
  `sessao` varchar(255) DEFAULT NULL,
  `utilizador_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.historicos`
--

CREATE TABLE `infra.historicos` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `temperatura` varchar(255) DEFAULT NULL,
  `humidade` varchar(255) DEFAULT NULL,
  `rede` varchar(255) DEFAULT NULL,
  `ups` varchar(255) DEFAULT NULL,
  `gerador` varchar(255) DEFAULT NULL,
  `inundacao` varchar(255) DEFAULT NULL,
  `combustivel` varchar(255) DEFAULT NULL,
  `agua` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  `last_live_data` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.permissions`
--

CREATE TABLE `infra.permissions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `nivel` int(11) NOT NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.roles`
--

CREATE TABLE `infra.roles` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `tipo` int(11) NOT NULL DEFAULT 1 COMMENT 'se 0 o role é do sistema',
  `description` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.role_permissions`
--

CREATE TABLE `infra.role_permissions` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `role_id` bigint(20) UNSIGNED DEFAULT NULL,
  `permission_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.sites`
--

CREATE TABLE `infra.sites` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `estado` varchar(255) NOT NULL DEFAULT '1',
  `municipio_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.tickets`
--

CREATE TABLE `infra.tickets` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `estado` int(11) NOT NULL DEFAULT 0,
  `estado_tecnico` int(11) NOT NULL DEFAULT 0,
  `descricao` text DEFAULT NULL,
  `is_suporte_afrizona` int(11) NOT NULL DEFAULT 0,
  `tipo_problema_id` bigint(20) UNSIGNED DEFAULT NULL,
  `data_resolucao` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.ticket_historicos`
--

CREATE TABLE `infra.ticket_historicos` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `ticket_id` bigint(20) UNSIGNED DEFAULT NULL,
  `historico_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.tipo_problemas`
--

CREATE TABLE `infra.tipo_problemas` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.utilizador_roles`
--

CREATE TABLE `infra.utilizador_roles` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `utilizador_id` bigint(20) UNSIGNED DEFAULT NULL,
  `role_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.utilizador_sites`
--

CREATE TABLE `infra.utilizador_sites` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `utilizador_id` bigint(20) UNSIGNED DEFAULT NULL,
  `site_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `infra.utilizador_tickets`
--

CREATE TABLE `infra.utilizador_tickets` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `utilizador_id` bigint(20) UNSIGNED DEFAULT NULL,
  `ticket_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `infra.chats`
--
ALTER TABLE `infra.chats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Índices para tabela `infra.equipamento`
--
ALTER TABLE `infra.equipamento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `site_id` (`site_id`);

--
-- Índices para tabela `infra.equipamento_historicos`
--
ALTER TABLE `infra.equipamento_historicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `equipamento_id` (`equipamento_id`),
  ADD KEY `historico_id` (`historico_id`);

--
-- Índices para tabela `infra.errors`
--
ALTER TABLE `infra.errors`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.historicos`
--
ALTER TABLE `infra.historicos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.permissions`
--
ALTER TABLE `infra.permissions`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.roles`
--
ALTER TABLE `infra.roles`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.role_permissions`
--
ALTER TABLE `infra.role_permissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`),
  ADD KEY `permission_id` (`permission_id`);

--
-- Índices para tabela `infra.sites`
--
ALTER TABLE `infra.sites`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.tickets`
--
ALTER TABLE `infra.tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tipo_problema_id` (`tipo_problema_id`);

--
-- Índices para tabela `infra.ticket_historicos`
--
ALTER TABLE `infra.ticket_historicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ticket_id` (`ticket_id`),
  ADD KEY `historico_id` (`historico_id`);

--
-- Índices para tabela `infra.tipo_problemas`
--
ALTER TABLE `infra.tipo_problemas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `infra.utilizador_roles`
--
ALTER TABLE `infra.utilizador_roles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`);

--
-- Índices para tabela `infra.utilizador_sites`
--
ALTER TABLE `infra.utilizador_sites`
  ADD PRIMARY KEY (`id`),
  ADD KEY `site_id` (`site_id`);

--
-- Índices para tabela `infra.utilizador_tickets`
--
ALTER TABLE `infra.utilizador_tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `infra.chats`
--
ALTER TABLE `infra.chats`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.equipamento`
--
ALTER TABLE `infra.equipamento`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.equipamento_historicos`
--
ALTER TABLE `infra.equipamento_historicos`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.errors`
--
ALTER TABLE `infra.errors`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.historicos`
--
ALTER TABLE `infra.historicos`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.permissions`
--
ALTER TABLE `infra.permissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.roles`
--
ALTER TABLE `infra.roles`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.role_permissions`
--
ALTER TABLE `infra.role_permissions`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.sites`
--
ALTER TABLE `infra.sites`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.tickets`
--
ALTER TABLE `infra.tickets`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.ticket_historicos`
--
ALTER TABLE `infra.ticket_historicos`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.tipo_problemas`
--
ALTER TABLE `infra.tipo_problemas`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.utilizador_roles`
--
ALTER TABLE `infra.utilizador_roles`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.utilizador_sites`
--
ALTER TABLE `infra.utilizador_sites`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `infra.utilizador_tickets`
--
ALTER TABLE `infra.utilizador_tickets`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `infra.chats`
--
ALTER TABLE `infra.chats`
  ADD CONSTRAINT `infra.chats_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `infra.tickets` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.equipamento`
--
ALTER TABLE `infra.equipamento`
  ADD CONSTRAINT `infra.equipamento_ibfk_1` FOREIGN KEY (`site_id`) REFERENCES `infra.sites` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.equipamento_historicos`
--
ALTER TABLE `infra.equipamento_historicos`
  ADD CONSTRAINT `infra.equipamento_historicos_ibfk_1` FOREIGN KEY (`equipamento_id`) REFERENCES `infra.equipamento` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `infra.equipamento_historicos_ibfk_2` FOREIGN KEY (`historico_id`) REFERENCES `infra.historicos` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.role_permissions`
--
ALTER TABLE `infra.role_permissions`
  ADD CONSTRAINT `infra.role_permissions_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `infra.roles` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `infra.role_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `infra.permissions` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.tickets`
--
ALTER TABLE `infra.tickets`
  ADD CONSTRAINT `infra.tickets_ibfk_1` FOREIGN KEY (`tipo_problema_id`) REFERENCES `infra.tipo_problemas` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.ticket_historicos`
--
ALTER TABLE `infra.ticket_historicos`
  ADD CONSTRAINT `infra.ticket_historicos_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `infra.tickets` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `infra.ticket_historicos_ibfk_2` FOREIGN KEY (`historico_id`) REFERENCES `infra.historicos` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.utilizador_roles`
--
ALTER TABLE `infra.utilizador_roles`
  ADD CONSTRAINT `infra.utilizador_roles_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `infra.roles` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.utilizador_sites`
--
ALTER TABLE `infra.utilizador_sites`
  ADD CONSTRAINT `infra.utilizador_sites_ibfk_1` FOREIGN KEY (`site_id`) REFERENCES `infra.sites` (`id`) ON DELETE CASCADE;

--
-- Limitadores para a tabela `infra.utilizador_tickets`
--
ALTER TABLE `infra.utilizador_tickets`
  ADD CONSTRAINT `infra.utilizador_tickets_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `infra.tickets` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
