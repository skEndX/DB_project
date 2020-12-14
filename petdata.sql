insert into member values ('01012341234','Amy','23513','W');
insert into member values ('01037144918','Jacob','22934','M');
insert into member values ('01033453237','Ethan','94021','M');
insert into member values ('01004004392','Michael','52193','W');
insert into member values ('01040935392','Daniel','05593','M');

insert into pet values ('01012341234','410846459730954', 141103, 'W', 'Cookie', 'Maltese', '5.3');
insert into pet values ('01037144918','410146805739832', 150506, 'M', 'Bebe', 'Pomeranian', '3.4');
insert into pet values ('01033453237','410397006766532', 130318, 'M', 'Coco', 'Toy Poodle', '3.2');
insert into pet values ('01004004392','410146532632766', 171226, 'W', 'Elsa', 'Bichon Frise', '4.5');
insert into pet values ('01040935392','410176654680532', 160829, 'M', 'Favian', 'Shih Tzu', '4.0');
insert into pet values ('01040935392','410805766146532', 140114, 'W', 'Gem', 'Maltese', '2.7');

insert into instructor values ('01032942346', 1990, 'Joy', 'W', 5);
insert into instructor values ('01010542346', 1992, 'Thomas', 'M', 3);
insert into instructor values ('01032944489', 1992, 'Linda', 'W', 3);

insert into reservation values ('01012341234','01032942346','410846459730954','2020-11-14',14);
insert into reservation values ('01037144918','01032942346','410146805739832','2020-11-11',9);
insert into reservation values ('01033453237','01010542346','410397006766532','2020-12-12',11);
insert into reservation values ('01004004392','01032944489','410146532632766','2020-11-16',13);
insert into reservation values ('01040935392','01032942346','410176654680532','2020-10-26',17);
insert into reservation values ('01040935392','01032944489','410176654680532','2020-12-13',15);
insert into reservation values ('01040935392','01010542346','410805766146532','2020-11-19',11);
insert into reservation values ('01040935392','01032944489','410805766146532','2020-12-25',20);

insert into daily_log values ('410146805739832', '01037144918', '2020-09-14', 'Y', 'Sweet pumpkin, tofu');
insert into daily_log values ('410397006766532', '01033453237', '2020-10-10', 'Y', 'egg, carrot, fork');
insert into daily_log values ('410397006766532', '01033453237', '2020-10-24', 'N', 'carrot, tofu');
insert into daily_log values ('410397006766532', '01033453237', '2020-11-02', 'Y', 'chicken,egg');
insert into daily_log values ('410805766146532','01040935392','2020-10-10','Y','egg, carrot, fork');
insert into daily_log values ('410805766146532','01040935392','2020-10-23','N','fish, carrot');
insert into daily_log values ('410146532632766','01004004392','2020-10-28','Y','chicken,egg');
