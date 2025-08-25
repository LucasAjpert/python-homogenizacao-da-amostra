-- Primeiro, crie o banco de dados (se ainda não existir)
CREATE DATABASE IF NOT EXISTS homogenizacao_db;

-- Use o banco de dados que acabamos de criar
USE homogenizacao_db;

-- Crie a tabela para os imóveis urbanos
CREATE TABLE IF NOT EXISTS imoveis_urbanos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    endereco VARCHAR(255),
    area_construida float(10),
    idade_imovel int(3),
    valor_total float(15),
    valor_unitario float(10),
    padrao_construtivo float(10),
    valor_residual FLOAT(10),
    conservacao_foc FLOAT(10),
    indice_fiscal INT(5),
    frentes_multiplas BOOL,
    idade_referencial INT(3),
    estado_conservacao FLOAT(10),
    fator_oferta FLOAT(3),
    padao_const FLOAT(10),
    conservacao FLOAT(10),
    localizacao FLOAT(10),
    frentes_m FLOAT(3),
    unitario_homog FLOAT(15),
    benfeitorias FLOAT(15),
    descricao_benfeitorias TEXT,
    tipo_cadastro BOOL
);

-- Crie a tabela para os imóveis rurais
CREATE TABLE IF NOT EXISTS imoveis_rurais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_cadastro BOOL,
	endereco VARCHAR(255),
    area_imovel FLOAT(10),
    valor_imovel_sem_benf FLOAT(15),
    benfeitorias FLOAT(15),
    valor_unitario FLOAT(10),
    fonte FLOAT(3),
    fator_na FLOAT(10),
    nota_agronomica FLOAT(10),
    unitario_homog FLOAT(15),
    classe_1 INT(3),
    classe_2 INT(3),
    classe_3 INT(3),
    classe_4 INT(3),
    classe_5 INT(3),
    classe_6 INT(3),
    classe_7 INT(3),
    classe_8 INT(3)
);