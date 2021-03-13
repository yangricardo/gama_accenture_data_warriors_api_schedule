-- Tabela de Países

CREATE TABLE public.country (
	countrycode varchar(2) NOT NULL,
	countryname varchar(44) NOT NULL,
	countryslug varchar(44) NOT NULL,
	CONSTRAINT pk_country PRIMARY KEY (countrycode)
);

-- Tabela de registros diários
CREATE TABLE public.daily (
	datereg date NOT NULL,
	countrycode varchar(2) NOT NULL,
	totalconfirmed int4 NOT NULL,
	totaldeaths int4 NOT NULL,
	newconfirmed int4 NOT NULL,
	newdeaths int4 NOT NULL,
	CONSTRAINT pk_daily PRIMARY KEY (datereg, countrycode),
    CONSTRAINT fk_daily_country FOREIGN KEY (countrycode) REFERENCES country(countrycode)
);

-- Tabela de registros consolidados

CREATE TABLE public.summary (
	countrycode varchar(2) NOT NULL,
	lastupdated varchar(25) NOT NULL,
	newconfirmed int4 NOT NULL,
	newdeaths int4 NOT NULL,
	totalconfirmed int4 NOT NULL,
	totaldeaths int4 NOT NULL,
	CONSTRAINT pk_summary PRIMARY KEY (countrycode),
    CONSTRAINT fk_summary_country FOREIGN KEY (countrycode) REFERENCES country(countrycode)
);

-- Tabela de continentes
CREATE TABLE public.continent (
	continentcode varchar(2) NOT NULL,
	continentname varchar(20) NOT NULL,
	CONSTRAINT pk_continent PRIMARY KEY (continentcode)
);

-- Tabela de países associados a continentes
CREATE TABLE public.country_continent (
	countrycode varchar(2) NOT NULL,
	continentcode varchar(2) NOT NULL,
	CONSTRAINT pk_country_continent PRIMARY KEY (countrycode, continentcode)
    CONSTRAINT fk_country_continent_country FOREIGN KEY (countrycode) REFERENCES country(countrycode)
    CONSTRAINT fk_country_continent_continent FOREIGN KEY (continentcode) REFERENCES continent(continentcode)
);