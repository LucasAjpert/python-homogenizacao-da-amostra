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