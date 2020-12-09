-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 30-Out-2020 às 19:58
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `ecommerce`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `carrinho`
--

CREATE TABLE `carrinho` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_produto` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL,
  `pedido_feito` int(11) NOT NULL,
  `id_pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `carrinho`
--

INSERT INTO `carrinho` (`id`, `id_usuario`, `id_produto`, `quantidade`, `pedido_feito`, `id_pedido`) VALUES
(84, 6, 7, 2, 1, 84),
(86, 6, 8, 1, 1, 86),
(91, 2, 10, 1, 1, 90),
(100, 6, 9, 1, 1, 100),
(101, 6, 10, 1, 1, 100);

-- --------------------------------------------------------

--
-- Estrutura da tabela `cobranca`
--

CREATE TABLE `cobranca` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `numero_cartao` varchar(150) NOT NULL,
  `nome_titular` varchar(150) NOT NULL,
  `data_exp` varchar(150) NOT NULL,
  `csv` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cobranca`
--

INSERT INTO `cobranca` (`id`, `id_usuario`, `numero_cartao`, `nome_titular`, `data_exp`, `csv`) VALUES
(2, 4, '123123', '1231231', '12312312', '12312312');

-- --------------------------------------------------------

--
-- Estrutura da tabela `endereco`
--

CREATE TABLE `endereco` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `rua` varchar(150) NOT NULL,
  `numero` varchar(150) NOT NULL,
  `cep` varchar(150) NOT NULL,
  `bairro` varchar(150) NOT NULL,
  `municipio` varchar(150) NOT NULL,
  `estado` varchar(150) NOT NULL,
  `pais` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `endereco`
--

INSERT INTO `endereco` (`id`, `id_usuario`, `rua`, `numero`, `cep`, `bairro`, `municipio`, `estado`, `pais`) VALUES
(1, 0, 'Jorge', 'Jorge', 'Jorge', 'Jorge', 'Jorge', 'Jorge', 'Jorge'),
(2, 0, 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen'),
(4, 52, 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen', 'Carmen');

-- --------------------------------------------------------

--
-- Estrutura da tabela `pedido`
--

CREATE TABLE `pedido` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_endereco` int(11) NOT NULL,
  `id_pedido` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `pedido`
--

INSERT INTO `pedido` (`id`, `id_usuario`, `id_endereco`, `id_pedido`) VALUES
(49, 6, 0, 84),
(50, 6, 0, 86),
(51, 6, 0, 87),
(52, 2, 0, 90),
(53, 6, 0, 100);

-- --------------------------------------------------------

--
-- Estrutura da tabela `produto`
--

