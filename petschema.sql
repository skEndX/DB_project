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
	r_day int,
	r_time int,
	PRIMARY KEY(m_num,i_num,p_num,r_day,r_time),
	FOREIGN KEY(m_num) REFERENCES member(m_num)
	on delete cascade on update cascade,
	FOREIGN KEY(i_num) REFERENCES instructor(i_num),
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

CREATE TABLE disease(
	p_num text,
	d_type text,
	PRIMARY KEY(p_num, d_type),
	FOREIGN KEY(p_num) REFERENCES pet(p_num)
	on delete cascade on update cascade
);

CREATE TABLE daily_log(
	p_num text,
	m_num text,
	log_day int,
	sleep text,
	diet text,
	PRIMARY KEY(p_num, m_num,log_day),
	FOREIGN KEY(p_num) REFERENCES pet(p_num)
	on delete cascade on update cascade,
	FOREIGN KEY(m_num) REFERENCES member(m_num)
	on delete cascade on update cascade
);
