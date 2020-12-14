DROP TABLE IF EXISTS member;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS reservation;
DROP TABLE IF EXISTS disease;
DROP TABLE IF EXISTS daily_log; 

CREATE TABLE member(
	m_num text,
	m_name text,
	m_addr text,
	m_sex text,
	PRIMARY KEY(m_num)
);

CREATE table instructor(
	i_num text,
	i_birth int,
	i_name text,
	i_sex text,
	i_career int,
	PRIMARY key(i_num)
);

CREATE TABLE reservation(
	m_num text,
	i_num text,
	p_num text,
	r_day text,
	r_time int,
	PRIMARY KEY(m_num,i_num,p_num,r_day,r_time),
	FOREIGN KEY(m_num) REFERENCES member(m_num)
	on delete cascade on update cascade,
	FOREIGN KEY(i_num) REFERENCES instructor(i_num)
	on delete cascade on update cascade,
	FOREIGN KEY(p_num) REFERENCES pet(p_num)
	on delete cascade on update cascade
);

CREATE TABLE pet(
	m_num text,
	p_num text,
	p_birth int,
	p_sex text,
	p_name text,
	p_breed text,
	p_weight real,
	PRIMARY KEY(p_num),
	FOREIGN KEY(m_num) REFERENCES member(m_num)
	on delete cascade on update cascade
);

CREATE TABLE daily_log(
	p_num text,
	m_num text,
	log_day text,
	sleep text,
	diet text,
	PRIMARY KEY(p_num, m_num,log_day),
	FOREIGN KEY(p_num) REFERENCES pet(p_num)
	on delete cascade on update cascade,
	FOREIGN KEY(m_num) REFERENCES member(m_num)
	on delete cascade on update cascade
);