CREATE TABLE `produto` (
  `id_produto` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `preco` float NOT NULL,
  `estoque` int(11) NOT NULL,
  `url_img` varchar(150) NOT NULL,
  `detalhes` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `produto`
--

INSERT INTO `produto` (`id_produto`, `nome`, `preco`, `estoque`, `url_img`, `detalhes`) VALUES
(7, 'Camisa', 23.99, 12, './imagens/img1.jpg', 'Este é o detalhes do produto referente ao produto camisa: </br > </br >\r\nCurabitur quis gravida orci, sed fringilla ligula. Phasellus leo tellus, faucibus volutpat tellus sit amet, lobortis ornare risus. Integer mauris urna, porta quis egestas quis, dignissim et augue. Proin maximus, arcu quis aliquam venenatis, purus sem finibus purus, eu pellentesque magna felis id lectus. Phasellus nulla felis, hendrerit vel eros non, ultricies rhoncus ex. Nullam non ante fringilla, aliquam tortor ac, lacinia dolor. Pellentesque dignissim massa non quam finibus viverra. Cras ipsum erat, commodo nec neque eg'),
(8, 'Calça', 21.99, 12, './imagens/img1.jpg', 'Este é o detalhes do produto referente ao produto calça: </br > </br >\r\nCurabitur quis gravida orci, sed fringilla ligula. Phasellus leo tellus, faucibus volutpat tellus sit amet, lobortis ornare risus. Integer mauris urna, porta quis egestas quis, dignissim et augue. Proin maximus, arcu quis aliquam venenatis, purus sem finibus purus, eu pellentesque magna felis id lectus. Phasellus nulla felis, hendrerit vel eros non, ultricies rhoncus ex. Nullam non ante fringilla, aliquam tortor ac, lacinia dolor. Pellentesque dignissim massa non quam finibus viverra. Cras ipsum erat, commodo nec neque eg'),
(9, 'Calça Lagging', 12.99, 35, './imagens/img4.jpg', 'Este é o detalhes do produto referente ao produto lagging: </br > </br >\r\nCurabitur quis gravida orci, sed fringilla ligula. Phasellus leo tellus, faucibus volutpat tellus sit amet, lobortis ornare risus. Integer mauris urna, porta quis egestas quis, dignissim et augue. Proin maximus, arcu quis aliquam venenatis, purus sem finibus purus, eu pellentesque magna felis id lectus. Phasellus nulla felis, hendrerit vel eros non, ultricies rhoncus ex. Nullam non ante fringilla, aliquam tortor ac, lacinia dolor. Pellentesque dignissim massa non quam finibus viverra. Cras ipsum erat, commodo nec neque e'),
(10, 'Blusa Cropped', 10.99, 98, './imagens/img3.jpg', 'Este é o detalhes do produto referente ao produto Blusa Cropped: </br > </br >\r\nCurabitur quis gravida orci, sed fringilla ligula. Phasellus leo tellus, faucibus volutpat tellus sit amet, lobortis ornare risus. Integer mauris urna, porta quis egestas quis, dignissim et augue. Proin maximus, arcu quis aliquam venenatis, purus sem finibus purus, eu pellentesque magna felis id lectus. Phasellus nulla felis, hendrerit vel eros non, ultricies rhoncus ex. Nullam non ante fringilla, aliquam tortor ac, lacinia dolor. Pellentesque dignissim massa non quam finibus viverra. Cras ipsum erat, commodo nec n');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nome`, `email`, `senha`) VALUES
(1, 'Matheus', 'Matheus', 'Matheus'),
(2, 'Cleysson', 'cleysson.santos1@hotmail.com', '$2b$12$Fh7zMBVP1j8DtvfWR92PVeKFlcS4Kq2f7mj9RzwKw./vZivh4QWTG'),
(3, 'string', 'string', '$2b$12$hM0rGFu70TQyEWEeoox0dO0CKc6E22DbmapxkMToUYD3e/rs5P7vS'),
(4, 'asdasd', 'asdasdas', '$2b$12$.n7Od6FWkpNU6KzvRJR.ZuvYy9dIZ.SvWCS0BjFTBUvVC.XL9Svia'),
(5, 'Lucas', 'lucaslimapkts@gmail.com', '$2b$12$tiVyYATyg9OU1MuWRBcS1uBGHZwLWnwY.OLSNmEYgLhacOEyiMfIC'),
(6, 'Mathias', 'malaila951@gmail.com', '$2b$12$Y8HswxOwScS7G4thfKI9M.075kxvDbMSz2zr06PzoxNl9N49CqyDO'),
(7, 'string', 'st4ring', '$2b$12$XhhhuV9HnGDa0MHNdExQuekYzSF8/RVk/yMHtNUfUYA6PfIO5eMM.');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `carrinho`
--
ALTER TABLE `carrinho`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carrinho_FK` (`id_produto`),
  ADD KEY `carrinho_FK_1` (`id_usuario`);

--
-- Índices para tabela `cobranca`
--
ALTER TABLE `cobranca`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `endereco`
--
ALTER TABLE `endereco`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_FK` (`id_usuario`);

--
-- Índices para tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`);

--
-- Índices para tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `carrinho`
--
ALTER TABLE `carrinho`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT de tabela `cobranca`
--
ALTER TABLE `cobranca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `endereco`
--
ALTER TABLE `endereco`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `pedido`
--
ALTER TABLE `pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `id_produto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `carrinho`
--
ALTER TABLE `carrinho`
  ADD CONSTRAINT `carrinho_FK` FOREIGN KEY (`id_produto`) REFERENCES `produto` (`id_produto`),
  ADD CONSTRAINT `carrinho_FK_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Limitadores para a tabela `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_FK` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
