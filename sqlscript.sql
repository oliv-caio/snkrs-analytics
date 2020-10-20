SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


CREATE TABLE IF NOT EXISTS site_refer (
  `idsite_refer` INT NOT NULL AUTO_INCREMENT,
  `refer_href` TEXT NOT NULL,
  `refer_preco` DOUBLE ,
  `refer_nome_modelo` TEXT ,
  `refer_modelo` TEXT ,
  PRIMARY KEY (`idsite_refer`),
  CONSTRAINT fk_site_refer_modelo_id FOREIGN KEY (idsite_refer) REFERENCES Modelo (idModelo) ON DELETE CASCADE ON UPDATE NO ACTION
  )


-- -----------------------------------------------------
-- Table `mydb`.`site_reven`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS site_reven (
  `idsite_reven` INT NOT NULL AUTO_INCREMENT,
  `reven_html` TEXT NOT NULL,
  `reven_preco` DOUBLE NOT NULL,
  `reven_nome_modelo` TEXT NOT NULL,
  `reven_modelo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsite_reven`),
  CONSTRAINT fk_site_reven_modelo_id FOREIGN KEY (idsite_reven) REFERENCES Modelo (idModelo) ON DELETE CASCADE ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table `mydb`.`Estoque_refer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Estoque_refer (
  `idEstoque` INT NOT NULL AUTO_INCREMENT,
  `estq_data` DATE NOT NULL,
  `estq_disp` TINYINT NOT NULL,
  `estq_grade` INT NOT NULL,
  `estq_qntd` INT NOT NULL,
  PRIMARY KEY (`idEstoque`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Instagram`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Instagram (
  `idInstagram` INT NOT NULL AUTO_INCREMENT,
  `url_instagram` TEXT NOT NULL,
  `num_coment_instagram` INT NOT NULL,
  `nome_instgram` TEXT NOT NULL,
  PRIMARY KEY (`idInstagram`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Modelo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Modelo (
  `idModelo` INT NOT NULL AUTO_INCREMENT,
  `mod_nome` VARCHAR(45) NOT NULL,
  `mod_tipo` VARCHAR(45) NOT NULL,
  `mod_marca` VARCHAR(45) NOT NULL,
  `id_refer` INT NOT NULL,
  `id_reven` INT NOT NULL,
  `Instagram_idInstagram` INT NOT NULL,
  PRIMARY KEY (`idModelo`),
  INDEX `fk_Modelo_site_refer1_idx` (`id_refer` ASC) VISIBLE,
  INDEX `fk_Modelo_site_reven1_idx` (`id_reven` ASC) VISIBLE,
  INDEX `fk_Modelo_Instagram1_idx` (`Instagram_idInstagram` ASC) VISIBLE,
  CONSTRAINT `fk_Modelo_site_refer1`
    FOREIGN KEY (`id_refer`)
    REFERENCES site_refer (`idsite_refer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Modelo_site_reven1`
    FOREIGN KEY (`id_reven`)
    REFERENCES site_reven (`idsite_reven`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Modelo_Instagram1`
    FOREIGN KEY (`Instagram_idInstagram`)
    REFERENCES Instagram (`idInstagram`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);



-- -----------------------------------------------------
-- Table `mydb`.`Estoque_reven`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Estoque_reven (
  `idEstoque` INT NOT NULL AUTO_INCREMENT,
  `estq_reven_data` DATE NOT NULL,
  `estq_reven_disp` TINYINT NOT NULL,
  `estq_reven_grade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEstoque`));



-- -----------------------------------------------------
-- Table `mydb`.`Logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Logs (
  `idLogs` INT NOT NULL AUTO_INCREMENT,
  `html_logs` TEXT NOT NULL,
  `data_hora_logs` DATE NOT NULL,
  `tipo_site` INT NOT NULL,
  PRIMARY KEY (`idLogs`));



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;